#!/usr/bin/env python3
"""Validate SEO metadata in a built Jekyll site without network requests."""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.canonical = []
        self.blocks = []
        self.h1 = []
        self.images = []
        self.links = []
        self.author_profile = False
        self.capture = None
        self.buffer = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            key = attrs.get('name', attrs.get('property'))
            if key:
                self.meta.setdefault(key, []).append(attrs.get('content', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href'))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'a':
            self.links.append(attrs.get('href'))
        if 'author-profile' in attrs.get('class', '').split():
            self.author_profile = True
        if tag == 'h1' or (tag == 'script' and attrs.get('type') == 'application/ld+json'):
            self.capture, self.buffer = tag, ''

    def handle_data(self, data):
        if self.capture:
            self.buffer += data

    def handle_endtag(self, tag):
        if self.capture == tag:
            (self.h1 if tag == 'h1' else self.blocks).append(self.buffer.strip())
            self.capture = None

    def value(self, name):
        values = self.meta.get(name, [])
        return values[0] if len(values) == 1 else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', nargs='?', type=Path, default=Path('_site'))
    args = parser.parse_args()
    root = args.site.resolve()
    if not (root / 'index.html').is_file():
        parser.error('Build the site first with npm run build.')
    errors, counts, descriptions = [], Counter(), []

    def require(condition, path, message):
        if not condition:
            errors.append(f'{path}: {message}')

    for file in sorted(root.rglob('*.html')):
        path = file.relative_to(root)
        page = Page()
        page.feed(file.read_text())
        is_post = path.parts[0] == 'post'
        if is_post:
            counts['posts'] += 1
            require(len(page.blocks) == 1, path, 'expected one JSON-LD block')
        if not page.blocks:
            continue  # Standalone layouts such as the resume have their own head.
        counts['pages_with_json_ld'] += 1
        require(len(page.canonical) == 1, path, 'expected one canonical URL')
        canonical = page.canonical[0] if page.canonical else ''
        require(urlsplit(canonical).scheme == 'https', path, 'canonical must use HTTPS')
        for key in ['description', 'og:title', 'og:description', 'og:url',
                    'og:image', 'og:image:alt', 'twitter:title', 'twitter:description',
                    'twitter:image', 'twitter:image:alt']:
            require(bool(page.value(key)), path, f'missing or duplicate {key}')
        title, description = page.value('og:title'), page.value('description')
        require(title == page.value('twitter:title'), path, 'social titles differ')
        require(title and not title.startswith(('/', 'http')), path, 'title is a URL')
        require(description == page.value('og:description') == page.value('twitter:description'),
                path, 'descriptions differ')
        require(page.value('og:url') == canonical, path, 'OG URL differs from canonical')
        image = page.value('og:image') or ''
        require(image == page.value('twitter:image'), path, 'social images differ')
        require(urlsplit(image).scheme == 'https', path, 'image must use an absolute HTTPS URL')
        if urlsplit(image).netloc == urlsplit(canonical).netloc:
            image_file = root / unquote(urlsplit(image).path).lstrip('/')
            require(image_file.is_file(), path, f'image file not found: {image}')
            if image_file.is_file():
                signature = image_file.read_bytes()[:12]
                supported = (signature.startswith(b'\x89PNG\r\n\x1a\n') or
                             signature.startswith(b'\xff\xd8') or
                             signature.startswith((b'GIF87a', b'GIF89a')) or
                             (signature.startswith(b'RIFF') and signature[8:12] == b'WEBP'))
                require(supported, path, 'social image must be PNG, JPEG, GIF, or WebP')
        for block in page.blocks:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                errors.append(f'{path}: {exc}')
                continue
            counts['valid_json_ld'] += 1
            require(data.get('url') == canonical, path, 'schema URL differs from canonical')
            require(data.get('description') == description, path, 'schema description differs')
            if not is_post:
                continue
            require(data.get('@type') == 'BlogPosting', path, 'incorrect article schema type')
            require(data.get('headline') == title, path, 'schema headline differs from social title')
            visible_title = ' '.join(page.h1[0].split()) if page.h1 else ''
            require(title == visible_title, path, 'metadata title differs from visible heading')
            require(data.get('image') == image, path, 'schema image differs from social image')
            require(bool(data.get('datePublished')), path, 'missing publication date')
            author = data.get('author', {})
            require(bool(author.get('name') and author.get('url')), path, 'missing author identity')
            require(author.get('url') in page.links and page.author_profile,
                    path, 'missing visible author profile link')
        if is_post:
            descriptions.append(description)
            for img in page.images:
                counts['post_images'] += 1
                alt = img.get('alt', '').strip()
                require(alt.lower() not in ['', 'text', 'image', 'img', 't', '1'],
                        path, f'missing or generic image alt: {img.get("src")}')
    require(counts['posts'] > 0, root, 'no blog posts found')
    require(len(descriptions) == len(set(descriptions)), root, 'duplicate post descriptions')
    about = root / 'about.html'
    require(about.is_file(), root, 'missing author page')
    if about.is_file():
        page = Page()
        page.feed(about.read_text())
        schemas = []
        for block in page.blocks:
            try:
                schemas.append(json.loads(block))
            except json.JSONDecodeError:
                pass  # Reported by the general JSON-LD check above.
        require(any(d.get('@type') == 'ProfilePage' and
                    d.get('mainEntity', {}).get('@type') == 'Person' for d in schemas),
                'about.html', 'missing author ProfilePage schema')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        print(f'FAIL: {len(errors)} SEO checks failed.', file=sys.stderr)
        return 1
    print(f'PASS: {counts["valid_json_ld"]} JSON-LD blocks across '
          f'{counts["pages_with_json_ld"]} pages; {counts["posts"]} posts with '
          f'consistent metadata, local social images, and author profiles; '
          f'{counts["post_images"]} images with descriptive alt text.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
