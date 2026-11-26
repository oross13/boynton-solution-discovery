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
    glossary_business_rules: true
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

completeness.enriched.glossary_business_rules is true, but the body omits the "Glossary & business
rules" section. This fixture is intentionally semantically NONCONFORMING: the flag/section pairing
rule requires the section whenever the flag is true. It passes structural validation only because the
validator does not inspect the body; it is an intake-gap test case, not a conforming handoff. BSEF
project-intake must flag the missing section as a gap for human review.
Expected: Discovery exit 0; BSEF exit 0 (intake raises the gap).

---8<--- END OF COPYABLE PROMPT ---8<---
