#!/usr/bin/env python3
"""Boynton Solution Discovery PostToolUse advisory hook — approval-record check.

Read-only. Never blocks. Always exits 0. Flags any approval row marked 'Approved'
with no human approver recorded (potential AI self-approval). Applies to
project/governance/approval-records.md.

Run with `python3 -I`; this script adds its own directory to sys.path explicitly.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _frontmatter import (  # noqa: E402
    read_hook_input, tool_file_path, read_text, is_nullish, emit,
)


def main():
    payload = read_hook_input()
    path = tool_file_path(payload)
    if not path or os.path.basename(path) != "approval-records.md":
        emit()  # not the approval ledger — stay silent

    text = read_text(path)
    if text is None:
        emit()

    flagged = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # Expected columns: Gate | Artifact(s) | Decision | approved_by | approved_at | Notes
        if len(cells) < 5:
            continue
        gate, decision, approved_by, approved_at = (
            cells[0], cells[2], cells[3], cells[4]
        )
        if gate.lower().startswith("gate") is False and not gate.lower().startswith("solution"):
            # skip header/separator rows
            if gate.lower() in ("gate", "") or set(gate) <= set("-: "):
                continue
        if decision.strip().lower() == "approved" and (
            is_nullish(approved_by) or is_nullish(approved_at)
        ):
            flagged.append(gate or "(unnamed gate)")

    if flagged:
        emit(system_message=(
            "[boynton-solution-discovery] approval-records.md advisory: "
            f"{len(flagged)} row(s) marked 'Approved' with no human approver "
            f"recorded ({', '.join(flagged)}). An AI may recommend but must never "
            "record its own approval — a human sets approved_by/approved_at."
        ))

    emit()  # clean — silent


if __name__ == "__main__":
    main()
