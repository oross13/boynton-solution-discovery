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

Cases come in two kinds:

**Single-turn behavior cases** — `non-software-recommendation`, `simplicity-local`,
`problem-vs-solution`, `no-invented-data`, `confirmation-gate`. These score 1.00 in the plugin arm
with Δ 0.00 vs. baseline — the base model already satisfies them, so they act as *non-regression +
skill-fires* checks.

**Multi-turn uplift cases** — `uplift-governed-kickoff` and `uplift-fact-assumption-separation`. The
agent reads the skill's references and **writes deliverable files**, which are then graded. These show
measurable lift over the no-plugin baseline (plugin arm passes; bare-model baseline fails), because a
bare model does not reproduce the governed frontmatter, the kickoff copy-markers, the
"framework runs its own gates" instruction, or strict fact/assumption separation. They need
`--allow-tools Write`.

Run them:
```bash
# Full suite with with/without ablation (shows Δ); uplift cases need Write:
claude plugin eval ./plugins/boynton-solution-discovery --trust-plugin --allow-tools Write
# One case, single run, no baseline:
claude plugin eval ./plugins/boynton-solution-discovery --case simplicity-local --runs 1 --ablation none --no-publish --trust-plugin
```

Run outputs go to `plugins/boynton-solution-discovery/evals/results/` (gitignored). CI runs these
weekly / on demand via `.github/workflows/eval.yml` (needs the `ANTHROPIC_API_KEY` secret).

> **Grader note.** Deterministic `regex` grading with `target: files` did not read the agent-written
> files in testing (content was present on disk but the grader matched nothing), so the uplift cases
> use the verified grader types: `file_exists` (deterministic existence) + `llm` (content, judge
> model) + `tool_used` (skill-fired indicator, with-only under ablation). Regex-over-created-files
> grading is deferred pending confirmation of its exact schema.

> A model-graded pass indicates the behavior was observed in a sample — it does **not** prove
> perfect reasoning. Treat Layer 2 as evidence, not proof.
