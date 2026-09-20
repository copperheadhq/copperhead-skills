#!/usr/bin/env bash
# Link every skill in this repo into ~/.claude/skills/ so Claude Code picks it up.
# Symlinks, not copies: edit the skill here and the change is live immediately.
#
#   ./install.sh            link all skills
#   ./install.sh humanizer  link one
#   ./install.sh --list     show what is linked now

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO/skills"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

if [[ "${1:-}" == "--list" ]]; then
  for link in "$DEST"/*; do
    [[ -L "$link" ]] || continue
    target="$(readlink "$link")"
    [[ "$target" == "$SRC"/* ]] && printf '%s -> %s\n' "$(basename "$link")" "$target"
  done
  exit 0
fi

mkdir -p "$DEST"

if [[ $# -gt 0 ]]; then
  skills=("$@")
else
  skills=()
  for d in "$SRC"/*/; do skills+=("$(basename "$d")"); done
fi

for name in "${skills[@]}"; do
  from="$SRC/$name"
  to="$DEST/$name"

  if [[ ! -f "$from/SKILL.md" ]]; then
    echo "skip $name: no SKILL.md at $from" >&2
    continue
  fi

  if [[ -L "$to" ]]; then
    if [[ "$(readlink "$to")" == "$from" ]]; then
      echo "ok   $name (already linked)"
      continue
    fi
    rm "$to"
  elif [[ -e "$to" ]]; then
    echo "skip $name: $to exists and is not a symlink - move it aside first" >&2
    continue
  fi

  ln -s "$from" "$to"
  echo "link $name -> $from"
done
