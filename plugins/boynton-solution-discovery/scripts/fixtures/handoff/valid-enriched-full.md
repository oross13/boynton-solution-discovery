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
    glossary_business_rules: true
    evidence_sources: true
branding:
  mode: approved-alternative
  alternative: Acme House Style
  document_presentation_logo: via-approved-templates
  ui_logo:
    status: approved
    asset_ref: acme-ui-logo.svg
  ui_brand_reference:
    source: acme-brand-guide-2026
    palette: ["#101820"]
    typography: "Inter"
    confirmation: approved
  visual_exceptions: none
  open_questions: []
  decision_source: 03-assumptions-risks-decisions.md; confirmed by a human
---

# Framework Kickoff Prompt - Facilities Maintenance

---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW BSEF SESSION ---8<---

# Project Kickoff - Facilities Maintenance

v1.1 handoff with all three optional enrichment sections; branding fully approved.
Expected: Discovery exit 0 (errors-only); BSEF exit 0 (no warnings).

## Prioritized assumptions
| ID | Assumption | Why it matters | Evidence / confidence | Risk if wrong | Test first? | Validation method | Owner |
|---|---|---|---|---|---|---|---|
| A-001 | Weekly legacy-sheet logging | Sync cadence | reported | Sync rework | P0 | interview | - |

## Glossary & business rules
**Glossary**
| Term | Definition | Source |
|---|---|---|
| Work order | A maintenance task with a status | 02 s0 |

**Business rules**
| ID | Rule | Compliant example | Non-compliant example | Source |
|---|---|---|---|---|
| BR-001 | No close with open checks | all checks done | one check open | 02 s5 |

## Evidence & sources
| Supports | Source type | Reference | Date | Status |
|---|---|---|---|---|
| FR-001 | interview | registro.md #8 | 2026-11-20 | reported |
| A-001 | assumption | 03 s2 | - | unverified |

---8<--- END OF COPYABLE PROMPT ---8<---
