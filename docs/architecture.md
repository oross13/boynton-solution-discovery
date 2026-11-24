# Architecture

**Document date: 2026-11-24 · Plugin v0.1.0**

## Shape
A single-plugin marketplace that mirrors the engineering framework's conventions so its output is
drop-in compatible.

- **Marketplace** `boynton` → one plugin `boynton-solution-discovery`.
- **One skill + one agent**, by deliberate design.

## Why the skill runs in the main conversation
Adaptive, one-question-at-a-time discovery requires an interactive back-and-forth with the user. A
subagent cannot hold that conversation. So the **`solution-discovery` skill orchestrates in the main
session** — intake, adaptive questioning, state-keeping, the confirmation gate, and artifact writes.

## Why the agent is read-only advisory
The **`solution-discovery-analyst`** is invoked at decision points for focused reasoning
(problem-vs-solution, assumption rating, risk, alternatives, readiness). It is `Read, Grep, Glob`
only: it never writes deliverables and never confirms a solution. This mirrors the framework's
`architect` / `product-discovery` advisory agents and keeps a clean separation — the skill owns
writes and the human owns approval.

## Discovery state model
`00-discovery-state.md` is a persisted artifact (not chat memory) that tracks problem understanding,
confirmed facts, assumptions (rated importance × confidence), hypotheses, unknowns, stakeholders,
requirements, risks, decisions, scope, architecture considerations, and readiness. It keeps the four
knowledge categories strictly distinct.

## Adaptive questioning engine
`skills/solution-discovery/references/question-strategy.md` encodes a next-best-question loop that
scores candidate questions (known? needed? material? reduces top uncertainty? defer? asked?
user-knowable? inferable? example-helpful?) and asks the single highest-impact one, prioritized by
impact on business value, scope, UX, architecture, data, security, cost, delivery risk, and
operational complexity.

## Governance & compatibility
- All deliverables carry the framework's governed 7-field frontmatter and the 4-value status enum,
  so the framework's own hooks accept them.
- A single human gate — **Solution Confirmation** — precedes generation of `06`. The AI recommends;
  a human sets `approved_by`/`approved_at`.
- Advisory hooks (never block, never mutate, exit 0) check frontmatter and flag self-approval.

## Handoff
`06-framework-kickoff-prompt.md` is standalone and instructs the framework to run its **own** formal
discovery and gates. Discovery prepares; it does not bypass. The framework begins at its own
`00-project-intake`.

## Deferred
`experimental.evals` runnable wiring and a plugin icon are deferred to a later phase, consistent with
the reference framework.
