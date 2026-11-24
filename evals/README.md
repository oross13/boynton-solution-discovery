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

- `evals/skills/discovery-skill-cases.md` — skill behavior, IDs `EC-NN`.
- `evals/agents/agent-cases.md` — analyst-agent behavior, IDs `AC-NN`.

Each case has `Input`, `Expect`, `Fail`. The 12 required scenarios and the negative tests from the
project brief are covered here. Once Claude Code's `experimental.evals` runnable format is confirmed,
these specs can be converted into runnable eval prompts referenced from `plugin.json`. That wiring
is intentionally deferred (it is also deferred upstream in the reference framework).

> A model-graded pass indicates the behavior was observed in a sample — it does **not** prove
> perfect reasoning. Treat Layer 2 as evidence, not proof.
