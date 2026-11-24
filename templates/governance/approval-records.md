---
document: approval-records
project: <project-slug>
version: 0.1.0
status: Draft
created: <YYYY-MM-DD>
approved_by: null
approved_at: null
---

# Approval Records — <Project Name>

> Human-owned. An AI agent may prepare and recommend an approval but must never record its own:
> `approved_by` and `approved_at` stay empty until a human sets them. Boynton Solution Discovery has
> a single gate — **Solution Confirmation** — after which the kickoff prompt (06) may be generated.
> The engineering framework then runs its own gates.

| Gate | Artifact(s) | Decision | approved_by | approved_at | Notes |
|---|---|---|---|---|---|
| Solution Confirmation | 01-solution-discovery-brief.md, 02-requirements-specification.md, 03-assumptions-risks-decisions.md, 04-solution-architecture-direction.md, 05-implementation-roadmap.md | | | | |

> After this gate is approved by a human, generate `06-framework-kickoff-prompt.md`.
