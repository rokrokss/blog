# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based blog built on the TeXt Theme framework. The blog is hosted at https://rokrokss.com and uses GitHub Pages for deployment.

## Common Development Commands

### Local Development
- **Start local server**: `npm run serve` or `bundle exec jekyll serve -H 0.0.0.0`
- **Build site**: `npm run build` or `bundle exec jekyll build`
- **Development mode with trace**: `npm run default` (includes -t flag for tracing)

### Linting
- **Lint CSS/SCSS**: `npm run css-lint`
- **Fix CSS/SCSS issues**: `npm run css-fix`

### Testing
For theme development testing:
- **Test with development config**: `npm run dev`
- **Test demo site**: `npm run demo-dev`
- **Test production demo**: `npm run demo-production`

## Code Architecture

### Directory Structure
- **_posts/**: Blog posts in Markdown format with YYYY-MM-DD prefix
- **_page/**: Special pages outside of blog posts
- **_layouts/**: Jekyll layout templates (article, home, archive, etc.)
- **_includes/**: Reusable components and partials
- **_sass/**: SCSS stylesheets organized by component and theme
- **_data/**: YAML configuration files for navigation, authors, locale
- **assets/**: Images, CSS compilation entry point, and static assets

### Key Configuration Files
- **_config.yml**: Main Jekyll configuration (site settings, author info, theme)
- **Gemfile**: Ruby dependencies (Jekyll, GitHub Pages, theme)
- **package.json**: Node.js scripts and development dependencies

### Theme System
The blog uses a skinning system with multiple themes:
- Available skins: default, dark, forest, ocean, chocolate, orange
- Syntax highlighting themes: default, tomorrow variants
- Configure in _config.yml: `text_skin` and `highlight_theme`

### Content Types
1. **Blog Posts** (_posts/): Standard blog entries with front matter
2. **Pages** (_page/): Standalone pages with custom layouts
3. **Documentation** (docs/): Theme documentation and examples

### Important Patterns
- Posts use front matter for metadata (title, tags, categories, author)
- Layouts inherit from base.html through Jekyll's layout system
- Components are modular and located in _includes/
- SCSS files use a component-based organization
- Responsive design with mobile-first approach

## Jekyll Collections

The site uses multiple collections beyond standard posts:
- **docs**: Theme documentation (output: true)
- **page**: Special pages with custom layouts (output: true)
- **articles**: Additional article collection (output: true)

Collections are configured in `_config.yml` under `collections:` with output settings.

## Markdown Enhancements

The blog supports enhanced markdown features (configured in _config.yml):
- **MathJax**: Mathematical expressions rendering (`mathjax: true`)
- **Mermaid**: Diagram and flowchart support (`mermaid: true`)
- **Chart**: Chart.js integration (`chart: true`)

These can be enabled/disabled per post using front matter.

## Front Matter Requirements

### Post Front Matter
```yaml
---
title: Post Title
key: unique-identifier (optional)
tags:
  - tag1
  - tag2
categories: category-name
comments: true # Enable Disqus comments
aside:
  toc: true # Show table of contents
show_edit_on_github: true
pageview: true # Enable page view tracking
---
```

### Default Values
Posts automatically inherit these defaults from _config.yml:
- layout: article
- license: true (CC-BY-NC-4.0)
- category: post
- aside.toc: true
- show_edit_on_github: true
- pageview: true

## SCSS Architecture

The main stylesheet entry point is `assets/css/main.scss` which imports in order:
1. Theme skin (based on site.text_skin)
2. Syntax highlighting theme
3. Common utilities and variables
4. Components (button, image, card, hero, menu, toc, item)
5. Animations (fade-in variants)
6. Site components (article, header, footer, search)
7. Additional styles (alert, tag, photo-frame, iframe)
8. Layout styles (base, page, article, articles, archive, home, landing, 404)

When modifying styles, follow the existing component-based organization in `_sass/`.

## Multilingual Support

The theme supports multiple languages configured in `_data/locale.yml`:
- Navigation items in `_data/navigation.yml` support language-specific titles
- Language is set in `_config.yml` with `lang: kr` (currently Korean)
- Supported languages: en, zh, zh-Hans, zh-Hant, kr

## Jekyll Plugins

The site uses these Jekyll plugins (via github-pages gem):
- **jekyll-feed**: RSS/Atom feed generation
- **jekyll-paginate**: Blog post pagination (5 posts per page)
- **jekyll-sitemap**: Sitemap.xml generation
- **jemoji**: GitHub emoji support

## Image Handling

Images are stored in `assets/images/` with subdirectories for different content:
- Blog post images: Referenced using GitHub raw URLs
- Example: `![alt text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/folder/image.png)`

## Deployment Considerations

- The site is configured for GitHub Pages deployment
- Repository: `rokrokss/blog` (master branch)
- CNAME file contains custom domain: rokrokss.com
- Excluded files from build: docs/, test/, node_modules/, screenshots/

## Analytics and Comments

- **Analytics**: Google Analytics enabled (tracking_id in _config.yml)
- **Comments**: Disqus integration (shortname: rokrokss)
- **Page views**: LeanCloud integration for view counting (optional)

## Development Tips

- When changing _config.yml, restart the Jekyll server
- Use `bundle exec` prefix to ensure correct gem versions
- The `-t` flag enables trace mode for debugging
- The `-H 0.0.0.0` flag allows network access for mobile testing

## SEO Guidelines for Blog Posts

### Essential Front Matter for SEO
```yaml
---
title: 포스트 제목 (60자 이내 권장)
excerpt: 포스트 요약 (160자 이내, 검색 결과에 표시됨)
tags:
  - 관련태그1
  - 관련태그2
categories: 카테고리명
image: /assets/images/post-thumbnail.jpg # 소셜 미디어 공유시 표시될 이미지
date: 2025-01-01 # 게시 날짜
modify_date: 2025-01-15 # 수정 날짜 (선택사항)
---
```

### SEO Best Practices
1. **제목 최적화**
   - 주요 키워드를 제목 앞부분에 배치
   - 60자 이내로 작성 (검색 결과에서 잘림 방지)
   - 명확하고 구체적인 제목 사용

2. **Excerpt (요약문) 작성**
   - 160자 이내로 포스트의 핵심 내용 요약
   - 주요 키워드 자연스럽게 포함
   - 검색 결과와 소셜 미디어에서 표시됨

3. **이미지 최적화**
   - 대표 이미지 설정 (image: 필드 사용)
   - 이미지 파일명은 설명적으로 (예: claude-code-tutorial.jpg)
   - Alt 텍스트 반드시 포함: `![설명적인 alt 텍스트](이미지경로)`

4. **내용 구조화**
   - H2, H3 태그를 사용한 계층적 구조
   - 주요 키워드를 자연스럽게 분산
   - 목차 자동 생성 활용 (aside.toc: true)

5. **내부 링크**
   - 관련 포스트끼리 서로 링크
   - 앵커 텍스트는 설명적으로

### 기술적 SEO (자동 처리됨)
- Open Graph 메타 태그 ✓
- Twitter Cards ✓
- 구조화된 데이터 (Schema.org) ✓
- Sitemap 자동 생성 ✓
- robots.txt ✓
- Lazy loading for images ✓
- Preconnect for external resources ✓

### 추가 권장사항
- **이미지 크기**: 대표 이미지는 1200x630px 권장 (Facebook/Twitter 최적 크기)
- **이미지 포맷**: WebP 또는 최적화된 JPEG 사용
- **파일명**: 한글 파일명 대신 영문 사용 (SEO 친화적)
- **URL 구조**: 날짜 기반 URL이 자동 생성됨 (permalink: date)