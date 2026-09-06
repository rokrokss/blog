#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

# macOS ships an older Ruby; use the project's Homebrew Ruby when needed.
if ! ruby -e 'exit(Gem::Version.new(RUBY_VERSION) >= Gem::Version.new("3.3") ? 0 : 1)' 2>/dev/null; then
  if command -v brew >/dev/null 2>&1; then
    ruby_prefix="$(brew --prefix ruby@3.3)"
    if [ -x "$ruby_prefix/bin/ruby" ]; then
      export PATH="$ruby_prefix/bin:$PATH"
    fi
  fi
fi

exec bundle exec jekyll "$@"
