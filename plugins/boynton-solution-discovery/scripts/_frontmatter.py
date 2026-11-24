"""Shared helpers for Boynton Solution Discovery advisory hooks.

These hooks are ADVISORY ONLY: they never block a tool call, never modify any
file, and always exit 0. They emit a JSON object on stdout with a `systemMessage`
(and optional `hookSpecificOutput.additionalContext`) when they have advice.

No third-party imports. Safe to run with `python3 -I`.
"""
import json
import os
import re
import sys

# A "governed artifact" is a markdown file under project/discovery or
# project/governance — the discovery deliverables and governance ledgers.
GOVERNED_DIR_RE = re.compile(r"(^|/)project/(discovery|governance)/[^/]+\.md$")

REQUIRED_FIELDS = [
    "document", "project", "version", "status", "created",
    "approved_by", "approved_at",
]
VALID_STATUS = {"Draft", "Under Review", "Approved", "Superseded"}
NULLISH = {None, "", "null", "~", "None"}


def read_hook_input():
    """Parse the hook JSON delivered on stdin. Returns {} on any problem."""
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def tool_file_path(payload):
    """Best-effort extraction of the target file path from the tool input."""
    ti = (payload or {}).get("tool_input") or {}
    for key in ("file_path", "path", "notebook_path"):
        val = ti.get(key)
        if isinstance(val, str) and val:
            return val
    return None


def is_governed(path):
    if not path:
        return False
    norm = path.replace("\\", "/")
    return bool(GOVERNED_DIR_RE.search(norm))


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except Exception:
        return None


def parse_frontmatter(text):
    """Return a flat dict of top-level YAML frontmatter keys, or None."""
    if not text:
        return None
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if line[:1] not in (" ", "\t") and ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def is_nullish(value):
    return (value if value is not None else None) in NULLISH


def emit(system_message=None, context=None):
    """Emit an advisory and exit 0. Silence (no output) if nothing to say."""
    out = {}
    if system_message:
        out["systemMessage"] = system_message
    if context:
        out["hookSpecificOutput"] = {"additionalContext": context}
    if out:
        sys.stdout.write(json.dumps(out))
    sys.exit(0)
