# Analytical Memo Structure

## Purpose

Структура аналитической записки, которая отделяет обязательный управленческий слой от рабочего evidence-пакета.

## MVP memo standard

Обязательные блоки:

1. DQ status.
2. Plan / Fact / Delta / ABS Delta.
3. Top deviations by ABS Delta.
4. Row type.
5. Timing status.
6. Planning risk + risk basis.
7. Confidence + why not higher.
8. Confirmed cause vs hypothesis.
9. Required action + owner + due date.
10. Limitations / open questions.

## Must / Should / Conditional / Optional

| Block | Status | Notes |
|---|---|---|
| DQ status | Must | Без DQ нельзя публиковать сильный вывод |
| Plan / Fact / Delta / ABS Delta | Must | Базовый слой отклонений |
| Top deviations | Must | Ранжировать по ABS Delta или materiality |
| Row type | Must | Например: real variance / timing / data issue / mapping issue |
| Timing status | Must when relevant | candidate / confirmed / partial / not timing |
| Risk + risk basis | Must for management memo | Risk без basis не публиковать |
| Confidence + rationale | Must | Low Confidence не финальная причина |
| Confirmed cause vs hypothesis | Must | Не смешивать |
| Action + owner + due date | Must for управленческого действия | Иначе это observation |
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
Key numbers:
Top deviations:
Main driver / hypothesis:
Risk:
Confidence:
Action:
Limitations:
Evidence:
```
