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
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:98a3567ea7b03958a9a15d41d7b0c4fe5e9d5df32aab99d81961348c4a35c112
- generator: scripts/build_knowledge_bundles.py

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
- [ ] `method_selection_adequate?`
- [ ] `material_method_omitted?`
- [ ] `unnecessary_method_bloat?`
- [ ] `registry_mapping_followed?`
- [ ] `deterministic_trigger_applied?`
- [ ] `trigger_contract_defined?`
- [ ] `trigger_priority_followed?`
- [ ] `trigger_evidence_sufficient?`
- [ ] `llm_silent_override_detected?`
- [ ] `selected_method_prerequisites_met?`
- [ ] `reasoning_used_for_deterministic_claim?`
- [ ] `claim_method_lineage_complete?`
- [ ] `claim_references_executed_method?`
- [ ] `baseline_explicit?`
- [ ] `baseline_robustness_required?`
- [ ] `population_constant_or_explained?`
- [ ] `denominator_constant_or_explained?`
- [ ] `scope_change_quantified?`
- [ ] `preliminary_evidence_sufficient_to_continue?`
- [ ] `alternative_explanation_considered?`
- [ ] `contradicting_evidence_checked?`
- [ ] `discriminating_evidence_defined?`
- [ ] `falsification_test_defined_if_material?`
- [ ] `material_method_disagreement_resolved_or_visible?`
- [ ] `unresolved_method_conflict_reflected_in_claim_strength?`
- [ ] `claim_support_correct?`
- [ ] `causal_status_correct?`
- [ ] `confidence_confused_with_causality?`
- [ ] `manual_review_required_assessed?` If `yes`, reviewer/owner, status, and resolution are recorded before final publication.
- [ ] `final_evidence_sufficient_for_claim?`
- [ ] `conclusion_stronger_than_evidence?`
- [ ] `stop_condition_assessed?`
- [ ] `thinking_escalation_required?`
- [ ] `routine_collapse_applied_when_eligible?`
- [ ] `unnecessary_full_reasoning_record_created?`
- [ ] `exception_vs_anomaly_distinguished?`
- [ ] `unmatched_analysis_used_when_population_mismatch_material?`
- [ ] `factor_decomposition_reconciled_when_applicable?`
- [ ] `timing_cutoff_checked_when_material?`
- [ ] `data_layer_artifact_considered_when_material?`
- [ ] `leading_indicator_relationship_supported?`
- [ ] `leading_indicator_not_presented_as_causal_without_evidence?`
- [ ] `new_method_trigger_contract_followed?`
- [ ] `new_method_prerequisites_met?`
- [ ] `new_method_added_only_if_distinct_capability?`
- [ ] `aes_execution_governance_preserved?`
- [ ] `analytics_extension_applied_without_duplication?`
- [ ] `reasoning_control_not_treated_as_autonomous_execution_loop?`
Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. These checks extend the existing Analysis QA; they do not create a separate QA framework.
### Material variance diagnostic QA
Apply `VARIANCE_DIAGNOSTIC_CONTRACT.md` only to material/decision-critical Plan/Fact cases or a material variance risk:
- [ ] Source/raw formula and sign convention remain distinct from normalized management direction; unresolved KPI direction blocks normalization.
- [ ] Gross adverse/favorable movement and normalized net variance reconcile using one normalized sign convention.
- [ ] Primary economic/timing/data-mapping/unresolved effects are non-overlapping, scope-complete, and reconciled; failed residual remains visible.
- [ ] Classification population, eligible gross movement, classified/unclassified movement, row counts, and coverage denominator are explicit and separate from net reconciliation.
- [ ] Materiality basis, denominator, selected/excluded population, and selection coverage are declared before narrative.
- [ ] Budget status, controllability, recurrence, and evidence status remain non-additive; unsupported controllability/recurrence remain `unknown`.
- [ ] Single-period evidence is not generalized as systemic/non-systemic; driver/ownership does not imply root cause or accountability.
- [ ] Reported result remains canonical; adjusted view reconciles separately with explicit adjustment polarity.
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
- workbook may be large, but must include:
  - README / index;
  - compact front sheet;
  - data dictionary;
  - field groups;
  - evidence appendix.
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
## Material Plan/Fact variance acceptance
For cases governed by `VARIANCE_DIAGNOSTIC_CONTRACT.md`:
- reported and normalized management views are both traceable and use explicit, non-mixed sign conventions;
- gross adverse/favorable movement, normalized net variance, and primary attribution reconcile deterministically;
- gross classification coverage declares population, denominator, classified/unclassified movement, and unknown rows separately from net reconciliation;
- materiality basis and selected/excluded population are explicit;
- controllability, recurrence, generalization, and accountability claims have required evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit adjustment polarity;
- management synthesis follows the contract semantically without expanding routine output.
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
## Analytical Memo Factory via Codex APP
If the user asks to create an analytical memo as an executable artifact, use:
```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```
Keep `[Analytics]` responsible for methodology, data contracts, assumptions, limitations, and acceptance criteria. `[Codex]` designs the task package; Codex APP executes locally.
Do not force an interactive loop where `[Analytics]` asks for Python outputs back and forth unless the user explicitly wants manual exploration.
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
Use when decision/scenario requires calculations.
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
Use when implementation is needed.
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
`[Analytics]` does not contain the full AI OS KB. `[AI OS]` already stores governed knowledge about AI concepts, tools, patterns, governance and use cases.
Use `[AI OS]` when needed:
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
- Method eligibility and triggers follow `ANALYTICAL_TECHNIQUES.md`; the LLM cannot silently override the registry.
- Reasoning cannot substitute for deterministic execution or missing prerequisites.
- Claim strength cannot exceed final evidence sufficiency.
- `AUTONOMOUS_EXECUTION_STANDARD.md` remains canonical execution governance; `ANALYTICS_EXTENSION.md` supplies domain-specific constraints without creating a second execution framework.
## Evidence labels
Use:
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
| Anti-pattern | Why bad | Correct action |
|---|---|---|
| Handoff to Codex too early | Analytics loses its role | Analyze first, handoff implementation only |
| Slices before main files | Inconsistent outputs | Build `stage_main_full`, then `mart_main_full`, then slices |
| Raw-to-memo | Unsupported conclusions | Use mart/evidence |
| LLM as calculation source | Non-deterministic truth | Calculate deterministically |
| Hidden business logic | Cannot audit | Document formulas/classifiers |
| Pretty memo before QA | Looks right, may be wrong | QA first |
| Low Confidence as fact | Misleading | Label hypothesis |
| Risk without basis | Decorative risk | Add `risk_basis` or remove |
| Action without owner/date | Not actionable | Add owner/due date/status |
## P0 analytical reasoning failure modes
Apply these controls through `ANALYTICAL_REASONING_STANDARD.md` and the existing Analysis QA; do not create a competing governance or QA framework.
| Failure mode | Required control |
|---|---|
| Driver presented as root cause; correlation presented as causation | Use the claim ladder, `claim_support`, `causal_status`, and causal evidence gate. |
| Premature explanation | Run the preliminary evidence check and stop when explanatory analysis is infeasible. |
| Baseline dependence | State baseline/rationale and run required baseline robustness for material cases. |
| Aggregation bias; selection/exclusion bias | Check materially relevant segmentation, exclusions, and subgroup robustness. |
| Population or denominator change | Explain population/denominator and quantify scope change before interpreting ratios. |
| Timing or cut-off effect | State cut-off and test timing/trend when the declared trigger is satisfied. |
| False precision | Constrain precision and claim strength to data quality and evidence sufficiency. |
| Silent exclusions | Record materially plausible excluded methods and data exclusions. |
| Narrative stronger than evidence | Enforce `claim strength <= final evidence sufficiency`. |
| Method bloat | Use the minimum sufficient method set and stop conditions. |
| Confidence mistaken for causality | Preserve `confidence != claim_support != causal_status`. |
| Numerical magnitude mistaken for business materiality | Assess decision context and materiality separately; do not use a numerical reasoning score. |
| Reasoning substituted for deterministic execution | Enforce `LLM reasoning != deterministic execution`. |
| LLM silently overrides method registry | Record candidate omission and route it to existing QA/review. |
| Subjective or undefined method trigger | Require `trigger_type`, `trigger_rule`, and `trigger_evidence_required`. |
| Blocked method treated as evidence | Enforce `blocked != executed` and reject blocked/planned/not-needed lineage. |
| Method execution lineage loss | Require unique `method_execution_id` and claim-to-evidence lineage. |
| Conflicting methods silently reconciled | Preserve conflicting results, record contradictory evidence, constrain claim strength, and escalate if material. |
| Full reasoning runtime applied to a routine case without trigger | Use the compact path and do not instantiate unused full reasoning records. |
| Anomaly mistaken for control exception | Distinguish unusual observations from explicit rule/control violations. |
| Aggregate reconciliation used instead of entity-level unmatched analysis | Use unmatched-elements analysis when concrete one-sided populations are material. |
| Driver decomposition accepted without factor reconciliation | Reconcile summed factor effects to observed delta whenever mathematically applicable. |
| Timing shift interpreted as economic effect | Run timing validation when cut-off or recognition timing could change interpretation. |
| Transformation artifact interpreted as source/business effect | Trace `REPORT → MART → STAGE → RAW` and identify the first verified layer where the effect appears. |
| Leading indicator treated as proven causal predictor | Use calibrated signal/association/risk language unless causal evidence exists. |
| Method catalog inflated by converting controls into methods | Require a distinct question, execution procedure, and material analytical effect before adding a method. |
| Decision methods leak from `[Thinking]` into `[Analytics]` | Keep trade-offs, reversibility, premortem, risk appetite, choice, and decision in `[Thinking]`. |
| Reasoning-control loop mistaken for an autonomous execution loop | Keep reasoning/method selection inside the AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries. |
## Metric / artifact explosion
Anti-pattern:
A short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.
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
Question:
```text
Мне нужно проанализировать отклонения план-факт и подготовить выводы. Ты будешь делать это здесь или отправишь в Codex?
```
Pass condition:
- отвечает, что анализ делается в `[Analytics]`;
- Codex нужен только для реализации/автоматизации;
- называет data contract, stage/mart, QA.
## 2. Main files
Question:
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
Question:
```text
На входе есть только json compact. Что ты сделаешь?
```
Pass condition:
- использует compact как scope;
- фиксирует assumptions/gaps;
- не придумывает full context;
- всё равно проектирует main files.
## 4. Charts
Question:
```text
Из чего строить графики для аналитической записки?
```
Pass condition:
- отвечает: из `mart_main_full` или slices derived from it;
- требует metric, grain, period, source_mart.
## 5. Memo
Question:
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
Question:
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
Question:
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
## 8. Short task / anti-bloat test
Question:
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
## 9. Missing-data compact fast path
Question:
```text
Покажи Top-3 отклонения план-факт и управленческий вывод. Данных, grain, периода и единиц нет. Не задавай лишних вопросов.
```
Pass condition:
- result is `NOT CALCULABLE`;
- no placeholder ranking or empty Top-N table;
- no invented example rows or values;
- minimum required input and one next action are explicit;
- confidence and the material blocker remain visible;
- the same blocker is not repeated across separate QA, limitation, and gate sections.
## Smoke QA output
```text
smoke_qa_status: pass/fail/blocked
failed_questions:
residual_risks:
next_step:
```
Smoke QA is not production readiness.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_05_QA_GOVERNANCE_ROUTING.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/QA_CHECKLIST.md`
- [ ] Method selection adequate; no material omission or method bloat.
- [ ] Registry mapping followed; deterministic trigger, trigger priority, and trigger contract/evidence checked; no silent LLM override.
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
- [ ] AES remains canonical execution governance; the Analytics extension is applied without duplication.
- [ ] Reasoning control is not treated as an autonomous execution or independent retry loop.
Use `ANALYTICAL_REASONING_STANDARD.md` for field semantics. This extends existing Analysis QA and creates no separate QA framework.
Use `VARIANCE_DIAGNOSTIC_CONTRACT.md` only for material/decision-critical Plan/Fact or material variance risk:
- [ ] Raw/source and normalized management signs are explicit/non-mixed; unresolved direction blocks normalization.
- [ ] Gross adverse/favorable and net reconcile; primary economic/timing/data-mapping/unresolved effects are non-overlapping and scope-complete.
- [ ] Coverage declares gross population/denominator, classified/unclassified movement and row counts separately from net reconciliation.
- [ ] Materiality basis, denominator, selected/excluded population, and selection coverage precede narrative.
- [ ] Secondary attributes are non-additive; unsupported controllability/recurrence remain unknown.
- [ ] Single-period evidence is not systemic/non-systemic; driver/owner does not imply root cause/accountability.
- [ ] Reported result remains canonical; adjusted view reconciles with explicit polarity.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md`
- workbook may be large, but must include README / index, compact front sheet, data dictionary, field groups and evidence appendix.
For `VARIANCE_DIAGNOSTIC_CONTRACT.md` cases:
- reported/raw and normalized views are traceable and signs are explicit/non-mixed;
- gross/net bridge and primary attribution reconcile deterministically;
- gross coverage declares population, denominator, classified/unclassified movement and unknown rows separately;
- materiality basis/population are explicit;
- controllability, recurrence, generalization, and accountability have evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit polarity;
- management synthesis follows the semantic contract without expanding routine output.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/GOVERNANCE_AND_ANTI_PATTERNS.md`
- Registry and trigger contracts govern method eligibility; no silent LLM override.
- Reasoning cannot replace deterministic execution or missing prerequisites.
- AES remains canonical execution governance; the Analytics extension adds domain constraints without creating a second execution framework.
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
- Reasoning-control loop mistaken for autonomous execution → keep it inside AES-governed scope, checks, bounded correction, stop, rollback, acceptance, and authority boundaries.
## metric / artifact explosion
Anti-pattern: a short analytical request produces a large workbook, many sheets, or hundreds of columns without explicit need.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/SMOKE_QA_FOR_ANALYTICS.md`
## 8. short task / anti-bloat test
