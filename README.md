This blog is built with some modifications based on [TeXt Theme](https://github.com/kitian616/jekyll-TeXt-theme)

## Local development (macOS)

Install Ruby and the project's gems once:

```sh
brew install ruby@3.3
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
gem install bundler -v 4.0.20 --no-document
bundle config set --local path vendor/bundle
bundle install
```

Start the blog with `npm run serve`, then open http://127.0.0.1:4000.
The script selects Homebrew Ruby if the current Ruby is too old.
Changes to posts and templates rebuild automatically; restart after editing `_config.yml`.
Use `npm run build` for a static build. `npm run dev` uses the separate docs configuration.

## Post metadata

Add a page-specific `description`, `image` (a local PNG, JPEG, GIF, or WebP path),
and `image_alt` to each post's front matter. Keep `excerpt` for the homepage preview;
the search and social descriptions use `description` first. Use ordinary quoted
YAML strings for titles, including colons and quotation marks, rather than HTML entities.
Set `modify_date` only when the article's content has actually been updated.

Article metadata, Open Graph, Twitter cards, and JSON-LD share the same title,
description, canonical URL, and representative image. Posts show the author profile
configured in `_config.yml`; `/about.html` supplies the corresponding author page.

For an article without a suitable image, use `/assets/images/social/<post-key>.png`
and run `python3 tools/generate-social-cards.py`. This optional authoring command
requires Pillow and a Korean-capable font (`--font /path/to/font.ttf`); generated
PNGs are checked in, so normal Jekyll builds need neither. It also generates the
site-wide fallback card.

After editing templates or metadata, run `npm run build` and `npm run check:seo`.
The check parses generated JSON-LD and verifies titles, descriptions, author links,
local image files, and image alternative text without contacting external services.
If `jekyll serve` is running, use `npm run build -- --destination /tmp/blog-seo-build`
and `npm run check:seo -- /tmp/blog-seo-build` to keep the development server from
overwriting the production output during validation.
