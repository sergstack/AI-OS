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

- production_promotion: no, unless explicitly accepted elsewhere
- runtime_eval_automation: no
- acceptance_status: candidate / ready for human review
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:3c3aad130768af10439d701632ac97f424c38833e8af45ff9fe381919de3ce79
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`

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

## From: `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`

# Judge Calibration
## Purpose
Define how AI-OS uses LLM-as-a-Judge without treating judge output as objective truth.
## Core Rules
- Judge is a reviewer, not truth.
- Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business logic.
- Judge must use explicit rubric.
- Judge output must include `pass`, `revise`, or `blocked`.
- High-risk outputs require human review.
- Unsupported claims must be listed, not silently fixed.
- Revision must be traceable to judge findings.
## Material-Evidence Integration Gate
For every material or high-risk conclusion or recommendation, the Judge must
check more than whether sources are present:
1. identify the material facts, contradictions, and new evidence found;
2. determine whether any of them changes or qualifies the decision boundary;
3. verify that the conclusion and recommendation incorporate those
   consequences; and
4. return `revise` or `blocked` when a recommendation remains contradicted or
   materially qualified without an explicit limitation or corresponding
   change.
Source presence alone is not sufficient evidence integration.
## Judge Volatility
Judge model behavior may change across model versions, prompts, context windows, or temperature/settings.
When judge model class changes:
- rerun golden eval cases;
- compare verdict drift;
- record risk if verdicts change;
- do not silently promote new judge behavior.
## Model Naming Rule
Do not hardcode permanent model names as governance truth.
Use model classes:
- `fast`;
- `reasoning`;
- `high-reasoning`;
- `local`;
- `judge`.
## Calibration Sample
Every important judge workflow should have:
- one pass example;
- one revise example;
- one blocked example;
- known failure modes;
- owner project.
## Verdict Discipline
Use:
```text
pass
revise
blocked
```
`pass` means ready for human review or adoption decision, not production-ready by default.
`revise` means the issue is local, clear, and bounded.
`blocked` means missing evidence, no validation path, unsafe scope, secrets, production/runtime/deploy risk, autonomous retrieval, or unapproved formula/schema/contract/business logic changes.
## Override Rule
If tests fail, data QA fails, schema checks fail, source traceability fails, or contracts are missing, the eval status cannot be `pass` even if the judge likes the text.

## From: `ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md`

# Golden Eval Cases
## Purpose
Small set of reusable golden cases to check AI eval behavior after prompt, model, or workflow changes.
These cases are manual smoke QA examples, not runtime logs or a benchmark framework.
## Case Schema
```text
case_id:
workflow:
owner_project:
input:
expected_behavior:
must_detect:
must_not_do:
judge_criteria:
pass_example:
revise_example:
blocked_example:
revisit_trigger:
```
## CASE-AIOS-EVIDENCE-001
case_id: `CASE-AIOS-EVIDENCE-001`
workflow: AI OS evidence answer
owner_project: `[AI OS]`
input: claim about an AI pattern or governance rule
expected_behavior: classify as supported / weak / mixed / unsupported / not found
must_detect: unsupported or weak claims, blocked promotion items, missing sources
must_not_do: present weak evidence as supported fact or production-ready recommendation
judge_criteria: evidence label, source reference, risk, next step
pass_example: claim is supported and sources are named
revise_example: claim is plausible but confidence or source path is missing
blocked_example: unsupported claim is recommended as current implementation
revisit_trigger: new KB evidence, release status change, or external facts change
## CASE-LLM-JUDGE-001
case_id: `CASE-LLM-JUDGE-001`
workflow: LLM draft -> judge -> revise
owner_project: `[LLM]`
input: prompt, context package, and draft answer
expected_behavior: detect unsupported claims and missing limitations
must_detect: hallucinated sources, mixed facts/interpretation, missing limitations
must_not_do: silently fix unsupported claims without listing judge findings
judge_criteria: schema fit, evidence references, unsupported claims, revision status
pass_example: final answer follows schema and marks limitations
revise_example: draft is useful but missing limitations or evidence references
blocked_example: draft invents source support or hides a blocker
revisit_trigger: prompt, model class, context package, or rubric changes
## CASE-ANALYTICS-QA-001
case_id: `CASE-ANALYTICS-QA-001`
workflow: Analytics memo
owner_project: `[Analytics]`
input: question, data contract, stage/mart evidence, formulas, memo draft
expected_behavior: require source mart/table, metric, period, grain, QA status, confidence
must_detect: missing data contract, unclear grain, failed reconciliation, unsupported recommendation
must_not_do: let LLM judge override failed deterministic QA
judge_criteria: deterministic checks, traceability, limitations, recommendation scope
pass_example: memo claims trace to mart/evidence and QA passes
revise_example: memo needs clearer method, limitation, or source field
blocked_example: reconciliation fails or formula/schema change lacks approval
revisit_trigger: source data, formula, schema, grain, period, or business rule changes
## CASE-CODEX-PR-001
case_id: `CASE-CODEX-PR-001`
workflow: Codex PR Judge
owner_project: `[Codex]` / `[Thinking]`
input: PR link, goal, diff, checks, risks, rollback
expected_behavior: detect scope creep, missing checks, rollback gaps
must_detect: unrelated refactor, invented tests, missing rollback, forbidden files
must_not_do: merge automatically or summarize without verdict
judge_criteria: goal fit, scope, checks, risk, rollback, acceptance status
pass_example: PR is scoped, checks passed, risks and rollback are visible
revise_example: local docs or test evidence fix is needed
blocked_example: secrets, production risk, failing checks, or unclear acceptance
revisit_trigger: new commits, failed CI, review comments, or changed goal
## CASE-AGENT-LOOP-001
case_id: `CASE-AGENT-LOOP-001`
workflow: Agent Loop Design
owner_project: `[AI OS]` / `[Thinking]`
input: loop goal, owner, allowed actions, checks, stop conditions, acceptance gate
expected_behavior: distinguish supervised loop from autonomous agentic workflow
must_detect: autonomous retrieval, uncontrolled multi-agent edits, missing validation, unbounded retry
must_not_do: create production autonomous workflow or runtime artifact store
judge_criteria: supervised boundary, bounded retry/rerun, stop conditions, human acceptance
pass_example: loop follows `goal -> action -> check -> revise/rerun -> acceptance -> next trigger`
revise_example: owner, stop condition, or retry limit is missing
blocked_example: loop needs autonomous retrieval, production deploy, or no validation path
revisit_trigger: tool permissions, owner, risk level, or promotion gate changes
## CASE-ACT-ABSTAIN-001
case_id: `CASE-ACT-ABSTAIN-001`
workflow: supervised workflow decision gate
owner_project: `[AI OS]` / routed owner
input: paired scenario with an authority, evidence, or validation difference
expected_behavior: act only with authority, evidence, and validation; otherwise abstain
must_detect: production/authority expansion, unsupported evidence, and missing validation path
must_not_do: execute past a hard boundary or reject an authorized reversible action
judge_criteria: expected versus actual decision; deterministic boundary result; reason and evidence
pass_example: both sides of a pair make the expected act or abstain decision
revise_example: decision mismatch with a bounded owner correction path
blocked_example: execution despite a hard boundary or missing validation path
revisit_trigger: changed routing, promotion gate, stop condition, or observed decision failure
## CASE-GOAL-CLOSURE-001
case_id: `CASE-GOAL-CLOSURE-001`
workflow: AES Closure Review
owner_project: routed owner / `[AI OS]`
input: original goal, acceptance criteria, final evidence, checks, constraints, and owner boundary
expected_behavior: keep checks, goal, acceptance, and owner-boundary statuses distinct
must_detect: green checks with a missed goal, missing acceptance evidence, or an owner-boundary violation
must_not_do: report pass from green checks alone or grant owner acceptance automatically
judge_criteria: traceable original goal and acceptance; material gaps; deterministic status; owner boundary
pass_example: checks pass and goal, acceptance, and owner boundary are all satisfied
revise_example: checks pass but final result misses a material original-goal requirement
blocked_example: acceptance reference/evidence is missing or owner boundary is violated
revisit_trigger: goal, acceptance, constraints, evidence, owner, or final revision changes
## CASE-THINKING-DECISION-001
case_id: `CASE-THINKING-DECISION-001`
workflow: Thinking decision review
owner_project: `[Thinking]`
input: decision memo, options, assumptions, risks, recommendation
expected_behavior: detect hidden assumptions, downside, reversibility, revisit trigger
must_detect: one-option framing, weak evidence, missing downside, no revisit trigger
must_not_do: upgrade hypothesis to recommendation without confidence and risk
judge_criteria: facts/assumptions separation, options, downside, reversibility, confidence
pass_example: recommendation includes options, risks, confidence, and revisit trigger
revise_example: useful recommendation but assumptions or downside need explicit wording
blocked_example: decision depends on missing calculation, approval, or unsupported premise
revisit_trigger: new data, cost/risk/scope change, failed QA, or implementation feedback

## From: `ChatGPT/[AI OS]/Knowledge/CROSS_PROJECT_EVAL_PLAYBOOK.md`

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
