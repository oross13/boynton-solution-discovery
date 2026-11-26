# Boynton Discovery-to-Engineering Handoff — Contract of Record

**Owner (canonical):** Boynton Solution Discovery (`oross13/boynton-solution-discovery`).
Discovery owns this contract and its conformance fixtures. BSEF keeps a **pinned, vendored** copy and
verifies it; BSEF never edits the contract.

- **Current contract version:** `1.1`  (handoff standard `boynton-discovery-to-engineering`)
- **Supported by BSEF:** major `1.x` (v1.0 and v1.1).
- **Spec:** `plugins/boynton-solution-discovery/skills/solution-discovery/references/kickoff-prompt-standard.md`
- **Producer validator:** `plugins/boynton-solution-discovery/scripts/validate_handoff.py` (errors-only, 0/1).
- **Canonical fixtures:** `plugins/boynton-solution-discovery/scripts/fixtures/handoff/*.md`
  (excluding `CONFORMANCE.md`, which is documentation).
- **Canonical fixture manifest:** `plugins/boynton-solution-discovery/scripts/fixtures/handoff/fixtures.sha256`
- **Conformance table:** `plugins/boynton-solution-discovery/scripts/fixtures/handoff/CONFORMANCE.md`

## Versioning & compatibility policy
- `handoff_standard_version` is `MAJOR.MINOR`. MAJOR breaks required structure (BSEF rejects an
  unsupported MAJOR). MINOR is additive/optional; unknown additive fields are ignored.
- v1.1 is additive over v1.0. **A BSEF consumer that supports v1.1 continues to accept existing v1.0
  handoffs without modification.** A document that declares `1.0` **remains a v1.0 document**.

## Enrichment flag/section pairing (v1.1)
- Each `completeness.enriched` flag pairs with one optional body section. A flag is `true` **iff** its
  section is present. Keep a section ⇒ its flag is `true`; drop a section ⇒ delete the flag (or set false).
  Never leave a flag `true` without its section (an intake GAP), or a section without its flag true.

## Conformance expectations (producer vs consumer — intentionally different)
- **Producer (Discovery):** errors-only — exit `0` valid, `1` errors.
- **Consumer (BSEF):** errors + warnings + compatibility gates — exit `0` clean, `1` errors, `2` warnings.
- Structural differences are enumerated per fixture in `CONFORMANCE.md`. Semantic intake behavior is a
  manual acceptance checklist in BSEF `docs/HANDOFF_SUPPORT.md`, not a validator assertion.

## Fixtures vs documentation
- `fixtures.sha256` covers **only the handoff fixture `*.md` files**. `CONFORMANCE.md` is documentation, not
  a handoff fixture; excluded from the manifest and inventory tests. Its integrity rides on the sync PR.

## Integrity vs provenance
- Manifest + hash tests prove **integrity** (fixtures match their manifest), offline.
- **Provenance/canonicity** = recorded source revision in BSEF's `PROVENANCE.md` + reviewed sync PR.

## BSEF synchronization procedure (low-maintenance, offline)
1. Update version/spec/fixtures/manifest/CONFORMANCE here; Discovery CI (`structural-and-hooks`) green.
2. In BSEF, open a **sync PR** copying verbatim the changed fixtures, `fixtures.sha256`, `CONFORMANCE.md`;
   update `plugins/bsef/scripts/fixtures/PROVENANCE.md` (contract version + source SHA).
3. BSEF CI (`structural`) re-verifies vendored hashes; both repos green before merge.
