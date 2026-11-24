# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Runnable `claude plugin eval` cases under `plugins/boynton-solution-discovery/evals/`:
  five single-turn behavior cases (`non-software-recommendation`, `simplicity-local`,
  `problem-vs-solution`, `no-invented-data`, `confirmation-gate`) and two multi-turn **uplift** cases
  that generate deliverables as files (`uplift-governed-kickoff`, `uplift-fact-assumption-separation`).
- `experimental.evals: "evals"` wiring in `plugin.json`.
- Plugin listing icon at `plugins/boynton-solution-discovery/.claude-plugin/icon.png`
  (1024×1024), with a reproducible generator `scripts/make-icon.py`.
- Separate, non-blocking `eval` CI workflow (`.github/workflows/eval.yml`) — manual + weekly,
  requires the `ANTHROPIC_API_KEY` secret; the deterministic `validate` workflow remains the gate.
- `.gitignore` entries for eval `results/` output.

### Fixed
- **Skill is now self-contained.** The governed frontmatter block and the kickoff copy-markers are
  embedded in the skill's `references/` (requirements-guidance, kickoff-prompt-standard) and noted in
  `SKILL.md`. The repo-root `templates/` do NOT ship inside an installed plugin, so the skill must
  not depend on reading a template file at runtime. An uplift eval surfaced this gap (the agent
  reported "template files were blocked"); with the fix, the agent reproduces correct deliverables
  from the shipped references alone.

### Verified
- `claude plugin eval` runs the full suite; the `solution-discovery` skill fires in every plugin arm.
- Single-turn behavior cases score 1.00 in the plugin arm (Δ 0.00 — non-regression + skill-fires).
- Both uplift cases demonstrate measurable lift over the no-plugin baseline — each ~Δ +0.50
  (plugin arm 1.00, baseline 0.50) — confirming the plugin's standards add value a bare model does
  not reproduce.

### Notes
- Deterministic `regex`-over-created-files grading (`target: files`) did not read agent-written files
  in testing, so uplift cases use the verified grader types (`file_exists` + `llm` + `tool_used`).
  Regex-over-files grading is deferred pending schema confirmation.
- Phase 4 isolated-install round-trip (project scope) was validated and fully torn down.

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
