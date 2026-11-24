# Usage Examples

**Document date: 2026-11-24 · Plugin v0.1.0**

Short, illustrative shapes of a discovery. Actual conversations adapt to your answers.

## Example 1 — Replace an existing application
> **You:** We want to replace our old job-tracking app.
>
> **Discovery:** What does the current app do well that we must not lose, and what fails today? …
> (later) Is there historical data that must be preserved, and what downtime is acceptable during
> a switchover?

It investigates functionality, users, data/history, integrations, reports, migration, and continuity
before suggesting any direction — and flags migration/data-preservation obligations for the kickoff
prompt.

## Example 2 — "Build an app" that isn't the best answer
> **You:** I want an app to remind the team about our weekly meeting.
>
> **Discovery:** A recurring calendar invite or a channel reminder would do this with no app to
> build or maintain — shall we treat a non-software option as the recommendation?

It is willing to recommend **not** building software.

## Example 3 — AI-assisted, with a reality check
> **You:** Use AI to categorize support tickets.
>
> **Discovery:** Before AI — would a handful of keyword rules get you most of the way at far lower
> cost and risk? If AI is still warranted: what accuracy do you need, who reviews low-confidence
> cases, and what data may the model see?

## Example 4 — Proceeding with documented assumptions
> **You:** Just assume the usual and move on.
>
> **Discovery:** Noted. I'll record these as explicit assumptions, mark which must be validated
> before build, and carry them into the kickoff prompt with validation instructions for the
> framework — not as confirmed facts.

## The confirmation gate
Before any kickoff prompt, you will see a concise solution summary and an explicit request to
confirm. If you confirm, the six deliverables are generated and your confirmation is recorded in
`approval-records.md` (by you, not the AI).
