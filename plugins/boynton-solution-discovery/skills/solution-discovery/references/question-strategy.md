# Adaptive Questioning Strategy

The defining behavior of this skill. Determine the **next best question** from the current state of
discovery. Maximize the *quality* of discovery, never the *number* of questions.

## The next-best-question loop
At each turn, generate candidate questions from the active stages and the discovery state, then
score each candidate:

1. **Do we already know this?** (from a prior answer or supplied material) → drop it.
2. **Do we still need it?** Is the answer necessary for the solution, scope, or a key decision?
3. **Materiality:** could the answer materially change the solution, scope, architecture, cost,
   risk, or user experience? Higher materiality ranks higher.
4. **Uncertainty reduction:** does it resolve the single most important open uncertainty right now?
5. **Timing:** is the answer needed now, or can it be safely deferred?
6. **Already asked?** Never repeat a question the user has answered or explicitly deferred.
7. **Will the user know?** If unlikely, reframe, offer options, or mark for later/validation.
8. **Inferable safely?** If it can be inferred from materials with confidence, infer it and
   *confirm* rather than ask cold.
9. **Would an example help?** If the question is abstract, attach concrete example answers.

Ask the single highest-scoring question. Then re-score after the answer.

## Prioritization dimensions
When several questions tie, prefer the one with the greatest impact on, in rough order:
business value → scope → user experience → architecture → data → security → cost → delivery risk →
operational complexity.

## How to ask
- One meaningful question at a time. Conversational, clear, contextual, non-repetitive.
- Briefly say **why** the question matters when it is not obvious.
- Offer example answers or alternatives, especially for open or technical questions.
- Allow the user to say "I don't know" or "defer that" — then help them reason, or record it as a
  deferred question / assumption to validate.
- Follow up when an answer is incomplete or ambiguous — one targeted clarification, not a barrage.
- Match the user's technical level. Never use unexplained engineering jargon with a business user.
- When a technical decision is needed, explain the implications in plain language first, then ask
  for a preference. When asked for a recommendation, give one with its rationale.

## Milestone summaries
At meaningful points (end of a stage, before a direction shift, before deliverables), give a short
recap: what is established, what is still open, what is assumed. Keep it brief — do not dump
analysis after every single answer.

## Anti-patterns (do not do these)
- A fixed questionnaire asked of every user in the same order.
- Asking what is already known or safely inferable.
- Repeating questions or re-asking deferred ones without reason.
- Prolonging discovery to seem thorough. Stop when enough is known to proceed responsibly.
- Burying a non-technical user in jargon.
