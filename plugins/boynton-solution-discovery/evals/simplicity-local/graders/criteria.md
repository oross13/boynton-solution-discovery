---
type: llm
weight: 1
---

Scenario: a single user wants a personal, offline, laptop-only tool to track books they read.

PASS if the response keeps the solution proportionate to a single-user local tool — e.g. it leans
toward a simple local app with local storage, and/or it explicitly avoids or does not introduce
accounts/authentication, multi-user features, cloud hosting, or multi-tenancy. Asking a relevant
clarifying question is fine.

FAIL if the response proposes enterprise or multi-user architecture for this personal tool: user
accounts/login, cloud sync or hosting as a requirement, multi-tenancy, role-based access control, or
a server/identity-provider stack that a one-person offline tool does not need.
