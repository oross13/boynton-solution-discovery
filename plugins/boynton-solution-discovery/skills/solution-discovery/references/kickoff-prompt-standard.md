# Kickoff Prompt Standard

Deliverable `06-framework-kickoff-prompt.md` is the most important output. It is a complete,
standalone prompt the user copies into a **new** Claude Code session to start the project with the
Boynton / AIBADF engineering framework.

**Generate it only after adequate discovery and explicit human confirmation of the solution.**

## Required file shape (reproduce exactly — do not rely on an external template file)
Every deliverable — including `06` — begins with the governed frontmatter block. Fill the values;
keep `approved_by` and `approved_at` as `null` (only a human sets them):

```markdown
---
document: framework-kickoff-prompt
project: <project-slug>
version: 0.1.0
status: Draft
created: <YYYY-MM-DD>
approved_by: null
approved_at: null
---
```

After a short title/preamble, the copyable prompt is delimited by these exact marker lines so the
user knows what to paste into the new framework session:

```
---8<--- COPY EVERYTHING BELOW THIS LINE INTO THE NEW FRAMEWORK SESSION ---8<---

<the standalone prompt>

---8<--- END OF COPYABLE PROMPT ---8<---
```

(The `templates/` directory holds the full fill-in versions for working directly in this repo, but
you must be able to produce a correct deliverable from this reference alone, since the templates do
not ship inside the installed plugin.)

## Non-negotiables
- **Standalone:** a new session must understand the project without the original discovery
  conversation. Do not omit important context to shorten it.
- **Project-specific:** no generic boilerplate and no leftover placeholders where the information is
  already known. Only genuine open items remain, clearly labeled.
- **Honest about uncertainty:** carries assumptions, unknowns, and deferred decisions as such — never
  dressed up as settled fact.

## Required content
The prompt must include:
- Project name and objectives.
- Business context.
- Confirmed requirements (functional and non-functional, with `FR-`/`NFR-` IDs).
- Approved scope (in and explicitly out).
- User roles and workflows.
- Business rules.
- Technical constraints.
- Recommended architecture direction (with the note that the framework runs its own detailed
  architecture process).
- Integrations and data requirements.
- Security and privacy requirements.
- Migration requirements (when applicable) and data-preservation obligations.
- Assumptions and unresolved questions.
- Risks and dependencies.
- Success criteria.
- Expected deliverables.
- Human approval gates.
- Implementation expectations.
- Testing and validation expectations (including requirement → implementation → test traceability).
- Documentation expectations.

## Required instructions to the framework
The prompt must explicitly instruct the engineering framework to:
- Inspect existing materials before implementation.
- Preserve existing data when relevant; prohibit destructive actions without explicit approval.
- Challenge unsupported assumptions rather than accept them.
- **Run its own formal discovery and governance process and honor its own approval gates.** Boynton
  Solution Discovery *prepares* the project; it does not bypass the framework's gates.

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
10. Assumptions, unknowns, risks, dependencies, deferred decisions.
11. Deliverables, approval gates, and the explicit "run your own discovery/governance" instruction.
12. Implementation, testing/traceability, and documentation expectations.

## Self-check before presenting
- Could a fresh session build the right thing from this alone?
- Is every claimed fact actually confirmed, and every assumption labeled?
- Are there any stray placeholders that should have been filled?
- Does it instruct the framework to run its own gates and never self-approve?
