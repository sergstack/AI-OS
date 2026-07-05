# Cross Project Eval Playbook

## Purpose

Route eval and judge work to the right AI-OS project.

## Ownership Map

| Work item | Owner project | Use |
|---|---|---|
| Evidence confidence, promotion gate, AI OS pattern | `[AI OS]` | AI OS evidence check |
| LLM output quality, prompt quality, judge/revise | `[LLM]` | LLM quality gate |
| Calculations, data QA, schemas, marts, analytical memo | `[Analytics]` | deterministic QA plus memo QA |
| PR review, implementation checks, test evidence | `[Codex]` | PR Judge and workflow eval |
| Strategic critique, risk review, revisor pass | `[Thinking]` | judge/revisor decision review |

## Eval Flow

```text
route eval type
-> gather compact evidence
-> run deterministic checks where applicable
-> run judge/review
-> revise or block
-> final status
-> human acceptance or next step
```

## Deterministic First

Use deterministic checks before LLM judge for:

- arithmetic;
- reconciliation;
- tests;
- schemas;
- contracts;
- formulas;
- metric definitions;
- column names;
- business logic.

LLM judge can review clarity, evidence gaps, unsupported claims, scope fit, risks, and missing acceptance criteria.

## Eval / Judge Output

```text
Eval type:
Owner project:
Evidence checked:
Deterministic checks:
Judge verdict:
Required revision:
Risks / limitations:
Final status:
Next step:
```

## Boundaries

This playbook does not add:

- runtime RAGAS;
- SWE-Bench benchmark setup;
- embeddings;
- vector DB;
- semantic search;
- web UI;
- autonomous retrieval;
- runtime artifacts;
- logs;
- secrets;
- production eval automation.

RAGAS and SWE-Bench remain future/reference patterns only.
