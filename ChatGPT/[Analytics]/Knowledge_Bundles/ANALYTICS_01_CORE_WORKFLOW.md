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

| File | Purpose | Use when |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Главные инструкции проекта | Всегда; вставить в Project Instructions |
| `ANALYTICS_PROJECT_FILES_INDEX.md` | Индекс пакета | Нужно понять, какой файл использовать |
| `ANALYTICS_WORKFLOW.md` | End-to-end workflow | Любая аналитическая задача |
| `IN_PROJECT_ANALYSIS_MODE.md` | Правило “анализ внутри проекта” | Есть риск преждевременного handoff |
| `MAIN_FILES_STANDARD.md` | Стандарт главных stage/mart файлов | Любые данные, marts, slices, BI/Excel |
| `DATA_CONTRACTS.md` | Data contract | Перед расчётами и marts |
| `MARTS_DESIGN.md` | Проектирование marts | Нужны метрики, витрины, cuts, dashboard |
| `ANALYTICAL_TECHNIQUES.md` | Методы анализа | Нужно выбрать variance/driver/bridge/etc. |
| `CHART_SELECTION_STANDARD.md` | Подбор графиков | Нужны графики из mart |
| `MEMO_PIPELINE.md` | Превращение анализа в memo | Нужна аналитическая записка |
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
| `CHANGELOG.md` | История изменений | После обновлений |

## Priority rules

1. Для аналитических задач сначала используй `ANALYTICS_WORKFLOW.md`, `IN_PROJECT_ANALYSIS_MODE.md`, `MAIN_FILES_STANDARD.md`.
2. Для данных и расчётов используй `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`, `ANALYTICAL_TECHNIQUES.md`.
3. Для memo/report используй `MEMO_PIPELINE.md`, `ANALYTICAL_MEMO_STRUCTURE.md`, `WORD_REPORT_STANDARD.md`, `TEXT_QA_AND_STYLE.md`.
4. Для QA используй `QA_CHECKLIST.md` и `ACCEPTANCE_CRITERIA.md`.
5. Для передачи в Codex используй `CODEX_TASK_PACKETS.md` и `ROUTING_AND_HANDOFF.md`.

## Non-negotiable rule

Не превращай `[Analytics]` в проект, который только выдаёт ТЗ. Он должен сам проводить анализ, если у него есть данные/контекст и задача не требует implementation.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_WORKFLOW.md`

# Analytics Workflow

## Purpose

Давать проверяемый аналитический результат: расчёт, data contract, stage, mart, analysis, charts, memo, QA или handoff.

## Step 0 — Output mode and artifact budget

```text
mode: quick / standard / full / autoloop_analysis
requested_output:
max_visible_metrics:
max_visible_columns:
max_sheets:
must_create_files: yes/no
evidence_depth: light / normal / full
```

If mode = `quick`, collapse to: question → minimal inputs → grain / period / filters → calculation or reasoning → compact result → QA note → limitation.

Do not run full RAW/STAGE/MART/slices/charts/report workflow unless required by the task.

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
→ LLM context package
→ memo / report
→ judge / QA
→ revise or rerun
→ acceptance
→ next run trigger
```

## `autoloop_analysis`

`autoloop_analysis` is a supervised analytical loop, not an autonomous agent. Backward-compatible alias: `autoloop`.

Rules:

- deterministic calculations first;
- judge/QA before final memo;
- revise or rerun only from visible QA findings;
- stop on blockers, missing data contract, failed DQ, unclear grain, or no validation path;
- do not add autonomous retrieval, vector DB, embeddings, semantic search, web UI, logs, journals, or runtime artifacts.

## Workflow steps

1. Question / scope: business question, decision context, audience, period, grain, metrics, filters, owner, expected output.
2. Inputs: available files, missing files, compact/full JSON, source systems, refresh date, required joins, directories/mappings, limitations.
3. Data contract: no calculation without grain; no memo without method; no mart without expected output.
4. RAW: original input only; no business logic, classifications, interpretations, or memo conclusions.
5. `stage_main_full`: cleaned, normalized, typed, identity/mapping joins only, no metrics/classifiers.
6. `mart_main_full`: complete analysis-ready table with metrics, formulas, flags, risk/confidence, QA and evidence fields.
7. `mart_main_tz` / compact: shortened mart for task, audience or executive memo.
8. Slices: derive all slices from `mart_main_full`.
9. Analysis: variance, driver, bridge, cohort, anomaly, reconciliation, segmentation, trend.
10. Charts: source from `mart_main_full` or a documented derived slice.
11. Memo: use verified analysis, not raw assumptions.
12. QA and acceptance: run QA before final conclusion.

## Default output

```text
Question / scope:
Data status:
Grain / period / filters:
Method:
Findings:
QA:
Limitations:
Decision / recommendation:
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

## Routing boundaries

Передавать в Codex только если нужно изменить файлы репозитория, написать Python/SQL/DAX/Power Query, создать тесты, автоматизировать pipeline, сгенерировать DOCX/PDF/PPTX программно, построить production-ready ETL, изменить структуру пакета документов или выполнить diff/release/rollback.

Передавать в LLM только если нужны prompt library, model routing, LLM evaluation, orchestration, generation workflow, or long-form narrative polish after verified numbers.

Передавать в Thinking только если нужно стратегическое решение, сценарий, decision memo, trade-off analysis or risk appetite.

Передавать в AI OS только если нужны AI pattern, AI governance, evidence/confidence по AI-концепции, новые модели/tools/use cases.

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

Correct flow:

```text
RAW
→ stage_main_full
→ mart_main_full
→ mart_main_tz / mart_main_compact
→ slices from mart_main_full
→ charts / memo / dashboard / Excel
```

Wrong flow:

```text
raw slice
→ mini mart
→ isolated conclusion
```

## Stage main file

`stage_main_full` is the cleaned, normalized and typed data array without business metrics or analytical classifiers.

Contains source metadata, period, date fields, entity keys, normalized dimensions, mapped IDs, currency/unit, technical lineage and row status for technical issues.

Does not contain business metrics, classification labels, materiality flags, risk labels, confidence labels, interpretation, memo text, or management conclusions.

## Mart main files

Required:

```text
mart_main_full
mart_main_tz
```

or

```text
mart_main_full
mart_main_compact
```

`mart_main_full` is the full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence. It contains metrics, formulas, dimensions, grain/keys, classification/materiality/variance/driver/timing/risk/confidence/action/QA/evidence/source lineage fields.

`mart_main_tz` / `mart_main_compact` is a shortened management-ready mart for the task, audience or executive memo. It does not replace `mart_main_full`.

## User-facing compact-first rule

For `quick` and `standard` tasks:

- show compact result first;
- keep full mart as evidence/reuse/design layer;
- do not expose all QA, lineage, risk, confidence and technical fields in the main view;
- if full mart exists, provide a compact front sheet with the top findings.

A correct analytical result can be compact if key numbers are traceable, formulas are documented, limitations are visible, and full evidence can be produced if requested.

Rule: full mart is evidence layer, not default user interface.

## Slice rule

All slices must be derived from `mart_main_full` and state source, filter logic, grain, metrics, purpose, and use.

## Compact/full JSON input logic

When compact and full are both provided: compact defines executive requirements and short output; full defines full data/method/evidence requirements.

When only compact is provided: define a minimal data contract, required main files, missing fields, unsupported claims and assumptions register.

## Naming convention

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
- [ ] Slices are derived from `mart_main_full`.
- [ ] Charts and memo reference mart/slice source.
- [ ] QA totals available.
- [ ] Limitations recorded.
