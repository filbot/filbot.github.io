#!/usr/bin/env bash
# Stop hook: when site sources have uncommitted changes, make sure the
# production build still passes before Claude hands the turn back.
input=$(cat)
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false')" = true ] && exit 0

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
[ -z "$(git status --porcelain -- content layouts assets static archetypes hugo.toml)" ] && exit 0

out=$(mktemp -d)
trap 'rm -rf "$out"' EXIT
if ! log=$(hugo --gc --minify --logLevel error -d "$out" 2>&1); then
  printf 'Hugo production build failed:\n%s\n' "$log" >&2
  exit 2
fi
