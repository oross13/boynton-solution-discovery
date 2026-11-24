---
type: llm
weight: 1
---

Scenario: the user has described only a solution ("build a mobile app with push notifications for
warehouse staff") and not the underlying problem.

PASS if the response separates the stated solution from the underlying problem and investigates the
problem first — e.g. it asks what is going wrong today, what outcome is wanted, or why a mobile app
specifically, before scoping or designing the app. It is acceptable (and good) to note that a
different solution might fit once the problem is clear.

FAIL if the response takes "mobile app with push notifications" as settled and begins scoping,
choosing a stack, or listing app features without first probing the underlying problem.
