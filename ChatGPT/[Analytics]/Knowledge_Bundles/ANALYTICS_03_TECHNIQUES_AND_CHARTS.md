# [Analytics] — Techniques and Charts

## Purpose

Compact upload artifact for [Analytics] covering techniques and charts.

## Source files

- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`
- `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`

# Analytical Techniques
## Core techniques
## Output rule
```text
method:
metric:
period:
grain:
data source:
source mart:
limitation:
```
## Main file dependency
```text
mart_main_full
or documented mart slices derived from mart_main_full
```
Do not run final conclusions directly on raw/stage unless the task is explicitly a data QA task.
## Technique selection guide
- “Почему отклонение?” → variance + driver.
- “Что изменилось от начала к концу?” → bridge.
- “Где самые большие проблемы?” → contribution + segmentation.
- “Это ошибка или реальное событие?” → reconciliation + anomaly.
- “Какая динамика?” → trend.
- “Какие группы ведут себя по-разному?” → cohort / segmentation.
- “Можно ли доверять данным?” → reconciliation + DQ checks.


## From: `ChatGPT/[Analytics]/Knowledge/CHART_SELECTION_STANDARD.md`

# Chart Selection Standard
## Purpose
## Source rule
```text
chart_name:
purpose:
source_mart:
source_slice:
metric:
period:
grain:
filter:
caption_claim:
limitations:
```
Source must be:
```text
mart_main_full
or mart slice derived from mart_main_full
```
## Recommended chart types
## Do not use chart when
- metric is not defined;
- source mart is missing;
- grain is mixed;
- currency/unit not normalized;
- sample is too small;
- caption is stronger than data;
- chart duplicates table without insight.
## Executive visual and language standard
- Графики для executive memo используют спокойную управленческую палитру.
- Executive chart colors must be muted and business-readable; no neon colors and no default bright matplotlib palette.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in visible executive chart elements unless the chart is explicitly in appendix / evidence context.
- Technical IDs may remain in chart specs, datasets, catalog technical fields and evidence layer.
- Captions must not exceed evidence.
## Chart acceptance
- [ ] Purpose clear.
- [ ] Source mart listed.
- [ ] Metric listed.
- [ ] Grain listed.
- [ ] Period listed.
- [ ] Caption does not exceed evidence.
- [ ] Limitation visible.
- [ ] Executive chart uses compact mart or slice from full mart.
- [ ] Chart labels are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Technical IDs only in appendix / evidence.
