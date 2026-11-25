---
document: framework-kickoff-prompt
project: facilities-maintenance
version: 0.1.0
status: Draft
created: 2026-11-25
approved_by: null
approved_at: null
handoff_standard: boynton-discovery-to-engineering
handoff_standard_version: "1.0"
target_framework: other-framework@x
target_framework_min_version: "1.0.0"
confirmed_by: A Human
confirmed_at: 2026-11-25
discovery_plugin: boynton-solution-discovery@boynton
discovery_plugin_version: "0.1.0"
source_deliverables:
  - project/discovery/01-solution-discovery-brief.md
  - project/discovery/05-implementation-roadmap.md
completeness:
  required_complete: true
  conditional_present: [integrations]
  open_questions_count: 0
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
  decision_source: confirmed by a human
---

# Based on valid-clean.md with ONLY target_framework changed to a mismatched value.
# Expected: WARNING only (target_framework is 'other-framework@x'; expected 'bsef@bsef'), exit 2.
