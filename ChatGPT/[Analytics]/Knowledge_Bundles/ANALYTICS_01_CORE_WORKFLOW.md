# [Analytics] — Core Workflow

## Purpose

Compact upload artifact for [Analytics] covering core workflow.

## Source files

- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`
- `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`
- `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_PROJECT_FILES_INDEX.md`

# Analytics Project Files Index
## Core files
| `IN_PROJECT_ANALYSIS_MODE.md` | Правило “анализ внутри проекта” | Есть риск преждевременного handoff |
| `TEXT_QA_AND_STYLE.md` | Редактура и стиль | Нужно отладить текст и оформление |
| `QA_CHECKLIST.md` | Data/calculation/memo/doc QA | Перед публикацией результата |
| `ROUTING_AND_HANDOFF.md` | Routing | Нужно понять, куда передать задачу |
| `AI_OS_REFERENCE.md` | Связь с AI OS | Нужны AI evidence/patterns |
| `SMOKE_QA_FOR_ANALYTICS.md` | Проверка проекта | После загрузки пакета |
## Priority rules
1. Для аналитических задач сначала используй `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `MAIN_FILES_STANDARD.md`.
2. Для данных и расчётов используй `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`, `ANALYTICAL_TECHNIQUES.md`.
3. Для memo/report используй `MEMO_PIPELINE.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `WORD_REPORT_STANDARD.md`, `TEXT_QA_AND_STYLE.md`.
4. Для QA используй `QA_CHECKLIST.md` и `ACCEPTANCE_CRITERIA.md`.
5. Для передачи в Codex используй `CODEX_TASK_PACKETS.md` и `ROUTING_AND_HANDOFF.md`.
## Non-negotiable rule


## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`

# Analytics Workflow
## Purpose
Давать проверяемый аналитический результат: расчёт, data contract, stage, mart, analysis, charts, memo, QA или handoff.
## Canonical workflow
```text
Question
→ Inputs
→ Data contract
→ RAW
→ STAGE MAIN FULL
→ STAGE slices, if needed
→ MART MAIN FULL
→ MART MAIN TZ / COMPACT
→ MART slices from MART MAIN FULL
→ ANALYSIS
→ CHARTS
→ LLM context package, if needed
→ REPORT / MEMO / DOCX structure
→ QA
→ ACCEPTANCE
→ ARCHIVE / HANDOFF
```
## Step 1 — Question / scope
- business question;
- decision context;
- audience;
- period;
- grain;
- metrics;
- filters;
- owner;
- expected output.
## Step 2 — Inputs
- available files;
- missing files;
- compact/full JSON;
- source systems;
- refresh date;
- required joins;
- directories/mappings;
- known limitations.
## Step 3 — Data contract
## Step 4 — RAW
RAW is original input. Do not add business logic here.
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
- cleaned;
- normalized;
- typed;
- joined only where needed for identity/mapping;
- no metrics and no classifiers.
## Step 6 — MART MAIN FULL
- business metrics;
- metric formulas;
- classification flags;
- risk fields;
- confidence fields;
- QA fields;
- evidence references;
- output eligibility fields.
## Step 7 — MART MAIN TZ / COMPACT
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
- variance analysis;
- driver analysis;
- bridge analysis;
- cohort analysis;
- anomaly detection;
- reconciliation;
- segmentation;
- trend analysis.
## Step 10 — Charts
Charts must be sourced from `mart_main_full` or a documented slice derived from it.
## Step 11 — Memo
Important sentences must be backed by metric/table/mart/period/evidence or marked as interpretation.
## Step 12 — QA and acceptance
Run QA before final conclusion.
## Default output
- stage_main_full:
- mart_main_full:
- mart_main_tz / compact:
QA:


## From: `ChatGPT/[Analytics]/Knowledge/IN_PROJECT_ANALYSIS_MODE.md`

# In-Project Analysis Mode
## Purpose
## Default rule
```text
Если задача аналитическая — решай в [Analytics].
Если нужна реализация/код/автоматизация — готовь handoff в [Codex].
```
## Делать внутри `[Analytics]`
- определение бизнес-вопроса;
- выбор метрик;
- составление data contract;
- проектирование RAW/STAGE/MARTS;
- проектирование `stage_main_full`, `mart_main_full`, `mart_main_tz/compact`;
- расчёт вручную или с доступными инструментами, если данных достаточно;
- reconciliation logic;
- variance/driver/bridge/cohort/anomaly/trend analysis;
- подбор графиков;
- аналитические выводы;
- структура memo;
- таблицы выводов;
- QA checklist;
- acceptance status;
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
```text
Это нужно в Codex. Передайте туда.
```
```text
В [Analytics] фиксирую стандарт и аналитическую логику. В Codex передавать только реализацию изменений файлов и тесты.
```


## From: `ChatGPT/[Analytics]/Knowledge/MAIN_FILES_STANDARD.md`

# Main Files Standard
## Purpose
## Main principle
```text
Slices are secondary.
Main files are primary.
```
```text
RAW
→ stage_main_full
→ mart_main_full
→ mart_main_tz / mart_main_compact
→ slices from mart_main_full
→ charts / memo / dashboard / Excel
```
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
- row status for technical issues.
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
```text
mart_main_full
mart_main_compact
```
### `mart_main_full`
Purpose: full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence.
- all metrics required for analysis;
- all metric formulas documented;
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
- only decision-relevant fields;
- headline metrics;
- top deviations;
- materiality;
- risk summary;
- confidence;
- visible limitations;
- references back to `mart_main_full`.
## Slice rule
All slices must be derived from `mart_main_full`.
Each slice must state:
used_for: chart / memo / QA / dashboard / appendix
## Compact/full JSON input logic
### Both compact and full provided
json full → full data/method/evidence requirements
- full builds `stage_main_full` and `mart_main_full`;
- compact builds `mart_main_tz/compact` and memo focus.
### Only compact provided
- define minimal data contract;
- define required main files;
- mark missing fields;
- avoid unsupported claims;
- create assumptions register.
## Naming convention
## Acceptance criteria
- [ ] `stage_main_full` exists or is explicitly designed.
- [ ] `stage_main_full` has no metrics/classifiers.
- [ ] `mart_main_full` exists or is explicitly designed.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is explicitly designed.
- [ ] Mart metrics and formulas documented.
- [ ] Slices are derived from `mart_main_full`.
- [ ] Charts and memo reference mart/slice source.
- [ ] QA totals available.
- [ ] Limitations recorded.
