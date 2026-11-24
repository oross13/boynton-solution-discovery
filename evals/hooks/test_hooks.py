#!/usr/bin/env python3
"""Deterministic tests for the Boynton Solution Discovery advisory hooks.

Asserts the hook contract for all three hooks:
  * advisory (non-empty stdout) when a governed artifact violates a rule,
  * silent (empty stdout) when the artifact is clean or out of scope,
  * always exit 0,
  * never mutates the target file (verified by SHA-256 before/after).

Pure standard library. Run: `python3 evals/hooks/test_hooks.py` (exit 0 = pass).
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SCRIPTS = os.path.join(ROOT, "plugins", "boynton-solution-discovery", "scripts")

PRE = os.path.join(SCRIPTS, "protect_approved_artifacts.py")
FM = os.path.join(SCRIPTS, "validate_artifact_frontmatter.py")
AR = os.path.join(SCRIPTS, "validate_approval_record.py")

CLEAN = """---
document: solution-discovery-brief
project: demo
version: 0.1.0
status: Draft
created: 2026-11-24
approved_by: null
approved_at: null
---

# Brief
"""

NO_FM = "# Brief with no frontmatter\n"

APPROVED_NO_APPROVER = """---
document: solution-discovery-brief
project: demo
version: 0.1.0
status: Approved
created: 2026-11-24
approved_by: null
approved_at: null
---

# Approved but nobody approved it
"""

APPROVED_OK = """---
document: solution-discovery-brief
project: demo
version: 0.1.0
status: Approved
created: 2026-11-24
approved_by: Oscar Ross
approved_at: 2026-11-24
---

# Properly approved
"""

APPROVAL_REC_BAD = """---
document: approval-records
project: demo
version: 0.1.0
status: Draft
created: 2026-11-24
approved_by: null
approved_at: null
---

# Approval Records

| Gate | Artifact(s) | Decision | approved_by | approved_at | Notes |
|---|---|---|---|---|---|
| Solution Confirmation | 01-...md | Approved | | | self-approval attempt |
"""

APPROVAL_REC_OK = APPROVAL_REC_BAD.replace(
    "| Solution Confirmation | 01-...md | Approved | | | self-approval attempt |",
    "| Solution Confirmation | 01-...md | Approved | Oscar Ross | 2026-11-24 | ok |",
)

failures = []


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def run(hook, file_path):
    payload = json.dumps({"tool_input": {"file_path": file_path}})
    proc = subprocess.run(
        [sys.executable, "-I", hook],
        input=payload, capture_output=True, text=True,
    )
    return proc


def check(name, hook, content, filename, subdir, want_advisory):
    with tempfile.TemporaryDirectory() as td:
        d = os.path.join(td, "project", subdir)
        os.makedirs(d, exist_ok=True)
        fpath = os.path.join(d, filename)
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(content)
        before = sha(fpath)
        proc = run(hook, fpath)
        after = sha(fpath)

        if proc.returncode != 0:
            failures.append(f"{name}: exit {proc.returncode} (must be 0); stderr={proc.stderr!r}")
        if before != after:
            failures.append(f"{name}: hook mutated the file (SHA changed)")
        advised = bool(proc.stdout.strip())
        if want_advisory and not advised:
            failures.append(f"{name}: expected an advisory, got silence")
        if not want_advisory and advised:
            failures.append(f"{name}: expected silence, got advisory: {proc.stdout!r}")
        # Any emitted stdout must be valid JSON.
        if advised:
            try:
                json.loads(proc.stdout)
            except Exception as e:
                failures.append(f"{name}: stdout is not valid JSON ({e})")


def check_nongoverned(name, hook):
    with tempfile.TemporaryDirectory() as td:
        fpath = os.path.join(td, "notes.md")
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(NO_FM)
        proc = run(hook, fpath)
        if proc.returncode != 0:
            failures.append(f"{name}: exit {proc.returncode} on non-governed path")
        if proc.stdout.strip():
            failures.append(f"{name}: should be silent on non-governed path, got {proc.stdout!r}")


def main():
    # validate_artifact_frontmatter
    check("FM clean", FM, CLEAN, "01-solution-discovery-brief.md", "discovery", False)
    check("FM missing", FM, NO_FM, "01-solution-discovery-brief.md", "discovery", True)
    check("FM approved-no-approver", FM, APPROVED_NO_APPROVER,
          "01-solution-discovery-brief.md", "discovery", True)
    check_nongoverned("FM non-governed", FM)

    # validate_approval_record
    check("AR self-approval", AR, APPROVAL_REC_BAD, "approval-records.md", "governance", True)
    check("AR proper approval", AR, APPROVAL_REC_OK, "approval-records.md", "governance", False)

    # protect_approved_artifacts (PreToolUse: inspects on-disk state)
    check("PRE approved", PRE, APPROVED_OK, "01-solution-discovery-brief.md", "discovery", True)
    check("PRE draft", PRE, CLEAN, "01-solution-discovery-brief.md", "discovery", False)
    check_nongoverned("PRE non-governed", PRE)

    if failures:
        print("FAIL:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("All hook-contract tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
