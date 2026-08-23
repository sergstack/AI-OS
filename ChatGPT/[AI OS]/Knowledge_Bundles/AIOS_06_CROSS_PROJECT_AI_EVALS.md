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
- source_fingerprint: sha256:5e9c7676943c5ab29388a5d7214f741d3432d6de12ef2bb8429c6c17b340415d
- runtime_eval_automation: no
- acceptance_status: candidate / ready for human review

---

# Content

## AI Eval Registry Summary

Single lightweight registry of AI evals across AI-OS projects.

Status values:

```text
draft
candidate
active
blocked
deprecated
```

Verdict values:

```text
pass
revise
blocked
```

Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business rules.

Registry definitions:

| eval_id | workflow | owner_project | eval_type | judge/check |
|---|---|---|---|---|
| `AIOS-EVIDENCE` | AI OS evidence answer | `[AI OS]` | evidence | confidence and source check |
| `LLM-OUTPUT` | output QA; memo review is risk-triggered | `[LLM]` | deterministic QA + triggered judge | output contract + required Judge triggers |
| `ANALYTICS-QA` | analytical memo / QA | `[Analytics]` | deterministic QA + narrative judge | data contract, mart, metric, period, grain, QA status |
| `CODEX-PR` | PR Judge | `[Codex]` / `[Thinking]` | workflow eval | diff, checks, scope, rollback |
| `AGENT-LOOP` | supervised loop review | `[AI OS]` / `[Thinking]` | governance eval | loop acceptance checklist |
| `THINKING-DECISION` | decision review | `[Thinking]` | judge | assumptions, downside, reversibility, revisit trigger |

For memo generation, the active specialization is deterministic QA first,
Judge only when a documented trigger applies, and revision only from explicit
findings. Accepted run evidence is recorded in the canonical `[LLM]` project
status; the registry stores eval definitions rather than run results.

## Judge Calibration Summary

Judge is a reviewer, not truth.

Rules:

- Judge must use explicit rubric.
- Judge output must include `pass`, `revise`, or `blocked`.
- High-risk outputs require human review.
- Unsupported claims must be listed, not silently fixed.
- Revision must be traceable to judge findings.
- For material or high-risk conclusions, identify material facts,
  contradictions, and new evidence; determine whether they change the decision
  boundary; and verify that the conclusion or recommendation incorporates the
  consequence.
- Return `revise` or `blocked` when a recommendation remains contradicted or
  materially qualified without an explicit limitation or corresponding change.
- Source presence alone is not sufficient evidence integration.
- Do not hardcode permanent model names as governance truth.

Use model classes:

```text
fast
reasoning
high-reasoning
local
judge
```

When judge model class changes, rerun golden eval cases, compare verdict drift, record risk if verdicts change, and do not silently promote new judge behavior.

## Golden Eval Cases Summary

Golden cases are small reusable manual smoke QA examples, not runtime logs or benchmark framework.

Required cases:

- `CASE-AIOS-EVIDENCE-001`: AI OS evidence answer; must detect unsupported / weak claims.
- `CASE-LLM-JUDGE-001`: LLM draft -> judge -> revise; must detect unsupported claims and missing limitations.
- `CASE-ANALYTICS-QA-001`: Analytics memo; must require source mart/table, metric, period, grain, QA status, confidence.
- `CASE-CODEX-PR-001`: Codex PR Judge; must detect scope creep, missing checks, rollback gaps.
- `CASE-AGENT-LOOP-001`: Agent Loop Design; must distinguish supervised loop from autonomous agentic workflow.
- `CASE-THINKING-DECISION-001`: Thinking decision review; must detect hidden assumptions, downside, reversibility, revisit trigger.

## Cross-Project Eval Playbook Summary

Eval routing:

| Output / workflow | Owner project | Eval method | Verdict |
|---|---|---|---|
| AI concept / KB claim | `[AI OS]` | evidence / confidence check | supported / weak / mixed / unsupported |
| LLM draft / prompt output | `[LLM]` | judge -> revise | pass / revise / blocked |
| Financial / analytical memo | `[Analytics]` | deterministic QA + narrative judge | pass / revise / blocked |
| Repo change / PR | `[Codex]` | PR Judge + checks | pass / revise / blocked |
| Decision memo | `[Thinking]` | assumption / risk / reversibility judge | pass / revise / blocked |
| Agent loop design | `[AI OS]` | Loop Acceptance Checklist | pass / revise / blocked |

Evaluation order:

1. Deterministic checks first when available.
2. Source/evidence checks before narrative polish.
3. LLM judge reviews only against explicit criteria.
4. Revise only from visible judge findings.
5. Human acceptance for high-risk outputs.

Output format:

```text
Eval:
Owner project:
Input reviewed:
Checks:
Judge verdict:
Required fixes:
Residual risks:
Final quality status:
Next step:
```

## Boundaries

RAGAS and SWE-Bench may be referenced as future/reference patterns only.

This layer does not add runtime RAGAS setup, SWE-Bench benchmark runner, vector DB, embeddings, semantic search, web UI, autonomous retrieval, autonomous eval agents, production automation, logs, runtime artifacts, eval result database, secrets, or `.env`.
