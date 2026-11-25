# boynton-solution-discovery

**Boynton Solution Discovery** — an adaptive AI discovery consultant, packaged as a Claude Code
plugin. It turns an initial business problem, operational challenge, automation opportunity,
application idea, or integration requirement into a well-reasoned solution definition and a
comprehensive, **standalone kickoff prompt** — conforming to the Boynton Discovery-to-Engineering
Handoff Standard v1.0 — that starts a new project in the Boynton Solution Engineering Framework
(BSEF).

It is a **companion** to BSEF (`claude-code-engineering-environment`, plugin `bsef`), not a
replacement. It is independent, additive, and does not modify the framework, the application
starters, or any existing project.

> Boynton Solution Discovery *prepares* a project. It does **not** bypass BSEF's own discovery and
> approval gates.

## What it does

- Runs an **adaptive** discovery conversation — one meaningful question at a time, not a fixed
  questionnaire. Questions adapt to the problem, the answers so far, and what is still uncertain.
- **Challenges assumptions** and separates the real problem from a proposed solution.
- Explores alternatives and recommends the **simplest adequate** solution — including a non-software
  option when that fits.
- Tracks **confirmed facts vs. assumptions vs. unknowns** and never silently promotes one to another.
- Requires **explicit human confirmation** before producing the final kickoff prompt. The AI
  recommends; a human approves.
- Works across domains: new apps, replacements, automation, integrations, AI-assisted solutions,
  reporting, local/personal tools, and process changes.

## Components

- **Skill `solution-discovery`** — orchestrates the discovery conversation in the main session and
  produces the deliverables. Supporting references live under `skills/solution-discovery/references/`.
- **Agent `solution-discovery-analyst`** — read-only advisory analyst for assumptions, risks,
  alternatives, and readiness. It never approves its own recommendations.
- **Advisory hooks** — read-only, never-blocking, always-exit-0 checks on governed artifact
  frontmatter and approval records (self-approval guard).
- **Templates** — the discovery-state model and six deliverable templates, plus governance ledgers,
  all carrying the framework's governed frontmatter so output is framework-compatible.

## Deliverables

1. `01-solution-discovery-brief.md`
2. `02-requirements-specification.md`
3. `03-assumptions-risks-decisions.md`
4. `04-solution-architecture-direction.md`
5. `05-implementation-roadmap.md`
6. `06-framework-kickoff-prompt.md` — the standalone kickoff prompt (the most important output)

A living `00-discovery-state.md` persists progress across sessions.

## Install & use

**📘 Full walkthrough: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)** (install → activate → run a
discovery → outputs → manage). See also [installation.md](docs/installation.md) and
[getting-started.md](docs/getting-started.md).

Install into your Claude Code profile from the public marketplace:

```bash
claude plugin marketplace add oross13/boynton-solution-discovery
claude plugin install boynton-solution-discovery@boynton --scope user
```

Or try it without installing (nothing persisted to `~/.claude`):

```bash
claude --plugin-dir ./plugins/boynton-solution-discovery
```

Then invoke the skill — `/solution-discovery` — and describe your problem in your own words.

## Validate

```bash
python3 scripts/structural-check.py      # manifests + frontmatter (no CLI needed)
python3 evals/hooks/test_hooks.py        # advisory-hook contract
scripts/validate-repository.sh           # claude plugin validate (plugin + marketplace)
claude plugin eval ./plugins/boynton-solution-discovery --trust-plugin --allow-tools Write  # model-graded suite
```

Deterministic checks run in CI (`.github/workflows/validate.yml`); the model-graded eval runs
separately (`eval.yml`, manual/weekly, needs the `ANTHROPIC_API_KEY` secret).

## Layout

```
.claude-plugin/marketplace.json          # marketplace "boynton"
plugins/boynton-solution-discovery/      # the plugin
  .claude-plugin/plugin.json
  agents/solution-discovery-analyst.md
  skills/solution-discovery/SKILL.md + references/
  hooks/hooks.json  scripts/             # advisory governance hooks
templates/discovery/  templates/governance/
evals/  scripts/  docs/
```

## Principle

Help the user think through a problem before committing to a solution. Be curious, analytical,
adaptive, practical, and honest about uncertainty. The goal is not the longest prompt — it is the
**right** project definition and kickoff prompt for the problem at hand.

## License

MIT — see [LICENSE](LICENSE).
