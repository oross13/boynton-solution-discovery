# Skill Behavioral Cases — `solution-discovery`

Model-graded specs. Each: **Input / Expect / Fail**. IDs are stable.

## Required scenarios

### EC-01 · Replace an existing business application
- **Input:** "We want to replace our old job-tracking app with something modern."
- **Expect:** investigates current functionality, users, data/history, integrations, reports,
  limitations, migration, access, continuity, and acceptable downtime; records them in the state;
  does not jump to a tech stack before the problem and current state are understood.
- **Fail:** proposes an architecture or stack before current-state and migration needs are explored.

### EC-02 · New application from an initial idea
- **Input:** "I have an idea for an app to help my team request equipment."
- **Expect:** establishes problem, users, roles, core workflows, data, rules, MVP vs. later; keeps
  scope tight.
- **Fail:** produces a broad feature list the user never asked for.

### EC-03 · Business process automation
- **Input:** "Approving expense reports takes too long."
- **Expect:** maps the current process, participants, manual steps, bottlenecks, rules, decision
  points, exceptions, approvals, and measurable benefits before proposing automation.
- **Fail:** proposes a tool without understanding the current process.

### EC-04 · Integration between two existing systems
- **Input:** "Our CRM and billing system don't talk to each other."
- **Expect:** asks about systems, data ownership, APIs/methods, direction/frequency, auth, error
  handling, reconciliation, monitoring; never asserts an API exists without evidence.
- **Fail:** assumes an integration method or API that was not confirmed.

### EC-05 · AI-powered business solution
- **Input:** "I want AI to categorize incoming support tickets."
- **Expect:** asks whether deterministic rules would suffice, then inputs/outputs, accuracy needs,
  human review, data privacy, model dependency, cost, failure handling, evaluation.
- **Fail:** accepts "use AI" without testing whether simpler automation fits.

### EC-06 · Single-user local application
- **Input:** "A small tool just for me to track my personal reading."
- **Expect:** recommends the simplest adequate solution; no multi-tenancy, cloud, or complex auth.
- **Fail:** proposes enterprise architecture for a single-user local tool.

### EC-07 · Multi-user application with role-based access
- **Input:** "A team tool where managers approve and staff submit."
- **Expect:** models roles with permissions AND denials; includes no-permission paths.
- **Fail:** captures permissions but omits denial/no-permission handling.

### EC-08 · Poorly defined problem with significant uncertainty
- **Input:** "Things are chaotic and I think we need software."
- **Expect:** slows down, separates symptoms from root cause, records unknowns, and does not force
  premature completeness.
- **Fail:** fabricates a concrete problem/solution to appear decisive.

### EC-09 · User who does not know technical answers
- **Input:** user answers "I don't know" to a database/hosting question.
- **Expect:** explains implications in plain language, offers options, or defers and records it for
  validation; never badgers with jargon.
- **Fail:** repeats the jargon question or stalls.

### EC-10 · User changes requirements during discovery
- **Input:** user contradicts an earlier answer.
- **Expect:** updates the state, reconciles the change, flags downstream impact, revisits affected
  stages.
- **Fail:** silently keeps the stale requirement or ignores the conflict.

### EC-11 · User wants to skip questions and proceed with assumptions
- **Input:** "Just assume the usual and move on."
- **Expect:** records explicit assumptions, marks which must be validated before build, and carries
  them into `03` and the kickoff prompt with validation instructions.
- **Fail:** proceeds while treating the assumptions as confirmed facts.

### EC-12 · A problem where a custom application is not the best solution
- **Input:** "We need an app to remind people of a weekly meeting."
- **Expect:** willing to recommend a non-software solution (calendar/config/process) instead of
  building an app.
- **Fail:** insists on building an application when a simpler option clearly fits.

## Negative tests

### EC-13 · No invented requirements
- **Expect:** requirements trace to stated facts or labeled assumptions.
- **Fail:** adds requirements the user never implied.

### EC-14 · No invented integrations
- **Expect:** integrations appear only with evidence they exist.
- **Fail:** asserts an API/integration not confirmed.

### EC-15 · No unjustified technology recommendation
- **Expect:** each tech choice tied to a requirement/constraint.
- **Fail:** names a stack "by default" without justification.

### EC-16 · No premature architecture decision
- **Expect:** architecture direction comes after enough problem understanding.
- **Fail:** fixes architecture during intake.

### EC-17 · No artificially prolonged discovery
- **Expect:** stops when enough is known; maximizes quality, not question count.
- **Fail:** keeps asking low-value questions past readiness.

### EC-18 · No bypassing user approval
- **Expect:** asks for explicit confirmation before generating `06`; never self-approves.
- **Fail:** generates the kickoff prompt without confirmation, or sets `approved_by`/`approved_at`.

### EC-19 · No incomplete kickoff prompt
- **Expect:** `06` is standalone and project-specific, covering all required sections, with no stray
  placeholders where info exists, and instructs the framework to run its own gates.
- **Fail:** emits a generic/placeholder-laden prompt or omits the "run your own discovery" instruction.

### EC-20 · No assumption silently treated as fact
- **Expect:** assumptions stay labeled across all artifacts.
- **Fail:** an assumption appears as a confirmed fact in a later document.
