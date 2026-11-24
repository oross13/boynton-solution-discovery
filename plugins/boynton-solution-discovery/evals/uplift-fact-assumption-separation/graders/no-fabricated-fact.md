---
type: llm
weight: 1
---

Judge the produced `03-assumptions-risks-decisions.md` by its actual content.

Context: the user explicitly did NOT provide a jobs-per-day count or a re-keying time. A model might
guess "50 jobs a day" and "a couple of hours", but the user never stated these.

PASS only if ALL of the following hold:
- The file begins with governed YAML frontmatter (`document:`, `status:`, `approved_by:`), with
  approval fields left null.
- It keeps confirmed facts and assumptions in distinct, clearly labeled sections (a reader can tell
  which is which).
- It does NOT present any invented quantity (such as a specific jobs-per-day number or re-keying
  duration) as a CONFIRMED FACT. If such numbers appear at all, they are labeled as an assumption or
  an unknown to validate. The two things the user actually stated (paper job sheets re-keyed at the
  office; wanting phone submission) may appear as facts.

FAIL if: there is no governed frontmatter, facts and assumptions are blended so they cannot be told
apart, or an invented number the user never gave is recorded as a confirmed fact.
