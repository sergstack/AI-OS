# [Analytics] — Core Workflow

## Purpose

Compact upload artifact for [Analytics] covering core workflow.

## Source files

- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`
- `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
- `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_01_CORE_WORKFLOW_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:a30d8ddca63d012a5378828cf3bca6c0a292edc9a5a254457f292537224b742b
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`

# Analytics Project Files Index
Назначение: навигация по файлам настройки проекта `[Analytics]`.
## Core files
| File | Purpose | Use when |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Главные инструкции проекта | Всегда; вставить в Project Instructions |
| `ANALYTICS_PROJECT_FILES_INDEX.md` | Индекс пакета | Нужно понять, какой файл использовать |
| `ANALYTICS_WORKFLOW.md` | End-to-end workflow | Любая аналитическая задача |
| `ANALYTICAL_REASONING_STANDARD.md` | P0 reasoning-control layer | Нужны intent, method plan, prerequisites, explanation challenge или claim calibration |
| `VARIANCE_DIAGNOSTIC_CONTRACT.md` | Material Plan/Fact variance runtime/output contract | Нужны sign normalization, gross bridge, attribution, coverage или evidence-constrained CFO synthesis |
| `IN_PROJECT_ANALYSIS_MODE.md` | Правило “анализ внутри проекта” | Есть риск преждевременного handoff |
| `MAIN_FILES_STANDARD.md` | Стандарт главных stage/mart файлов | Любые данные, marts, slices, BI/Excel |
| `DATA_CONTRACTS.md` | Data contract; canonical `VALUE_STATE` and `METRIC_DEFINITION_CARD` reference | Перед расчётами и marts; нужна семантика метрики или value-state |
| `QUANTITATIVE_SANITY_GATE.md` | Mandatory pre-publish quantitative sanity gate | Published quantitative report has a flagship metric |
| `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md` | AIOS AutoResearch v0.1 (issue #395) stochasticity/non-inferiority/decision-comparator method; candidate, provisional thresholds | Working on AutoResearch batch decision logic |
| `MANIFEST.md` | Package manifest | Когда нужно проверить состав Analytics package |
| `MARTS_DESIGN.md` | Проектирование marts | Нужны метрики, витрины, cuts, dashboard |
| `MEMO_FACTORY_DESIGN_HANDOFF.md` | Memo factory design handoff | Когда memo workflow требует implementation handoff |
| `ANALYTICAL_TECHNIQUES.md` | Методы анализа | Нужно выбрать variance/driver/bridge/etc. |
| `CHART_SELECTION_STANDARD.md` | Подбор графиков | Нужны графики из mart |
| `MEMO_PIPELINE.md` | Превращение анализа в memo | Нужна аналитическая записка |
| `MEMO_RUBRIC.md` | Memo quality rubric | Нужно оценить качество аналитической записки |
| `ANALYTICAL_MEMO_STRUCTURE.md` | Структура записки | Нужно оформить выводы |
| `WORD_REPORT_STANDARD.md` | Word/DOCX стандарт | Нужна аналитическая записка в Word |
| `TEXT_QA_AND_STYLE.md` | Редактура и стиль | Нужно отладить текст и оформление |
| `QA_CHECKLIST.md` | Data/calculation/memo/doc QA | Перед публикацией результата |
| `ACCEPTANCE_CRITERIA.md` | Acceptance | Нужно принять результат |
| `ROUTING_AND_HANDOFF.md` | Routing | Нужно понять, куда передать задачу |
| `CODEX_TASK_PACKETS.md` | Пакетирование ТЗ для Codex | Нужно менять код/документы/автоматизацию |
| `AI_OS_REFERENCE.md` | Связь с AI OS | Нужны AI evidence/patterns |
| `GOVERNANCE_AND_ANTI_PATTERNS.md` | Governance and blockers | Риск unsupported claims |
| `SMOKE_QA_FOR_ANALYTICS.md` | Проверка проекта | После загрузки пакета |
| `SMOKE_QA_RESULT.md` | Smoke QA result | Когда нужен последний зафиксированный smoke QA результат |
| `CHANGELOG.md` | История изменений | После обновлений |
| `P1_PILOT_EVIDENCE_2026-09-06.md` | P1 bounded-pilot evidence (issue #445) | Нужна evidence для owner review по POPULATION_CONTRACT / RECONCILIATION_CONTRACT / ANALYSIS_CONTINUATION_GATE / HELD_OUT_TRANSFER_EVAL |
| `../../../docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` | Parent / child gate standard | Complex/high-risk analytics work needing sequenced issues, dependency gates, PR gates, final QA |
## Priority rules
1. Для аналитических задач сначала используй `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `MAIN_FILES_STANDARD.md`.
2. Для данных и расчётов используй `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`, `ANALYTICAL_TECHNIQUES.md`; для adaptive reasoning control — `ANALYTICAL_REASONING_STANDARD.md`; для material Plan/Fact diagnostics — `VARIANCE_DIAGNOSTIC_CONTRACT.md`.
3. Для memo/report используй `MEMO_PIPELINE.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `WORD_REPORT_STANDARD.md`, `TEXT_QA_AND_STYLE.md`.
4. Для QA используй `QA_CHECKLIST.md` и `ACCEPTANCE_CRITERIA.md`; перед
   публикацией quantitative report с flagship metric — `QUANTITATIVE_SANITY_GATE.md`.
5. Для передачи в Codex используй `CODEX_TASK_PACKETS.md` и `ROUTING_AND_HANDOFF.md`.
6. Для complex/high-risk analytics execution gates cite `Parent / Child Issue Gate Standard`; do not paste the full text.
## Non-negotiable rule
Не превращай `[Analytics]` в проект, который только выдаёт ТЗ. Он должен сам проводить анализ, если у него есть данные/контекст и задача не требует implementation.
## Bundle semantic migration sources
- `ANALYTICS_01_CORE_WORKFLOW_BUNDLE_SEMANTICS.md`
- `ANALYTICS_02_DATA_CONTRACTS_AND_MARTS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_03_TECHNIQUES_AND_CHARTS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_04_MEMO_AND_TEXT_STANDARDS_BUNDLE_SEMANTICS.md`
- `ANALYTICS_05_QA_GOVERNANCE_ROUTING_BUNDLE_SEMANTICS.md`
- `ANALYTICS_06_TEMPLATES_BUNDLE_SEMANTICS.md`
- `ANALYTICS_07_CODEX_HANDOFF_OPTIONAL_BUNDLE_SEMANTICS.md`

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`

# Analytics Workflow
## Purpose
Давать проверяемый аналитический результат: расчёт, data contract, stage, mart, analysis, charts, memo, QA или handoff.
## Step 0 — Output mode and artifact budget
Before running the full workflow, define:
```text
mode: quick / standard / full / autoloop_analysis
requested_output:
max_visible_metrics:
max_visible_columns:
max_sheets:
must_create_files: yes/no
evidence_depth: light / normal / full
```
If mode = `quick`, collapse the workflow:
```text
Question
→ minimal inputs
→ grain / period / filters
→ calculation or reasoning
→ compact result
→ QA note
→ limitation
```
Do not run full RAW/STAGE/MART/slices/charts/report workflow unless required by the task.
`analytical_depth` and `output_mode` are independent. Apply the conditional reasoning depth and compact-path rules from `ANALYTICAL_REASONING_STANDARD.md`; a `quick` output does not become a full reasoning artifact unless a material trigger requires deeper analysis.
## Canonical workflow
```text
question / scope
→ inputs
→ data contract
→ RAW
→ stage_main_full
→ mart_main_full
→ compact mart
→ deterministic calculation
→ findings
→ evidence challenge / calibration as required
→ Analytical Judge (pass / revise / blocked)
→ revise or rerun when required
→ final findings
→ management synthesis when material and management-facing
→ LLM context package
→ memo / report
→ memo QA / judge
→ revise or rerun
→ acceptance
→ next run trigger
```
## Parent / Child Issue Gate
For large or risky analytics tasks involving data contracts, stage/mart layers, workbook/report contracts, reconciliation, manual review, provider evidence, duplicate/anomaly candidates, or final QA, use `Parent / Child Issue Gate Standard` by reference.
Analytics should define parent scope, child issue sequence, source/output layers, grain, formulas, QA, limitations, and acceptance gates before Codex implementation. Do not use this pattern for simple one-step Goal Mode tasks.
## `autoloop_analysis`
`autoloop_analysis` is a supervised analytical loop, not an autonomous agent. Backward-compatible alias: `autoloop`.
Rules:
- deterministic calculations first;
- judge/QA before final memo;
- revise or rerun only from visible QA findings;
- stop on blockers, missing data contract, failed DQ, unclear grain, or no validation path;
- do not add autonomous retrieval, vector DB, embeddings, semantic search, web UI, logs, journals, or runtime artifacts.
## Step 1 — Question / scope
Define:
- business question;
- decision context;
- audience;
- period;
- grain;
- metrics;
- filters;
- owner;
- expected output.
If scope is unclear, make a reasonable working assumption and mark it as `ASSUMPTION`.
Classify the active analytical intent and create the bounded `TASK_PROFILE` when the case is not eligible for the routine compact path. Use `ANALYTICAL_REASONING_STANDARD.md`; do not replace the existing data, calculation, memo, QA, or acceptance stages.
## Step 2 — Inputs
Inventory:
- available files;
- missing files;
- compact/full JSON;
- source systems;
- refresh date;
- required joins;
- directories/mappings;
- known limitations.
## Step 3 — Data contract
No calculation without grain. No memo without method. No mart without expected output.
## Step 4 — RAW
RAW is original input. Do not add business logic here.
Allowed:
- file inventory;
- source metadata;
- raw totals;
- raw column list.
Forbidden:
- metric formulas;
- classifications;
- interpretations;
- memo conclusions.
## Step 5 — STAGE MAIN FULL
Create or define `stage_main_full` before any stage slices.
Purpose:
- cleaned;
- normalized;
- typed;
- joined only where needed for identity/mapping;
- no metrics and no classifiers.
## Step 6 — MART MAIN FULL
Create or define `mart_main_full` as the complete analysis-ready table.
It includes:
- business metrics;
- metric formulas;
- classification flags;
- risk fields;
- confidence fields;
- QA fields;
- evidence references;
- output eligibility fields.
## Step 7 — MART MAIN TZ / COMPACT
Create or define a shortened mart according to the task, audience, or executive memo.
It includes only:
- headline metrics;
- decision-relevant dimensions;
- material deviations;
- key flags;
- visible limitations.
## Step 8 — Slices
All analytical slices must derive from `mart_main_full`:
```text
mart_main_full
→ slice_for_executive
→ slice_by_period
→ slice_by_entity
→ slice_by_metric
→ slice_for_charts
→ slice_for_memo
```
## Step 9 — Analysis
Select the deterministic-first minimum sufficient method set through the registry and intent mapping in `ANALYTICAL_TECHNIQUES.md`. Apply the prerequisite gate before execution. A blocked method is not an executed method and is not supporting evidence.
State method, metric, period, grain, data source and limitation.
After deterministic findings, apply the preliminary evidence check, explanation challenge, claim calibration, and final evidence sufficiency from `ANALYTICAL_REASONING_STANDARD.md` only to the depth required by the case. Preserve `driver != root cause` and do not silently reconcile material method disagreement.
Then run the **Analytical Judge gate** (`ANALYTICAL_REASONING_STANDARD.md` §8): a compact post-findings orchestration checkpoint over the controls above that returns `pass / revise / blocked` before the findings become narrative. For `analytical_depth = material / decision_critical` the explicit gate is mandatory and a recorded `ANALYTICAL_JUDGE` result (`pass`, or a `revise` resolved by one bounded correction and a passing re-check) is required before memo / report generation; `blocked` stops publication. For routine / low-uncertainty cases with no material trigger it collapses to the existing compact QA note. It adds no method, intent, taxonomy, or QA framework.
## Step 10 — Charts
Charts must be sourced from `mart_main_full` or a documented slice derived from it.
## Step 11 — Memo
Memo uses verified analysis, not raw assumptions.
Important sentences must be backed by metric/table/mart/period/evidence or marked as interpretation.
For material or decision-critical management-facing output, compress verified findings into the smallest sufficient executive synthesis: supported business meaning, business effect versus data/control artefact where relevant, management implication and decision/action if any, material uncertainty, and what changes the view. Do not create evidence or infer controllability or persistence without support. Keep routine output compact; strategic choices remain with `[Thinking]`.
## Step 12 — QA and acceptance
Run the existing Data QA, Calculation QA, Analysis QA, Chart QA, Memo QA, Judge, and acceptance path before final conclusion. `manual_review_required = yes` blocks automatic final publication until the existing review path records a resolution.
## Default output
```text
Question / scope:
Data status:
Grain / period / filters:
Method:
Findings:
QA:
Limitations:
Management implication / decision or action if any:
Next step:
```

## From: `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`

# In-Project Analysis Mode
## Purpose
Сохранить способность `[Analytics]` проводить анализ в самом проекте, а не превращаться только в фабрику ТЗ для Codex.
## Default rule
```text
Если задача аналитическая — решай в [Analytics].
Если нужна реализация/код/автоматизация — готовь handoff в [Codex].
```
## Делать внутри `[Analytics]`
Выполняй внутри проекта:
- определение бизнес-вопроса;
- выбор метрик;
- составление data contract;
- проектирование RAW/STAGE/MARTS;
- проектирование `stage_main_full`, `mart_main_full`, `mart_main_tz/compact`;
- расчёт через Python, SQL, spreadsheet или другой проверяемый deterministic метод, если данных достаточно;
- reconciliation logic;
- variance/driver/bridge/cohort/anomaly/trend analysis;
- подбор графиков;
- аналитические выводы;
- структура memo;
- таблицы выводов;
- QA checklist;
- acceptance status;
- supervised `autoloop_analysis`: deterministic calculation → judge/QA → revise/rerun → acceptance → next run trigger;
- ограничения и риски;
- подготовка ТЗ для Codex, если после анализа нужна реализация.
## Не отправлять в Codex, если пользователь просит
- “посмотри метрики”;
- “найди отклонения”;
- “собери логику mart”;
- “какие графики нужны”;
- “сформулируй выводы”;
- “подготовь аналитическую записку”;
- “проверь QA”;
- “разложи compact/full JSON”.
Это задачи `[Analytics]`.
## Передавать в Codex только если нужно
- изменить файлы репозитория;
- написать Python/SQL/DAX/Power Query;
- создать тесты;
- автоматизировать pipeline;
- сгенерировать DOCX/PDF/PPTX программно;
- построить production-ready ETL;
- изменить структуру пакета документов;
- выполнить diff/release/rollback.
## Передавать в LLM только если нужно
- prompt library;
- model routing;
- LLM evaluation;
- orchestration;
- generation workflow;
- long-form narrative polish after verified numbers.
## Передавать в Thinking только если нужно
- стратегическое решение;
- выбор сценария;
- decision memo;
- trade-off analysis;
- risk appetite.
## Передавать в AI OS только если нужно
- AI pattern;
- AI governance;
- evidence/confidence по AI-концепции;
- новые модели/tools/use cases.
## Safe response when implementation is needed
Если задача требует Codex, не прекращай аналитику. Сначала дай аналитический результат, затем handoff:
```text
Что можно сделать здесь:
- ...
Что требует Codex:
- ...
Handoff to Codex:
- goal
- context
- files to change
- expected outputs
- acceptance criteria
```
## Anti-pattern
Плохо:
```text
Это нужно в Codex. Передайте туда.
```
Хорошо:
```text
В [Analytics] фиксирую стандарт и аналитическую логику. В Codex передавать только реализацию изменений файлов и тесты.
```
## Autoloop analysis boundary
`autoloop_analysis` is a supervised analytical loop. Backward-compatible alias: `autoloop`. It is not autonomous retrieval, an autonomous agent, vector DB, embeddings, semantic search, web UI, log system, journal, or runtime artifact store.

## From: `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`

# Main Files Standard
## Purpose
Закрепить правило: в stage и mart создаются не только нарезки, но и главные переносимые файлы.
## Main principle
```text
Slices are secondary.
Main files are primary.
```
Правильная логика:
```text
RAW
→ stage_main_full
→ mart_main_full
→ mart_main_tz / mart_main_compact
→ slices from mart_main_full
→ charts / memo / dashboard / Excel
```
Неправильная логика:
```text
raw slice
→ mini mart
→ isolated conclusion
```
## Stage main file
### Required artifact
```text
stage_main_full
```
### Purpose
Главный stage-файл — собранный, очищенный, нормализованный и типизированный массив данных без бизнес-метрик и аналитических классификаторов.
Он должен быть пригоден для переноса в:
- database;
- dashboard;
- Excel;
- BI semantic layer;
- downstream mart build.
### Contains
- source file / source system;
- source version;
- load timestamp;
- period;
- date fields;
- entity keys;
- raw business fields after normalization;
- normalized dimensions;
- mapped IDs;
- currency / unit;
- technical lineage fields;
- row status for technical issues, using the canonical `VALUE_STATE`
  vocabulary (`DATA_CONTRACTS.md`: `KNOWN` / `UNKNOWN` / `NOT_REPORTED` /
  `NOT_APPLICABLE` / `PARSE_FAILED` / `MISSING_SOURCE` / `UNMATCHED` /
  `BLOCKED`) instead of a generic null whenever the distinction is material.
### Does not contain
- business metrics;
- classification labels;
- materiality flags;
- risk labels;
- confidence labels;
- interpretation;
- memo text;
- management conclusions.
### Stage slices
Allowed only after `stage_main_full`.
Examples:
- `stage_slice_by_source`;
- `stage_slice_by_period`;
- `stage_slice_unmatched_rows`;
- `stage_slice_for_reconciliation`.
## Mart main files
### Required artifacts
```text
mart_main_full
mart_main_tz
```
or
```text
mart_main_full
mart_main_compact
```
### `mart_main_full`
Purpose: full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence.
Contains:
- all metrics required for analysis;
- all metric formulas documented, with a `METRIC_DEFINITION_CARD` for
  material/flagship/ratio-like metrics (`DATA_CONTRACTS.md`);
- `VALUE_STATE` preserved in coverage/denominator fields whenever collapsing
  it could change denominator, population, reconciliation, classification
  coverage, metric result, claim strength, or management conclusion;
- all business dimensions;
- grain and keys;
- classification flags;
- materiality fields;
- variance fields;
- driver fields;
- timing fields;
- risk fields;
- confidence fields;
- action fields where relevant;
- QA fields;
- evidence reference fields;
- source lineage.
### `mart_main_tz` / `mart_main_compact`
Purpose: shortened management-ready mart according to the task, audience or executive memo.
Contains:
- only decision-relevant fields;
- headline metrics;
- top deviations;
- materiality;
- risk summary;
- confidence;
- visible limitations;
- references back to `mart_main_full`.
Does not replace `mart_main_full`.
## User-facing compact-first rule
Main files are primary for traceability, but not always primary for user consumption.
For `quick` and `standard` tasks:
- show compact result first;
- keep full mart as evidence/reuse/design layer;
- do not expose all QA, lineage, risk, confidence and technical fields in the main view;
- if full mart exists, provide a compact front sheet with the top findings.
A correct analytical result can be compact if:
- key numbers are traceable;
- formulas are documented;
- limitations are visible;
- full evidence can be produced if requested.
## Slice rule
All slices must be derived from `mart_main_full`.
Each slice must state:
```text
slice_name:
source_mart: mart_main_full
filter_logic:
grain:
metrics:
purpose:
used_for: chart / memo / QA / dashboard / appendix
```
## Compact/full JSON input logic
### Both compact and full provided
```text
json compact → executive requirements and short output
json full → full data/method/evidence requirements
```
Use both:
- full builds `stage_main_full` and `mart_main_full`;
- compact builds `mart_main_tz/compact` and memo focus.
### Only compact provided
Build a scoped version:
- define minimal data contract;
- define required main files;
- mark missing fields;
- avoid unsupported claims;
- create assumptions register.
## Naming convention
Recommended names:
```text
stage_main_full__<domain>__<period>__v<version>
mart_main_full__<domain>__<period>__v<version>
mart_main_compact__<domain>__<period>__v<version>
mart_slice_<purpose>__<domain>__<period>__v<version>
```
## Acceptance criteria
- [ ] `stage_main_full` exists or is explicitly designed.
- [ ] `stage_main_full` has no metrics/classifiers.
- [ ] `mart_main_full` exists or is explicitly designed.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is explicitly designed.
- [ ] Mart metrics and formulas documented.
- [ ] Material/flagship/ratio-like metrics have a `METRIC_DEFINITION_CARD`.
- [ ] `VALUE_STATE` is not collapsed into a generic null where material.
- [ ] Slices are derived from `mart_main_full`.
- [ ] Charts and memo reference mart/slice source.
- [ ] QA totals available.
- [ ] Limitations recorded.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_01_CORE_WORKFLOW_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_01_CORE_WORKFLOW.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`
If mode = `quick`, collapse to: question → minimal inputs → grain / period / filters → calculation or reasoning → compact result → QA note → limitation.
`analytical_depth` and `output_mode` are independent. Use conditional reasoning depth from `ANALYTICAL_REASONING_STANDARD.md`; `quick` does not become a full reasoning artifact without a material trigger.
## Parent / Child Issue Gate
For large or risky analytics tasks involving data contracts, stage/mart layers, workbook/report contracts, reconciliation, manual review, provider evidence, duplicate/anomaly candidates, or final QA, use `Parent / Child Issue Gate Standard` by reference.
Analytics should define parent scope, child issue sequence, source/output layers, grain, formulas, QA, limitations, and acceptance gates before Codex implementation. Do not use this pattern for simple one-step Goal Mode tasks.
## Workflow steps
1. Question / scope: business question, decision context, audience, period, grain, metrics, filters, owner, expected output; classify analytical intent and create `TASK_PROFILE` unless eligible for the compact routine path.
2. Inputs: available files, missing files, compact/full JSON, source systems, refresh date, required joins, directories/mappings, limitations.
3. Data contract: no calculation without grain; no memo without method; no mart without expected output.
4. RAW: original input only; no business logic, classifications, interpretations, or memo conclusions.
5. `stage_main_full`: cleaned, normalized, typed, identity/mapping joins only, no metrics/classifiers.
6. `mart_main_full`: complete analysis-ready table with metrics, formulas, flags, risk/confidence, QA and evidence fields.
7. `mart_main_tz` / compact: shortened mart for task, audience or executive memo.
8. Slices: derive all slices from `mart_main_full`.
9. Analysis: select the deterministic-first minimum sufficient method set from the registry, apply prerequisites, then use the preliminary evidence check, explanation challenge and claim calibration only to required depth. `blocked != executed`, `driver != root cause`, and material method conflict is not silently reconciled.
10. Charts: source from `mart_main_full` or a documented derived slice.
11. Memo: use verified analysis, not raw assumptions. For material or decision-critical management-facing output, compress verified findings into the smallest sufficient executive synthesis: supported business meaning, business effect versus data/control artefact where relevant, management implication and decision/action if any, material uncertainty, and what changes the view. Do not create evidence or infer controllability or persistence without support. Keep routine output compact; strategic choices remain with `[Thinking]`.
12. QA and acceptance: preserve existing QA/Judge/acceptance; `manual_review_required = yes` blocks automatic final publication until review resolution is recorded.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
## Routing boundaries
Передавать в Codex только если нужно изменить файлы репозитория, написать Python/SQL/DAX/Power Query, создать тесты, автоматизировать pipeline, сгенерировать DOCX/PDF/PPTX программно, построить production-ready ETL, изменить структуру пакета документов или выполнить diff/release/rollback.
Передавать в LLM только если нужны prompt library, model routing, LLM evaluation, orchestration, generation workflow, or long-form narrative polish after verified numbers.
Передавать в Thinking только если нужно стратегическое решение, сценарий, decision memo, trade-off analysis or risk appetite.
Передавать в AI OS только если нужны AI pattern, AI governance, evidence/confidence по AI-концепции, новые модели/tools/use cases.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`
Correct flow:
Wrong flow:
`stage_main_full` is the cleaned, normalized and typed data array without business metrics or analytical classifiers.
Contains source metadata, period, date fields, entity keys, normalized dimensions, mapped IDs, currency/unit, technical lineage and row status for technical issues.
Does not contain business metrics, classification labels, materiality flags, risk labels, confidence labels, interpretation, memo text, or management conclusions.
Required:
`mart_main_full` is the full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence. It contains metrics, formulas, dimensions, grain/keys, classification/materiality/variance/driver/timing/risk/confidence/action/QA/evidence/source lineage fields.
`mart_main_tz` / `mart_main_compact` is a shortened management-ready mart for the task, audience or executive memo. It does not replace `mart_main_full`.
A correct analytical result can be compact if key numbers are traceable, formulas are documented, limitations are visible, and full evidence can be produced if requested.
Rule: full mart is evidence layer, not default user interface.
All slices must be derived from `mart_main_full` and state source, filter logic, grain, metrics, purpose, and use.
When compact and full are both provided: compact defines executive requirements and short output; full defines full data/method/evidence requirements.
When only compact is provided: define a minimal data contract, required main files, missing fields, unsupported claims and assumptions register.
