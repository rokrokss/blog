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
