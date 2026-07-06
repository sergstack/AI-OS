# Cross-Project Eval Playbook

## Purpose

Route AI evals to the right project and choose the right judge/check.

This playbook connects existing checks; it does not replace project-specific QA, PR Judge, judge/revise, or evidence rules.

## Eval Routing

| Output / workflow | Owner project | Eval method | Verdict |
|---|---|---|---|
| AI concept / KB claim | `[AI OS]` | evidence / confidence check | supported / weak / mixed / unsupported |
| LLM draft / prompt output | `[LLM]` | judge -> revise | pass / revise / blocked |
| Financial / analytical memo | `[Analytics]` | deterministic QA + narrative judge | pass / revise / blocked |
| Repo change / PR | `[Codex]` | PR Judge + checks | pass / revise / blocked |
| Decision memo | `[Thinking]` | assumption / risk / reversibility judge | pass / revise / blocked |
| Agent loop design | `[AI OS]` | Loop Acceptance Checklist | pass / revise / blocked |

## Evaluation Order

1. Deterministic checks first when available.
2. Source/evidence checks before narrative polish.
3. LLM judge reviews only against explicit criteria.
4. Revise only from visible judge findings.
5. Human acceptance for high-risk outputs.

## What Overrides Judge

- failed tests;
- failed data reconciliation;
- missing source evidence;
- schema/output contract mismatch;
- secrets or `.env`;
- production/runtime risk;
- explicit governance blocker.

## Output Format

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

This playbook does not add:

- runtime RAGAS setup;
- SWE-Bench benchmark runner;
- vector DB;
- embeddings;
- semantic search;
- web UI;
- autonomous retrieval;
- autonomous eval agents;
- production automation;
- logs;
- runtime artifacts;
- eval result database;
- secrets;
- `.env`.

RAGAS and SWE-Bench remain future/reference patterns only.
