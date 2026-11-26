# Handoff Conformance Table (canonical)

Owned by Boynton Solution Discovery; vendored verbatim into BSEF. Documentation, not a handoff fixture;
excluded from fixtures.sha256. Producer (Discovery) and consumer (BSEF) validators have intentionally
different responsibilities, so some fixtures have different expected outcomes. "S" = structural-validator
decision; "H" = semantic issue handled by BSEF human-reviewed project-intake (validator passes).

| Fixture | Discovery exit | BSEF exit | BSEF warnings | Kind | Reason |
|---|---|---|---|---|---|
| valid-clean.md | 0 | 0 | - | S | v1.0 fully resolved |
| valid-open-items.md | 0 | 2 | O2 pending, O1 proposed | S | v1.0 pending branding |
| valid-min-version-equal.md | 0 | 0 | - | S | min == installed |
| invalid-unconfirmed.md | 1 | 1 | - | S | confirmed_* null |
| invalid-approved-set.md | 1 | 1 | - | S | approved_* set |
| invalid-missing-required.md | 1 | 1 | - | S | missing target_framework |
| invalid-malformed-branding.md | 1 | 1 | - | S | branding structure |
| invalid-empty-source-deliverables.md | 1 | 1 | - | S | empty list |
| invalid-parse-tab.md | 1 | 1 | - | S | tab in frontmatter |
| invalid-bad-standard-version.md | 1 | 1 | - | S | bad MAJOR.MINOR |
| invalid-bare-standard-version.md | 1 | 1 | - | S | bare version |
| invalid-unsupported-version.md | 0 | 1 | - | S | consumer-only MAJOR gate |
| invalid-min-version-too-high.md | 0 | 1 | - | S | consumer-only min gate |
| warn-required-complete-false.md | 0 | 2 | required_complete is false | S | consumer warns incomplete |
| warn-unknown-additive.md | 0 | 2 | unknown additive field | S | consumer warns unknown top-level |
| warn-wrong-target-framework.md | 0 | 2 | target_framework is | S | consumer warns framework mismatch |
| valid-enriched-full.md | 0 | 0 | - | S | v1.1 full enrichment, approved branding |
| valid-enriched-partial.md | 0 | 2 | O2 pending, O1 proposed | S | v1.1 + pending branding |
| valid-v11-no-enrichment.md | 0 | 0 | - | S | bare v1.1 (declares 1.1, no enrichment) |
| valid-enriched-hint-no-body.md | 0 | 0 | - | H | structurally valid but intentionally semantically NONCONFORMING (flag true, section absent) -> intake gap |
| valid-enriched-contradictory.md | 0 | 0 | - | H | contradictory rules / assumption-as-confirmed -> intake review |

Rows marked "H" are structurally valid; their semantic handling is a BSEF project-intake behavior verified
by the manual acceptance checklist in BSEF docs/HANDOFF_SUPPORT.md (v1.1 intake acceptance), not by the
structural validator. Note: valid-enriched-hint-no-body.md is intentionally semantically NONCONFORMING (a
true completeness.enriched flag without its body section); it passes structural validation only because the
validator does not read the body, and is not a fully contract-conforming handoff.
