# AI Eval Registry

## Purpose

Define a lightweight cross-project eval registry for AI-OS.

This registry connects existing judge/revise, PR Judge, Codex workflow evals, Analytics QA, and AI OS evidence checks without adding runtime eval automation.

## Rule

LLM-as-a-Judge is a reviewer, not truth.

Deterministic checks override LLM judge for:

- calculations;
- tests;
- schemas;
- contracts;
- formulas;
- metric definitions;
- column names;
- business rules.

If deterministic evidence and LLM judge disagree, use deterministic evidence and mark the judge result as `revise` or `blocked`.

## Eval Types

| Eval type | Owner project | Primary evidence | Verdict |
|---|---|---|---|
| AI OS evidence check | `[AI OS]` | source files, confidence labels, promotion gates | supported / weak / unsupported |
| LLM output quality | `[LLM]` | context package, prompt, output, unsupported claims | pass / revise / blocked |
| Analytics memo QA | `[Analytics]` | data contract, stage, mart, formulas, QA checklist | pass / revise / blocked |
| Codex PR Judge | `[Codex]` / `[Thinking]` | diff, checks, scope, rollback, risks | pass / revise / blocked |
| Agent loop review | `[AI OS]` / `[Thinking]` | loop goal, allowed actions, checks, stop conditions | pass / revise / blocked |

## Lightweight Eval Record

```text
eval_id:
owner_project:
eval_type:
input:
evidence_checked:
deterministic_checks:
judge_verdict:
required_revision:
final_status:
limitations:
next_step:
```

## Reference-Only Patterns

RAGAS and SWE-Bench may be referenced as future or external patterns for inspiration.

Do not add runtime RAGAS setup, SWE-Bench benchmark setup, embeddings, vector DB, semantic search, web UI, autonomous retrieval, runtime artifacts, logs, secrets, or production eval automation.
