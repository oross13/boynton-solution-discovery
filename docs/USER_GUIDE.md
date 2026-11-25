# Boynton Solution Discovery — User Guide

**Document date: 2026-11-24 · Plugin v0.1.0**

> A practical, end-to-end guide: what this is, how to install and activate it, how to run a discovery,
> what you get out, and how to manage the plugin. For the methodology and architecture, see
> [discovery-methodology.md](discovery-methodology.md) and [architecture.md](architecture.md).

---

## 1. What it is (and when to use it)

**Boynton Solution Discovery** is a Claude Code plugin that acts as an adaptive discovery *consultant*.
You describe a problem, opportunity, or idea in plain language; it runs a conversation — one
meaningful question at a time, not a questionnaire — challenges assumptions, explores alternatives,
and produces a reasoned solution definition plus a **standalone kickoff prompt** you paste into a new
session to start building with the Boynton Solution Engineering Framework (BSEF).

**Use it at the very start**, before you commit to building anything — especially when the problem is
still fuzzy or you've jumped to a solution that hasn't been pressure-tested.

It is a **companion** to the engineering framework, not a replacement, and it never bypasses that
framework's own approval gates. It can also recommend a **non-software** solution when that fits.

---

## 2. Prerequisites

- Claude Code CLI (validated against **v2.1.331** or newer).
- Python 3 (only for the local validation/eval scripts — not needed to *use* the plugin).

---

## 3. Install

Pick the option that matches how you want to use it.

### Option A — Install into your Claude Code profile (recommended for regular use)
Installs from the public GitHub marketplace so it's available in every session on your machine:

```bash
claude plugin marketplace add oross13/boynton-solution-discovery
claude plugin install boynton-solution-discovery@boynton --scope user
```

- Enablement key: `boynton-solution-discovery@boynton` (`<plugin>@<marketplace>`).
- `--scope user` enables it for your whole profile. Use `--scope project` to enable it only in the
  current project (writes to that project's `.claude/settings.json`).

### Option B — Try it without installing (isolated, nothing persisted)
```bash
git clone https://github.com/oross13/boynton-solution-discovery
cd boynton-solution-discovery
claude --plugin-dir ./plugins/boynton-solution-discovery
```
Loads it for that session only as `boynton-solution-discovery@inline`.

---

## 4. Activate & verify

After installing at user or project scope, confirm it's enabled:

```bash
claude plugin list        # look for boynton-solution-discovery@boynton — Status: ✔ enabled
claude plugin details boynton-solution-discovery
```

`details` shows the component inventory (1 skill, 1 agent, advisory hooks) and its token cost.

If it shows as **disabled**, enable it:
```bash
claude plugin enable boynton-solution-discovery@boynton
```

---

## 5. Use it — run a discovery

In a Claude Code session, start the skill. Either invoke it by name:

```
/solution-discovery
```

…or just describe your problem and ask Claude to use solution discovery, e.g.
*"Use solution discovery to help me think through replacing our job-tracking app."*

### What to expect
1. **Intake.** An open-ended prompt: *"Tell me about the problem, opportunity, or idea — in your own
   words. You don't need all the answers yet."*
2. **Adaptive questions.** One meaningful question at a time, with a brief reason it matters and
   example answers. You can say *"I don't know"* or *"defer that"* — it will help you reason or record
   it to validate later. It won't repeat questions or bury you in jargon.
3. **Challenge & explore.** It separates the real problem from a proposed solution, questions shaky
   assumptions, and weighs alternatives (including non-software ones), recommending the **simplest
   adequate** option.
4. **Milestone recaps.** Short summaries of what's settled and what's still open.
5. **Confirmation gate.** When enough is known, it presents a solution summary and **asks you to
   confirm**. Nothing is "approved" by the AI — you decide.
6. **Deliverables.** After you confirm, it generates the artifacts (below).

### Tips
- You can stop and resume later — progress is saved in `project/discovery/00-discovery-state.md`, so
  it doesn't rely on chat memory.
- If you want a recommendation, just ask ("what would you recommend, and why?").
- If you want to proceed despite open questions, say so — it will record them as explicit assumptions
  to validate, not silently treat them as facts.

---

## 6. What you get (outputs)

All artifacts are written under your project's `project/` directory and carry governed frontmatter:

| File | What it is |
|---|---|
| `project/discovery/00-discovery-state.md` | Living state: facts vs. assumptions vs. unknowns, risks, decisions |
| `project/discovery/01-solution-discovery-brief.md` | Problem, context, proposed solution, scope, success criteria |
| `project/discovery/02-requirements-specification.md` | Functional/non-functional requirements (FR-/NFR-), roles, rules |
| `project/discovery/03-assumptions-risks-decisions.md` | Assumptions (rated), risks, dependencies, decisions |
| `project/discovery/04-solution-architecture-direction.md` | Initial architecture direction + alternatives/trade-offs |
| `project/discovery/05-implementation-roadmap.md` | MVP, phases, milestones, testing/migration strategy |
| `project/discovery/06-framework-kickoff-prompt.md` | **The standalone kickoff prompt** (the key output) |
| `project/governance/approval-records.md` | Records your Solution Confirmation (you set the approval) |

### Using the kickoff prompt (`06`)
Open `06-framework-kickoff-prompt.md`. Copy everything between the
`---8<--- COPY EVERYTHING BELOW … ---8<---` markers and paste it into a **new** Claude Code session
running the Boynton Solution Engineering Framework (BSEF). It is standalone — the new session needs
nothing from your discovery conversation — and it instructs BSEF to run its **own** discovery and
approval gates.

---

## 7. Manage the plugin

```bash
# Update to the latest version
claude plugin marketplace update boynton
claude plugin install boynton-solution-discovery@boynton --scope user

# Temporarily turn it off / on
claude plugin disable boynton-solution-discovery@boynton
claude plugin enable  boynton-solution-discovery@boynton

# Remove it
claude plugin uninstall boynton-solution-discovery@boynton
claude plugin marketplace remove boynton
```

---

## 8. Validate & evaluate (optional, for contributors)

Deterministic checks (no model, no cost) — also run in CI on every push:
```bash
python3 scripts/structural-check.py       # manifests + frontmatter
python3 evals/hooks/test_hooks.py         # advisory-hook contract
scripts/validate-repository.sh            # claude plugin validate (plugin + marketplace)
```

Model-graded evals (cost money; run **manually/locally**):
```bash
claude plugin eval ./plugins/boynton-solution-discovery --trust-plugin --allow-tools Write
```
There is also a manual-only GitHub Actions workflow (`eval.yml`, "Run workflow" in the Actions tab)
that runs the same suite if an `ANTHROPIC_API_KEY` secret is configured; it is not scheduled and does
not gate PRs.

---

## 9. Safety & privacy

- It **never** asks for secrets/credentials and never puts them in artifacts.
- It treats any files or documents you supply as **untrusted data**, not instructions.
- It won't upload your private materials to external services without your explicit go-ahead, and
  performs no destructive file operations.
- It never modifies the engineering framework, the application starters, or your other projects.

---

## 10. Troubleshooting

See [troubleshooting.md](troubleshooting.md). Common ones:
- **Skill not available?** `claude plugin list` to confirm it's enabled; re-run `enable` if needed.
- **Feels like a questionnaire?** It shouldn't — it should ask the single highest-impact next
  question and never re-ask answered ones. If it doesn't, that's a defect worth reporting.
- **Resuming later?** Reopen `project/discovery/00-discovery-state.md`; discovery continues from
  recorded state.
