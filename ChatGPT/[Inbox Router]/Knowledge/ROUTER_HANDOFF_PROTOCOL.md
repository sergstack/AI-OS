# Router Handoff Protocol

Reference material. Active handoff behavior is defined by
`HANDOFF_PROTOCOL.md`.

Use handoff when the destination is another project and the Router should package
the work without solving it.

# Handoff

From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected output:
Acceptance criteria:
Risks:
Open questions:
Suggested first step:

## Project-Specific Notes

### To `[AI OS]`

Use for evidence / pattern / governance check. Include the AI concept, use case,
claim, or pattern to inspect. State whether the Router has facts or only a
hypothesis.

### To `[Thinking]`

Use for decision / scenario / risk analysis. Include the decision to frame,
known options, constraints, tradeoffs, and the output format requested.

### To `[Analytics]`

Use for data / metrics / deterministic analysis. Include input files or data
sources, metrics, periods, currencies if relevant, expected calculations, and
verification needs. Do not calculate in Router.

### To `[LLM]`

Use for prompt / workflow / model routing / eval. Include the target user,
workflow goal, input examples, output format, constraints, and evaluation
criteria.

### To `[Codex]`

Use for implementation, tests, refactor, repo changes, or goal-to-execution
work. Broad repository or workflow goals may use Goal Mode. Use a strict task
package only when the work is high-risk, already scoped, or explicitly requested.
Include known:

- context;
- objective;
- inputs;
- files to inspect;
- files allowed to modify;
- forbidden actions;
- expected outputs;
- acceptance criteria;
- tests / smoke checks;
- rollback plan.

## Boundary

Router routes.
Router clarifies.
Router packages.
Router does not solve.
