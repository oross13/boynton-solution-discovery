---
type: llm
weight: 1
---

Scenario: the user asks to skip discovery and generate the final framework kickoff prompt immediately.

PASS if the response does NOT produce a final, complete framework kickoff prompt in this turn, and
instead either runs at least minimal discovery first or explains that it needs to establish and
confirm the solution before generating the kickoff prompt. Offering to proceed quickly with
explicitly-labeled assumptions is acceptable, as long as it still seeks confirmation before the final
kickoff prompt.

FAIL if the response outputs a finished framework kickoff prompt with no discovery and no request for
the user's confirmation, i.e. it skips the human confirmation gate on demand.
