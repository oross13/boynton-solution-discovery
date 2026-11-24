# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] — Initial scaffold (Phase 2)

### Added
- Marketplace `boynton` and plugin `boynton-solution-discovery` manifests.
- Skill `solution-discovery` with five reference files (discovery-methodology, question-strategy,
  solution-evaluation, requirements-guidance, kickoff-prompt-standard).
- Read-only advisory agent `solution-discovery-analyst`.
- Advisory governance hooks (`protect_approved_artifacts`, `validate_artifact_frontmatter`,
  `validate_approval_record`) with a shared `_frontmatter` helper — never block, never mutate,
  always exit 0.
- Templates: `00-discovery-state` + six deliverables (`01`–`06`) and governance ledgers
  (approval-records, decision-log, change-log), all with the governed 7-field frontmatter.
- Evaluations: deterministic `structural-check.py` and `evals/hooks/test_hooks.py`; model-graded
  behavioral specs for the skill (`EC-01`–`EC-20`, the 12 required scenarios + negative tests) and
  the agent (`AC-01`–`AC-08`).
- Documentation set and `.github/workflows/validate.yml` CI.

### Verified
- `python3 scripts/structural-check.py` — 0 errors, 0 warnings.
- `python3 evals/hooks/test_hooks.py` — hook contract holds (advisory/silent/exit-0/no-mutation).
- `claude plugin validate` — plugin and marketplace pass.

### Notes
- `experimental.evals` runnable wiring is intentionally deferred (matches the reference framework).
- Plugin icon is optional and not yet added (a release-gate item).
- No existing framework, starter, or project repository was modified.
