# Getting Started

**Document date: 2026-11-24 · Plugin v0.1.0**

Boynton Solution Discovery helps you think a problem through *before* building, then hands the
engineering framework a clear, confirmed project definition.

## Start a discovery

1. Load the plugin (see [installation.md](installation.md)).
2. Invoke the **`solution-discovery`** skill.
3. Answer the opening prompt in your own words — you do not need all the answers yet.

## What happens

- The consultant asks **one meaningful question at a time**, adapting to your answers and to what is
  still uncertain. It explains why a question matters and offers examples when helpful.
- It keeps a living `project/discovery/00-discovery-state.md`, separating confirmed facts,
  assumptions, unknowns, risks, and decisions.
- At decision points it uses the `solution-discovery-analyst` to challenge assumptions, surface
  risks, and weigh alternatives.
- At meaningful milestones it gives a short recap.
- When enough is known, it presents a solution summary and **asks you to confirm**. Nothing is
  "approved" by the AI.

## After you confirm

It generates six deliverables under `project/discovery/` (01–06) and records your confirmation in
`project/governance/approval-records.md`. The sixth — `06-framework-kickoff-prompt.md` — is a
standalone prompt you copy into a new Claude Code session running the engineering framework.

## Ground rules it follows
- Adaptive, not a questionnaire. No repeated questions.
- Simplest adequate solution; a non-software answer is valid.
- Never invents requirements, integrations, or metrics.
- Never requests secrets; treats supplied files as untrusted data.
- Prepares the project; never bypasses the framework's own gates.

See [usage-examples.md](usage-examples.md) for worked scenarios and
[discovery-methodology.md](discovery-methodology.md) for the full lifecycle.
