#!/usr/bin/env bash
# gen-manifest.sh — Generates AGENT_MANIFEST.md from System/ contents
# Delegates to gen-manifest.py (bash 3.2 on macOS lacks associative arrays)

set -euo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel)"
python3 "$REPO_ROOT/docs-generators/gen-manifest.py" "$REPO_ROOT"
