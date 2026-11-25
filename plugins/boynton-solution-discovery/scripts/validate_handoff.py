#!/usr/bin/env python3
"""Validate a Boynton Discovery-to-Engineering handoff (deliverable 06).

Checks that the YAML frontmatter of a `06-framework-kickoff-prompt.md` handoff is:
  * syntactically valid, tab-free, and consistently 2-space indented;
  * independently parseable (by this stdlib parser; additionally cross-checked
    with PyYAML when that happens to be installed);
  * complete per the Handoff Standard v1.0 required/optional/branding fields;
  * governed correctly — `approved_by`/`approved_at` stay null (engineering
    approval is BSEF's), while `confirmed_by`/`confirmed_at` are set (Discovery
    confirmation provenance).

Dependency-free: safe to run with `python3 -I validate_handoff.py <file.md>`.
Unlike the advisory hooks, this is a dev/test validator and exits non-zero on
failure. It never modifies any file.
"""
from __future__ import annotations

import re
import sys

HANDOFF_STANDARD = "boynton-discovery-to-engineering"
VALID_STATUS = {"Draft", "Under Review", "Approved", "Superseded"}
VALID_MODE = {"default-dole", "approved-alternative"}
VALID_UI_LOGO_STATUS = {"pending", "approved"}
VALID_CONFIRMATION = {"proposed", "approved"}
SEMVER_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")
STD_VER_RE = re.compile(r"^\d+\.\d+$")
PLACEHOLDER_RE = re.compile(r"^<.*>$")


class ParseError(ValueError):
    """Raised when the frontmatter is not syntactically valid YAML (our subset)."""


# --------------------------------------------------------------------------- #
# Frontmatter extraction + a small, strict, stdlib-only YAML-subset parser.
# Supports: block maps, block sequences (`- item`), inline flow lists (`[...]`),
# quoted/plain scalars, `null`/`~`/empty -> None, ints, booleans, and `#` comments.
# --------------------------------------------------------------------------- #

def extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        raise ParseError("file does not start with a '---' frontmatter fence")
    rest = text.split("\n", 1)[1] if "\n" in text else ""
    end = rest.find("\n---")
    if end == -1:
        raise ParseError("no closing '---' frontmatter fence found")
    return rest[:end]


def _strip_comment(line: str) -> str:
    out = []
    quote = None
    i = 0
    while i < len(line):
        c = line[i]
        if quote:
            out.append(c)
            if c == quote:
                quote = None
        elif c in ('"', "'"):
            quote = c
            out.append(c)
        elif c == "#" and (i == 0 or line[i - 1] in (" ", "\t")):
            break
        else:
            out.append(c)
        i += 1
    return "".join(out).rstrip()


def _scalar(token: str):
    token = token.strip()
    if token.startswith("[") and token.endswith("]"):
        inner = token[1:-1].strip()
        if not inner:
            return []
        return [_scalar(p) for p in _split_flow(inner)]
    if len(token) >= 2 and token[0] == token[-1] and token[0] in ('"', "'"):
        return token[1:-1]
    low = token.lower()
    if token == "" or low in ("null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    if re.fullmatch(r"-?\d+", token):
        return int(token)
    return token


def _split_flow(inner: str):
    parts, buf, quote = [], [], None
    for c in inner:
        if quote:
            buf.append(c)
            if c == quote:
                quote = None
        elif c in ('"', "'"):
            quote = c
            buf.append(c)
        elif c == ",":
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(c)
    if buf:
        parts.append("".join(buf).strip())
    return [p for p in parts if p != ""]


def parse_frontmatter(text: str):
    lines = []
    for raw in text.splitlines():
        if "\t" in raw:
            raise ParseError(f"tab character in frontmatter line: {raw!r}")
        stripped = _strip_comment(raw)
        if stripped.strip() == "":
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        if indent % 2 != 0:
            raise ParseError(f"indentation is not a multiple of 2: {raw!r}")
        lines.append((indent, stripped.strip()))

    pos = 0

    def parse(indent: int):
        nonlocal pos
        result = None
        while pos < len(lines):
            ind, content = lines[pos]
            if ind < indent:
                break
            if ind > indent:
                raise ParseError(f"unexpected indentation at: {content!r}")
            if content.startswith("- "):
                if result is None:
                    result = []
                elif not isinstance(result, list):
                    raise ParseError(f"list item mixed into a map at: {content!r}")
                pos += 1
                result.append(_scalar(content[2:]))
            else:
                if result is None:
                    result = {}
                elif not isinstance(result, dict):
                    raise ParseError(f"map key mixed into a list at: {content!r}")
                key, sep, val = content.partition(":")
                if not sep:
                    raise ParseError(f"line is neither a key nor a list item: {content!r}")
                key = key.strip()
                val = val.strip()
                pos += 1
                if val == "":
                    child = parse(indent + 2)
                    result[key] = {} if child is None else child
                else:
                    result[key] = _scalar(val)
        return result

    data = parse(0)
    if not isinstance(data, dict):
        raise ParseError("frontmatter is not a mapping")
    return data


# --------------------------------------------------------------------------- #
# Schema validation
# --------------------------------------------------------------------------- #

def _is_unset(v) -> bool:
    """None, empty string, or an unfilled <placeholder> all count as unset."""
    if v is None:
        return True
    if isinstance(v, str) and (v.strip() == "" or PLACEHOLDER_RE.match(v.strip())):
        return True
    return False


def validate(data: dict) -> list[str]:
    errs: list[str] = []

    def require_set(key):
        if key not in data or _is_unset(data[key]):
            errs.append(f"required field '{key}' is missing or unset")

    # Governed base fields
    if data.get("document") != "framework-kickoff-prompt":
        errs.append("document must be 'framework-kickoff-prompt'")
    require_set("project")
    v = data.get("version")
    if _is_unset(v) or not (isinstance(v, str) and SEMVER_RE.match(v)):
        errs.append("version must be a semver string (e.g. 0.1.0)")
    if data.get("status") not in VALID_STATUS:
        errs.append(f"status must be one of {sorted(VALID_STATUS)}")
    require_set("created")

    # The confirmed_* vs approved_* distinction (core governance rule)
    if not _is_unset(data.get("approved_by")):
        errs.append("approved_by MUST be null in a handoff (engineering approval is BSEF's)")
    if not _is_unset(data.get("approved_at")):
        errs.append("approved_at MUST be null in a handoff (engineering approval is BSEF's)")
    if _is_unset(data.get("confirmed_by")):
        errs.append("confirmed_by MUST be set (human Discovery confirmation provenance)")
    if _is_unset(data.get("confirmed_at")):
        errs.append("confirmed_at MUST be set (human Discovery confirmation provenance)")

    # Handoff standard identity + compatibility
    if data.get("handoff_standard") != HANDOFF_STANDARD:
        errs.append(f"handoff_standard must be '{HANDOFF_STANDARD}'")
    sv = data.get("handoff_standard_version")
    if _is_unset(sv) or not (isinstance(sv, str) and STD_VER_RE.match(sv)):
        errs.append("handoff_standard_version must be a MAJOR.MINOR string (e.g. '1.0')")
    require_set("target_framework")
    require_set("target_framework_min_version")

    # Provenance
    require_set("discovery_plugin")
    require_set("discovery_plugin_version")
    sd = data.get("source_deliverables")
    if not isinstance(sd, list) or len(sd) == 0:
        errs.append("source_deliverables must be a non-empty list")

    # Completeness block
    comp = data.get("completeness")
    if not isinstance(comp, dict):
        errs.append("completeness must be a mapping")
    else:
        if not isinstance(comp.get("required_complete"), bool):
            errs.append("completeness.required_complete must be a boolean")
        if not isinstance(comp.get("conditional_present"), list):
            errs.append("completeness.conditional_present must be a list")
        oqc = comp.get("open_questions_count")
        if not isinstance(oqc, int) or isinstance(oqc, bool) or oqc < 0:
            errs.append("completeness.open_questions_count must be a non-negative integer")

    # Branding block
    errs.extend(_validate_branding(data.get("branding")))
    return errs


def _validate_branding(b) -> list[str]:
    errs: list[str] = []
    if not isinstance(b, dict):
        return ["branding must be a mapping"]

    mode = b.get("mode")
    if mode not in VALID_MODE:
        errs.append(f"branding.mode must be one of {sorted(VALID_MODE)}")
    if mode == "approved-alternative" and _is_unset(b.get("alternative")):
        errs.append("branding.alternative must be set when mode is 'approved-alternative'")
    if _is_unset(b.get("document_presentation_logo")):
        errs.append("branding.document_presentation_logo must be set")

    ui_logo = b.get("ui_logo")
    if not isinstance(ui_logo, dict):
        errs.append("branding.ui_logo must be a mapping")
    else:
        status = ui_logo.get("status")
        if status not in VALID_UI_LOGO_STATUS:
            errs.append(f"branding.ui_logo.status must be one of {sorted(VALID_UI_LOGO_STATUS)}")
        asset = ui_logo.get("asset_ref")
        if status == "approved" and _is_unset(asset):
            errs.append("branding.ui_logo.asset_ref must be set when status is 'approved'")
        if status == "pending" and not _is_unset(asset):
            errs.append("branding.ui_logo.asset_ref must be null while status is 'pending'")

    ref = b.get("ui_brand_reference")
    if not isinstance(ref, dict):
        errs.append("branding.ui_brand_reference must be a mapping")
    else:
        if _is_unset(ref.get("source")):
            errs.append("branding.ui_brand_reference.source must be set")
        if not isinstance(ref.get("palette"), list) or len(ref.get("palette")) == 0:
            errs.append("branding.ui_brand_reference.palette must be a non-empty list")
        if _is_unset(ref.get("typography")):
            errs.append("branding.ui_brand_reference.typography must be set")
        if ref.get("confirmation") not in VALID_CONFIRMATION:
            errs.append(f"branding.ui_brand_reference.confirmation must be one of {sorted(VALID_CONFIRMATION)}")

    if "visual_exceptions" not in b or _is_unset(b.get("visual_exceptions")):
        errs.append("branding.visual_exceptions must be present (use 'none' when there are none)")
    if not isinstance(b.get("open_questions"), list):
        errs.append("branding.open_questions must be a list")
    if _is_unset(b.get("decision_source")):
        errs.append("branding.decision_source must be set")
    return errs


def _cross_check_pyyaml(fm_text: str, parsed: dict) -> list[str]:
    """If PyYAML is installed, confirm it parses the same frontmatter without error."""
    try:
        import yaml  # type: ignore
    except Exception:
        return []
    try:
        yaml.safe_load(fm_text)
    except Exception as exc:  # pragma: no cover - depends on optional dep
        return [f"PyYAML could not parse the frontmatter: {exc}"]
    return []


def validate_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    try:
        fm_text = extract_frontmatter(text)
        data = parse_frontmatter(fm_text)
    except ParseError as exc:
        return [f"frontmatter parse error: {exc}"]
    errs = validate(data)
    errs.extend(_cross_check_pyyaml(fm_text, data))
    return errs


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: validate_handoff.py <06-framework-kickoff-prompt.md>\n")
        return 2
    errors = validate_file(argv[1])
    if errors:
        sys.stderr.write(f"HANDOFF INVALID: {argv[1]}\n")
        for e in errors:
            sys.stderr.write(f"  - {e}\n")
        return 1
    sys.stdout.write(f"HANDOFF OK: {argv[1]}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
