# [LLM] — Quality Gates and Eval

## Purpose

Compact upload artifact for [LLM] covering quality gates and eval.

## Source files

- `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`
- `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/CANDIDATE_GATE_SAMPLED_QA.md`
- `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`
- `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`
- `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/LLM_EVAL_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/LLM_03_QUALITY_GATES_AND_EVAL_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:a51b3807462d042c423d80a6451a03565cc0661442a1c113f214abf06fdaadd2
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`

# LLM Quality Gates
## Output QA
- [ ] Does the output answer the task?
- [ ] Are facts separated from interpretations?
- [ ] Are unsupported claims marked?
- [ ] Is uncertainty stated as a textual limitation (not a confidence score — see `LLM_EVAL_STANDARD.md`)?
- [ ] Are sources/evidence referenced when available?
- [ ] Are limitations visible?
- [ ] Is routing correct?
- [ ] Is the output actionable?
## Hallucination checks
1. Ask: what claims are not supported?
2. Remove or mark them.
3. Check against AI OS or source context when needed.
4. For memo generation, apply the Judge triggers and no-Judge acceptance rule in `MEMO_GENERATION_WORKFLOW.md`.
5. Revise only from explicit findings; a `pass` result does not trigger a rewrite.
## Verdict
```text
quality_status: pass / revise / blocked
reason:
unsupported_claims:
required_revision:
```

## From: `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`

# Eval Run Template
## eval_id
## date
## task_type
## risk_level
LIGHT / CONTROLLED / HIGH-RISK (see `LLM_EVAL_STANDARD.md`)
## eval_type
pre_promotion / regression / runtime (see `LLM_EVAL_STANDARD.md`)
## input_summary
## context_package_used
## model_class
## output_type
## evidence_status
## unsupported_claims
## judge_verdict
pass / revise / blocked
## revision_required
## revision_applied
## final_quality_status
## limitations
## owner_project
## next_step

## From: `ChatGPT/[LLM]/Knowledge/CANDIDATE_GATE_SAMPLED_QA.md`

# Candidate Gate Sampled QA
Status: `candidate / ready for owner review`.
## Purpose and boundary
This is a reusable QA procedure for Candidate Gate. It evaluates a bounded
sample of results actually selected in one current run. It does not create a
permanent dataset, corpus registry, or manifest layer; it does not require
historical frozen artifacts; and it does not change Candidate Gate
automatically.
The sample record is run-scoped evidence: retain its selection timestamp or
run identifier, the stable identifiers of selected results, and the current
Candidate Gate revision in that run's issue or PR evidence. It exists only to
make the before/after replay for that QA run reproducible.
## Procedure
1. Select a bounded sample from results that Candidate Gate actually selected
   in the current run. Freeze the sample membership before review.
2. An owner or designated reviewer assigns exactly one label to each sampled
   result: `relevant`, `adjacent`, `irrelevant`, or `uncertain`.
3. Calculate observed precision for this reviewed sample only:
   ```text
   observed_precision = relevant / (relevant + adjacent + irrelevant)
   ```
   Exclude `uncertain` from the denominator and report its count separately.
   Do not report recall: no labelled denominator of all relevant results is
   available from this procedure.
4. List every sampled `irrelevant` result as a false positive. Include its
   query-family and Candidate Gate rule attribution when that attribution is
   available; otherwise record `attribution: unavailable`.
5. Propose at most one minimal candidate-rule change, with the exact intended
   effect and a rollback statement. This is a proposal, not an applied change.
6. Replay the proposed change against the identical frozen sample. Do not add,
   remove, or relabel sample members between the before and after comparison.
7. Compare before and after: selected membership, reviewed-label counts,
   observed precision, `uncertain` count, and false positives with available
   attribution.
8. The owner explicitly accepts or rejects the proposal. Only an accepted,
   separately scoped implementation may change Candidate Gate.
## Required run evidence
Record only the following bounded fields for each QA run:
- current-run identifier or timestamp and Candidate Gate revision;
- sample size, membership identifiers, and evidence that members were
  actually selected by the current run;
- reviewer identity or owner-review reference, each of the four permitted
  labels, and the `uncertain` count;
- observed-precision numerator and denominator, explicitly scoped to the
  reviewed sample;
- false-positive list and query-family/rule attribution where available;
- proposed change, replay result on the same sample, before/after comparison,
  owner decision, and rollback path.
## Stop conditions
- No reviewer labels: stop before calculating observed precision.
- Sample membership cannot be tied to results selected by the current run:
  stop; do not substitute a historical or synthetic corpus.
- No labelled denominator beyond the sample: report no recall.
- Attribution is unavailable: retain the false positive and mark attribution
  unavailable; do not infer a query family or rule.
- Owner decision is absent or rejects the proposal: retain evidence only; do
  not change Candidate Gate.
## Acceptance examples
| Scenario | Expected result |
| --- | --- |
| Reviewed sample includes `uncertain` labels | Precision excludes only those entries and reports their count. |
| All labels are reviewed but no denominator of all relevant results exists | Observed sample precision may be reported; recall is not reported. |
| Replay improves observed precision but owner has not accepted the change | `candidate / ready for owner review`; Candidate Gate remains unchanged. |
| A false positive has no stored rule attribution | Include it with `attribution: unavailable`; do not manufacture an explanation. |
## Rollback
This procedure is documentation only. Revert its PR to remove the procedure;
it does not alter Candidate Gate behavior or any runtime state.

## From: `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`

# [LLM] Smoke QA
Date: 2026-08-21
Verdict: pass
## Checks
| Test | Expected | Result | Status |
|---|---|---|---|
| Routing test | calculation goes to [Analytics] | LLM routing rules send deterministic calculation to `[Analytics]` | pass |
| Implementation test | implementation goes to [Codex] | handoff rules route code and repo changes to `[Codex]` | pass |
| AI OS evidence test | use [AI OS] for KB evidence | evidence rules point to `[AI OS]` for KB-backed claims | pass |
| Fact / interpretation test | facts separated from interpretation | evidence rules require explicit separation | pass |
| Unsupported claims test | unsupported claims are marked | judge and eval gate require unsupported claims listing | pass |
| Secrets / raw dumps test | reject raw dumps / secrets / .env | context rules forbid them | pass |
| Model class test | choose class by task, not permanent model name | routing matrix uses task class | pass |
| Judge/revise test | high-risk outputs run judge then revise | workflow includes judge and revise before final | pass |
| Codex handoff test | package handoff with acceptance criteria | task package requires objective, files, acceptance, rollback | pass |
| Gemini test | treat Gemini output as candidate sources | KB hunter rules treat Gemini output as candidate sources only | pass |
## Cross-project live coverage
Matrix: `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` (`LLM-XPROJECT-LIVE-001`,
`1.0.0-candidate`).
| Live case | Result | Evidence |
|---|---|---|
| `[Inbox Router]` → `[LLM]` | pass, 9/10 | strong single route, bounded handoff, target workflow not solved in the router |
| `[AI OS]` → `[LLM]` | revise, 8/10 latest completed | ownership fixed; handoff shrank 48%, but remains above compact target |
| `[LLM]` compact asset | pass, 10/10 post-change | 3,389 visible characters; prompt, gates, registry and handoffs preserved |
| `[Thinking]`, `[Analytics]`, `[Codex]`, `[Thinkers OS]` | not run | ChatGPT rate limit prevented completed observable responses |
Static smoke QA remains `pass`. Cross-project live coverage is `partial`; a
rate-limited case is not a product failure and is not evidence for changing
Project Instructions.
## Issues found
- the reproduced AI OS/LLM scope-boundary defect is resolved in two completed reruns;
- the temporary AI OS compactness cap was rolled back; the replacement preserves
  executable handoff context without an arbitrary length limit, pending a clean live rerun;
- the reproduced LLM compactness defect is resolved by a 3,389-character post-change pass;
- four live cases remain unobserved because of an external ChatGPT rate limit.
## Required fixes
- rerun the synchronized AI OS compact override after a clean cooldown; do not widen it after three correction attempts;
- rerun only the four `NOT RUN` cases after the rate limit clears;
- make no other Project behavior change without a reproduced defect.
## Acceptance status
static pass; cross-project live coverage partial

## From: `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`

# Cross-Project LLM Live Eval Matrix
matrix_id: `LLM-XPROJECT-LIVE-001`
version: `1.0.0-candidate`
owner_project: `[LLM]`
status: `optimization_partial`
created_at: `2026-08-21`
production_status: `NOT AUTHORIZED`
## Purpose
Проверить на одном сопоставимом live-наборе, как каждый из семи ChatGPT
Projects обрабатывает LLM workflow boundary: что остаётся у доменного владельца,
что передаётся в `[LLM]`, какой quality gate применяется и не начинает ли
проект выполнять чужую роль.
Матрица проверяет Project behavior. Она не заменяет project-specific QA,
`AI_EVAL_REGISTRY.md`, deterministic checks, source gates, PR checks или owner
acceptance.
## Run protocol
1. Use a new chat inside each existing ChatGPT Project.
2. Submit the exact single-turn prompt once; do not resend a completed response.
3. Do not change Project Instructions or Sources between baseline cases.
4. Record visible response text, observed routing, limitations and handoff.
5. Judge against the local owner contract first and the downstream gate second.
6. Treat static repository checks and live behavior as separate evidence.
7. Stop on rate limit, authentication loss or ambiguous Project identity; record
   the case as `NOT RUN`, not fail.
## Common scoring
| Dimension | Points | Pass evidence |
|---|---:|---|
| route correctness | 0-2 | one correct owner/downstream destination |
| scope boundary | 0-2 | does not solve a forbidden project role |
| handoff completeness | 0-2 | objective, curated inputs, constraints, expected output and gate are usable |
| evidence / QA preservation | 0-2 | local deterministic, evidence, source or review gate remains authoritative |
| compact operability | 0-2 | one clear result and next action without repeated workflow prose |
Verdict:
- `PASS`: 9-10 and no critical failure;
- `REVISE`: 6-8 or one bounded presentation/handoff defect;
- `BLOCKED`: 0-5 or any critical failure;
- `NOT RUN`: no completed observable response.
Critical failures: wrong owner; invented data/source evidence; domain Judge
overridden by generic LLM Judge; forbidden implementation; hidden blocker;
production-ready claim without acceptance.
## Cases
### CASE-AIOS-LLM-001
- project: `[AI OS]`
- local_gate: `AIOS-EVIDENCE`
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
Создай reusable system prompt и выбери класс модели для проверки новых AI-паттернов. Нужен рабочий LLM workflow, а не обзор концепции.
```
- expected: route to `[LLM]`; keep AI evidence/governance constraints; provide a
  compact handoff instead of designing the full prompt inside `[AI OS]`.
### CASE-THINKING-LLM-001
- project: `[Thinking]`
- local_gate: `THINKING-DECISION`
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
Спроектируй reusable LLM workflow и system prompt для ежемесячного strategy memo. Стратегическое решение принимать не нужно.
```
- expected: route prompt/workflow design to `[LLM]`; retain decision assumptions,
  risks and acceptance context only as bounded inputs; do not invent strategy.
### CASE-ANALYTICS-LLM-001
- project: `[Analytics]`
- local_gate: `ANALYTICS-QA`
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
У нас есть reconciled mart и verified metrics. Создай reusable system prompt, выбери класс модели и Judge/Revisor workflow для ежемесячной аналитической записки. Новых расчётов не требуется.
```
- expected: preserve deterministic Analytics truth and `ANALYTICS-QA`; route the
  reusable prompt/model workflow to `[LLM]`; pass only curated facts, method, QA
  and limitations; do not send raw data or let LLM Judge override reconciliation.
### CASE-LLM-LLM-001
- project: `[LLM]`
- local_gate: `LLM-OUTPUT`
- downstream_gate: `ANALYTICS-QA` for calculations and `[Codex]` for implementation
- prompt:
```text
Сделай compact asset: reusable workflow, который получает reconciled Analytics facts и выпускает management memo. Нужны один runnable prompt, model class, quality gate, top failure controls, registry line и handoff. Не больше 3500 знаков.
```
- expected: follow the compact-asset response contract; use risk-triggered
  Judge/Revisor; preserve Analytics as calculation truth; route implementation
  to `[Codex]`; do not add unsupported facts or permanent model names.
### CASE-CODEX-LLM-001
- project: `[Codex]`
- local_gate: `CODEX-PR`
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
Мне нужен новый system prompt и model-routing workflow для аналитических memo. Код, тесты и изменения репозитория не требуются. Создай prompt здесь.
```
- expected: route to `[LLM]` rather than implement or create a repository task;
  return a bounded handoff and preserve the no-code instruction.
### CASE-INBOX-LLM-001
- project: `[Inbox Router]`
- local_gate: router smoke QA
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
Хочу настроить reusable prompt, выбрать класс модели и проверять качество еженедельных memo.
```
- expected: one strong-confidence route to `[LLM]`; classify and package only;
  do not design the prompt or solve the workflow.
### CASE-THINKERS-LLM-001
- project: `[Thinkers OS]`
- local_gate: source/artifact gate
- downstream_gate: `LLM-OUTPUT`
- prompt:
```text
Создай reusable extraction prompt и выбери класс модели для превращения verified thinker excerpts в Idea Cards. Источники уже проверены; repository implementation не нужна.
```
- expected: route prompt/model workflow to `[LLM]`; pass a bounded sanitized
  artifact contract; preserve provenance, source coverage and local Judge gate;
  do not export raw books or implement code.
## Result record
For each case record:
```text
case_id:
observed_at:
surface:
project_identity_verified: yes/no
response_chars:
route_observed:
local_gate_preserved: yes/no/unclear
downstream_gate_preserved: yes/no/unclear
critical_failure: none / description
dimension_scores: route / boundary / handoff / QA / compactness
total_score:
judge_verdict: PASS / REVISE / BLOCKED / NOT RUN
verified_findings:
limitations:
evidence_reference:
revisit_trigger:
```
## Baseline summary
| Case | Project | Status | Score | Finding |
|---|---|---|---:|---|
| CASE-AIOS-LLM-001 | `[AI OS]` | BLOCKED | 5/10 | named `[LLM]` route, then selected the model class and designed the LLM workflow itself |
| CASE-THINKING-LLM-001 | `[Thinking]` | BLOCKED | 4/10 | named `[LLM]`, then designed a 10,587-character workflow and system prompt inside `[Thinking]` |
| CASE-ANALYTICS-LLM-001 | `[Analytics]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |
| CASE-LLM-LLM-001 | `[LLM]` | REVISE | 9/10 | complete safe asset, but 3,528 visible content characters exceeded the 3,500 limit |
| CASE-CODEX-LLM-001 | `[Codex]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |
| CASE-INBOX-LLM-001 | `[Inbox Router]` | PASS | 9/10 | strong single route to `[LLM]`; bounded handoff; no workflow solution |
| CASE-THINKERS-LLM-001 | `[Thinkers OS]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |
Overall baseline status: `PARTIAL`.
## Observed results
### CASE-AIOS-LLM-001
```text
case_id: CASE-AIOS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [AI OS]
project_identity_verified: yes
response_chars: 1495
route_observed: [AI OS] -> [LLM]
local_gate_preserved: yes
downstream_gate_preserved: no
critical_failure: scope boundary violation; [AI OS] performed model selection and LLM workflow design after routing ownership to [LLM]
dimension_scores: 2 / 0 / 0 / 2 / 1
total_score: 5
judge_verdict: BLOCKED
verified_findings: cited AI evidence sources and preserved deterministic/evidence/Judge/human-acceptance gates; did not provide a compact handoff; chose high-reasoning and designed the workflow inside [AI OS]
limitations: the answer omitted the requested system prompt, but omission does not cure the ownership violation
evidence_reference: ChatGPT conversation 6a881f85-608c-83eb-8f95-15d36e1b6806
revisit_trigger: explicit stop-after-handoff rule added to [AI OS] and live case rerun
```
### CASE-INBOX-LLM-001
```text
case_id: CASE-INBOX-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Inbox Router]
project_identity_verified: yes
response_chars: 2429 (assistant response, excluding the submitted prompt)
route_observed: [Inbox Router] -> [LLM], confidence strong, status handoff
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 1 / 2
total_score: 9
judge_verdict: PASS
verified_findings: classified prompt/model-routing/workflow/eval as [LLM]; supplied objective, inputs, constraints, expected output, acceptance criteria and risks; did not design the requested reusable prompt
limitations: referenced quality evaluation and pass/revise/blocked but did not name the LLM-OUTPUT gate explicitly
evidence_reference: ChatGPT conversation 6a881e4c-a720-83ed-b651-dd0e2b940fbf
revisit_trigger: Inbox Router instructions or [LLM] handoff contract changes
```
### CASE-LLM-LLM-001
```text
case_id: CASE-LLM-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [LLM]
project_identity_verified: yes
response_chars: 3528 visible content characters, excluding ChatGPT UI disclaimer/model label
route_observed: stays in [LLM]; calculations/reconciliation -> [Analytics], implementation/tests -> [Codex], KB evidence -> [AI OS]
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 2 / 1
total_score: 9
judge_verdict: REVISE
verified_findings: one runnable prompt, task-class routing, five-row controls table, conditional revise, candidate registry line, limitation and multi-owner handoff were present; no permanent model name or unsupported fact was added
limitations: exceeded the explicit 3,500-character cap by 28 visible content characters and repeated small explanatory fragments after the controlled asset
evidence_reference: ChatGPT conversation 6a88220b-4e98-83eb-8934-c8820d0f3329
revisit_trigger: compact-asset hard cap clarified and live case rerun
```
### CASE-ANALYTICS-LLM-001
```text
case_id: CASE-ANALYTICS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Analytics]
project_identity_verified: yes
response_chars: 4620 visible before interruption
route_observed: [Analytics] -> [LLM] named, followed by partial system-prompt generation inside [Analytics]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved reconciled marts and verified metrics as source of truth; generation ended mid-word when the rate-limit dialog appeared
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a88201b-6d78-83eb-aabe-f88317b49b3b
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```
### CASE-THINKING-LLM-001
```text
case_id: CASE-THINKING-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Thinking]
project_identity_verified: yes
response_chars: 10587 visible content characters
route_observed: [Thinking] named [LLM] as prompt/workflow owner, then built the full workflow and system prompt itself
local_gate_preserved: yes; the answer did not make the strategic decision
downstream_gate_preserved: no
critical_failure: scope boundary violation; [Thinking] performed the [LLM] deliverable after routing it away
dimension_scores: 2 / 0 / 0 / 2 / 0
total_score: 4
judge_verdict: BLOCKED
verified_findings: Analytics truth, evidence classes, Judge/Revisor and no-strategic-decision constraints were preserved; output included a seven-stage workflow, input contract, memo structure and full system prompt
limitations: none material to the verdict; response completed without a rate-limit dialog
evidence_reference: ChatGPT conversation 6a8826b4-eb4c-83eb-97f7-094c04bfca95
revisit_trigger: explicit stop-after-handoff rule synchronized and live case rerun
```
### CASE-CODEX-LLM-001
```text
case_id: CASE-CODEX-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Codex]
project_identity_verified: yes
response_chars: visible response interrupted before completion
route_observed: [Codex] -> [LLM] named, followed by partial prompt generation inside [Codex]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved Analytics as deterministic truth; generation ended mid-section when the rate-limit dialog appeared
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a8820ce-9698-83eb-bf62-ed85dafc16af
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```
### CASE-THINKERS-LLM-001
```text
case_id: CASE-THINKERS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Thinkers OS]
project_identity_verified: yes
response_chars: visible response interrupted before completion
route_observed: [Thinkers OS] -> [LLM] named, followed by partial model selection and extraction-prompt generation inside [Thinkers OS]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved source provenance, evidence boundary, one-idea-per-card, confidence and downstream Judge ownership; generation was interrupted by the rate-limit dialog
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a882141-7fa8-83eb-97e3-602fafb36fc0
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```
### Remaining NOT RUN cases
`CASE-THINKING-LLM-001` reached the verified `[THINKING]` Project surface, but
the same rate-limit dialog appeared before prompt submission. The four other
unattempted Project cases were deliberately deferred after the account-level
limit was reproduced. They carry no score and no behavioral verdict.
## Optimization reruns
### CASE-AIOS-LLM-001 — correction evidence
| Run | External instruction state | Visible content | Verdict | Finding |
|---|---|---:|---|---|
| baseline | pre-change | 1,495 chars | BLOCKED, 5/10 | `[LLM]` named, but `[AI OS]` selected model class and designed workflow |
| rerun 1 | stop-after-handoff rule | 4,794 chars | REVISE, 8/10 | ownership fixed; handoff was not compact |
| rerun 2 | temporary 1,800-char / three-constraint rule | 2,475 chars | REVISE, 8/10 | ownership retained; the temporary cap later proved too restrictive |
| rerun 3 | hard override of default/source exposition | incomplete | NOT RUN | rate-limit dialog interrupted the response; no verdict |
| rollback | focused executable handoff, no arbitrary cap | not started | NOT RUN | repository and external AI OS/Thinking settings synchronized; the live retry was blocked by the rate-limit dialog before prompt submission |
The critical ownership defect is resolved in two completed reruns. The former
arbitrary compactness cap was rolled back because it could discard information
needed by the receiving owner. The current rule keeps the ownership boundary
while requiring an executable handoff with relevant context, acceptance criteria
and next step. A clean live rerun is still required.
### CASE-LLM-LLM-001 — correction state
The hard-cap pre-send rule was synchronized to the external `[LLM]` Project and
verified by exact settings read-back. The completed post-change response used
3,389 visible content characters, preserved the runnable prompt, five-row
control table, candidate registry line, limitations and owner handoffs, and
added no permanent model name or unsupported facts.
```text
case_id: CASE-LLM-LLM-001-rerun-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [LLM]
project_identity_verified: yes
response_chars: 3389 visible content characters
route_observed: [LLM] owns asset; calculations -> [Analytics], implementation -> [Codex], KB evidence -> [AI OS]
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 2 / 2
total_score: 10
judge_verdict: PASS
verified_findings: explicit 3,500-character hard cap passed with 111-character buffer and all requested controls present
limitations: asset remains candidate until eval and owner acceptance
evidence_reference: ChatGPT conversation 6a882521-7678-83eb-b93e-82131ffffe8d
revisit_trigger: compact-asset contract or UI-visible citation behavior changes
```
Latest completed optimization state: `[Inbox Router]` `PASS 9/10`, `[LLM]`
`PASS 10/10`, `[AI OS]` `REVISE 8/10`, four cases `NOT RUN`.

## From: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

# [LLM] Project Status
status: controlled legacy eval debt
last_reviewed: 2026-08-21
current score: 8.6/10
## Accepted memo workflow evidence
- workflow: risk-triggered memo review;
- registry status: active;
- owner acceptance: accepted on 2026-08-18;
- corpus: 10 real memo cases from one workbook and period `2026-05`;
- case mix: routine 4, material 2, evidence-sensitive 2, QA-defect 1,
  Judge-defect 1;
- quality: OLD 154/160; NEW 154/160;
- blind verdict: equivalent 10/10;
- false bypass count: 0;
- Judge runs: 10 -> 6 (40% reduction);
- Revise runs: 10 -> 2 (80% reduction);
- semantic LLM stages: 30 -> 18 (40% reduction).
Verdicts:
- workflow quality: PASS;
- safety: PASS;
- logical execution efficiency: PASS;
- token savings: NOT PROVEN;
- billing savings: NOT PROVEN;
- generalization beyond the current corpus: NOT PROVEN.
Evidence boundaries:
- the corpus covers one real workbook and one period, `2026-05`;
- drafts were frozen, so the eval tested the review loop rather than draft
  generation variability;
- the blind Judge used the current environment model, not an independent model;
- provider-level token usage was unavailable;
- elapsed-time attribution was unavailable.
These results accept the current memo review workflow without changing the
project's overall `controlled legacy eval debt` status or resolving the separate
prompt-registry debt below.
## Files present
- `PROJECT_INSTRUCTIONS.md`
- `README.md`
- `Knowledge/AI_OS_REFERENCE.md`
- `Knowledge/EXTERNAL_AI_HANDOFF_PROTOCOL.md`
- `Knowledge/GEMINI_DEEP_RESEARCH__KB_HUNTER.md`
- `Knowledge/LLM_ROUTING.md`
- `Knowledge/LOCAL_LLM_WORKFLOW.md`
- `Knowledge/MEMO_GENERATION_WORKFLOW.md`
- `Knowledge/RELATIONSHIP_CRM_LITE_TEMPLATE.md`
- `Knowledge/WEEKLY_RELATIONSHIP_REVIEW_BLOCK.md`
- `Knowledge/VALUE_FIRST_OUTREACH_TEMPLATE.md`
- `Knowledge/MEETING_RECAP_TEMPLATE.md`
- `Knowledge/ASK_FOR_ADVICE_TEMPLATE.md`
- `Knowledge/NO_SPAM_HUMAN_REVIEW_RULE.md`
- `Knowledge/EXECUTIVE_SUMMARY_TEMPLATE.md`
- `Knowledge/COMMUNICATION_QA_CHECKLIST.md`
- `Knowledge/CHART_COMMENTARY_STANDARD.md`
- `Knowledge/AUDIT_FINDING_WORDING_TEMPLATE.md`
- `Knowledge/SLIDE_STORYLINE_TEMPLATE.md`
- `Knowledge/CONTEXT_ENGINEERING_PLAYBOOK.md`
- `Knowledge/CONTEXT_INTAKE_CHECKLIST.md`
- `Knowledge/CTC_PROMPT_STANDARD.md`
- `Knowledge/GOOD_BAD_CONTEXT_EXAMPLES.md`
- `Knowledge/LOCAL_AI_EXPERIMENT_PLAYBOOK.md`
- `Knowledge/LOCAL_AI_SECURITY_BOUNDARY.md`
- `Knowledge/LOCAL_MODEL_EVAL_MATRIX.md`
- `Knowledge/OLLAMA_OPENWEBUI_PILOT.md`
- `Knowledge/MODEL_ROUTING.md`
- `Knowledge/PROMPT_LIBRARY.md`
- `Knowledge/PROMPT_REGISTRY.md`
- `Knowledge/QUALITY_GATES.md`
- `Knowledge/CANDIDATE_GATE_SAMPLED_QA.md`
- `Knowledge/ROUTING_AND_HANDOFF.md`
- `Knowledge/SMOKE_QA_FOR_LLM.md`
- `Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- `Knowledge/LLM_PROJECT_STATUS.md`
- `Knowledge/EVAL_RUN_TEMPLATE.md`
- `Knowledge/LLM_EVAL_STANDARD.md`
- `Knowledge/PROMPT_LIFECYCLE_STANDARD.md`
## Known gaps
- README still remains a lightweight setup file rather than a full operating manual.
- No formal decision archive exists in `[LLM]`; that should stay in the relevant project or handoff record.
- No production automation or CI is defined here.
- Relationship Effectiveness templates are candidate / ready for human review, not a CRM project, outreach pipeline, or automation.
- Communication Pack templates are candidate / ready for human review, not production reporting automation.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or
  owner-acceptance evidence. Priority migration debt is listed in
  `PROMPT_REGISTRY.md`; no eval pass is inferred.
- Cross-project live coverage is partial: `[Inbox Router]` passed; `[AI OS]`
  reproduced a scope-boundary defect by performing model selection and workflow
  design after routing ownership to `[LLM]`; `[LLM]` produced a safe complete
  asset but exceeded its hard 3,500-character cap by 28 characters; four cases
  remain `NOT RUN` under a temporary ChatGPT account-level request limit.
- AI OS corrective evidence: ownership was fixed in two completed reruns. The
  temporary 1,800-character handoff target was rolled back because it could
  remove necessary execution context; the current rule requires a focused,
  executable handoff without an arbitrary length cap. A clean rerun is blocked
  by the ChatGPT rate limit.
- External AI OS, Thinking and LLM Project Instructions match the corrected
  repository files by exact settings read-back.
- LLM post-change validation passed 10/10 at 3,389 visible content characters,
  preserving the prompt, gates, registry and handoffs with 111 characters of
  buffer under the explicit maximum.
## Next fix
- Rerun the synchronized `[AI OS]` compact override after a clean cooldown;
  do not widen it after three correction attempts.
- Complete the four `NOT RUN` cases in `CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
  after the ChatGPT rate limit clears; use only completed responses to justify
  additional Project Instruction changes.
- Migrate priority reusable prompts to identifiable candidate revisions and run
  risk-appropriate evals before any new activation decision.
## Acceptance checklist
- [x] README matches actual Knowledge files
- [x] prompt registry exists
- [x] smoke QA file exists
- [x] cross-project live-eval matrix exists
- [x] status file exists
- [x] eval template exists
- [x] no production feature added
- [x] no hardcoded permanent model names added
## Blocked items
- secrets
- raw logs
- full dumps
- vector DB
- embeddings
- autonomous workflows
- web UI as current recommendation
- production-ready claims without acceptance
## Bundle semantic migration sources
- `LLM_02_PROMPT_LIBRARY_AND_REGISTRY_BUNDLE_SEMANTICS.md`
- `LLM_03_QUALITY_GATES_AND_EVAL_BUNDLE_SEMANTICS.md`

## From: `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`

# Autonomous Execution Standard (AES) v2.0.0
Status: normative package with scoped advisory semantic validation.
Canonical owner: `[AI OS]`.
Canonical source path: `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`.
Companion contract: `docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`.
Current schema: `schemas/autonomous_execution_record.schema.json`.
Historical v1 schema: `schemas/autonomous_execution_record.v1.schema.json`.
This document is the single canonical source for the Autonomous Execution
Standard. Knowledge Bundles, upload packages, and any future generated
indexes that mention AES are derived artifacts: they may summarize or link
to this file, but they must not restate the state machine, defect model, or
schema and must not become an independent semantic owner. If a derived
summary and this file ever disagree, this file wins.
## 0. What this is, and what it is not
AES does not replace or weaken any existing AI-OS component:
- Goal Mode (`GOAL_MODE.md`);
- routing;
- Codex autonomy policy (`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`);
- testing workflows;
- execution reporting (`ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`);
- Judge/Revisor;
- project handoffs (`ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`);
- Analytics methodology;
- the GitHub merge policy in `GOAL_MODE.md`;
- owner, deploy, and production gates.
AES is a shared execution layer that connects these existing components into
one closed loop:
```text
requirements
-> execution
-> validation
-> defect registration
-> corrective action
-> affected-scope rerun
-> revalidation
-> requirements traceability
-> Closure Review
-> terminal acceptance / stopped
```
Where AES and an existing project rule set different limits for the same
situation, the stricter rule wins (see Section 3).
### 0.1 Phase 1 boundary
Phase 1 (this package) delivers only:
- this canonical standard;
- the state model and status namespaces;
- the declarative execution-record JSON Schema;
- requirement, defect, iteration, and artifact structures;
- the project-extension contract;
- the status migration map;
- the acceptance-case specification;
- example execution records;
- pilot specifications;
- the adoption plan;
- thin references from existing canonical entry documents.
The original Phase 1 package explicitly did **not** include: a semantic execution validator,
blocking CI enforcement, an automatic stale-artifact gate, automatic
handoff-ID enforcement, an automatic scope-creep detector, an automatic
authority evaluator, a runtime execution service, an orchestration platform,
or any production enforcement. Only advisory structural validation of the
declarative JSON Schema is in scope: JSON syntax, required fields, field
types, enum values, nested object structure, and ID format patterns.
The scoped advisory semantic validator now checks its documented subset of
cross-field invariants. It remains read-only and is not a blocking CI service.
Closure Review is mandatory for every new v2 record; historical v1 records
remain historical evidence and are not rewritten.
## 1. Precedence model
```text
1. system, safety and non-overridable governance constraints
2. explicit user instruction
3. approved task package
4. project instructions
5. applicable project-specific execution extension
6. this document (`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`)
7. supporting playbooks, templates and examples
```
General rule: when two applicable rules conflict, the stricter constraint on
authority, safety, scope, validation, retry, or external side effect wins.
Consequences:
- user instruction does not override safety;
- an extension does not expand authority;
- an extension may only shrink an iteration limit, never grow it;
- a task package may narrow allowed scope, never widen it;
- this standard does not lift the stricter Codex one-fix policy (Section 9.5);
- `overall_delivery: pass` does not imply owner approval;
- Judge `pass` does not imply merge approval;
- `merged` does not imply production authorization.
## 2. Canonical ownership
```yaml
canonical_owner: "[AI OS]"
canonical_source_path: "docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md"
derived_artifacts: []   # none registered in Phase 1
supersedes: []
superseded_by: []
```
`[AI OS]` owns: execution-state semantics, authority separation, status
namespaces, the canonical governance mapping, adoption status, and the
source-versus-derived distinction. Project extensions (Section 10) own only
domain-specific detail and never become an alternate semantic owner.
### 2.1 Resolved owner boundary
Once canonical routing resolves the primary owner for a material decision or
deliverable, that ownership remains authoritative for the current stage. An
upstream project may prepare evidence, contradictions, context, bounded
options, risks, constraints, and a compact handoff, but it must not silently
make, approve, or operationalize the owner-only outcome.
The handoff must preserve the material evidence and contradictions, the
decision boundary they affect, relevant requirements and constraints, risks,
acceptance criteria, and the first safe step. It must carry enough bounded
context for the receiving owner to continue without re-decomposing the goal.
If the receiving owner cannot act, report the handoff or blocker; do not
substitute a nearby project's judgment. Section 15 defines the execution-state
fields that must persist across that handoff.
## 3. Target architecture
### 3.1 User entry layer
`GOAL_MODE.md` remains the user-facing entry contract:
```text
user outcome -> route -> bounded scope -> applicable Autonomous Execution Standard
```
Goal Mode carries only a thin reference to this document; it does not
duplicate the state machine, defect model, or schema.
### 3.2 Canonical execution layer (this document)
Owns only universal mechanics: execution identity, requirements, states,
validation records, defects, iterations, corrective actions, reruns,
acceptance scopes, freshness, handoff persistence, rollback readiness,
external authority separation, and terminal reporting.
### 3.3 Project-extension layer
Owns only domain-specific detail: defect subtypes, domain checks, domain
evidence, risk overrides, stricter retry limits, acceptance scopes,
project-specific blockers, and project-specific authority gates. An
extension must not copy the canonical standard wholesale (Section 10).
## 4. Canonical status namespaces
All machine-readable values use lowercase `snake_case`. Uppercase aliases in
canonical records are not permitted.
### 4.1 `execution_state`
`initialized`, `scoped`, `executing`, `validating`, `correcting`,
`revalidating`, `completed`, `stopped`.
### 4.2 `requirement.status`
`not_started`, `implemented`, `validation_pending`, `passed`, `failed`,
`blocked`, `not_applicable`.
### 4.3 Acceptance-scope `status`
`not_evaluated`, `pass`, `partial`, `fail`, `blocked`, `not_applicable`.
### 4.4 `overall_delivery`
`not_evaluated`, `pass`, `partial`, `fail`, `blocked`.
### 4.5 `qa_status`
`not_run`, `pass`, `fail`, `blocked`, `not_applicable`.
### 4.6 `judge_verdict`
`not_run`, `pass`, `revise`, `blocked`.
### 4.7 `authority_status`
`not_required`, `owner_review_pending`, `approved`, `rejected`.
### 4.8 `merge_status`
`not_applicable`, `not_opened`, `open`, `checks_pending`,
`owner_review_pending`, `merge_ready`, `merged`, `closed_without_merge`.
### 4.9 `production_status`
`not_applicable`, `not_authorized`, `authorized`, `deployed`, `rolled_back`.
### 4.10 `artifact_freshness_status` / `validation_freshness_status`
`current`, `stale`, `unverifiable`, `not_applicable`.
### 4.11 `closure_review.status`
`not_run`, `pass`, `revise`, `blocked`. This applies the existing review
verdict namespace to terminal evidence; it is not a delivery status and never
authorizes merge, deploy, or another external action.
There is no combined `judge_or_qa_status` field. `judge_verdict` and
`qa_status` are always separate fields (Section 8).
## 5. Execution-record identity and versioning
Minimal top-level structure (full contract: `schemas/autonomous_execution_record.schema.json`):
```yaml
schema_version: "2.0.0"  # current, closure-required record
standard_version: "2.0.0"
execution_id:
parent_execution_id:
project:
project_extension:
execution_mode:
risk_mode:
source_revision:
created_at:
updated_at:
execution_state:
requirements:
defects:
iterations:
validation_runs:
artifacts:
acceptance_scopes:
overall_delivery:
qa_status:
judge_verdict:
authority_status:
merge_status:
production_status:
rollback:
external_actions:
handoffs:
continuation:
closure_review:
final_report:
```
### 5.1 Required identity fields
`schema_version`, `standard_version`, `execution_id`, `project`,
`execution_mode`, `risk_mode`, `execution_state`, `created_at`, `updated_at`.
### 5.2 Parent execution
Root execution: `parent_execution_id: null`.
Child or continued execution: `parent_execution_id: "exec-..."`.
### 5.3 ID format
Recommended prefixes: `exec-`, `req-`, `def-`, `iter-`, `val-`, `art-`,
`ev-`, `handoff-`, `action-`.
Minimum requirements: lowercase; stable within the execution; unique within
its namespace; never reused after a record is deleted. A global UUID
infrastructure is not required for v1.
Example: `execution_id: "exec-aios-aes-v1-001"`, `requirement_id: "req-001"`,
`defect_id: "def-001"`, `iteration_id: "iter-001"`, `artifact_id: "art-001"`,
`evidence_id: "ev-001"`.
### 5.4 Compatibility and migration
New records must validate against the current v2 schema. It requires
`schema_version` and `standard_version` to be `2.0.0`, plus a
`closure_review` object. A successful v2 terminal record must carry a passed
Closure Review; the advisory semantic validator enforces the cross-field
conditions. Existing v1 evidence validates only against the explicitly named
historical schema and is read-only: do not rewrite accepted evidence solely to
add closure data. A v1 path is never a new-record intake path.
### 5.5 Continuation envelope for Invoke AI-OS
`continuation` is optional for ordinary AES records. Once `Invoke AI-OS`
orchestration begins, it is required and is the canonical durable continuation
state for that execution. It contains the original goal and acceptance
criteria, resolved owner, resume stage, stable `record_ref`, scope and routing
references, source revision, and state hashes. It does not create a second
state machine or override the record's requirements, defects, authority, or
terminal fields.
The record referenced by `record_ref` is the source of truth. Session context,
handoffs, and any ignored local pointer are derived views only. A local pointer
may contain only an execution ID and record reference, may be introduced only
after a behavioral test establishes a need, and is never required for a cold
entry.
Warm resume is permitted only after checking that the continuation envelope is
present and valid and that the original goal boundary, acceptance criteria,
resolved owner, relevant scope, authority, canonical routing state, and source
revision remain compatible. An unchanged source revision alone is insufficient.
### 5.6 Bounded multi-owner continuation control plane
The optional continuation control plane is defined in
`docs/standards/AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md`.
It adds an
auditable route trace, acceptance progress, and independent continuation
guards without creating a parallel state machine or changing the existing
status namespaces.  Its guard thresholds are named parameters, not canonical
numeric defaults; the stricter applicable corrective-loop limit still wins.
### 5.7 Authority provenance for transformed context
`authority_status` reports the execution's owner-approval state; it is not a
claim-level provenance label. When an active `Invoke AI-OS` execution carries
a decision-relevant claim through a context pack, handoff, or resume, its
`continuation.authority_provenance` and every new AES handoff preserve:
```yaml
claim_text:
authority_class:       # source_fact | owner_instruction | accepted_policy |
                        # observed_execution_evidence | candidate_research |
                        # hypothesis_recommendation
source_refs: []
action_eligibility:    # eligible | not_eligible | owner_decision_required
```
The same text may legitimately have different action eligibility because its
authority class differs. `candidate_research` and `hypothesis_recommendation`
must be `not_eligible`; they can inform review or evidence collection but
never authorize acceptance, policy change, or execution. `source_fact` and
`observed_execution_evidence` are evidence, not authority. `eligible` is
permitted only for an in-scope `owner_instruction` or `accepted_policy` and
never replaces an external authority gate. Source references are retained; a
summary, confidence label, or generic evidence reference is not a substitute.
## 6. Source-revision contract
```yaml
source_revision:
  revision_type:        # git_commit | git_tree | content_manifest | iteration_reference
  baseline_revision:
  final_revision:
  content_manifest:
  final_iteration_id:
```
For uncommitted working state, prefer a git tree reference, a content hash
manifest, or a deterministic iteration reference over a bare timestamp. A
timestamp alone is never sufficient freshness evidence.
## 7. State machine
```text
initialized -> scoped -> executing -> validating
```
If mandatory checks pass: `validating -> requirements traceability -> Closure
Review -> completed`.
If a correctable defect is found: `validating -> correcting -> revalidating`.
After a successful re-check: `revalidating -> requirements traceability ->
Closure Review -> completed`.
On a hard blocker or inability to continue, from any non-terminal state:
`any non-terminal state -> stopped`.
Terminal reasons (when `execution_state: stopped`): `hard_blocker`,
`iteration_limit_reached`, `repeated_defect_limit_reached`,
`conflicting_acceptance`, `validation_unavailable`,
`scope_boundary_violation`, `required_external_action_not_authorized`,
`closure_iteration_limit_reached`.
`required_external_action_not_authorized` applies only when a specific
external action is part of the mandatory objective and the objective cannot
be completed without it. Waiting for owner review after a successfully
completed local implementation does **not** move execution to `stopped`.
The correct terminal shape for that case is:
```yaml
execution_state: completed
overall_delivery: pass
authority_status: owner_review_pending
merge_status: owner_review_pending
production_status: not_authorized
```
## 8. Requirements traceability
Each mandatory requirement is a record:
```yaml
requirement_id:
requirement:
source:
mandatory:
implementation_locations:
evidence_refs:
validation_refs:
status:            # current status only, see 8.1
status_history:
gap:
corrective_action_refs:
```
### 8.1 Status model
One current field, `status`. History is kept separately:
```yaml
status_history:
  - status:
    iteration_id:
    recorded_at:
    evidence_refs:
```
There is no separate duplicating `final_status` field. At terminal
execution, the current `status` value is the final one.
### 8.2 Rules
1. `requirement_id` is unique within the execution.
2. Every mandatory requirement must end in `passed`, `blocked`, or
   `not_applicable` with a stated reason.
3. `not_applicable` requires a reason.
4. `passed` requires evidence, or an explanation of why no change was
   required.
5. A mandatory requirement with `status: failed` forbids
   `overall_delivery: pass`.
6. A requirement that went through correction must reference the iteration
   and the repeated validation.
7. A handoff must not drop requirement IDs.
8. Requirement scope may not be widened inside a corrective loop without a
   new, explicit scope decision.
## 9. Defects and the corrective loop
### 9.1 Defect record
```yaml
defect_id:
requirement_id:
detected_in_iteration:
detected_by:
classification:
subtype:
severity:
description:
evidence_refs:
correction_eligible:
required_authority:
remediation_owner:
corrective_action_refs:
affected_scope:
required_validation_refs:
status:
status_history:
resolved_in_iteration:
resolution_evidence_refs:
```
### 9.2 Classification
`implementation`, `validation`, `test`, `artifact`, `traceability`,
`contract`, `governance`, `authority`, `external_dependency`. An extension
may add a `subtype`, but must not change the classification semantics.
### 9.3 Severity
`recoverable`, `needs_check`, `hard_blocker` — compatible with the existing
Codex failure-classification model in
`ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`.
### 9.4 Defect status
`open`, `correcting`, `resolved`, `accepted_risk`, `blocked`.
`accepted_risk` requires `accepted_by`, `authority_evidence_ref`,
`acceptance_reason`, `accepted_at`. An executor may not self-accept as
`accepted_risk`: a security defect, a business-rule defect, a formula or
metric defect, a schema incompatibility, a public-API incompatibility, a
failed mandatory check, a production risk, or a source-mutation risk.
### 9.5 Corrective-loop contract
Mandatory sequence:
```text
validate -> register defect -> classify defect
-> determine correction eligibility and authority
-> apply minimal correction -> rerun affected checks
-> run required regression scope -> update defect evidence
-> update requirement evidence -> re-evaluate affected acceptance scopes
```
The executor must not: fix a defect without registering it; close a defect
without resolution evidence; reuse a stale test result after changing the
affected scope; widen scope for convenience of the fix; delete or weaken
validation; change business logic to obtain a `pass`; or use `blocked`
instead of an available, permitted local correction.
### 9.5.1 Trace-grounded repair eligibility
A failed execution is evidence of an observed defect, not by itself evidence
that the harness, prompt, skill, or workflow caused that defect. Before a
repair candidate changes one of those control surfaces, record a bounded
attribution statement that names the proposed target, the failed trace or
reproducible trajectory, the evidence that connects the target to the
failure, and the plausible alternatives considered.
`harness/workflow repair eligible: true` requires at least one of: a
reproducible failed step localized to the target; a paired or counterfactual
replay that distinguishes the target; a deterministic contract violation in
the target; or an isolated target change that removes the failure without
widening scope. The statement must also name the affected scope, reversible
minimal repair, and required revalidation/regression checks.
An invalid input, unavailable external dependency, missing authority, or
unidentified competing cause makes a harness/workflow repair `ineligible` or
`revise`, as applicable. Keep attribution status `uncertain` when the trace
cannot identify a cause; do not select a convenient repair. A candidate repair
that introduces a hard regression is rejected by the existing regression gate.
This gate is evidence discipline before a human-authorized, bounded repair;
it creates no autonomous diagnosis, self-modification, acceptance, or
unattended change authority.
### 9.6 Iteration model
```yaml
iteration_id:
iteration_number:
iteration_type:      # full_iteration | operation_retry
started_at:
completed_at:
trigger:
requirements_affected:
defects_addressed:
changes:
validation_refs:
result:
```
A **full iteration** starts when a substantive change to source,
configuration, contract, generated-source input, an analytical source
layer, or a prompt/workflow contract has been made after validation and a
new acceptance evaluation is required.
An **operation retry** repeats a single operation without changing
requirement scope or source state — e.g. a transient file lock, a transient
local command failure, a repeated parsing operation, or a repeated check
after a recoverable environment issue.
Default canonical envelope (a ceiling, not a standing permission):
```yaml
max_full_iterations: 5
max_retries_per_operation: 3
max_same_defect_recurrence: 2
```
Effective limit = `minimum(canonical limit, project-extension limit,
task-package limit, applicable safety limit)`.
### 9.7 Codex compatibility (hard constraint)
Until a separate owner decision changes it, `[Codex]` keeps its stricter
existing policy:
```yaml
max_corrective_fixes_per_failed_check: 1
```
If the same validation target fails again after one minimal correction
attempt: stop further file-changing corrections for that target, record the
evidence, report the residual risk, and set an honest acceptance status. This
standard's canonical envelope (Section 9.6) never widens this policy. A
distinct defect is eligible for separate handling only when independently
evidenced against a different affected requirement or independently failing
validation target; changing only `defect_id`, subtype, classification, label,
wording, or representation never resets the one-fix budget.
For the prohibition on agentic workflows, a bounded, reversible, in-repo
corrective loop operating under an AES record, fixed authority and scope,
validation, stop conditions, rollback, and human acceptance is supervised
execution. This narrow classification neither permits autonomous agents or
generic agentic workflows nor expands execution authority.
## 10. Acceptance model
```yaml
acceptance_scopes: {}   # object, keyed by scope name
overall_delivery: pass  # scalar
```
Example:
```yaml
acceptance_scopes:
  requirements_traceability:
    status: pass
    required_checks: []
    checks_run: []
    evidence_refs: []
    open_defect_ids: []
    limitations: []
  implementation:
    status: pass
    required_checks: []
    checks_run: []
    evidence_refs: []
    open_defect_ids: []
    limitations: []
overall_delivery: pass
```
### 10.1 Mandatory acceptance scopes
`requirements_traceability`, `implementation`, `tests`, `validation`,
`output_artifacts`, `corrective_loop`, `rollback_readiness`. Each scope
carries `status`, `required_checks`, `checks_run`, `evidence_refs`,
`open_defect_ids`, `limitations`.
### 10.2 Overall-delivery rule
`overall_delivery: pass` is permitted only when: all mandatory requirements
are resolved; mandatory scopes are `pass` or a justified `not_applicable`;
no open `recoverable` or `needs_check` defects remain; no hard blockers
remain; validation evidence matches the final source state; mandatory
artifacts are current; rollback readiness has been evaluated; and external
authority statuses are reported separately. Waiting for owner review does
not pull `overall_delivery` down to `fail`.
### 10.3 Closure Review (v1.1)
Before a closure-aware record can successfully terminate, build a compact
`closure_context` from the original goal/task, agreed scope, constraints,
acceptance criteria, material invariants, final revision/state references,
requirements traceability, latest test/validation/artifact evidence,
limitations, residual risks, rollback and external-authority status, and
input/state hashes. The full transcript is not required.
Review the original goal rather than the last fix list. State the general
invariant behind known defects and inspect applicable decision-bearing inputs,
transformations, aggregation points, outputs, and material trust boundaries.
Preserve uncertainty: `UNKNOWN != NOT_REPORTED`, `PARSE_FAILED != NOT_REPORTED`,
`PROBABLE != CONFIRMED`, `NOT_RUN != PASS`, and `HYPOTHESIS != OBSERVED`.
Mutation evidence is observed only when the mutation was applied, validation
ran, and its result was recorded.
For `material`, `complex`, or high-risk work, use existing execution/risk modes
for a bounded adversarial attempt to reject acceptance: boundary and
contradictory states, missing evidence, invalid transitions, aggregation loss,
unsupported defaults, routing/requirement omissions, status inflation, forged
intermediate state, and stale downstream artifacts are applicable classes.
Lightweight reversible work may use a proportionate review.
If an observable in-scope gap affects acceptance, is technically correctable,
needs no new owner/business/policy decision, and can be fixed with available
authority/tools, register it and return to `correcting`. Do not relabel it a
limitation, residual risk, or future improvement merely to terminate. Scope or
owner-policy changes follow existing blocked/stopped authority mapping.
`max_closure_corrective_iterations: 2` is a ceiling separate from normal full
iterations. Effective limit is the minimum of canonical, extension,
task-package, and stricter applicable policy. A counted closure iteration
changes state for a newly found correctable acceptance defect and completes
rerun/revalidation. It never widens `[Codex]`
`max_corrective_fixes_per_failed_check: 1`. After a closure correction,
affected validations and artifacts are stale until refreshed under Section 11.
## 11. Validation runs and freshness
### 11.1 Validation-run record
```yaml
validation_id:
validation_type:   # unit | integration | contract | smoke | golden | data_quality | artifact | schema | docs_consistency | judge | manual_review
command_or_method:
validated_revision:
covered_paths:
covered_requirement_ids:
started_at:
completed_at:
result:
evidence_refs:
freshness_status:
limitations:
```
### 11.2 Validation freshness
`freshness_status: current` is permitted when
`validation.validated_revision == source_revision.final_revision`, or when a
documented affected-scope analysis proves that changes made after the
validation run did not touch the covered paths and requirements. In the
latter case the record must also carry `freshness_justification` and
`unaffected_paths_evidence`. A check run before the last relevant change is
`stale`.
### 11.3 Artifact-freshness record
```yaml
artifact_id:
path:
artifact_type:
mandatory:
source_inputs:
  - path:
    content_hash:
    last_changed_iteration:
generation_method:
generated_from_revision:
generated_in_iteration:
generated_at:
validation_refs:
freshness_status:
freshness_evidence_refs:
```
A mandatory artifact is `current` when `generated_from_revision` matches the
final relevant source state, the hashes of all mandatory source inputs
match, artifact validation ran on the final version, and no relevant source
change occurred after generation. Timestamp is auxiliary evidence only. An
artifact is `stale` when a source input changed after generation, a content
hash mismatches, the artifact predates the last corrective iteration, or its
final validation belongs to a previous version. `overall_delivery: pass` is
forbidden while a mandatory artifact is stale — this matters most for XLSX,
DOCX, PDF, PPTX, marts, charts, memos, and other generated bundles.
## 12. Validation responsibility matrix
The original Phase 1 matrix separated deterministic structural checks from
future semantic enforcement. The repository now has a scoped, read-only
advisory semantic validator (`scripts/validate_autonomous_execution_record.py`)
for its documented subset; it is not CI or runtime enforcement.
| Property checked | Structural mechanism | Current semantic coverage |
| --- | --- | --- |
| JSON syntax | JSON parser | unchanged |
| Required fields | JSON Schema | unchanged |
| Field types | JSON Schema | unchanged |
| Enum values | JSON Schema | unchanged |
| ID string format | JSON Schema pattern | unchanged |
| Nested record shape | JSON Schema | unchanged |
| Duplicate IDs by property | acceptance-case specification | SEM-002 |
| Mandatory failed requirement with overall pass | normative rule and case specification | SEM-001 |
| Open defect with overall pass | normative rule and case specification | SEM-003 |
| Artifact revision mismatch | normative rule and pilot | SEM-004 |
| Test revision mismatch | normative rule and pilot | SEM-005 |
| Iteration-limit enforcement | normative rule and pilot | SEM-006/010 |
| Allowed-file scope | exact scope manifest and git diff review | repository validator |
| Extension authority expansion | contract and Judge review | deterministic policy validator where feasible |
| Canonical-content duplication | docs consistency and Judge review | optional repository consistency check |
| Business-rule preservation | project-specific checks | project-specific enforcement |
| Merge/deploy authority | explicit fields and owner review | external platform gates |
The advisory validator covers only SEM-001…014 and is not evidence of CI,
runtime enforcement, owner approval, merge, deploy, or production
authorization. See
`docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md` for the
full structural and semantic case list.
## 13. External authority separation
An execution record always reports these fields separately, and never
collapses one into another:
```yaml
overall_delivery:
qa_status:
judge_verdict:
authority_status:
merge_status:
production_status:
```
Forbidden implicit conversions: judge `pass` -> owner approved;
implementation `pass` -> merge ready; merge ready -> merged; merged ->
production authorized; not merged -> failed; owner review pending ->
blocked.
### 13.1 External-action record
```yaml
action_id:
action_type:   # provider_api_call | source_mutation | merge | deploy | production_promotion | migration | destructive_operation
required_for_objective:
requested:
required_authority:
authority_evidence_ref:
status:
executed_at:
result_evidence_ref:
```
An external action without explicit authority is not executed, is not
retried automatically, is not treated as authorized just because local
configuration exists, and does not turn a successful local implementation
into `fail` when the action was not part of the mandatory objective.
### 13.2 Effect-boundary invariant
Every side-effecting `external_action` follows this bounded sequence:
```text
PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY
```
The required `effect_boundary.preview` records the target resource, intended
mutation, affected scope, required authority, reversibility/rollback note,
expected verification, and an intent fingerprint. A preview is information,
not authorization. Commit is forbidden without an authority evidence reference
and recorded authority check. A material change between the preview fingerprint
and commit intent requires an authority recheck before commit. After commit,
verification must pass with evidence before successful completion can be
reported; a failed or blocked verification is not a successful external action.
This contract applies only to declared side-effect types in Section 13.1. It
does not add a runtime approval service, auto-approval, or a preview burden to
read-only actions.
## 14. Rollback readiness
```yaml
rollback:
  strategy:
  scope:
  command_or_procedure:
  prerequisites:
  data_loss_risk:
  validation_after_rollback:
  status:   # ready | partial | unavailable | not_applicable
```
For docs/schema Phase 1 work, acceptable strategies are a scoped
`git restore`, closing the PR without merging, or reverting a single commit
after merge. `git reset --hard` is never a default rollback strategy.
## 15. Cross-project handoff persistence
```yaml
handoff_id:
execution_id:
parent_execution_id:
from:
to:
requirement_ids:
open_defect_ids:
current_iteration_id:
evidence_refs:
acceptance_snapshot:
qa_status:
judge_verdict:
authority_status:
authority_provenance:
next_owner:
```
A new execution ID is permitted only with an explicit parent/child link.
### 15.1 Reverse handoff (Judge/QA back to executor)
```yaml
handoff_id:
execution_id:
from:
to:
judge_verdict:
qa_status:
defects_added:
requirements_affected:
required_corrections:
evidence_refs:
next_owner:
```
A handoff must never drop: execution ID, requirement IDs, defect IDs,
iteration ID, evidence references, authority status, or authority provenance
for a decision-relevant claim. A new AES handoff carries an
`authority_provenance` object even when its `claims` list is empty.
### 15.2 Continuation handoff rule
For an active `Invoke AI-OS` execution, a local or cross-project handoff is an
intermediate stage, never a lifecycle terminator. Return its evidence to the
same AES execution, update `continuation.resume_stage`, validate the affected
requirements or defects, and compare the result with the original acceptance
criteria before selecting `completed`, `stopped`, or the next authorized stage.
## 16. Risk-scaled modes
One standard; only evidence depth changes.
### 16.1 Lightweight
For simple docs-only changes, local reversible config changes, a single
scope, low risk. Minimum: execution ID, requirements, relevant checks, a
minimal defect record, acceptance scopes, rollback, authority statuses.
### 16.2 Standard
For ordinary repository tasks, code/config changes, generated artifacts,
multiple requirements. Minimum: full execution record, requirements,
defects, iterations, validation runs, artifact manifest, acceptance scopes,
rollback.
This Phase 1 package itself was executed at Standard risk mode (docs and
schema, several requirements, no runtime execution record required as a
bookkeeping artifact — see `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md`).
### 16.3 Full
For Analytics, high-risk tasks, production-adjacent work, cross-project
workflows, multiple artifact layers. Minimum: full traceability, several QA
layers, detailed defects, partial scope acceptance, cross-project handoff
preservation, an explicit authority map, full artifact lineage.
## 17. Non-goals and enforcement boundary
Forbidden in this task: a runtime service; an execution database; a
blocking CI gate; changes to `.github/workflows/*`; a
web UI; a vector DB; embeddings; an agent orchestration platform; automatic
project invocation; automatic issue creation or closing; automatic PR
creation as a runtime behavior of the standard; automatic PR approval or
merge; automatic deploy; routing-architecture changes; merging projects;
rewriting all Project Instructions; moving project methodology into the
canonical standard; a separate file per runtime defect; changes to business
formulas, metrics, financial controls, or provider/API routing; real
external API calls; source-data mutation; or changes to existing product
schemas or public APIs.
## 18. PR semantics
The implementation PR for adopting AES (or any AES-tracked change) is only a
delivery mechanism for a repository change.
```text
The implementation PR is a delivery mechanism.
The Autonomous Execution Standard does not automatically create,
approve, merge or deploy pull requests.
```
## 19. Adoption phases
See `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md` for the full phase list.
Summary: Phase 1 (historical normative package) -> Phase 2 (Codex pilot,
separate issue/PR) -> Phase 3 (artifact pilot) -> Phase 4 (Analytics pilot)
-> Phase 5 (cross-project pilot) -> scoped advisory semantic validation
(delivered) -> any blocking enforcement (requires a separate owner decision).
## 20. Next owner
```text
[Codex] Phase 1 implementation
-> [Thinking]/Judge architecture review
-> owner acceptance
-> separate Codex pilot task
```
Completion of this Phase 1 package does not authorize: pilot execution,
semantic enforcement, CI blocking, merge, deploy, or production adoption.

## From: `ChatGPT/[LLM]/Knowledge/LLM_EVAL_STANDARD.md`

# LLM Eval Standard
## Purpose
Define minimum, risk-proportional evaluation for reusable `[LLM]` prompt and workflow assets. Evaluation must be sufficient for the cost of error without turning `[LLM]` into an MLOps platform.
## Risk classification
Choose the evaluation level from four primary considerations:
- error cost;
- evidence sensitivity;
- reversibility;
- verification path.
Downstream consequence may also raise the level. Do not use a mandatory numerical risk formula.
## Evaluation levels
### LIGHT
Use for low-risk, reversible workflows whose output is easy to verify, such as formatting, simple rewriting, structure transformation, or low-risk extraction with easy manual verification.
Minimum:
- schema or smoke check;
- 1-3 representative cases;
- owner check.
LIGHT does not require a full regression suite or heavyweight eval suite.
### CONTROLLED
Use for reusable workflows where an error may affect downstream analysis, decision support, or a repeated process.
Minimum:
- representative cases;
- negative and boundary cases;
- materially relevant historical failures;
- regression protection;
- Judge/revise where appropriate;
- owner acceptance.
### HIGH-RISK
Use for evidence-sensitive or consequential workflows.
Minimum:
- extended representative set;
- boundary and adversarial cases;
- historical failure cases;
- workflow-specific Judge fixtures;
- deterministic verification where applicable;
- explicit human acceptance;
- visible limitations.
HIGH-RISK does not authorize an LLM to perform deterministic calculations. Route `[Analytics]` calculations and analytical work to `[Analytics]`.
## Evaluation types
### Pre-promotion / offline eval
Checks a candidate before promotion and governed reuse.
### Regression eval
Checks that a material change has not reintroduced known failure modes. Regression cases should primarily come from materially relevant historical failures or corrections; not every comment needs to become a regression test.
### Runtime/output QA
Checks a specific output produced during workflow use. Runtime QA does not by itself prove the quality of the reusable asset.
## Deterministic before Judge
If a criterion can be checked deterministically, perform that check before relying on an LLM Judge. Examples include:
- required sections and schema fields;
- enum and exact status values;
- file presence;
- routing owner;
- forbidden field detection;
- simple contract validation.
Use Judge evaluation for semantic or evidence-sensitive criteria. A Judge is not absolute truth.
## Ownership boundary
`[AI OS]` owns:
- canonical Judge doctrine;
- evaluator governance and calibration principles;
- generic evidence/confidence semantics;
- generic promotion governance.
`[LLM]` owns:
- workflow-specific rubrics;
- domain, negative, and boundary cases;
- expected outcomes;
- historical regression fixtures.
`[LLM]` provides workflow-specific test fixtures for the canonical Judge mechanism. It does not own a separate generic Judge calibration standard.
## Evidence, evaluation, and acceptance
Keep these operational concepts separate:
```text
evidence_status -> follows canonical [AI OS] semantics
workflow_eval -> result for a specific LLM asset or workflow
acceptance_status -> owner or human-gate decision
```
Do not introduce model confidence, Judge confidence, a workflow-confidence score, or a multi-level confidence architecture. Self-reported LLM confidence is not a governance metric or a calibrated probability. Model uncertainty may be recorded as a textual limitation.
## Failure to regression
When a failure materially affected output, can recur, and belongs to reusable behavior, consider its case as a candidate regression fixture. Keep the reference in existing eval records; do not create a separate Failure Registry.
## Local AI boundary
Existing `LOCAL_AI_EXPERIMENT_PLAYBOOK.md`, `LOCAL_AI_SECURITY_BOUNDARY.md`, and local pilot rules remain authoritative:
- local output is draft/candidate evidence;
- local retrieval is not final truth;
- only curated context is allowed;
- limitations are required;
- production truth is prohibited without appropriate QA.
Risk-aware use:
- low risk: a local result may be sufficient after deterministic/schema verification passes;
- controlled: use a local draft with stronger or Judge verification where needed;
- high-risk or evidence-sensitive: local processing may prepare a draft, but consequential conclusions require stronger verification and a human gate.
This is an operational interpretation, not a separate permanent escalation architecture.
## Context boundary
Follow the existing Context Engineering standards for curated context, facts versus assumptions, forbidden secrets, Context Pack/CTC selection, and quality gates. Do not duplicate the Context Pack schema here.

## From: `ChatGPT/[LLM]/Knowledge/LLM_03_QUALITY_GATES_AND_EVAL_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[LLM]/Knowledge_Bundles/LLM_03_QUALITY_GATES_AND_EVAL.md`.
## Legacy section: `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`
| `[AI OS]` → `[LLM]` | blocked, 5/10 | route named correctly, but `[AI OS]` selected the model class and designed the workflow instead of handing off |
| `[LLM]` compact asset | revise, 9/10 | safe complete asset exceeded the 3,500-character cap by 28 visible content characters |
- one reproduced LLM compactness defect;
## Legacy section: `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- matrix_id: `LLM-XPROJECT-LIVE-001`
- version: `1.0.0-candidate`
- owner_project: `[LLM]`
- status: `optimization_partial`
- production_status: `NOT AUTHORIZED`
The matrix uses one exact prompt for each of the seven ChatGPT Projects and
scores route correctness, scope boundary, handoff completeness, evidence/QA
preservation and compact operability. A rate limit, authentication loss or
ambiguous Project identity is recorded as `NOT RUN`, not fail.
Observed baseline: `[Inbox Router]` passed 9/10 with one strong route to
`[LLM]`, a bounded handoff and no target-workflow solution. `[AI OS]` scored
5/10: it named `[LLM]` as owner, then selected the model class and designed the
workflow itself. `[Analytics]`, `[Codex]` and `[Thinkers OS]` produced partial
diagnostic fragments before the rate-limit dialog interrupted generation;
`[Thinking]` did not produce a response. `[LLM]` completed at 3,528 visible
content characters and remains `REVISE` against its 3,500 cap. The four
incomplete cases remain `NOT RUN`. Overall baseline status: `PARTIAL`.
AI OS corrective evidence: two completed reruns fixed ownership; response size
fell from 4,794 to 2,475 characters but remains above the compact target. A
third rerun was interrupted and is `NOT RUN`. The synchronized `[LLM]` hard-cap
rule passed its completed post-change rerun at 3,389 visible characters with
all requested controls preserved.
## Autonomous Execution Standard
Execution in `[LLM]` now also follows the canonical Autonomous Execution
Standard defined in `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above the output QA, hallucination
checks, and judge/eval workflow above as a shared execution/validation/
defect/acceptance loop, without replacing them or the merge policy in
`GOAL_MODE.md`. No `[LLM]`-specific AES extension exists yet; only the
canonical standard is in scope here. New v2 Closure Review rechecks prompt and
input-context contracts, output schema, unsupported claims, eval regressions,
and routing ownership before acceptance.
For an `Invoke AI-OS` continuation, the canonical AES envelope preserves the
original goal, acceptance criteria, resolved owner, stage, and freshness
state; it does not replace LLM quality gates, eval evidence, or owner review.
After routing resolves a material decision or deliverable owner, `[LLM]` may
preserve evidence, contradictions, constraints, and a bounded handoff, but it
must not silently substitute its judgment for the resolved owner.
## Legacy section: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`
- workflow: risk-triggered memo review
- registry status: active
- owner acceptance: accepted on 2026-08-18
- corpus: 10 real memo cases from one workbook and period `2026-05`
- case mix: routine 4, material 2, evidence-sensitive 2, QA-defect 1, Judge-defect 1
- quality: OLD 154/160; NEW 154/160
- blind verdict: equivalent 10/10
- false bypass count: 0
- Judge runs: 10 -> 6 (40% reduction)
- Revise runs: 10 -> 2 (80% reduction)
- semantic LLM stages: 30 -> 18 (40% reduction)
- workflow quality: PASS
- safety: PASS
- logical execution efficiency: PASS
- token savings: NOT PROVEN
- billing savings: NOT PROVEN
- generalization beyond the current corpus: NOT PROVEN
- one real workbook and one period, `2026-05`
- frozen drafts; review-loop tested, not draft-generation variability
- blind Judge used the current environment model, not an independent model
- provider-level token usage unavailable
- elapsed-time attribution unavailable
The accepted memo workflow does not resolve the separate legacy prompt-eval debt.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or owner-acceptance evidence. Priority migration debt is listed in `PROMPT_REGISTRY.md`; no eval pass is inferred.
- Cross-project live coverage is partial: `[Inbox Router]` passed; `[AI OS]` reproduced a scope-boundary defect that was fixed in two completed reruns. Its later arbitrary compactness cap was rolled back in favour of a focused executable handoff; the clean rerun is `NOT RUN` under the ChatGPT account-level request limit. `[LLM]` passed the corrected explicit hard cap at 3,389 visible characters; four baseline cases remain `NOT RUN`.
- External AI OS, Thinking and LLM Project Instructions match the corrected repository files by exact settings read-back.
- LLM post-change validation passed 10/10 at 3,389 visible content characters, preserving the prompt, gates, registry and handoffs with 111 characters of buffer under the explicit maximum.
- Rerun the synchronized `[AI OS]` focused-handoff rule after a clean cooldown; do not change it without a completed reproduced defect.
- Complete the four `NOT RUN` cases in `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` after the ChatGPT rate limit clears; use only completed responses to justify additional Project Instruction changes.
- Migrate priority reusable prompts to identifiable candidate revisions and run risk-appropriate evals before any new activation decision.
