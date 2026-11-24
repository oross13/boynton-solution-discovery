# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `docs/USER_GUIDE.md` — end-to-end user instructions (install, activate, run a discovery, outputs,
  manage, troubleshoot), linked from the README and installation docs.

### Changed
- `eval` CI workflow is now **manual-only** (`workflow_dispatch`); the weekly schedule was removed.
  Model-graded evals are run manually or locally; the deterministic `validate` workflow remains the
  always-on gate.

## [0.1.0] — 2026-11-24

Initial release of the Boynton Solution Discovery companion plugin.

### Added
- Marketplace `boynton` and plugin `boynton-solution-discovery` manifests (semver kept in sync).
- Skill `solution-discovery` (main-session orchestrator) with five self-contained reference files
  (discovery-methodology, question-strategy, solution-evaluation, requirements-guidance,
  kickoff-prompt-standard).
- Read-only advisory agent `solution-discovery-analyst`.
- Advisory governance hooks (`protect_approved_artifacts`, `validate_artifact_frontmatter`,
  `validate_approval_record`) with a shared `_frontmatter` helper — never block, never mutate,
  always exit 0.
- Templates: `00-discovery-state` + six deliverables (`01`–`06`) and governance ledgers
  (approval-records, decision-log, change-log), all with the governed 7-field frontmatter.
- Listing icon `.claude-plugin/icon.png` (1024×1024) + reproducible `scripts/make-icon.py`.
- Evaluations:
  - Deterministic: `structural-check.py` and `evals/hooks/test_hooks.py`.
  - Model-graded specs: skill `EC-01`–`EC-20` (12 scenarios + negatives), agent `AC-01`–`AC-08`.
  - Runnable `claude plugin eval` cases wired via `experimental.evals`: five single-turn behavior
    cases plus two multi-turn uplift cases (`uplift-governed-kickoff`,
    `uplift-fact-assumption-separation`).
- CI: deterministic `validate` workflow (always-on) and a separate non-blocking `eval` workflow
  (manual + weekly, needs `ANTHROPIC_API_KEY`).
- Documentation set, README, LICENSE, `.gitignore`.

### Design notes
- The skill is **self-contained**: the governed frontmatter block and kickoff copy-markers live in
  the shipped `references/`, because the repo-root `templates/` do not ship inside an installed
  plugin. (This gap was surfaced by an uplift eval and fixed.)

### Verified
- `structural-check.py`, `test_hooks.py`, and `claude plugin validate` (plugin + marketplace) pass;
  `validate` CI green on the remote.
- Phase 3 dry-run exercised the full six-deliverable pipeline and all six advisory-hook behaviors.
- Phase 4 isolated-install round-trip (project scope) validated and fully torn down; runtime
  discoverability of the skill and agent confirmed.
- `claude plugin eval`: single-turn cases score 1.00 in the plugin arm (Δ 0.00 — non-regression +
  skill-fires); both uplift cases ~Δ +0.50 over the no-plugin baseline.

### Known limitations
- `experimental.evals` runnable wiring is used, but deterministic `regex`-over-created-files grading
  (`target: files`) did not read agent-written files in testing, so uplift cases use the verified
  grader types (`file_exists` + `llm` + `tool_used`).
- No existing framework, starter, or project repository was modified.
