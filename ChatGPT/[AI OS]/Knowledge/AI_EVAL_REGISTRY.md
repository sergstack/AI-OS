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
| `LLM-OUTPUT` | output QA; memo review is risk-triggered | `[LLM]` | prompt output / memo text | deterministic QA + triggered judge | output contract passes; required Judge passes when triggered | explicit QA or Judge findings require a bounded revision | hallucinated sources, hidden blockers, no evidence path, or required Judge omitted | 2026-08-18 | active |
| `ANALYTICS-QA` | analytical memo / QA | `[Analytics]` | data / memo / mart | deterministic QA + narrative judge | data contract, source mart/table, metric, period, grain, QA status | deterministic QA passes and memo claims trace to evidence | fixable missing method, limitation, or traceability field | failed reconciliation, missing contract, unclear grain, or unapproved formula/schema change | 2026-07-06 | active |
| `CODEX-PR` | PR Judge | `[Codex]` / `[Thinking]` | repo change / PR | workflow eval | diff, checks, scope, rollback | goal match, checks observed, rollback and risks visible | bounded scope or documentation fixes needed | secrets, production risk, failing checks, unsafe scope, or missing acceptance | 2026-07-06 | active |
| `AGENT-LOOP` | supervised loop review | `[AI OS]` / `[Thinking]` | loop design | governance eval | loop acceptance checklist | supervised loop, bounded retry, stop conditions, human acceptance | missing owner, retry rule, or stop condition | autonomous retrieval, uncontrolled agents, runtime artifacts, or no validation | 2026-07-06 | active |
| `ACT-ABSTAIN` | act-or-abstain decision | `[AI OS]` / routed owner | supervised workflow | governance eval | deterministic authority/evidence/validation check | expected and actual decision match | bounded decision mismatch or incomplete evidence | hard-boundary violation or no validation path | 2026-08-27 | candidate |
| `GOAL-CLOSURE` | AES Closure Review view | routed owner / `[AI OS]` | candidate output or change | closure eval | final evidence against original goal, acceptance, and owner boundary | checks pass and all closure dimensions satisfied | repairable goal or acceptance gap | missing acceptance/evidence or owner-boundary violation | 2026-08-27 | candidate |
| `FAILURE-REGRESSION` | observed failure lifecycle | routed owner / `[AI OS]` | workflow failure | deterministic-first regression | failure evidence and explicit expected contract | confirmed failure has a bounded regression case where material | evidence or expected contract incomplete | hard boundary or no validation path | 2026-08-27 | candidate |
| `BASELINE-REGRESSION` | baseline vs candidate | routed owner / `[AI OS]` | configuration change | regression matrix | accepted baseline, same required cases, deterministic checks | no hard regression and complete comparison | repairable or inconclusive comparison | unknown baseline, hard regression, or authority expansion | 2026-08-27 | candidate |
| `INTERMEDIATE-ASSERTION` | analytical intermediate state | `[Analytics]` / `[Codex]` | stage/mart/evidence QA | deterministic assertion | accepted analytical contract | all applicable checks pass | contract needs clarification or check not run | failed reconciliation/cardinality or unknown contract | 2026-08-27 | candidate |
| `THINKING-DECISION` | decision review | `[Thinking]` | decision memo / strategy | judge | assumptions, downside, reversibility, revisit trigger | options, risks, confidence, and revisit trigger are explicit | weak assumptions or missing downside can be revised | one-option decision, hidden blocker, or unsupported recommendation | 2026-07-06 | active |

## Required Eval Types

### AI OS Evidence Eval

Checks whether claims are supported, weak, mixed, unsupported, or not found.

### LLM Output Eval

Checks schema, facts vs interpretation, unsupported claims, evidence references,
limitations, and risk-appropriate judge/revise. For memo generation, the active
specialization is deterministic QA first, Judge only when a documented trigger
applies, and revision only from explicit findings. Accepted run evidence remains
in the canonical `[LLM]` project status artifact; this registry continues to
store definitions rather than run results.

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
