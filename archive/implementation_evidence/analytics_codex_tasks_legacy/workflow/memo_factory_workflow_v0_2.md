# Workflow v0.2 — полная фабрика аналитических записок

## Назначение

Цель: построить не одну записку и не MVP, а полноценную фабрику аналитических записок, где данные проходят путь:

```text
RAW → STAGE → FINANCE MART → ANALYSIS OVERLAYS → EVIDENCE → MEMO PACKAGES → DOCX/MD/XLSX → QA → RELEASE
```

Ключевой принцип: не перегружать один mart всем подряд. Финансовые расчёты, аналитические интерпретации, evidence, actions и тексты должны жить в разных слоях. Так фабрика остаётся управляемой, аудируемой и масштабируемой.

---

## 1. Целевая архитектура фабрики

```text
01. Memo Portfolio Map
02. Data Contract
03. RAW Inventory
04. Stage Layer
05. Finance Mart Layer
06. Analysis Overlay Layer
07. Evidence Ledger
08. Slice Catalog
09. Chart Manifest
10. Insight Cards
11. Action Tracker
12. Memo Context Packages
13. LLM Draft / Judge / Revise
14. Render Pipeline
15. QA Gates
16. Release Registry
17. Feedback Loop
18. Scale Waves
```

Главная логика: сначала единая аналитическая основа, потом инфраструктура контроля, потом записки как управляемые продукты.

---

## 2. Главный принцип фабрики

```text
Finance mart считает.
Analysis overlay объясняет.
Evidence ledger доказывает.
Insight cards формулируют.
Action tracker управляет.
LLM пишет только на основе проверенного context package.
QA решает, можно ли выпускать.
```

LLM не должен быть источником расчётной истины. Он не считает source-of-truth metrics, не придумывает причины и не создаёт неподтверждённые рекомендации.

---

## 3. Слои данных и ответственности

### 3.1 RAW Layer

**Назначение:** сохранить исходники и их инвентаризацию.

| Артефакт | Назначение |
|---|---|
| `raw_files/` | исходные Excel/CSV/JSON |
| `raw_inventory.xlsx` | список файлов, листов, колонок, периодов |
| `source_registry.yml` | источник, владелец, период, валюта, дата загрузки |
| `raw_profile_report.md` | первичный data quality обзор |

**Запрет:** не делать выводы из RAW напрямую.

---

### 3.2 STAGE Layer — `stage_main_full`

**Назначение:** очистить, нормализовать и типизировать данные.

```text
RAW → normalize columns → normalize dates → normalize amounts → map dimensions → stage_main_full
```

| В stage должно быть | В stage не должно быть |
|---|---|
| `source_file` | `delta` |
| `source_id` | `risk_level` |
| `load_timestamp` | `confidence` |
| `date`, `month`, `year` | `action_required` |
| `direction`, `type`, `article_1/2/3` | выводы |
| `counterparty`, `cfo`, `owner_candidate` | рекомендации |
| `amount`, `currency`, `plan_fact_flag` | memo text |
| `row_status`, `mapping_status` | root cause |

**Смысл:** stage — это чистый слой данных, а не аналитическая записка в маске таблицы.

---

### 3.3 Finance Mart Layer — `mart_finance_full`

**Назначение:** единый источник финансовых расчётов.

```text
stage_main_full → formulas → aggregations → variance → YoY/MoM → mart_finance_full
```

| Блок | Поля |
|---|---|
| Identity | `data_run_id`, `mart_version`, `period`, `grain`, `direction`, `article_path`, `cfo`, `counterparty` |
| Plan / Fact | `plan_value`, `fact_value` |
| Variance | `delta_value`, `abs_delta_value`, `delta_pct`, `execution_rate` |
| YoY | `prior_year_value`, `yoy_delta`, `yoy_pct` |
| MoM | `prior_month_value`, `mom_delta`, `mom_pct` |
| Mix | `share_of_total`, `share_of_direction`, `share_of_outflow` |
| Planning flags | `fact_without_plan`, `plan_without_fact`, `over_execution`, `under_execution` |
| QA | `dq_status`, `reconciliation_status`, `formula_version` |

**Важно:** здесь ещё нет финальных управленческих выводов. Это расчётная правда.

---

### 3.4 Analysis Overlay Layer — `analysis_overlay_full`

**Назначение:** добавить классификацию, риск, материализацию и объяснение.

```text
mart_finance_full → materiality rules → risk rules → confidence rules → analysis_overlay_full
```

| Блок | Поля |
|---|---|
| Materiality | `materiality_level`, `materiality_basis` |
| Risk | `risk_level`, `risk_basis`, `risk_driver` |
| Planning quality | `planning_issue_type`, `planning_issue_reason` |
| Timing | `timing_status`, `timing_basis` |
| Confidence | `confidence_level`, `confidence_reason` |
| Interpretation | `analyst_note_candidate`, `root_cause_candidate` |

**Почему отдельно:** если риск или confidence поменялись, не надо пересчитывать финансовую правду.

---

### 3.5 Executive Compact Layer — `mart_executive_compact`

**Назначение:** короткий управленческий слой для summary, top deviations и headline charts.

```text
mart_finance_full + analysis_overlay_full
→ top movements
→ headline metrics
→ visible limitations
→ mart_executive_compact
```

| Использование | Что берём |
|---|---|
| Executive summary | headline metrics |
| Short memo | top deviations |
| Board-style view | materiality + risk |
| First page DOCX | compact conclusions |
| Dashboard | top movements and flags |

**Правило:** compact mart не заменяет full mart. Он только витрина, не склад.

---

## 4. Evidence Layer

### 4.1 Evidence Ledger — `evidence_ledger`

**Назначение:** доказать каждое утверждение в записке.

```yaml
claim_id: CLM-2026-0001
memo_id: 01_executive_yoy_mom_budget_memo
memo_section: Executive summary
claim_text: "Основное отклонение сформировано статьёй X."
claim_type: fact / interpretation / recommendation
metric_name: delta_value
value: 123456.78
currency: EUR
period: 2026-05
grain: month_article_counterparty
filters:
  direction: OUT
  article_1: ...
source_table: mart_finance_full
source_snapshot: data_run_id
calculation_ref: formula_catalog.delta_value
source_row_count: 128
limitation: "Данные не включают ручные корректировки после даты выгрузки"
confidence: high / medium / low
status: supported / weak / unsupported
```

**Железное правило:** если в записке есть утверждение без `claim_id`, оно считается неподтверждённым.

---

### 4.2 Source References — `source_refs`

**Назначение:** дать LLM только разрешённые факты.

| Поле | Назначение |
|---|---|
| `source_ref_id` | ссылка на проверенный факт |
| `metric` | какая метрика |
| `value` | значение |
| `period` | период |
| `filter` | срез |
| `limitation` | ограничение |
| `allowed_usage` | где можно использовать |

LLM не ходит в raw, не угадывает факты, не досчитывает по смыслу. Только разрешённые факты.

---

## 5. Slice и Chart Infrastructure

### 5.1 Slice Catalog — `slice_catalog.yml`

**Назначение:** управлять всеми срезами, чтобы не плодить mini-marts.

```yaml
slice_id: top_plan_fact_deviations_by_article
source: mart_finance_full
grain: month_article_1
metrics:
  - plan_value
  - fact_value
  - delta_value
  - delta_pct
filters:
  period: current_month
  direction: OUT
sort: abs_delta_value_desc
limit: 20
used_by:
  - 01_executive_yoy_mom_budget_memo
  - 02_plan_fact_deviation_memo
qa:
  required_columns: [...]
  max_null_rate: 0.01
```

---

### 5.2 Chart Manifest — `chart_manifest.yml`

**Назначение:** каждый график должен быть воспроизводимым и проверяемым.

```yaml
chart_id: chart_01_top_deviations
memo_id: 01_executive_yoy_mom_budget_memo
source_slice: top_plan_fact_deviations_by_article
chart_type: bar
metric: delta_value
period: 2026-05
grain: article_1
caption: "Топ отклонений факт-план по статьям"
limitations:
  - "Показаны только топ-20 статей по абсолютному отклонению"
output_file: charts/chart_01_top_deviations.png
qa:
  min_width_px: 1200
  min_height_px: 700
  required_in_docx: true
```

**Запрет:** график не строится напрямую из RAW/STAGE. Только из finance mart или документированного slice.

---

## 6. Insight и Action Layer

### 6.1 Insight Cards — `insight_cards`

**Назначение:** превратить цифры в структурированные выводы до LLM-текста.

```yaml
insight_id: INS-2026-0001
memo_id: 01_executive_yoy_mom_budget_memo
title: "Основной вклад в отклонение дала статья X"
insight_type: variance / trend / risk / planning_quality / anomaly
supporting_claims:
  - CLM-2026-0001
  - CLM-2026-0002
business_interpretation: "Отклонение требует проверки владельцем бюджета"
confidence: medium
limitations:
  - "Причина отклонения не подтверждена первичным документом"
recommended_memo_section: Analysis
```

---

### 6.2 Action Tracker — `action_tracker`

**Назначение:** отделить рекомендации и управленческие действия от расчётного mart.

| Поле | Пример |
|---|---|
| `action_id` | ACT-2026-0001 |
| `memo_id` | 01_executive_yoy_mom_budget_memo |
| `linked_insight_id` | INS-2026-0001 |
| `action_required` | yes |
| `owner` | CFO / budget owner |
| `due_date` | 2026-06-10 |
| `priority` | high / medium / low |
| `status` | open / in_progress / done / rejected |
| `evidence_status` | supported / weak / unsupported |
| `next_review_date` | 2026-06-17 |

---

## 7. Memo Portfolio — каталог записок

Полная фабрика должна поддерживать не одну записку, а портфель.

### Волна 1 — базовые управленческие записки

| ID | Записка | Цель |
|---|---|---|
| `01_executive_yoy_mom_budget_memo` | Executive YoY/MoM Budget Memo | главный стандарт |
| `02_plan_fact_deviation_memo` | Plan-Fact Deviations | отклонения план-факт |
| `03_planning_quality_memo` | Planning Quality | качество планирования |
| `04_in_out_inout_flow_memo` | IN / OUT / IN-OUT | потоки и структура |

### Волна 2 — детализация

| ID | Записка | Цель |
|---|---|---|
| `05_counterparty_memo` | Counterparty Analysis | контрагенты |
| `06_article_hierarchy_memo` | Article Hierarchy | статьи 1-3 |
| `07_cfo_owner_memo` | CFO / Owner Analysis | ответственность |
| `08_timing_memo` | Timing Analysis | переносы и сезонность |

### Волна 3 — продвинутая аналитика

| ID | Записка | Цель |
|---|---|---|
| `09_anomaly_memo` | Anomaly Detection | выбросы |
| `10_recurrence_memo` | Recurrence Analysis | повторяемость |
| `11_forecast_scenario_memo` | Forecast / Scenario | прогноз и сценарии |
| `12_action_operating_model_memo` | Action Operating Model | управление действиями |

### Волна 4 — deep / audit / board pack

| ID | Записка | Цель |
|---|---|---|
| `13_deep_finance_working_memo` | Deep Finance Memo | рабочая финансовая записка |
| `14_evidence_appendix_memo` | Evidence Appendix | доказательная база |
| `15_board_summary_memo` | Board Summary | верхнеуровневый pack |
| `16_budget_owner_pack` | Budget Owner Pack | адресные действия |
| `17_risk_register_memo` | Risk Register | реестр рисков |
| `18_monthly_digest_memo` | Monthly Digest | регулярный выпуск |

---

## 8. Уровни каждой записки

Каждая тема может выпускаться в 4 уровнях.

| Уровень | Назначение | Объём |
|---|---|---|
| `short` | executive pack | 1-2 страницы |
| `standard` | управленческая записка | 4-8 страниц |
| `deep` | finance working memo | 8-20 страниц + appendix |
| `action` | action memo / tracker | задачи, владельцы, сроки |

Пилотная записка должна пройти все 4 уровня, потому что фабрика должна уметь производить полный комплект.

---

## 9. Memo Generation Pipeline

Пайплайн записки:

```text
verified numbers
→ evidence cards
→ context package
→ draft
→ judge
→ revise
→ final memo
→ QA
```

### 9.1 Context Package

```yaml
memo_id: 01_executive_yoy_mom_budget_memo
memo_level: standard
audience: CFO / CEO
period: 2026-05
data_run_id: DR-2026-05-22-001
mart_version: v1.0.0
formula_catalog_version: v1.0.0
input_tables:
  - mart_executive_compact
  - selected_slices
  - evidence_ledger
  - insight_cards
  - action_tracker
allowed_claims:
  - CLM-...
required_sections:
  - Executive summary
  - Key facts
  - Analysis
  - Risks
  - Recommendations
  - Limitations
  - Evidence appendix
forbidden:
  - inventing numbers
  - unsupported root causes
  - unverified recommendations
  - hidden assumptions
```

### 9.2 Draft

LLM пишет черновик только из context package.

```text
context package → draft memo
```

Результат:

```text
draft_memo.md
draft_claim_map.json
draft_limitations.md
```

### 9.3 Judge

Judge проверяет:

| Проверка | Вопрос |
|---|---|
| Unsupported claims | есть ли утверждения без claim_id |
| Missing evidence | хватает ли доказательств |
| Overconfidence | не сильнее ли вывод, чем evidence |
| Number clarity | понятны ли суммы, периоды, валюты |
| Structure | соответствует ли memo template |
| Audience fit | подходит ли CEO/CFO/owner |
| Actionability | есть ли конкретные действия |

### 9.4 Revise

Revisor исправляет только то, что разрешено judge review.

```text
draft memo
+ judge findings
+ evidence ledger
→ revised memo
```

**Запрет:** revisor не добавляет новые факты.

### 9.5 Render

```text
final_memo.md
→ DOCX
→ PDF optional
→ XLSX appendix
→ chart pack
→ release package
```

---

## 10. Full QA Gates

### 10.1 Data Contract Gate

| Проверка | Pass criteria |
|---|---|
| Period | все строки имеют валидный период |
| Currency | валюта определена и нормализована |
| Grain | grain соответствует контракту |
| Keys | ключи не пустые |
| Source lineage | у каждой строки есть `source_id` |
| Null policy | пустые значения классифицированы |
| Duplicate policy | дубли выявлены или объяснены |

### 10.2 Stage Gate

| Проверка | Pass criteria |
|---|---|
| Required columns | все обязательные поля есть |
| Type validation | суммы числовые, даты валидные |
| Mapping status | нет критичных unmapped строк |
| Row count | RAW count → STAGE count объясним |
| Amount reconciliation | отклонение в пределах допуска |

### 10.3 Finance Mart Gate

| Проверка | Pass criteria |
|---|---|
| Formula catalog | каждая метрика имеет формулу |
| Delta check | `fact - plan = delta` |
| YoY check | prior year period корректен |
| MoM check | prior month period корректен |
| Aggregation check | totals согласованы |
| Reconciliation | RAW → STAGE → MART объяснимо |
| Versioning | указан `mart_version` |

### 10.4 Overlay Gate

| Проверка | Pass criteria |
|---|---|
| Risk rules | каждый risk_level имеет basis |
| Confidence rules | confidence не пустой |
| Materiality rules | materiality считается по каталогу |
| Interpretation | интерпретации отделены от фактов |
| Weak evidence | слабые выводы промаркированы |

### 10.5 Evidence Gate

| Проверка | Pass criteria |
|---|---|
| Claim coverage | каждый ключевой вывод имеет `claim_id` |
| Source table | указан источник |
| Metric | указана метрика |
| Period | указан период |
| Filters | указаны фильтры |
| Status | supported / weak / unsupported |
| Limitation | ограничение видно |

### 10.6 Chart Gate

| Проверка | Pass criteria |
|---|---|
| Source slice | каждый график имеет source slice |
| Metric | метрика указана |
| Period | период указан |
| Caption | подпись есть |
| Limitations | ограничения есть |
| File exists | файл реально создан |
| DOCX presence | график реально вставлен в DOCX |

### 10.7 Text QA Gate

| Проверка | Pass criteria |
|---|---|
| Unsupported claims | 0 критичных |
| Numbers match evidence | суммы совпадают |
| No hidden calculations | LLM не досчитал сам |
| Limitations visible | ограничения видны |
| Risk wording | риск не завышен |
| Recommendations | рекомендации связаны с evidence/action |

### 10.8 Render QA Gate

| Проверка | Pass criteria |
|---|---|
| DOCX opens | файл открывается |
| Required sections | все разделы есть |
| Charts embedded | графики внутри документа |
| Appendix exists | evidence appendix есть |
| Page breaks | приложения отделены |
| Tables readable | таблицы не развалены |
| Style | единый шаблон |

### 10.9 Release Gate

| Проверка | Pass criteria |
|---|---|
| QA summary | есть pass/fail |
| Residual risks | указаны |
| Data run id | указан |
| Memo version | указан |
| Artifacts complete | DOCX/MD/XLSX/charts |
| Owner approval | статус принятия есть |
| Rollback note | понятно, к чему откатиться |

---

## 11. Versioning и audit trail

Каждый выпуск должен иметь:

```yaml
data_run_id: DR-2026-05-22-001
source_snapshot_date: 2026-05-22
stage_version: v1.0.0
mart_version: v1.0.0
formula_catalog_version: v1.0.0
overlay_rules_version: v1.0.0
evidence_schema_version: v1.0.0
prompt_package_version: v1.0.0
memo_template_version: v1.0.0
render_pipeline_version: v1.0.0
memo_version: 2026.05.22-v1
generation_timestamp: 2026-05-22T...
qa_status: pass / revise / blocked
```

Это защита от ситуации, когда цифры поменялись, а никто не знает, где именно.

---

## 12. Feedback Loop

```text
QA fail
→ classify failure
→ assign owner
→ fix correct layer
→ rerun affected stages only
→ regression QA
→ update changelog
→ release or reject
```

### Классификация ошибок

| Failure type | Где чинить |
|---|---|
| Source issue | RAW / source registry |
| Mapping issue | STAGE |
| Formula issue | finance mart / formula catalog |
| Risk logic issue | analysis overlay |
| Unsupported claim | evidence ledger / prompt |
| Bad chart | slice catalog / chart manifest |
| Bad text | LLM prompt / judge / revise |
| DOCX issue | render pipeline |
| Wrong action | action tracker |

---

## 13. Deterministic vs LLM boundary

| Deterministic pipeline | LLM |
|---|---|
| конвертация файлов | формулировка narrative |
| очистка данных | executive wording |
| расчёт сумм | структурирование выводов |
| delta / YoY / MoM | объяснение на основе evidence |
| reconciliation | draft memo |
| chart data | judge / revise |
| schema validation | улучшение читаемости |
| QA totals | выявление слабых формулировок |

**Запрет:** LLM не считает итоговые метрики, не придумывает причины, не создаёт неподтверждённые рекомендации.

---

## 14. Project Routing

| Работа | Проект |
|---|---|
| Стратегия записок, волны, аудитории, приоритеты | `[Thinking]` |
| RAW, stage, marts, reconciliation, formulas | `[Analytics]` |
| Prompts, context packages, judge/revise, QA text | `[LLM]` |
| Код, генераторы, тесты, DOCX/render pipeline | `[Codex]` |
| Evidence/governance patterns | `[AI OS]` |

---

## 15. Рекомендуемая структура папок

```text
memo_factory/
  00_governance/
    memo_portfolio_map.md
    data_contract.md
    formula_catalog.yml
    acceptance_matrix.yml
    release_policy.md

  01_raw/
    files/
    raw_inventory.xlsx
    source_registry.yml

  02_stage/
    stage_main_full.parquet
    stage_profile_report.md
    stage_qa_report.json

  03_marts/
    mart_finance_full.parquet
    mart_executive_compact.parquet
    mart_qa_report.json

  04_overlays/
    analysis_overlay_full.parquet
    risk_rules.yml
    confidence_rules.yml
    materiality_rules.yml

  05_slices/
    slice_catalog.yml
    slices/
    slice_qa_report.json

  06_charts/
    chart_manifest.yml
    charts/
    chart_qa_report.json

  07_evidence/
    evidence_ledger.parquet
    source_refs.json
    evidence_cards/
    evidence_qa_report.json

  08_insights/
    insight_cards/
    insight_register.json

  09_actions/
    action_tracker.xlsx
    action_register.json

  10_context_packages/
    01_executive_yoy_mom_budget_memo/
      short_context.json
      standard_context.json
      deep_context.json
      action_context.json

  11_prompts/
    draft_prompt.md
    judge_prompt.md
    revise_prompt.md
    executive_style_prompt.md

  12_outputs/
    01_executive_yoy_mom_budget_memo/
      short/
      standard/
      deep/
      action/

  13_qa/
    text_qa/
    docx_media_qa/
    release_qa/
    regression_qa/

  14_release/
    release_registry.xlsx
    monthly_packages/

  15_backlog/
    data_issues.md
    mart_v2_backlog.md
    prompt_v2_backlog.md
    chart_v2_backlog.md
```

---

## 16. Полная последовательность работ

```text
01. Составить memo_portfolio_map
02. Зафиксировать data_contract
03. Сделать raw_inventory
04. Собрать source_registry
05. Построить stage_main_full
06. Пройти stage QA
07. Собрать formula_catalog
08. Построить mart_finance_full
09. Пройти mart reconciliation QA
10. Построить analysis_overlay_full
11. Построить mart_executive_compact
12. Создать slice_catalog
13. Создать chart_manifest
14. Сгенерировать chart pack
15. Создать evidence_ledger
16. Создать source_refs
17. Создать insight_cards
18. Создать action_tracker
19. Собрать context packages для 4 уровней
20. Сгенерировать pilot memo 01: short / standard / deep / action
21. Прогнать judge / revise
22. Прогнать text QA
23. Прогнать chart QA
24. Прогнать DOCX media QA
25. Прогнать release QA
26. Зафиксировать memo_factory_standard
27. Масштабировать wave 1
28. Масштабировать wave 2
29. Масштабировать wave 3
30. Масштабировать wave 4
31. Вести feedback loop и regression QA
```

---

## 17. Acceptance Matrix

| Уровень | Минимальный pass |
|---|---|
| Data | RAW/STAGE/MART сверены |
| Formula | delta, YoY, MoM, execution имеют формулы |
| Evidence | ключевые claims имеют evidence |
| Charts | все графики имеют source slice |
| Text | 0 critical unsupported claims |
| DOCX | документ читается, графики внутри |
| Action | owner/due/status указаны для action items |
| Release | есть versioning, QA summary, residual risks |

---

## 18. Исправления после judge review

| Замечание judge | Исправление |
|---|---|
| `mart_main_full` перегружен | разделено на `mart_finance_full`, `analysis_overlay`, `evidence_ledger`, `action_tracker` |
| нет чёткого evidence model | добавлен контракт `evidence_ledger` |
| QA-гейты нетестируемы | добавлены pass criteria по каждому gate |
| нет versioning | добавлены `data_run_id`, `mart_version`, `formula_catalog_version`, `memo_version` |
| нет feedback loop | добавлен цикл QA fail → classify → fix owner → rerun → regression |
| не разведены deterministic и LLM | добавлена граница ответственности |
| риск слишком большой стройки | сохранена полная фабрика, но введены слои, gates и волны релиза |
| пилот мог выглядеть как MVP | пилот оставлен полным: short / standard / deep / action |

---

## 19. Итоговое решение

Фабрику надо строить не как один большой генератор DOCX, а как контролируемую аналитическую производственную линию:

```text
Data spine
→ Finance spine
→ Evidence spine
→ Memo spine
→ QA spine
→ Release spine
→ Feedback spine
```

Пилотная записка не сужает задачу. Она становится эталонным прогоном полной фабрики на одном направлении и всех четырёх уровнях: `short`, `standard`, `deep`, `action`. После этого остальные направления масштабируются волнами, но на той же архитектуре, с теми же gates и той же доказательной дисциплиной.

## Уверенность

**9/10.**

Оставшийся риск: точные поля, thresholds и formula catalog нужно подогнать под реальные raw-файлы и управленческую методику.
