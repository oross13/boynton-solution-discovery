---
document: assumptions-risks-decisions
project: <project-slug>
version: 0.1.0
status: Draft
created: <YYYY-MM-DD>
approved_by: null
approved_at: null
---

# Assumptions, Risks & Decisions — <Project Name>

> Keep confirmed facts, assumptions, hypotheses, and open questions strictly distinct. Clearly
> separate human-approved **decisions** from AI **recommendations**. An AI may recommend but must
> never record its own approval.

## 1. Confirmed facts
| # | Fact | Source |
|---|---|---|
| | | |

## 2. Assumptions
> **Must validate before build?** flags a hard validation *prerequisite* (Y/N). **Test-first priority**
> ranks *investigation order relative to other assumptions* and is independent of it: P0 = validate before
> substantial engineering investment, P1 = soon, P2 = opportunistic, — = not prioritized. A high-Importance
> + low-Confidence assumption is a high-impact assumption → give it a Test-first priority and an Evidence
> ref. Ordinary low-impact unknowns stay in §3. Priority is optional — never invented.
| ID | Assumption | Importance (H/M/L) | Confidence (H/M/L) | Must validate before build? | Test-first priority (P0/P1/P2/—) | Risk if wrong | Evidence ref | Recommended validation |
|---|---|---|---|---|---|---|---|---|
| A-001 | | | | | | | | |

## 3. Unknowns / open questions
| # | Question | Why it matters | Could it change the solution? |
|---|---|---|---|
| | | | |

## 4. Risks
| ID | Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|---|
| R-001 | | | | |

## 5. Dependencies
| # | Dependency | Type (external/technical) | Owner | Notes |
|---|---|---|---|---|
| | | | | |

## 6. Decisions made (human-approved)
| ID | Decision | Approved by (human) | Date | Rationale |
|---|---|---|---|---|
| D-001 | | | | |

## 7. Decisions deferred
| # | Decision | Why deferred | When needed by |
|---|---|---|---|
| | | | |

## 8. AI recommendations (not yet decisions)
| # | Recommendation | Rationale | Awaiting whose decision |
|---|---|---|---|
| | | | |

## 9. Recommended validation activities
-

*Unresolved items here are carried into the kickoff prompt (06) with validation instructions for the
framework. When §2 holds P0/P1 test-first assumptions, they populate the optional "Prioritized
assumptions" section of 06 (Evidence ref → that section's Evidence / confidence column; Test-first
priority → its Test first? column).*
