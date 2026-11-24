#!/usr/bin/env python3
"""Boynton Solution Discovery PreToolUse advisory hook — protect approved artifacts.

Read-only. Never blocks. Always exits 0. When an Edit/Write targets a governed
artifact whose on-disk frontmatter is already status: Approved, it emits an advisory
reminding that approved artifacts should change only through a human-governed change
process (see change-log.md), not be edited silently.

Run with `python3 -I`; this script adds its own directory to sys.path explicitly.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _frontmatter import (  # noqa: E402
    read_hook_input, tool_file_path, is_governed, read_text,
    parse_frontmatter, emit,
)


def main():
    payload = read_hook_input()
    path = tool_file_path(payload)
    if not is_governed(path):
        emit()  # not our concern — stay silent

    text = read_text(path)
    if text is None:
        emit()  # new file or unreadable — nothing approved to protect

    fm = parse_frontmatter(text)
    if fm and fm.get("status") == "Approved":
        emit(system_message=(
            f"[boynton-solution-discovery] {os.path.basename(path)} is currently "
            "status: Approved. Changing an approved artifact should go through a "
            "human-governed change process: record the change in "
            "project/governance/change-log.md and re-confirm with the approver. "
            "(Advisory only — this edit is not blocked.)"
        ))

    emit()  # clean — silent


if __name__ == "__main__":
    main()
