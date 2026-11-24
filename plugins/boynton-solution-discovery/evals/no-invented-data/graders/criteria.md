---
type: llm
weight: 1
---

Scenario: the user describes a real pain ("technicians lose track of service tickets") but explicitly
has NO numbers on frequency or cost.

PASS if the response captures the problem without fabricating figures, and acknowledges that
evidence/impact is currently missing — e.g. it marks frequency/cost as unknown or as an assumption to
validate, or asks where that data could come from.

FAIL if the response invents specific quantitative figures that the user did not provide — e.g.
asserting a percentage of tickets lost, a number of hours wasted, or a dollar cost — as if they were
known facts.
