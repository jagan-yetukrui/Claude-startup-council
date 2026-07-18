#!/usr/bin/env bash
# Install the council skill for Claude Code by linking this repo into your skills directory.
#
# Usage:
#   git clone <repo-url> council && cd council && ./install.sh
#
# Or skip the script entirely and clone straight into place:
#   git clone <repo-url> ~/.claude/skills/council
set -euo pipefail

SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="$SKILLS_DIR/council"

mkdir -p "$SKILLS_DIR"

if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
  echo "A non-symlink already exists at $TARGET."
  echo "Move it aside first, or clone this repo directly to that path."
  exit 1
fi

ln -sfn "$REPO_DIR" "$TARGET"
echo "Linked $TARGET -> $REPO_DIR"

if command -v python3 >/dev/null 2>&1; then
  python3 "$REPO_DIR/scripts/score.py" --self-test >/dev/null && echo "score.py: OK"
  python3 "$REPO_DIR/scripts/ledger.py" --self-test >/dev/null && echo "ledger.py: OK"
else
  echo "note: python3 not found — the scoring/ledger scripts need it at runtime."
fi

echo "Done. Restart Claude Code, then run:  /council"
