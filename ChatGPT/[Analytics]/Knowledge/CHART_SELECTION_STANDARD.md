# Chart Selection Standard

## Purpose

Подбирать графики только после определения метрики, grain, периода, аудитории и source mart.

## Source rule

Каждый график должен иметь:

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

| Analytical need | Recommended chart |
|---|---|
| Plan vs fact by period | Line chart or grouped bar |
| Top deviations | Bar chart sorted by ABS Delta |
| Structure / composition | Stacked bar or 100% stacked bar |
| Movement explanation | Bridge / waterfall |
| Trend over time | Line chart |
| Distribution / outliers | Box plot or histogram |
| Segment comparison | Bar chart / small multiples |
| Risk matrix | Heatmap or matrix |
| Flow | Sankey only if flow data is reliable |

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
