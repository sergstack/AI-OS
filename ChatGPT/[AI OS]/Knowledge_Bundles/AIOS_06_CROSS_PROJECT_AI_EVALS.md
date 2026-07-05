# [AI OS] — Cross-Project AI Evals

## Purpose

Compact upload artifact for [AI OS] covering lightweight AI eval and LLM-as-a-Judge governance across projects.

## Source files

- `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`
- `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`
- `ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md`
- `ChatGPT/[AI OS]/Knowledge/CROSS_PROJECT_EVAL_PLAYBOOK.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- runtime_eval_automation: no

---

# Content

## Eval Registry

LLM-as-a-Judge is a reviewer, not truth.

Deterministic checks override LLM judge for calculations, tests, schemas, contracts, formulas, metric definitions, column names, and business rules.

| Eval type | Owner project | Primary evidence | Verdict |
|---|---|---|---|
| AI OS evidence check | `[AI OS]` | source files, confidence labels, promotion gates | supported / weak / unsupported |
| LLM output quality | `[LLM]` | context package, prompt, output, unsupported claims | pass / revise / blocked |
| Analytics memo QA | `[Analytics]` | data contract, stage, mart, formulas, QA checklist | pass / revise / blocked |
| Codex PR Judge | `[Codex]` / `[Thinking]` | diff, checks, scope, rollback, risks | pass / revise / blocked |
| Agent loop review | `[AI OS]` / `[Thinking]` | loop goal, allowed actions, checks, stop conditions | pass / revise / blocked |

Minimal eval record:

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

## Judge Calibration

Judge output can help find unsupported claims, missing checks, weak evidence, scope creep, and unclear next steps.

Judge output cannot validate calculations, tests, schemas, formulas, contracts, metric definitions, column names, or business logic by opinion.

Judge results can vary by model class, prompt wording, context quality, missing evidence, output format, hidden assumptions, and broad criteria.

Use:

```text
pass
revise
blocked
```

`pass` means ready for human review or adoption decision, not production-ready by default.

If tests fail, data QA fails, schema checks fail, or contracts are missing, eval status cannot be `pass` even if the judge likes the text.

## Golden Eval Cases

Golden cases cover:

- AI OS evidence: source files or fresh sources named, confidence visible, promotion gates respected.
- LLM output: facts separated from interpretation, unsupported claims listed, judge/revise status present.
- Analytics memo: deterministic calculations, explicit grain/period/filter/method, claims trace to mart/evidence.
- Codex PR: scope matches goal, checks actually run or blockers stated, no unrelated refactor.
- Agent loop: supervised `goal -> action -> check -> revise/rerun -> acceptance -> next trigger` with bounded retry and human acceptance.

## Cross-Project Playbook

| Work item | Owner project | Use |
|---|---|---|
| Evidence confidence, promotion gate, AI OS pattern | `[AI OS]` | AI OS evidence check |
| LLM output quality, prompt quality, judge/revise | `[LLM]` | LLM quality gate |
| Calculations, data QA, schemas, marts, analytical memo | `[Analytics]` | deterministic QA plus memo QA |
| PR review, implementation checks, test evidence | `[Codex]` | PR Judge and workflow eval |
| Strategic critique, risk review, revisor pass | `[Thinking]` | judge/revisor decision review |

Flow:

```text
route eval type
-> gather compact evidence
-> run deterministic checks where applicable
-> run judge/review
-> revise or block
-> final status
-> human acceptance or next step
```

## Boundaries

RAGAS and SWE-Bench may be referenced as future/reference patterns only.

This layer does not add runtime RAGAS setup, SWE-Bench benchmark setup, embeddings, vector DB, semantic search, web UI, autonomous retrieval, runtime artifacts, logs, secrets, or production eval automation.
