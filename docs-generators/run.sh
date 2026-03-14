#!/usr/bin/env bash
# docs-generators/run.sh — Per-repo generator runner for Documentation
# Called by ~/.config/git/hooks/pre-commit on every commit

set -euo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "[docs-generators] Running generators..."

# Generator: AGENT_MANIFEST.md
bash "$REPO_ROOT/docs-generators/gen-manifest.sh"
git add AGENT_MANIFEST.md
echo "[docs-generators] AGENT_MANIFEST.md updated"

exit 0
