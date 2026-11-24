# Requirements Guidance

How to capture requirements for deliverable `02` and feed them into the kickoff prompt.

## Identifiers and traceability
- Functional requirements: `FR-001`, `FR-002`, …
- Non-functional requirements: `NFR-001`, `NFR-002`, …
- Keep IDs stable once assigned; new requirements get new IDs, never renumbered.
- Every requirement should be traceable: it ties back to a stated problem/objective and forward to
  acceptance criteria. The kickoff prompt instructs the framework to maintain traceability from
  requirements → implementation → tests.

## What a good requirement looks like
- **Atomic:** one testable statement.
- **Sourced:** derived from a confirmed fact or an explicitly labeled assumption — never invented to
  fill the document.
- **Prioritized:** e.g. MoSCoW (Must / Should / Could / Won't-now) or MVP vs. later phase.
- **Acceptance criteria:** a clear, checkable condition of done.

Mark any requirement that rests on an unvalidated assumption, and cross-reference it in
`03-assumptions-risks-decisions.md`.

## Functional coverage to consider (only what applies)
Features, user activities, workflows, business rules, notifications, reporting, integrations,
administrative capabilities, data lifecycle (create/read/update/delete/retain/archive).

## Non-functional coverage to consider (only what applies)
Security, privacy, performance, reliability, availability, scalability, accessibility,
maintainability, backup and recovery, auditability. Scale depth to the project — a personal tool
does not need an enterprise NFR set.

## Roles, workflows, business rules
- **Roles:** name each role and what it may and may not do; model denials, not just permissions.
- **Workflows:** the main paths plus error and no-permission paths.
- **Business rules:** state each rule and, where useful, a compliant and a non-compliant example and
  the system's expected behavior (this aligns with the engineering framework's rule style).

## Data and integrations
- **Data:** entities, ownership, sensitivity/privacy classification, retention, and (for
  replacements/migrations) historical-data and preservation requirements.
- **Integrations:** only those evidenced to exist — systems, direction, frequency, auth method,
  error handling, reconciliation, monitoring. Never assert an integration exists without evidence.
