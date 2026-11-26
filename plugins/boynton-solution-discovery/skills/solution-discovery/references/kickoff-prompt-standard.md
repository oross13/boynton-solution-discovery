# Kickoff Prompt Standard — Boynton Discovery-to-Engineering Handoff v1.1

Deliverable `06-framework-kickoff-prompt.md` is the most important output and the single
**handoff** across the boundary. It is a complete, standalone prompt the user copies into a **new**
Claude Code session running the **Boynton Solution Engineering Framework (BSEF, `bsef@bsef`)**.

**Generate it only after adequate discovery and explicit human confirmation of the solution.**

Boynton Solution Discovery **owns** this standard and produces the handoff; BSEF independently
validates the versions it supports. The handoff is a human-readable Markdown body plus a
machine-readable YAML frontmatter manifest — one file, no separate manifest.

## Required file shape (reproduce exactly — do not rely on an external template file)
Every deliverable begins with the governed frontmatter. For `06`, extend it with the handoff
manifest fields. Keep `approved_by`/`approved_at` as `null` — **Discovery confirmation is not
engineering approval; only BSEF records engineering approvals, and only a human sets them.**

```yaml
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
handoff_standard_version: "1.1"
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
  # OPTIONAL (v1.1): include a flag ONLY while its body section is present (this minimal example has none).
  enriched:
    prioritized_assumptions: false   # true only when the "Prioritized assumptions" body section is present
    glossary_business_rules: false   # true only when the "Glossary & business rules" body section is present
    evidence_sources: false          # true only when the "Evidence & sources" body section is present

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
```

After a short title/preamble, the copyable prompt is delimited by these exact marker lines so the
user knows what to paste into the new BSEF session:

```
---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW BSEF SESSION ---8<---

<the standalone prompt>

---8<--- END OF COPYABLE PROMPT ---8<---
```

(The `templates/` directory holds the full fill-in versions for working directly in this repo, but
you must be able to produce a correct deliverable from this reference alone, since the templates do
not ship inside the installed plugin.)

## Version policy
- `handoff_standard_version` is `MAJOR.MINOR` (current standard is `"1.1"`; `"1.0"` remains valid),
  independent of the document's own `version`.
- A **MAJOR** change breaks required fields/structure; BSEF rejects an unsupported MAJOR.
- A **MINOR** change is additive/optional; BSEF accepts it and ignores unknown additive fields.
- `target_framework_min_version` states the oldest BSEF expected, without pinning an exact version.
- **v1.1 is additive and backward-compatible:** a BSEF consumer that supports v1.1 continues to accept
  existing v1.0 handoffs without modification. A document that declares `1.0` stays a v1.0 document.

## Non-negotiables
- **Standalone:** a new session must understand the project without the original discovery
  conversation. Do not omit important context to shorten it.
- **Project-specific:** no generic boilerplate and no leftover placeholders where the information is
  already known. Only genuine open items remain, clearly labeled.
- **Honest about uncertainty:** carries assumptions, unknowns, and deferred decisions as such — never
  dressed up as settled fact.
- **No self-approval:** `approved_by`/`approved_at` stay `null`; branding and all other decisions
  ride on `confirmed_by`/`confirmed_at` (discovery confirmation), never on engineering approval.

## Required content
The prompt must include:
- Project name and objectives.
- Business context.
- Confirmed requirements (functional and non-functional, with `FR-`/`NFR-` IDs).
- Approved scope (in and explicitly out).
- User roles and workflows.
- Business rules.
- Technical constraints.
- Recommended architecture direction (with the note that BSEF runs its own detailed architecture
  process).
- Integrations and data requirements.
- Security and privacy requirements.
- Migration requirements (when applicable) and data-preservation obligations.
- Assumptions and unresolved questions.
- Risks and dependencies.
- Success criteria.
- Branding & visual identity decision (mode; document/presentation logo via approved templates;
  app-UI logo status; proposed UI color/typography reference; explicit exceptions; open questions).
- Expected deliverables.
- Human approval gates.
- Implementation expectations.
- Testing and validation expectations (including requirement → implementation → test traceability).
- Documentation expectations.

## Required instructions to BSEF
The prompt must explicitly instruct BSEF to:
- Inspect existing materials before implementation.
- Preserve existing data when relevant; prohibit destructive actions without explicit approval.
- Challenge unsupported assumptions rather than accept them.
- Preserve the confirmed branding decision through design, prototyping, UI, frontend, visual
  validation, and final documentation; never silently substitute or alter the approved logo or
  palette; keep the app-UI standalone logo pending until a human provides it, and flag any screen
  that cannot be completed without it; use the approved Word/PowerPoint templates for documents and
  decks. (BSEF applies this per its `docs/BRAND_AND_TEMPLATE_POLICY.md`.)
- **Run its own formal discovery and governance process and honor its own approval gates**
  (Discovery, Design/Prototype, Architecture, Release/Production). Boynton Solution Discovery
  *prepares* the project; it does not bypass BSEF's gates.

## Structure (suggested)
1. Title and one-paragraph project summary.
2. Context and problem.
3. Objectives and success criteria.
4. Users, roles, stakeholders.
5. Scope (in / out) and MVP.
6. Functional requirements (`FR-`), non-functional requirements (`NFR-`).
7. Workflows and business rules.
8. Data, integrations, security & privacy, migration.
9. Recommended architecture direction and technical constraints.
10. Branding & visual identity decision.
11. Assumptions, unknowns, risks, dependencies, deferred decisions.
12. Deliverables, approval gates, and the explicit "run your own discovery/governance" instruction.
13. Implementation, testing/traceability, and documentation expectations.

## Optional enrichment sections (v1.1, additive)
After section 11 (Assumptions…) the producer MAY add any of three OPTIONAL Markdown body sections. They
carry richer business context for BSEF intake WITHOUT making Discovery an engineering spec. The data lives
in the **body** (the parsers support no list-of-maps); the only frontmatter addition is the optional
`completeness.enriched` scalar-flag map. **Flag/section pairing:** a flag is `true` iff its section is
present. Keep a section ⇒ its flag is `true`; drop a section ⇒ remove the flag (or set false). A minimal
handoff omits both. Never leave a flag `true` without its section (an intake gap), or a section without
its flag `true`. These sections are advisory; the structural validator does NOT parse them.

- **A. Prioritized assumptions** — columns (exact): ID, Assumption, Why it matters, Evidence / confidence,
  Risk if wrong, Test first?, Validation method, Owner. When present, ID and Test first? are required per
  row; the rest optional. Never invent confidence/evidence/ownership. Use P0/P1/P2 for Test first?
  (P0 = validate before substantial engineering investment). Do NOT imply every assumption must be resolved.
- **B. Glossary & business rules** — a Glossary table (Term, Definition, Source) and a Business rules
  table (ID, Rule, Compliant example, Non-compliant example, Source). Business/domain level only.
- **C. Evidence & sources** — columns (exact): Supports, Source type, Reference, Date, Status, where Status
  is one of confirmed, reported, inferred, unverified. Never label an assumption confirmed just because it
  appears here; never fabricate a source/date/status.

Fill `completeness.enriched.<flag>: true` for each section present. Examples are in
`templates/discovery/06-framework-kickoff-prompt.md`.

## Self-check before presenting
- Could a fresh session build the right thing from this alone?
- Is every claimed fact actually confirmed, and every assumption labeled?
- Are there any stray placeholders that should have been filled?
- Is the frontmatter valid, consistently indented, and independently parseable?
- Are `approved_by`/`approved_at` still `null`, and is the branding decision recorded (not invented)?
- Does it instruct BSEF to run its own gates and never self-approve?
