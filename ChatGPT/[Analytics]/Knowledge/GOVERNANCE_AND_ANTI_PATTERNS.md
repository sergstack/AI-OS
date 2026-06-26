# Governance and Anti-Patterns

## Governance principles

- Deterministic calculations before LLM narrative.
- Traceability before automation.
- Main files before slices.
- Evidence before conclusions.
- Acceptance before production readiness.
- Analysis inside `[Analytics]` before handoff.

## Evidence labels

Use:

```text
DATA FACT
CALCULATION RESULT
INTERPRETATION
RECOMMENDATION
HYPOTHESIS
LIMITATION
BLOCKER
```

## Blockers

Do not publish final management conclusion when:

- data contract missing;
- grain missing;
- DQ Fail;
- unreconciled totals;
- missing metric formula;
- unsupported cause;
- risk without basis;
- action without owner/due date;
- no main mart for a mart-based conclusion.

## Anti-patterns

| Anti-pattern | Why bad | Correct action |
|---|---|---|
| Handoff to Codex too early | Analytics loses its role | Analyze first, handoff implementation only |
| Slices before main files | Inconsistent outputs | Build `stage_main_full`, then `mart_main_full`, then slices |
| Raw-to-memo | Unsupported conclusions | Use mart/evidence |
| LLM as calculation source | Non-deterministic truth | Calculate deterministically |
| Hidden business logic | Cannot audit | Document formulas/classifiers |
| Pretty memo before QA | Looks right, may be wrong | QA first |
| Low Confidence as fact | Misleading | Label hypothesis |
| Risk without basis | Decorative risk | Add `risk_basis` or remove |
| Action without owner/date | Not actionable | Add owner/due date/status |

## Metric / artifact explosion

Anti-pattern:
A short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.

Why bad:

- user cannot inspect the result;
- decision signal is buried;
- QA fields become noise;
- compact task becomes full audit project.

Correct action:

- classify output mode first;
- default to compact view;
- expose only decision-relevant metrics;
- move evidence/QA/lineage to appendix or internal design;
- ask for full audit mode only when needed.

## Production readiness rule

Do not claim production readiness unless:

- implementation exists;
- tests passed;
- smoke QA recorded;
- acceptance criteria passed;
- residual risks listed;
- rollback/release notes exist.
