# Analytical Memo Structure

## Purpose

Структура аналитической записки, которая отделяет обязательный управленческий слой от рабочего evidence-пакета.

## Executive layer for material management analysis

For `analytical_depth = material / decision_critical` and management-facing output, open with a compressed executive layer:

1. Executive verdict answering the business question.
2. Smallest sufficient set of material conclusions, usually 1–3 but never as a quota.
3. Supported business meaning and affected performance dimension.
4. Business effect versus data/control artefact where relevant.
5. Management implication and decision/action required, if any.
6. Material uncertainty and what would change the view.
7. Material limitations.

Rank by the business criterion relevant to the question, not mechanically by `ABS Delta`. Do not collapse materially different performance dimensions. State controllability or persistence only when supported; otherwise mark them unknown or omit them. The executive layer must be materially shorter than the supporting evidence. Routine output remains compact and does not instantiate this layer.

If DQ or reconciliation prevents reliable interpretation, that limitation becomes the executive verdict. Otherwise keep methodology and reconciliation in the evidence layer.

## Supporting evidence layer

Preserve the verified analytical detail:

1. DQ status.
2. Plan / Fact / Delta / ABS Delta where applicable.
3. Material deviations and their ranking criterion.
4. Row type.
5. Timing status.
6. Planning risk + risk basis.
7. Confidence + why not higher.
8. Confirmed cause vs hypothesis.
9. Supported action + owner + due date, if an action is asserted.
10. Limitations / open questions.

## Must / Should / Conditional / Optional

| Block | Status | Notes |
|---|---|---|
| DQ status | Must | Без DQ нельзя публиковать сильный вывод |
| Plan / Fact / Delta / ABS Delta | Must | Базовый слой отклонений |
| Top deviations | Must | Ранжировать по явному business criterion; `ABS Delta` не является универсальным критерием |
| Row type | Must | Например: real variance / timing / data issue / mapping issue |
| Timing status | Must when relevant | candidate / confirmed / partial / not timing |
| Risk + risk basis | Must for management memo | Risk без basis не публиковать |
| Confidence + rationale | Must | Low Confidence не финальная причина |
| Confirmed cause vs hypothesis | Must | Не смешивать |
| Action + owner + due date | Must only when an action is supported | Иначе это observation / monitoring / validation gap |
| INOUT | Conditional | Только при Definition Card |
| Forecast | Optional | Если вопрос про будущее решение |
| Scenario analysis | Optional / advanced | Если нужен выбор сценария |
| ML anomaly detection | Advanced | Не MVP по умолчанию |
| Methodology backlog | Should | Для улучшения системы |

## Stop conditions

| Condition | Action |
|---|---|
| DQ Fail | Do not publish management conclusion |
| No single currency/unit logic | Stop materiality conclusion |
| Low Confidence | Mark as hypothesis / not final cause |
| Timing only candidate | Do not call confirmed timing |
| Risk without basis | Do not publish risk |
| Action without owner/due date | Do not call management action |
| INOUT undefined | Do not use INOUT as explanation |

## Output template

```text
Verdict:
Material conclusions + why they matter:
Key numbers:
Top deviations:
Main driver / hypothesis:
Risk:
Confidence:
Management implication / decision or action if any:
What changes the view:
Limitations:
Evidence:
```
