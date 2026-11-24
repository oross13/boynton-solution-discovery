#!/usr/bin/env bash
# Validate the Boynton marketplace and the boynton-solution-discovery plugin.
# Read-only: runs `claude plugin validate`. Makes no changes to ~/.claude.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN_DIR="$REPO_ROOT/plugins/boynton-solution-discovery"

if ! command -v claude >/dev/null 2>&1; then
  echo "error: 'claude' CLI not found on PATH." >&2
  echo "Install Claude Code, then re-run this script." >&2
  exit 127
fi

STRICT=""
if [[ "${1:-}" == "--strict" ]]; then
  STRICT="--strict"
fi

echo "==> Validating plugin: $PLUGIN_DIR"
claude plugin validate "$PLUGIN_DIR" $STRICT

echo "==> Validating marketplace: $REPO_ROOT"
claude plugin validate "$REPO_ROOT" $STRICT

echo "==> Validation complete."
