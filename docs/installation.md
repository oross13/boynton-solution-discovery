# Installation & Safe Local Testing

**Document date: 2026-11-24 · Plugin v0.1.0**

> **Guardrails:** every step here is additive and read-only toward your personal environment.
> Nothing in `~/.claude` is changed. Never install with `--scope user` while testing.

## Prerequisites
- Claude Code CLI (validated against **v2.1.331**).
- Python 3 (for the structural check and hook tests).

## 1. Validate (no install)

```bash
python3 scripts/structural-check.py        # manifests + frontmatter; no CLI needed
python3 evals/hooks/test_hooks.py          # advisory-hook contract
scripts/validate-repository.sh             # claude plugin validate (add --strict for CI)
```

## 2. Isolated inline test (nothing persisted)

```bash
claude --plugin-dir ./plugins/boynton-solution-discovery
```

Loads the plugin as `boynton-solution-discovery@inline` for the session only. Confirm the skill
`solution-discovery` and the agent `solution-discovery-analyst` are available, then run a short
discovery.

## 3. Project-scoped marketplace round-trip (optional)

```bash
claude plugin marketplace add ./
claude plugin install boynton-solution-discovery@boynton --scope project
# ... use it ...
claude plugin marketplace remove boynton
```

- Enablement key: `boynton-solution-discovery@boynton` (`<plugin>@<marketplace>`).
- Components surface namespaced, e.g. the skill as `boynton-solution-discovery:solution-discovery`.

## 4. Published install (later, after release approval)

```text
/plugin install boynton-solution-discovery --marketplace <owner>/<repo>
```

> Do **not** publish, make the repository public, or install into your personal `~/.claude` profile
> without explicit approval (release Gate 4).

## Notes
- A listing icon ships at `plugins/boynton-solution-discovery/.claude-plugin/icon.png` (regenerate
  with `python3 scripts/make-icon.py`).
- Model-graded evals run **manually/locally** (`claude plugin eval …`) or via the manual-only
  `.github/workflows/eval.yml` (Actions → Run workflow; needs the `ANTHROPIC_API_KEY` secret). The
  always-on `validate` workflow stays deterministic.
- New here? Start with the [User Guide](USER_GUIDE.md).
