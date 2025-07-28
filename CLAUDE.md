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