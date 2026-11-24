#!/usr/bin/env python3
"""Structural validation for the Boynton Solution Discovery repository.

No Claude CLI required. Checks the marketplace + plugin manifests and the frontmatter
of every agent, skill, and governed template. Exit 0 = pass, 1 = errors. Complements
`claude plugin validate` and runs in CI. Usage: `python3 scripts/structural-check.py`.
"""
import json
import os
import re
import sys
import glob

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PLUGIN = os.path.join(ROOT, "plugins", "boynton-solution-discovery")
RESERVED_PREFIXES = ("claude-", "anthropic-", "anthropics-", "cc-plugin-")
RESERVED_EXACT = {"claude", "anthropic", "claude-code"}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VALID_STATUS = {"Draft", "Under Review", "Approved", "Superseded"}
TEMPLATE_REQUIRED = ["document", "project", "version", "status", "created",
                     "approved_by", "approved_at"]

errors, warnings = [], []


def err(m):
    errors.append(m)


def warn(m):
    warnings.append(m)


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---", open(path, encoding="utf-8").read(), re.S)
    if not m:
        return None
    d = {}
    for line in m.group(1).splitlines():
        if line[:1] not in (" ", "\t") and ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    return d


def check_manifests():
    mkt_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    plg_path = os.path.join(PLUGIN, ".claude-plugin", "plugin.json")
    try:
        mkt = json.load(open(mkt_path))
    except Exception as e:
        return err(f"marketplace.json invalid: {e}")
    try:
        plg = json.load(open(plg_path))
    except Exception as e:
        return err(f"plugin.json invalid: {e}")

    name = mkt.get("name", "")
    if not name:
        err("marketplace.json missing 'name'")
    if name.startswith(RESERVED_PREFIXES) or name in RESERVED_EXACT:
        err(f"marketplace name '{name}' uses a reserved prefix/name")
    if not (mkt.get("owner") or {}).get("name"):
        err("marketplace.json missing owner.name")
    plugins = mkt.get("plugins") or []
    if not plugins:
        err("marketplace.json has no plugins")
    for p in plugins:
        if not p.get("name") or not p.get("source"):
            err(f"marketplace plugin entry missing name/source: {p}")
        src = p.get("source", "")
        if isinstance(src, str) and not src.startswith("./"):
            err(f"plugin source should start with './': {src}")

    pname = plg.get("name", "")
    if not pname or not KEBAB.match(pname):
        err(f"plugin.json name missing or not kebab-case: '{pname}'")
    if pname.startswith(RESERVED_PREFIXES) or pname in RESERVED_EXACT:
        err(f"plugin name '{pname}' uses a reserved prefix/name")
    if pname and pname not in [p.get("name") for p in plugins]:
        err(f"plugin name '{pname}' not found as a marketplace entry name")

    # Versions must stay in sync between the marketplace entry and the plugin manifest.
    entry = next((p for p in plugins if p.get("name") == pname), None)
    if entry and entry.get("version") != plg.get("version"):
        err(f"version mismatch: marketplace '{entry.get('version')}' "
            f"vs plugin.json '{plg.get('version')}'")


def check_agents():
    files = glob.glob(os.path.join(PLUGIN, "agents", "*.md"))
    if not files:
        warn("no agents found")
    for f in files:
        fm = frontmatter(f)
        b = os.path.basename(f)
        if fm is None:
            err(f"agent {b}: no frontmatter")
            continue
        if not fm.get("name"):
            err(f"agent {b}: missing 'name'")
        if not fm.get("description"):
            err(f"agent {b}: missing 'description'")


def check_skills():
    files = glob.glob(os.path.join(PLUGIN, "skills", "*", "SKILL.md"))
    if not files:
        warn("no skills found")
    for f in files:
        fm = frontmatter(f)
        d = os.path.basename(os.path.dirname(f))
        if fm is None:
            err(f"skill {d}: no frontmatter")
            continue
        if not fm.get("name"):
            err(f"skill {d}: missing 'name'")
        if not fm.get("description"):
            warn(f"skill {d}: missing 'description' (recommended)")
        desc = fm.get("description", "")
        if len(desc) > 1536:
            warn(f"skill {d}: description exceeds 1536 chars ({len(desc)})")


def check_templates():
    for f in glob.glob(os.path.join(ROOT, "templates", "discovery", "*.md")) + \
             glob.glob(os.path.join(ROOT, "templates", "governance", "*.md")):
        fm = frontmatter(f)
        b = os.path.relpath(f, ROOT)
        if fm is None:
            err(f"template {b}: no frontmatter")
            continue
        missing = [k for k in TEMPLATE_REQUIRED if k not in fm]
        if missing:
            err(f"template {b}: missing frontmatter {missing}")
        if fm.get("status") not in VALID_STATUS:
            err(f"template {b}: invalid status '{fm.get('status')}'")


def main():
    check_manifests()
    check_agents()
    check_skills()
    check_templates()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    n_agents = len(glob.glob(os.path.join(PLUGIN, 'agents', '*.md')))
    n_skills = len(glob.glob(os.path.join(PLUGIN, 'skills', '*', 'SKILL.md')))
    print(f"\nChecked: {n_agents} agents, {n_skills} skills, "
          f"manifests, templates — {len(errors)} error(s), {len(warnings)} warning(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
