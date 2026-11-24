# Evaluations — Boynton Solution Discovery

Two layers, matching the engineering framework's convention.

## Layer 1 — Automated, deterministic (runs in CI, no Claude model needed)
- `scripts/structural-check.py` — validates the marketplace + plugin manifests and the frontmatter
  of every agent, skill, and governed template. Exit 0 pass / 1 error.
- `evals/hooks/test_hooks.py` — exercises the three advisory hooks against fixtures and asserts the
  **hook contract**: advisory-on-violation, silent-on-clean, always exit 0, and **no file
  mutation** (verified by SHA-256 before/after). Pure Python, no third-party deps.

Both run in `.github/workflows/validate.yml` on push / PR to `main`.

## Layer 2 — Behavioral case specs (model-graded)
Human- or model-checkable specifications of expected behavior. They are **not** deterministic
assertions — they describe what a correct discovery session should and should not do.

- `evals/skills/discovery-skill-cases.md` — skill behavior, IDs `EC-NN` (12 scenarios + negatives).
- `evals/agents/agent-cases.md` — analyst-agent behavior, IDs `AC-NN`.

Each case has `Input`, `Expect`, `Fail`. These remain the full human-readable reference.

## Layer 2 (runnable) — `claude plugin eval` cases
A subset of the specs is wired as runnable cases under the plugin, discovered via
`experimental.evals: "evals"` in `plugin.json`:

```
plugins/boynton-solution-discovery/evals/<case>/
  prompt.md            # frontmatter: max_turns, allowed_tools; body = the scenario
  graders/criteria.md  # type: llm   — PASS/FAIL criteria (judge model, default haiku)
  graders/skill-fired.md  # type: tool_used, tool: Skill — plugin-fired indicator (with-only)
```

Current cases: `non-software-recommendation`, `simplicity-local`, `problem-vs-solution`,
`no-invented-data`, `confirmation-gate`.

Run them:
```bash
claude plugin eval ./plugins/boynton-solution-discovery --trust-plugin           # full suite, with/without ablation
claude plugin eval ./plugins/boynton-solution-discovery --case simplicity-local --runs 1 --no-publish --trust-plugin
```

Run outputs go to `plugins/boynton-solution-discovery/evals/results/` (gitignored).

> **Known limitation (refinement direction).** The current runnable cases score Δ 0.00 vs. the
> no-plugin baseline: the base model already satisfies these criteria, so they function as
> *non-regression + skill-fires* checks rather than *uplift* demonstrations. Cases that would show
> the plugin's lift target harder behaviors — generating the full governed six-deliverable set with
> correct frontmatter, fact-vs-assumption separation in the state model, and a standalone kickoff
> prompt that instructs the framework to run its own gates. These need scaffolded multi-turn cases
> and are a planned addition.

> A model-graded pass indicates the behavior was observed in a sample — it does **not** prove
> perfect reasoning. Treat Layer 2 as evidence, not proof.
