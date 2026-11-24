#!/usr/bin/env python3
"""Boynton Solution Discovery PostToolUse advisory hook — frontmatter check.

Read-only. Never blocks. Always exits 0. Emits a JSON advisory only when a governed
discovery/governance artifact has missing or invalid frontmatter. Skips
approval-records.md (covered by validate_approval_record.py).

Run with `python3 -I`; this script adds its own directory to sys.path explicitly.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _frontmatter import (  # noqa: E402
    read_hook_input, tool_file_path, is_governed, read_text,
    parse_frontmatter, is_nullish, emit,
    REQUIRED_FIELDS, VALID_STATUS,
)


def main():
    payload = read_hook_input()
    path = tool_file_path(payload)
    if not is_governed(path):
        emit()  # not our concern — stay silent
    if os.path.basename(path) == "approval-records.md":
        emit()  # handled by the dedicated hook

    text = read_text(path)
    if text is None:
        emit()  # cannot read (e.g. mid-write race) — do not guess

    fm = parse_frontmatter(text)
    if fm is None:
        emit(system_message=(
            f"[boynton-solution-discovery] {os.path.basename(path)} is a governed "
            "artifact but has no YAML frontmatter. Add the 7 governed fields "
            "(document, project, version, status, created, approved_by, approved_at)."
        ))

    issues = []
    missing = [k for k in REQUIRED_FIELDS if k not in fm]
    if missing:
        issues.append(f"missing frontmatter fields: {', '.join(missing)}")

    status = fm.get("status")
    if status not in VALID_STATUS:
        issues.append(
            f"status '{status}' is not one of {sorted(VALID_STATUS)}"
        )

    if status == "Approved":
        if is_nullish(fm.get("approved_by")) or is_nullish(fm.get("approved_at")):
            issues.append(
                "status is Approved but approved_by/approved_at is empty — "
                "approval must be recorded by a human, not inferred"
            )

    if issues:
        emit(system_message=(
            f"[boynton-solution-discovery] {os.path.basename(path)} frontmatter "
            f"advisory: " + "; ".join(issues) + "."
        ))

    emit()  # clean — silent


if __name__ == "__main__":
    main()
