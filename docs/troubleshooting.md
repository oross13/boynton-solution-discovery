# Troubleshooting

**Document date: 2026-11-24 · Plugin v0.1.0**

## The skill or agent isn't available
- Confirm the plugin loaded: `claude --plugin-dir ./plugins/boynton-solution-discovery`.
- Run `scripts/validate-repository.sh`. It lists what the plugin provides — look for
  `skills: boynton-solution-discovery:solution-discovery` and the agent.

## `claude plugin validate` reports a missing README or icon
- **README:** a root `README.md` counts for a plugin in a sub-folder; this repo ships one.
- **Icon:** optional. The icon warning does not fail validation. Add
  `.claude-plugin/icon.png` (square, 512–2048 px) before release if a listing icon is wanted.

## `structural-check.py` reports a version mismatch
- The plugin `version` in `plugins/boynton-solution-discovery/.claude-plugin/plugin.json` must equal
  the `version` of its entry in `.claude-plugin/marketplace.json`. Keep them in sync on every bump.

## A hook printed an advisory while I was editing
- Hooks are **advisory only** — they never block and never change your file. The message points at a
  governed-artifact issue (missing/invalid frontmatter, an Approved artifact being edited, or an
  approval row with no human approver). Address it or ignore it; the edit already applied.

## The discovery feels like a questionnaire
- It should not. If questions feel rote or repeated, that is a defect against `EC-17`/the
  question-strategy reference. The engine should ask the single highest-impact next question and
  never re-ask answered or deferred ones.

## Hook tests fail locally
- Run `python3 evals/hooks/test_hooks.py`. Failures print the specific contract that broke
  (exit code, mutation, or advisory/silence expectation). The hooks require only the standard library.

## I need to continue a discovery later
- Progress is persisted in `project/discovery/00-discovery-state.md`. Reopen it; the skill resumes
  from recorded state rather than relying on conversation memory.
