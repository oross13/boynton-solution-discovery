# Release Checklist (Gate 4)

**Document date: 2026-11-24 · Plugin v0.1.0**

> **Guardrails:** release steps that expose the plugin to anyone beyond the owner's isolated testing
> require **explicit human approval** (master prompt §14 Phase 5, §16). An AI may prepare and
> recommend a release but must never make the repository public or submit it to a directory on its
> own. Nothing here changes repository visibility.

## A. Pre-release verification (automatable)
- [ ] `python3 scripts/structural-check.py` → 0 errors.
- [ ] `python3 evals/hooks/test_hooks.py` → hook contract holds.
- [ ] `scripts/validate-repository.sh` → plugin + marketplace validate (add `--strict` for CI).
- [ ] `claude plugin eval ./plugins/boynton-solution-discovery --trust-plugin --allow-tools Write`
      → single-turn cases pass in the plugin arm; uplift cases show positive Δ.
- [ ] `validate` CI is green on the target commit.

## B. Metadata & consistency
- [ ] Plugin `version` in `plugins/boynton-solution-discovery/.claude-plugin/plugin.json` equals the
      marketplace entry `version` in `.claude-plugin/marketplace.json`.
- [ ] `CHANGELOG.md` has a dated section for the version being released; `[Unreleased]` is empty or
      rolled in.
- [ ] Listing icon present at `.claude-plugin/icon.png` (square, 512–2048 px).
- [ ] README reflects the current component set and install/validate commands.

## C. Tag & draft release (reversible, private)
- [ ] Commit and push `main` to the private remote.
- [ ] Create a **draft** GitHub release for `vX.Y.Z` with notes from the CHANGELOG
      (`gh release create vX.Y.Z --draft --notes-file <notes>`). A draft on a private repo is visible
      only to collaborators and can be edited or deleted before publishing.

## D. Human-approval gate — do NOT perform without explicit owner approval
- [ ] Publish the draft release (makes the tag/release visible to repo collaborators).
- [ ] **Make the repository public** (irreversible exposure; owner decision only).
- [ ] **Submit to any plugin/marketplace directory** (owner decision only).
- [ ] **Install into the personal `~/.claude` profile** beyond isolated testing (owner decision only).
- [ ] Add the `ANTHROPIC_API_KEY` repository secret so the scheduled `eval` workflow can run
      (a secret — owner performs this; `gh secret set ANTHROPIC_API_KEY`).

## E. Post-release
- [ ] Bump to the next development version and open a fresh `[Unreleased]` CHANGELOG section.
- [ ] Capture any follow-ups (e.g. deterministic regex-over-files grading once the schema is
      confirmed; scaffolded `case.yaml` cases; additional uplift scenarios).

## Current status (v0.1.0)
- A, B, C prepared and verified; draft release created on the private repo.
- D items are **pending the owner's explicit authorization** and have not been performed.
