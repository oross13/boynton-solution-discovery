# Solution Evaluation

How to challenge thinking, separate problem from solution, and evaluate alternatives. Use this when
invoking the `solution-discovery-analyst` agent and when forming recommendations.

## Problem before solution
When the user proposes a solution before the problem is defined:
- Restate the underlying **problem** separately from the proposed **solution**.
- Identify the likely root cause vs. the presenting symptom.
- Ask whether a simpler alternative — including a **non-software** one (process change, existing
  tool configuration, a report, an integration) — could solve it.
- Name possible unintended consequences of the proposed solution.

Challenge questionable assumptions respectfully. Evaluate any proposed technology or architecture
for fit rather than accepting it by default.

## When to explore alternatives
Explore alternatives only when the answer is not already clear. Do not manufacture options to look
thorough. When you do explore, present two to four genuine options.

For each option, assess:
- Functional fit
- Complexity
- Cost
- Time to deliver
- Maintenance burden
- Security posture
- Reliability
- Integration effort
- Future flexibility
- Operational implications

Explain trade-offs in plain language. Recommend one option and say **why**. Make clear a
recommendation is a recommendation — the human decides.

## Complexity discipline
Recommend the simplest solution that adequately meets the requirements, security expectations, and
foreseeable needs. Do **not** introduce enterprise architecture, multi-tenancy, cloud
infrastructure, microservices, or complex authorization unless the problem warrants it. A
single-user local application must not inherit multi-tenant enterprise architecture.

## Fact discipline
Keep four categories strictly distinct and never silently promote between them:
- **Confirmed fact** — stated by the user or evidenced in supplied material.
- **Assumption** — taken as true for now; rate importance × confidence; note how to validate.
- **Hypothesis** — a candidate explanation still to be tested.
- **Open question / unknown** — not yet answered.

Identify which assumptions must be validated before implementation, and carry the rest forward with
explicit validation instructions for the framework.
