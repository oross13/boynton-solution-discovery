# Discovery Methodology

A flexible, staged lifecycle. Stages give structure; they are not a fixed sequence. Revisit any
earlier stage whenever new information requires it. Depth adapts to the project — a single-user
local tool does not get the same treatment as a multi-tenant system.

## Stage 1 — Initial intake
Start open-ended. Capture: initial problem statement, business/personal context, desired outcome,
existing solution (if any), known constraints, initial expectations. Do not prescribe a technical
solution yet.

## Stage 2 — Problem understanding
Establish what is happening today, what is not working, why it matters, who is affected, how often
it occurs, what happens if nothing changes, and what success looks like. Separate symptoms from
root causes.

## Stage 3 — Stakeholders and users
Identify only the relevant stakeholders, users, administrators, external parties, and
decision-makers. Capture responsibilities, expectations, access needs, and potential conflicts.

## Stage 4 — Current-state analysis
When an existing process, system, document, or application exists, investigate it. Identify
available source materials (source code, schemas, screenshots, process docs, spreadsheets, API
docs, business rules, sample reports, workflows) and request only those that would materially
improve discovery. Never assume a file, system, or integration exists without evidence.

## Stage 5 — Requirements discovery
Develop a clear understanding of **functional** requirements (features, activities, workflows,
business rules, notifications, reporting, integrations, admin) and **non-functional** requirements
(security, privacy, performance, reliability, availability, scalability, accessibility,
maintainability, backup/recovery, auditability). Adapt depth to the project; do not invent
requirements to fill a document.

## Stage 6 — Assumptions, risks, dependencies
Maintain explicit, separated records of confirmed facts, assumptions, hypotheses, unknowns,
constraints, risks, external dependencies, technical limitations, and decisions needing validation.
Classify assumptions by importance and confidence. Identify which must be validated before
implementation. Never silently convert an assumption into an approved requirement.

## Stage 7 — Solution exploration
Explore reasonable alternatives where appropriate. For each, weigh functional fit, complexity,
cost, time, maintenance, security, reliability, integration effort, future flexibility, and
operational implications. Explain trade-offs plainly and recommend an option with reasons. Do not
manufacture alternatives when the answer is already clear. A non-software solution is valid.

## Stage 8 — Technical discovery
Only after enough problem understanding. Consider (as relevant): application type, architecture,
frontend/backend, database, data ownership, APIs, integrations, identity/access, hosting/deployment,
local vs. cloud, offline needs, AI/LLM dependencies, dev tools, existing standards. Evaluate the
Boynton application starters when relevant, but do not pick one just because it exists. Every
technology recommendation must be justified by requirements and constraints.

## Stage 9 — Scope and delivery strategy
Establish in-scope and explicitly out-of-scope capabilities, MVP, future phases, dependencies,
milestones, acceptance criteria, and success measures. Do not confuse long-term vision with the
initial implementation scope.

## Stage 10 — Discovery readiness review
Assess whether enough is known. Identify what is understood, what remains uncertain, which
decisions are made vs. deferred, which assumptions are unvalidated, and whether any unresolved
issue could materially change the solution. Do not force artificial completeness. If the user
proceeds with open matters, document them and instruct the framework to validate them.

## Stage 11 — Solution confirmation
Present a concise but meaningful summary: problem, objectives, users/stakeholders, proposed
solution, major capabilities, scope, architecture direction, constraints, risks, open decisions,
success criteria. Ask for explicit human confirmation. The AI never approves its own
recommendations.

## Stage 12 — Deliverable generation
Only after confirmation, generate deliverables `01`–`06` and record the human confirmation in the
governance approval records.

## Scenario hints (bias the questions, never a mandatory flow)
- **Replace an existing application:** functionality, users, processes, data/history, integrations,
  reports, limitations, migration, access controls, continuity, acceptable downtime, support.
- **Automate a process:** current process, participants, manual steps, bottlenecks, rules, decision
  points, exceptions, approvals, existing systems, automation opportunities, measurable benefits.
- **New application:** problem, users, roles, core workflows, functionality, data, rules, reporting,
  security, integrations, scale, MVP vs. future.
- **Integrate systems:** systems, data ownership, APIs/methods, synchronization, frequency/direction,
  auth, error handling, retry/reconciliation, monitoring/audit.
- **AI-assisted:** why AI (vs. deterministic automation), inputs/outputs, accuracy needs, human
  review, data privacy, model dependencies, cost, failure handling, evaluation/monitoring.
