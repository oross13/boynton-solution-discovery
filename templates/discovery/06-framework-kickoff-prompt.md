---
document: framework-kickoff-prompt
project: <project-slug>
version: 0.1.0
status: Draft
created: <YYYY-MM-DD>
approved_by: null
approved_at: null

# Handoff Standard identity + compatibility
handoff_standard: boynton-discovery-to-engineering
handoff_standard_version: "1.0"
target_framework: bsef@bsef
target_framework_min_version: "1.0.0"

# Discovery confirmation provenance (distinct from engineering approval)
confirmed_by: <human>            # set by a human at Solution Confirmation; never by an AI
confirmed_at: <YYYY-MM-DD>

# Provenance / traceability back-link
discovery_plugin: boynton-solution-discovery@boynton
discovery_plugin_version: "0.1.0"
source_deliverables:
  - project/discovery/01-solution-discovery-brief.md
  - project/discovery/02-requirements-specification.md
  - project/discovery/03-assumptions-risks-decisions.md
  - project/discovery/04-solution-architecture-direction.md
  - project/discovery/05-implementation-roadmap.md

# Completeness self-declaration
completeness:
  required_complete: true
  conditional_present: []        # e.g. [current_state, integrations, migration]
  open_questions_count: 0

# Branding decision (proportionate; not a separate manifest)
branding:
  mode: default-dole             # default-dole | approved-alternative
  alternative: null              # name/description when mode = approved-alternative
  document_presentation_logo: via-approved-templates   # embedded Dole logo used only through the approved Word/PowerPoint templates
  ui_logo:
    status: pending              # pending | approved  (pending implies NO approved standalone UI asset)
    asset_ref: null              # set only when a human provides/approves a standalone UI logo
  ui_brand_reference:            # proposed UI canon, pending human confirmation before frontend
    source: powerpoint-dole-template-2025
    palette: ["#001489", "#78BE20", "#3A913F"]
    typography: "Lato"
    confirmation: proposed       # proposed | approved
  visual_exceptions: none
  open_questions: []
  decision_source: <discovery artifact ref + the human confirmation that established it>
---

# Framework Kickoff Prompt — <Project Name>

> The most important deliverable. Generate it **only after** adequate discovery and the user's
> **explicit confirmation** of the solution. Everything below the marker is a standalone prompt the
> user copies into a new Claude Code session running the Boynton Solution Engineering Framework
> (BSEF, `bsef@bsef`). Fill every section from confirmed discovery — no stray placeholders where the
> information exists. Keep assumptions and open questions labeled as such; never present them as
> settled fact. Keep `approved_by`/`approved_at` null — discovery confirmation is not engineering
> approval.

---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW BSEF SESSION ---8<---

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
<Recommended direction with justification. Note: BSEF runs its own detailed architecture process
and may revise this.>

## Branding & visual identity
- **Mode:** default Dole identity *(or)* explicitly approved alternative — <name>.
- **Document & presentation logo:** via the approved Dole Word/PowerPoint templates (embedded logo;
  not a standalone asset).
- **Application-UI logo:** `pending` — no approved standalone UI asset yet; do not extract,
  approximate, or invent one. Build non-logo work; flag any screen that cannot be completed
  faithfully without the approved asset.
- **Proposed UI color / typography:** navy `#001489`, green `#78BE20`, dark green `#3A913F`;
  typography `Lato` — **proposed from the approved PowerPoint template, pending human confirmation
  before frontend implementation.** (Word output keeps FS Albert; PowerPoint output keeps Lato.)
- **Approved visual exceptions:** <none, or the approved exception>.
- **Source of decision:** <discovery artifact + who confirmed>.
- **Open branding questions:** <labeled, or none>.

## Assumptions, unknowns, risks, dependencies, deferred decisions
- **Assumptions (to validate):**
- **Unknowns / open questions:**
- **Risks:**
- **Dependencies:**
- **Deferred decisions:**

## Deliverables and approval gates
- **Expected deliverables:**
- **Human approval gates:** <BSEF's own gates — Discovery, Design/Prototype, Architecture,
  Release/Production — a human approves each; an AI may recommend but never records its own approval.>

## Instructions to BSEF
Please run your **own formal discovery and governance process** and honor your own approval gates.
This kickoff prepares the project; it does not replace or bypass your gates. Specifically:
- Inspect all existing materials before implementing anything; do not assume a file, system, or
  integration exists without evidence.
- Preserve existing data when relevant; take no destructive action without explicit human approval.
- Challenge any unsupported assumption rather than accepting it; label facts vs. assumptions.
- Preserve the confirmed branding decision through design, prototyping, UI architecture, frontend,
  visual validation, and final documentation; never silently substitute or alter the approved logo
  or palette; keep the application-UI standalone logo pending until a human provides it, and flag any
  blocked screen; use the approved Word/PowerPoint templates (from the configured template
  directory) for documents and decks, verifying availability before generating.
- Maintain traceability from requirements → implementation → tests.
- Implement incrementally; verify with tests; document decisions.
- Never request or store secrets/credentials in artifacts.

## Implementation, testing, and documentation expectations
- **Implementation:**
- **Testing & traceability:**
- **Documentation:**

---8<--- END OF COPYABLE PROMPT ---8<---
