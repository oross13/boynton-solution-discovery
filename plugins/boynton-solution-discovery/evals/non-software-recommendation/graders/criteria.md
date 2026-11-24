---
type: llm
weight: 1
---

Scenario: the user wants to build a custom app to send reminders for a weekly meeting.

PASS if the response does at least one of: raises a simpler non-software option (e.g. a recurring
calendar invite, a channel/chat reminder, an existing tool's built-in reminder) as worth considering
before building an app, OR explicitly separates the underlying problem ("people forget the meeting")
from the proposed solution ("a custom app") and probes it. The response should behave like a
consultant, not immediately start scoping the app.

FAIL if the response accepts "build a custom app" at face value and proceeds to scope or design the
app without surfacing a simpler alternative or questioning whether an app is warranted.
