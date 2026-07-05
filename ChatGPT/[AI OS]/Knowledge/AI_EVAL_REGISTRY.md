# AI Eval Registry

## Purpose

Single lightweight registry of AI evals across AI-OS projects.

This registry defines eval standards only. It does not store run results, runtime logs, eval databases, or benchmark outputs.

## Eval Status Values

- `draft`
- `candidate`
- `active`
- `blocked`
- `deprecated`

## Verdict Values

- `pass`
- `revise`
- `blocked`

## Core Rule

LLM-as-a-Judge is a reviewer, not truth.

Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business rules.

## Registry

| eval_id | workflow | owner_project | task_type | eval_type | judge/check | pass criteria | revise criteria | blocked criteria | last_reviewed | status |
|---|---|---|---|---|---|---|---|---|---|---|
| `AIOS-EVIDENCE` | AI OS evidence answer | `[AI OS]` | claim / pattern / governance | evidence | confidence and source check | supported evidence or clearly marked weak/mixed/not found | missing confidence, weak sourcing, unclear routing | unsupported claim presented as fact or blocked promotion item recommended | 2026-07-06 | active |
| `LLM-OUTPUT` | draft -> judge -> revise | `[LLM]` | prompt output / memo text | judge | explicit rubric + unsupported claims check | schema followed, facts separated, limitations visible | local unsupported claims or missing limitations | hallucinated sources, hidden blockers, or no evidence path | 2026-07-06 | active |
| `ANALYTICS-QA` | analytical memo / QA | `[Analytics]` | data / memo / mart | deterministic QA + narrative judge | data contract, source mart/table, metric, period, grain, QA status | deterministic QA passes and memo claims trace to evidence | fixable missing method, limitation, or traceability field | failed reconciliation, missing contract, unclear grain, or unapproved formula/schema change | 2026-07-06 | active |
| `CODEX-PR` | PR Judge | `[Codex]` / `[Thinking]` | repo change / PR | workflow eval | diff, checks, scope, rollback | goal match, checks observed, rollback and risks visible | bounded scope or documentation fixes needed | secrets, production risk, failing checks, unsafe scope, or missing acceptance | 2026-07-06 | active |
| `AGENT-LOOP` | supervised loop review | `[AI OS]` / `[Thinking]` | loop design | governance eval | loop acceptance checklist | supervised loop, bounded retry, stop conditions, human acceptance | missing owner, retry rule, or stop condition | autonomous retrieval, uncontrolled agents, runtime artifacts, or no validation | 2026-07-06 | active |
| `THINKING-DECISION` | decision review | `[Thinking]` | decision memo / strategy | judge | assumptions, downside, reversibility, revisit trigger | options, risks, confidence, and revisit trigger are explicit | weak assumptions or missing downside can be revised | one-option decision, hidden blocker, or unsupported recommendation | 2026-07-06 | active |

## Required Eval Types

### AI OS Evidence Eval

Checks whether claims are supported, weak, mixed, unsupported, or not found.

### LLM Output Eval

Checks schema, facts vs interpretation, unsupported claims, evidence references, limitations, judge/revise.

### Analytics Eval

Checks deterministic QA, source mart/table, metric, period, grain, calculation method, QA status, confidence, and limitations.

### Codex PR Eval

Checks goal match, scope, tests/checks, forbidden changes, rollback, risks, and acceptance status.

### Agent Loop Eval

Checks supervised loop boundary, stop conditions, bounded retry/rerun, validation path, and human acceptance.

### Thinking Decision Eval

Checks assumptions, options, downside, reversibility, confidence, and revisit trigger.

## Reference-Only Patterns

RAGAS and SWE-Bench may be referenced as future or external patterns for inspiration.

Do not add runtime RAGAS setup, SWE-Bench benchmark runner, vector DB, embeddings, semantic search, web UI, autonomous retrieval, autonomous eval agents, production automation, logs, runtime artifacts, eval result database, secrets, or `.env`.
