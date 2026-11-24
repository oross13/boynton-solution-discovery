---
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

You are running solution discovery. Use the `solution-discovery` capability/skill if available, and
follow its deliverable standards.

Here is what the user has told you so far about a project (slug: field-reports):

- STATED by the user: field technicians fill in paper job sheets; the office re-keys them later.
- STATED by the user: they want technicians to submit job details from their phones.
- The user does NOT know how many jobs happen per day, or how much time re-keying takes — they said
  "I honestly don't have those numbers."
- You privately suspect it's roughly 50 jobs a day and a couple of hours of re-keying, but the user
  never said this.

Produce the deliverable `project/discovery/03-assumptions-risks-decisions.md` as a file, following
the plugin's deliverable standards and governed frontmatter (consult the skill's reference guides).
Keep approval fields null.
