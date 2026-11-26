---
document: framework-kickoff-prompt
project: facilities-maintenance
version: 0.1.0
status: Draft
created: 2026-11-25
approved_by: null
approved_at: null
handoff_standard: boynton-discovery-to-engineering
handoff_standard_version: "1.1"
target_framework: bsef@bsef
target_framework_min_version: "1.0.0"
confirmed_by: A Human
confirmed_at: 2026-11-25
discovery_plugin: boynton-solution-discovery@boynton
discovery_plugin_version: "0.1.0"
source_deliverables:
  - project/discovery/01-solution-discovery-brief.md
  - project/discovery/03-assumptions-risks-decisions.md
completeness:
  required_complete: true
  conditional_present: [integrations]
  open_questions_count: 0
  enriched:
    prioritized_assumptions: true
branding:
  mode: default-dole
  alternative: null
  document_presentation_logo: via-approved-templates
  ui_logo:
    status: pending
    asset_ref: null
  ui_brand_reference:
    source: powerpoint-dole-template-2025
    palette: ["#001489", "#78BE20", "#3A913F"]
    typography: "Lato"
    confirmation: proposed
  visual_exceptions: none
  open_questions: []
  decision_source: 03-assumptions-risks-decisions.md; confirmed by a human
---

# Framework Kickoff Prompt - Facilities Maintenance

---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW BSEF SESSION ---8<---

# Project Kickoff - Facilities Maintenance

v1.1 handoff with only the Prioritized assumptions enrichment; default Dole branding with the
UI logo pending and the UI canon proposed.
Expected: Discovery exit 0 (errors-only); BSEF exit 2 (O1 proposed + O2 pending warnings).

## Prioritized assumptions
| ID | Assumption | Why it matters | Evidence / confidence | Risk if wrong | Test first? | Validation method | Owner |
|---|---|---|---|---|---|---|---|
| A-001 | Weekly legacy-sheet logging | Sync cadence | reported | Sync rework | P0 | interview | - |
| A-002 | Under 50 users | NFR sizing | inferred | Low | - | defer to NFR | - |

---8<--- END OF COPYABLE PROMPT ---8<---
