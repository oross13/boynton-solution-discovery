#!/usr/bin/env python3
"""Tests for validate_handoff.py. Run: python3 -I test_validate_handoff.py

Stdlib-only (unittest). Writes temporary fixtures; modifies no repo files.
"""
import hashlib
import os
import re
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_handoff as vh  # noqa: E402

VALID = """\
---
document: framework-kickoff-prompt
project: facilities-maintenance
version: 0.1.0
status: Draft
created: 2026-11-25
approved_by: null
approved_at: null
handoff_standard: boynton-discovery-to-engineering
handoff_standard_version: "1.0"
target_framework: bsef@bsef
target_framework_min_version: "1.0.0"
confirmed_by: Oscar Ross
confirmed_at: 2026-11-25
discovery_plugin: boynton-solution-discovery@boynton
discovery_plugin_version: "0.1.0"
source_deliverables:
  - project/discovery/01-solution-discovery-brief.md
  - project/discovery/05-implementation-roadmap.md
completeness:
  required_complete: true
  conditional_present: [integrations]
  open_questions_count: 0
branding:
  mode: default-dole
  alternative: null
  document_presentation_logo: via-approved-templates
  ui_logo:
    status: pending
    asset_ref: null
  ui_brand_reference:
    source: powerpoint-dole-template-2025
    palette: ["#001489", "#78BE20", "#3A913F"]
    typography: "Lato"
    confirmation: proposed
  visual_exceptions: none
  open_questions: []
  decision_source: 03-assumptions-risks-decisions.md; confirmed by a human
---

# Project Kickoff — Facilities Maintenance

Body text here.
"""


def write_tmp(text):
    fd, path = tempfile.mkstemp(suffix=".md")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def errors_for(text):
    path = write_tmp(text)
    try:
        return vh.validate_file(path)
    finally:
        os.remove(path)


class HandoffValidatorTests(unittest.TestCase):
    def assertHasError(self, errors, needle):
        self.assertTrue(
            any(needle in e for e in errors),
            msg=f"expected an error containing {needle!r}; got {errors}",
        )

    def test_valid_handoff_passes(self):
        self.assertEqual(errors_for(VALID), [])

    def test_approved_by_set_is_rejected(self):
        bad = VALID.replace("approved_by: null", "approved_by: Oscar Ross")
        self.assertHasError(errors_for(bad), "approved_by MUST be null")

    def test_approved_at_set_is_rejected(self):
        bad = VALID.replace("approved_at: null", "approved_at: 2026-11-25")
        self.assertHasError(errors_for(bad), "approved_at MUST be null")

    def test_confirmed_by_null_is_rejected(self):
        bad = VALID.replace("confirmed_by: Oscar Ross", "confirmed_by: null")
        self.assertHasError(errors_for(bad), "confirmed_by MUST be set")

    def test_confirmed_by_placeholder_is_rejected(self):
        bad = VALID.replace("confirmed_by: Oscar Ross", "confirmed_by: <human>")
        self.assertHasError(errors_for(bad), "confirmed_by MUST be set")

    def test_wrong_handoff_standard_is_rejected(self):
        bad = VALID.replace(
            "handoff_standard: boynton-discovery-to-engineering",
            "handoff_standard: something-else",
        )
        self.assertHasError(errors_for(bad), "handoff_standard must be")

    def test_bad_standard_version_is_rejected(self):
        bad = VALID.replace('handoff_standard_version: "1.0"', 'handoff_standard_version: "v1"')
        self.assertHasError(errors_for(bad), "handoff_standard_version must be a MAJOR.MINOR")

    def test_invalid_status_is_rejected(self):
        bad = VALID.replace("status: Draft", "status: Cooking")
        self.assertHasError(errors_for(bad), "status must be one of")

    def test_empty_source_deliverables_is_rejected(self):
        bad = VALID.replace(
            "source_deliverables:\n"
            "  - project/discovery/01-solution-discovery-brief.md\n"
            "  - project/discovery/05-implementation-roadmap.md\n",
            "source_deliverables: []\n",
        )
        self.assertHasError(errors_for(bad), "source_deliverables must be a non-empty list")

    def test_negative_open_questions_count_is_rejected(self):
        bad = VALID.replace("open_questions_count: 0", "open_questions_count: -1")
        self.assertHasError(errors_for(bad), "open_questions_count must be a non-negative integer")

    def test_invalid_branding_mode_is_rejected(self):
        bad = VALID.replace("mode: default-dole", "mode: rainbow")
        self.assertHasError(errors_for(bad), "branding.mode must be one of")

    def test_approved_alternative_without_name_is_rejected(self):
        bad = VALID.replace("mode: default-dole", "mode: approved-alternative")
        self.assertHasError(errors_for(bad), "branding.alternative must be set")

    def test_ui_logo_approved_without_asset_is_rejected(self):
        bad = VALID.replace("    status: pending", "    status: approved")
        self.assertHasError(errors_for(bad), "branding.ui_logo.asset_ref must be set")

    def test_ui_logo_pending_with_asset_is_rejected(self):
        bad = VALID.replace("    asset_ref: null", "    asset_ref: some-logo.svg")
        self.assertHasError(errors_for(bad), "branding.ui_logo.asset_ref must be null")

    def test_missing_branding_is_rejected(self):
        idx = VALID.index("branding:")
        bad = VALID[:idx] + "---\n\n# body\n"
        self.assertHasError(errors_for(bad), "branding must be a mapping")

    def test_tab_in_frontmatter_is_parse_error(self):
        bad = VALID.replace("  ui_logo:", "\tui_logo:")
        self.assertHasError(errors_for(bad), "parse error")

    def test_odd_indentation_is_parse_error(self):
        bad = VALID.replace("    status: pending", "   status: pending")
        self.assertHasError(errors_for(bad), "parse error")

    def test_missing_closing_fence_is_parse_error(self):
        bad = VALID.replace("\n---\n\n# Project Kickoff", "\n\n# Project Kickoff")
        self.assertHasError(errors_for(bad), "parse error")


# --- Shared golden fixtures mirrored from BSEF (F3) ---------------------------------------
# Byte-identical files from plugins/bsef/scripts/fixtures/handoff/. Discovery owns the canonical
# spec, so these are the same examples both repos test. Discovery's validator is ERRORS-ONLY (no
# warnings/exit-2, no supported-major gate, no min-version comparison), so some BSEF ERROR/WARNING
# outcomes are a clean pass here BY DESIGN — documented per fixture in `note`. We do NOT change
# Discovery's validator/schema/version policy to force parity.
GOLDEN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "handoff")
MANIFEST = os.path.join(GOLDEN_DIR, "fixtures.sha256")

# Documentation that lives beside the fixtures but is NOT a handoff fixture:
NON_FIXTURE_MD = {"CONFORMANCE.md"}
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _fixture_names(dirpath):
    """Handoff-fixture *.md files only (excludes CONFORMANCE.md and any non-fixture docs)."""
    return {f for f in os.listdir(dirpath)
            if f.endswith(".md") and f not in NON_FIXTURE_MD}


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_manifest(path):
    """Parse '<sha256>  <name>' lines.

    Ignores blank lines and '#' comments. Raises ValueError on a malformed line, a digest that is not a
    lowercase 64-hex SHA-256, or a duplicate filename. Returns {name: digest}.
    """
    pinned = {}
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                raise ValueError(f"{path}:{lineno}: malformed manifest line: {raw!r}")
            digest, name = parts[0].strip(), parts[1].strip()
            if not _SHA256_RE.match(digest):
                raise ValueError(f"{path}:{lineno}: invalid SHA-256 {digest!r}")
            if name in pinned:
                raise ValueError(f"{path}:{lineno}: duplicate manifest entry {name!r}")
            pinned[name] = digest
    return pinned


GOLDEN_EXPECT = {
    # Valid / clean in both repos
    "valid-clean.md":                       {"errors": False},
    "valid-min-version-equal.md":           {"errors": False},
    # BSEF emits advisory WARNINGS (exit 2); Discovery is errors-only -> clean pass (intentional)
    "valid-open-items.md":                  {"errors": False, "note": "BSEF warns O1/O2 (logo pending, palette proposed); Discovery errors-only"},
    "warn-unknown-additive.md":             {"errors": False, "note": "BSEF warns unknown-additive; Discovery does not flag it"},
    "warn-required-complete-false.md":      {"errors": False, "note": "BSEF warns self-declared incomplete; Discovery errors-only"},
    "warn-wrong-target-framework.md":       {"errors": False, "note": "BSEF warns target_framework mismatch; Discovery does not check its value"},
    # Errors in both repos, same reason
    "invalid-unconfirmed.md":               {"errors": True, "has": ["confirmed_by MUST be set"]},
    "invalid-approved-set.md":              {"errors": True, "has": ["approved_by MUST be null"]},
    "invalid-missing-required.md":          {"errors": True, "has": ["'target_framework'"]},
    "invalid-malformed-branding.md":        {"errors": True, "has": ["branding.mode must be one of", "branding.ui_logo must be a mapping"]},
    "invalid-empty-source-deliverables.md": {"errors": True, "has": ["source_deliverables must be a non-empty list"]},
    "invalid-parse-tab.md":                 {"errors": True, "has": ["parse error"]},
    "invalid-bad-standard-version.md":      {"errors": True, "has": ["MAJOR.MINOR"]},
    "invalid-bare-standard-version.md":     {"errors": True, "has": ["MAJOR.MINOR"]},
    # Consumer-gated by BSEF only; Discovery (the producer) has no version-support gate (intentional)
    "invalid-unsupported-version.md":       {"errors": False, "note": "consumer-gated: BSEF rejects unsupported MAJOR; Discovery has no version-support gate"},
    "invalid-min-version-too-high.md":      {"errors": False, "note": "consumer-gated: BSEF rejects min>installed; Discovery has no min-version comparison"},
    # --- v1.1 enrichment fixtures (producer is errors-only; body sections are not validated here) ---
    "valid-enriched-full.md":               {"errors": False, "note": "v1.1 full enrichment; approved branding"},
    "valid-enriched-partial.md":            {"errors": False, "note": "v1.1 partial; BSEF warns O1/O2, producer errors-only"},
    "valid-v11-no-enrichment.md":           {"errors": False, "note": "bare v1.1; declares 1.1, no enrichment"},
    "valid-enriched-hint-no-body.md":       {"errors": False, "note": "hint set, body absent -> intake gap, not a structural error"},
    "valid-enriched-contradictory.md":      {"errors": False, "note": "semantic contradiction -> human review at intake, not structural"},
}


class GoldenFixtureTests(unittest.TestCase):
    """Run the shared BSEF golden fixtures through Discovery's errors-only validator."""

    def test_manifest_covers_every_fixture(self):
        on_disk = _fixture_names(GOLDEN_DIR)
        self.assertEqual(
            on_disk, set(GOLDEN_EXPECT),
            msg="GOLDEN_EXPECT and fixtures/handoff/*.md are out of sync",
        )

    def test_each_fixture_matches_discovery_contract(self):
        for name, exp in GOLDEN_EXPECT.items():
            with self.subTest(fixture=name):
                errors = vh.validate_file(os.path.join(GOLDEN_DIR, name))
                self.assertEqual(
                    bool(errors), exp["errors"],
                    msg=f"{name}: errors={errors}",
                )
                for needle in exp.get("has", []):
                    self.assertTrue(
                        any(needle in e for e in errors),
                        msg=f"{name}: expected error containing {needle!r}; got {errors}",
                    )


class ManifestIntegrityTests(unittest.TestCase):
    """CANONICAL manifest integrity: fixtures.sha256 must match Discovery's own fixtures.

    Discovery owns the contract, so this manifest is the source of truth BSEF vendors. Offline,
    stdlib-only. Detects duplicate/invalid-format (via _read_manifest), missing, unexpected, and mismatch.
    """

    def test_manifest_matches_fixture_inventory(self):
        pinned = _read_manifest(MANIFEST)          # raises on duplicate / invalid SHA-256
        fixtures = _fixture_names(GOLDEN_DIR)
        self.assertEqual(sorted(set(pinned) - fixtures), [], "manifest lists fixtures with no file")
        self.assertEqual(sorted(fixtures - set(pinned)), [], "fixture files missing from manifest")

    def test_each_fixture_matches_its_manifest_hash(self):
        for name, digest in _read_manifest(MANIFEST).items():
            with self.subTest(fixture=name):
                self.assertEqual(_sha256(os.path.join(GOLDEN_DIR, name)), digest,
                                 msg=f"{name}: fixture bytes do not match fixtures.sha256")


if __name__ == "__main__":
    unittest.main(verbosity=2)
