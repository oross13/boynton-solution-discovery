---
document: framework-kickoff-prompt
project: <project-slug>
version: 0.1.0
status: Draft
created: <YYYY-MM-DD>
approved_by: null
approved_at: null
---

# Framework Kickoff Prompt — <Project Name>

> The most important deliverable. Generate it **only after** adequate discovery and the user's
> **explicit confirmation** of the solution. Everything below the marker is a standalone prompt the
> user copies into a new Claude Code session running the Boynton / AIBADF engineering framework.
> Fill every section from confirmed discovery — no stray placeholders where the information exists.
> Keep assumptions and open questions labeled as such; never present them as settled fact.

---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW FRAMEWORK SESSION ---8<---

# Project Kickoff — <Project Name>

## Summary
<One paragraph a fresh session can orient from, with no access to the discovery conversation.>

## Context and problem
<Business context; the real problem (not just the proposed solution); why it matters now.>

## Objectives and success criteria
- **Objectives:**
- **Success criteria (measurable):**

## Users, roles, and stakeholders
| Role | Needs | Can / cannot |
|---|---|---|

## Scope
**In scope:**
-

**Out of scope:**
-

**MVP:**
-

## Functional requirements
| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| FR-001 | | | |

## Non-functional requirements
| ID | Category | Requirement | Acceptance criteria |
|---|---|---|---|
| NFR-001 | | | |

## Workflows and business rules
<Key workflows incl. error/no-permission paths; business rules with expected behavior.>

## Data, integrations, security & privacy, migration
- **Data:**
- **Integrations (evidenced only):**
- **Security & privacy:**
- **Migration & data preservation (if applicable):**

## Recommended architecture direction and technical constraints
<Recommended direction with justification. Note: the framework runs its own detailed architecture
process and may revise this.>

## Assumptions, unknowns, risks, dependencies, deferred decisions
- **Assumptions (to validate):**
- **Unknowns / open questions:**
- **Risks:**
- **Dependencies:**
- **Deferred decisions:**

## Deliverables and approval gates
- **Expected deliverables:**
- **Human approval gates:** <the framework's own gates — Discovery, Prototype/Design, Architecture,
  Production — a human approves each; an AI may recommend but never records its own approval.>

## Instructions to the engineering framework
Please run your **own formal discovery and governance process** and honor your own approval gates.
This kickoff prepares the project; it does not replace or bypass your gates. Specifically:
- Inspect all existing materials before implementing anything; do not assume a file, system, or
  integration exists without evidence.
- Preserve existing data when relevant; take no destructive action without explicit human approval.
- Challenge any unsupported assumption rather than accepting it; label facts vs. assumptions.
- Maintain traceability from requirements → implementation → tests.
- Implement incrementally; verify with tests; document decisions.
- Never request or store secrets/credentials in artifacts.

## Implementation, testing, and documentation expectations
- **Implementation:**
- **Testing & traceability:**
- **Documentation:**

---8<--- END OF COPYABLE PROMPT ---8<---
