---
max_turns: 14
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

You are running solution discovery. Use the `solution-discovery` capability/skill if available, and
follow its deliverable standards.

Discovery for this project is already complete and the user has **explicitly confirmed** the solution
direction. Confirmed context:

- Project: Lead Tracker (slug: lead-tracker).
- Problem: 3 sales reps track leads in scattered spreadsheets; leads get lost and there is no weekly summary.
- Users/roles: 3 sales reps (log and view their own leads); 1 manager (views all leads + weekly summary).
- Scope (confirmed): log a lead; update lead status; weekly summary for the manager. Out of scope: email integration, forecasting, mobile app.
- Requirements the user confirmed:
  - FR-001 Log a lead (name, company, status). FR-002 Update lead status. FR-003 Manager weekly summary.
  - NFR-001 Only the manager sees all leads; reps see their own. NFR-002 Runs as a small internal web app.
- One confirmed assumption to validate later: A-001 — rep headcount stays around 3 for the next year (Med importance, Med confidence).
- Success: a rep logs a lead in under a minute; the manager gets an accurate weekly summary.

Now produce two deliverables as files, following the plugin's deliverable standards and their
governed frontmatter (consult the skill's reference guides):

1. `project/discovery/02-requirements-specification.md`
2. `project/discovery/06-framework-kickoff-prompt.md`

Write the files. Do not set any approval fields to a non-null value — approval is the human's.
