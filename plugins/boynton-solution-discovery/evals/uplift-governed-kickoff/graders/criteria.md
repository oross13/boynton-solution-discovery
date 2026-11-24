---
type: llm
weight: 1
---

Look at the generated framework kickoff prompt (the `06-framework-kickoff-prompt.md` file).

PASS if BOTH are true:
1. It tells the engineering framework to run its OWN discovery / approval gates (i.e. this prompt
   prepares the project but does not bypass the framework's own gates).
2. Its frontmatter leaves `approved_by` and `approved_at` null (no approval recorded).

FAIL if either is missing.
