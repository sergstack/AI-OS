# [Analytics] — QA Governance Routing

## Purpose

Compact upload artifact for [Analytics] covering qa governance routing.

## Source files

- `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`
- `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
- `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`
- `ChatGPT/[Analytics]/Knowledge/AI_OS_REFERENCE.md`
- `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`
- `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:dd8159a551edce7651ecff7186ac4e6f8036dfd1c6f5a427fc0e82a5edd3db9b

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`

# Analytics QA Checklist
## Data QA
- [ ] Required files exist.
- [ ] Required columns exist.
- [ ] Data types valid.
- [ ] Dates parsed correctly.
- [ ] Currency / units normalized.
- [ ] Null policy applied.
- [ ] Duplicate policy applied.
- [ ] Freshness checked.
- [ ] Mapping tables checked.
- [ ] Unmatched rows listed.
## Main files QA
- [ ] `stage_main_full` exists or is designed.
- [ ] `stage_main_full` has no business metrics.
- [ ] `stage_main_full` has no analytical classifiers.
- [ ] `stage_main_full` is portable to DB / BI / Excel.
- [ ] `mart_main_full` exists or is designed.
- [ ] `mart_main_full` contains metrics and formulas.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is designed.
- [ ] Mart slices are derived from `mart_main_full`.
## Calculation QA
- [ ] RAW totals reconciled.
- [ ] STAGE totals reconciled.
- [ ] MART totals reconciled.
- [ ] Metric formulas documented.
- [ ] Edge cases tested or listed.
- [ ] Outliers reviewed.
- [ ] Thresholds explicit.
- [ ] Grain explicit.
- [ ] Period explicit.
## Analysis QA
- [ ] Method stated.
- [ ] Source mart stated.
- [ ] Top deviations ranked by materiality / ABS Delta.
- [ ] Driver logic documented.
- [ ] Timing status not overstated.
- [ ] Confirmed cause separated from hypothesis.
- [ ] Confidence rationale stated.
- [ ] Method selection adequate; no material omission or method bloat.
- [ ] Registry mapping followed; deterministic trigger and trigger contract/evidence checked; no silent LLM override.
- [ ] Selected prerequisites met; reasoning did not replace a deterministic claim.
- [ ] Claim lineage is complete and references an executed method.
- [ ] Baseline explicit; required baseline robustness assessed.
- [ ] Population/denominator explained and scope change quantified.
- [ ] Preliminary evidence sufficient to continue.
- [ ] Alternative explanation, contradicting/discriminating evidence, and material falsification test assessed.
- [ ] Material method disagreement recorded and unresolved conflict constrains claim strength.
- [ ] Claim support, causal status, and confidence are not confused.
- [ ] `manual_review_required` correctly set; when `yes`, review owner/status/resolution recorded before publication.
- [ ] Final evidence sufficient for the claim; conclusion is not stronger than evidence.
- [ ] Stop/escalation assessed; routine collapse applied; no unnecessary full reasoning record.
- [ ] Exception and anomaly distinguished.
- [ ] Unmatched analysis used when population mismatch is material.
- [ ] Factor decomposition reconciled when applicable.
- [ ] Timing/cut-off checked when material.
- [ ] Data-layer artifact considered when material.
- [ ] Leading-indicator relationship supported and not presented as causal without evidence.
- [ ] New-method trigger contract and prerequisites satisfied.
- [ ] New method added only for a distinct capability.

Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. This extends existing Analysis QA and creates no separate QA framework.
## Chart QA
- [ ] Chart source mart/slice listed.
- [ ] Metric listed.
- [ ] Grain listed.
- [ ] Period listed.
- [ ] Caption does not exceed data.
- [ ] Chart adds insight.
- [ ] Chart labels, legends, axes, titles and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Technical IDs are absent from executive chart body unless the chart is appendix / evidence.
## Memo QA
- [ ] No unsupported claims.
- [ ] Every key conclusion has evidence.
- [ ] Limitations visible.
- [ ] Recommendations do not exceed data.
- [ ] Confidence stated.
- [ ] Risk has `risk_basis`.
- [ ] Action has owner / due date / status.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` appear only in appendix / evidence context.
- [ ] Appendix is clearly separated from executive memo.
### Material management synthesis QA
Apply only to material / decision-critical management-facing output:
- [ ] Business question is answered by an executive verdict; material findings are prioritized by business relevance rather than catalogued.
- [ ] Supported business meaning is stated, or the evidence gap is explicit; any “main” issue has a supported criterion.
- [ ] Material performance dimensions remain distinct; business effect and data/control artefact are separated where relevant.
- [ ] Management implication and decision/action if any are evidence-constrained; material uncertainty remains visible.
- [ ] What would materially change the conclusion is stated when relevant, and strategic choice is routed to `[Thinking]`.
- [ ] Executive synthesis is materially shorter than supporting evidence; routine compact output is not expanded.
## Handoff QA
- [ ] Handoff only if another project is needed.
- [ ] Expected output clear.
- [ ] Acceptance criteria clear.
- [ ] Inputs listed.
- [ ] Risks listed.
- [ ] No unresolved analysis hidden in Codex task.


## From: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`

# Analytics Acceptance Criteria
A result is accepted when:
1. Question and scope are clear.
2. Inputs are listed.
3. Data contract exists or missing fields are explicit.
4. Grain, period and filters are documented.
5. Stage and mart main files are created or designed.
6. Calculation method is documented.
7. QA checks passed or failed with explanation.
8. Findings are traceable to data.
9. Limitations are explicit.
10. Handoff package is complete if another project is needed.
## Main file acceptance
```text
stage_main_full: pass/fail/blocked/not_applicable
mart_main_full: pass/fail/blocked/not_applicable
mart_main_tz_or_compact: pass/fail/blocked/not_applicable
slices_from_mart_main_full: pass/fail/blocked/not_applicable
```
## Acceptance status
```text
accepted: yes/no
qa_status: pass/fail/blocked
confidence: high/medium/low
residual_risks:
known_limitations:
next_step:
```
## Usability acceptance
A result is not accepted if it is technically complete but unusable for the requested task.

For `quick` mode:
- max 1 user-facing table;
- max 5 metrics;
- max 12 visible columns;
- no workbook unless explicitly requested;
- no hidden expansion into `full` package.

For `standard` mode:
- compact front view required;
- no more than 3-5 sheets unless justified;
- every extra sheet must have a business purpose.

For `full` mode:
- workbook may be large, but must include README / index, compact front sheet, data dictionary, field groups and evidence appendix.
## Material management synthesis acceptance
For `analytical_depth = material / decision_critical` and management-facing output:
- the business question is answered by an executive verdict;
- the smallest sufficient set of material findings is prioritized by a supported business criterion;
- headline business meaning is supported or its evidence gap is explicit;
- materially different performance dimensions and data/control artefacts remain distinct where relevant;
- management implication and decision/action if any do not exceed verified evidence;
- material uncertainty remains visible, with what would change the view where applicable;
- strategic choice is routed to `[Thinking]` when it depends on trade-offs, risk appetite, or preferences;
- the executive layer is materially shorter than the supporting evidence.
Routine compact tasks are excluded from expanded synthesis acceptance.
## Blocked status
Use `blocked` when:
- required data is missing;
- grain is unknown;
- DQ Fail;
- no reconciliation possible;
- metric formulas undefined;
- compact-only input is insufficient for requested conclusion;
- implementation is required before result can be produced.
## Not production-ready rule
Smoke QA or a good memo does not equal production readiness. Production readiness requires implementation evidence, tests, acceptance and rollback/release notes where relevant.


## From: `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`

# Routing and Handoff
## Project routing
```text
AI-концепция / supported KB pattern → [AI OS]
Стратегия / решение / риски → [Thinking]
Расчёты / данные / marts → [Analytics]
Prompts / model routing / LLM quality → [LLM]
Код / implementation / tests / release → [Codex]
```
## Analytics default
For metrics, marts, data contracts, QA, calculations, deviations, charts and analytical memo structure: stay in `[Analytics]`.
## Do not hand off too early
Before handoff, provide:
- analytical framing;
- data contract or missing fields;
- main files standard;
- expected metrics;
- QA requirements;
- acceptance criteria.
## Standard handoff format
```text
# Handoff

From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected outputs:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
```
## Thinking → Analytics
Pass:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.
## Analytics → LLM
Use when verified numbers need narrative, prompt workflow or model routing.
Pass:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.
## Analytics → Codex
Pass:
- files to inspect/change;
- input/output contract;
- main files rules;
- task packet;
- forbidden actions;
- tests;
- acceptance criteria.
## Codex → QA / Release
Pass:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.


## From: `ChatGPT/[Analytics]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
- understand a new AI concept;
- find supported AI pattern;
- check confidence / evidence for AI claims;
- connect AI trend to Sergey’s work;
- find governance rule;
- distinguish supported / weak / unsupported AI claim.
## Do not copy into Analytics
Do not copy:
- full AI OS compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## How to ask AI OS
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>

Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Boundary rule
AI OS gives evidence and patterns. `[Analytics]` applies them only when they affect analytics workflow, QA, marts, memo or reporting.


## From: `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`

# Governance and Anti-Patterns
## Governance principles
- Deterministic calculations before LLM narrative.
- Traceability before automation.
- Main files before slices.
- Evidence before conclusions.
- Acceptance before production readiness.
- Analysis inside `[Analytics]` before handoff.
- Registry and trigger contracts govern method eligibility; no silent LLM override.
- Reasoning cannot replace deterministic execution or missing prerequisites.
- Claim strength cannot exceed final evidence sufficiency.
## Evidence labels
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
| Handoff to Codex too early | Analytics loses its role | Analyze first, handoff implementation only |
| Raw-to-memo | Unsupported conclusions | Use mart/evidence |
| Pretty memo before QA | Looks right, may be wrong | QA first |
| Low Confidence as fact | Misleading | Label hypothesis |
| Action without owner/date | Not actionable | Add owner/due date/status |
## P0 analytical reasoning failure modes
- Driver/root-cause and correlation/causation confusion → claim ladder and causal evidence gate.
- Premature explanation → preliminary evidence stop gate.
- Baseline, aggregation, selection/exclusion, population, denominator, timing/cut-off bias → explicit controls and triggered robustness tests.
- False precision and narrative stronger than evidence → final evidence sufficiency cap.
- Method bloat → minimum sufficient set and stop rules.
- Confidence mistaken for causality → `confidence != claim_support != causal_status`.
- Numerical magnitude mistaken for business materiality → separate task profile; no numerical reasoning score.
- Reasoning substituted for deterministic execution → enforce deterministic boundary.
- Silent registry override or undefined trigger → require trigger type/rule/evidence and existing QA review.
- Blocked method used as evidence or execution lineage lost → `blocked != executed` and unique `method_execution_id`.
- Conflicting methods silently reconciled → preserve contradiction, constrain claim, escalate if material.
- Full reasoning applied to routine work without trigger → compact runtime collapse.
- Anomaly mistaken for control exception → distinguish unusual observation from explicit rule violation.
- Aggregate reconciliation replacing entity-level unmatched analysis → identify concrete one-sided elements when material.
- Driver decomposition accepted without factor reconciliation → reconcile factor effects when applicable.
- Timing shift interpreted as economic effect → run timing validation for material cut-off candidates.
- Transformation artifact interpreted as source/business effect → trace `REPORT → MART → STAGE → RAW`.
- Leading indicator treated as causal predictor → use signal/association/risk language without causal evidence.
- Method catalog inflated by controls → require distinct question, execution, and material effect.
- Decision methods leaking from `[Thinking]` → keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`.
## metric / artifact explosion
Anti-pattern: a short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.

Why bad:
- user cannot inspect the result;
- decision signal is buried;
- QA fields become noise;
- compact task becomes `full` package.

Correct action:
- classify output mode first;
- default to compact view;
- expose only decision-relevant metrics;
- move evidence/QA/lineage to appendix or internal design;
- ask for `full` mode only when needed.
## Production readiness rule
Do not claim production readiness unless:
- implementation exists;
- tests passed;
- smoke QA recorded;
- acceptance criteria passed;
- residual risks listed;
- rollback/release notes exist.


## From: `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`

# Smoke QA for Analytics
Назначение: проверить, что `[Analytics]` после загрузки пакета сохраняет способность проводить анализ и правильно использует routing, main files, QA и handoff.
## 1. Scope and routing
```text
Мне нужно проанализировать отклонения план-факт и подготовить выводы. Ты будешь делать это здесь или отправишь в Codex?
```
Pass condition:
- отвечает, что анализ делается в `[Analytics]`;
- Codex нужен только для реализации/автоматизации;
- называет data contract, stage/mart, QA.
## 2. Main files
```text
Какие главные файлы должны быть в stage и mart?
```
Pass condition:
- называет `stage_main_full`;
- говорит, что stage без метрик и классификаторов;
- называет `mart_main_full`;
- называет `mart_main_tz` или `mart_main_compact`;
- говорит, что slices строятся из `mart_main_full`.
## 3. Compact/full input
```text
На входе есть только json compact. Что ты сделаешь?
```
Pass condition:
- использует compact как scope;
- фиксирует assumptions/gaps;
- не придумывает full context;
- всё равно проектирует main files.
## 4. Charts
```text
Из чего строить графики для аналитической записки?
```
Pass condition:
- отвечает: из `mart_main_full` или slices derived from it;
- требует metric, grain, period, source_mart.
## 5. Memo
```text
Какие обязательные блоки MVP аналитической записки?
```
Pass condition:
- DQ;
- Plan / Fact / Delta / ABS Delta;
- top deviations;
- row type;
- timing;
- risk + basis;
- confidence;
- cause vs hypothesis;
- action + owner + due date;
- limitations.
## 6. Stop conditions
```text
Когда нельзя публиковать управленческий вывод?
```
Pass condition:
- DQ Fail;
- no grain;
- no data contract;
- no reconciliation;
- Low Confidence as final cause;
- risk without basis;
- action without owner/date;
- INOUT without Definition Card.
## 7. Acceptance
```text
Когда результат аналитики считается принятым?
```
Pass condition:
- scope clear;
- inputs listed;
- data contract;
- main files;
- calculation method;
- QA;
- traceable findings;
- limitations;
- handoff complete if needed.
## 8. short task / anti-bloat test
```text
Сделай короткий анализ: покажи 3 главных отклонения и вывод.
```
Pass condition:
- mode = `quick`;
- no workbook unless requested;
- no `full` package;
- max 1 table;
- max 5 metrics;
- max 12 visible columns;
- full mart is not generated by default;
- answer includes QA note and limitations;
- result is decision-readable.
## Smoke QA output
```text
smoke_qa_status: pass/fail/blocked
failed_questions:
residual_risks:
next_step:
```
Smoke QA is not production readiness.
