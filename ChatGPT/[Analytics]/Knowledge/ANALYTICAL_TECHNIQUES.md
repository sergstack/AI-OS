# Analytical Techniques

## Core techniques

| Technique | Use when | Output |
|---|---|---|
| Variance analysis | Plan vs fact / prior period | Deviation and explanation |
| Driver analysis | Need root cause | Ranked drivers |
| Bridge analysis | Need movement explanation | Start → changes → end |
| Cohort analysis | Behavior by group/time | Retention/conversion patterns |
| Anomaly detection | Outliers/spikes | Exception list |
| Reconciliation | Need trust in data | Totals match / mismatch |
| Segmentation | Different groups behave differently | Ranked segments |
| Trend analysis | Time dynamics | Direction and inflection |
| Mix analysis | Composition changes | Mix effect |
| Contribution analysis | Need impact ranking | Contribution to total delta |

## Output rule

For each technique state:

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

Techniques should run on:

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
