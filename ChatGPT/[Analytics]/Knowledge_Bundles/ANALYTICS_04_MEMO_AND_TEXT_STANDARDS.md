# [Analytics] — Memo and Text Standards

## Purpose

Compact upload artifact for [Analytics] covering memo and text standards.

## Source files

- `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`
- `ChatGPT/[Analytics]/Knowledge/WORD_REPORT_STANDARD.md`
- `ChatGPT/[Analytics]/Knowledge/TEXT_QA_AND_STYLE.md`
- `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/MEMO_PIPELINE.md`

# Analytical Memo Pipeline
## Purpose
Convert verified analysis into a memo without losing evidence.
## Pipeline
```text
mart_main_full
→ analysis tables
→ insight cards
→ evidence cards
→ mart_main_tz / compact
→ LLM context package, if needed
→ draft memo
→ judge review
→ revised memo
→ final report
```
## Memo structure
1. Executive summary.
2. Key numbers.
3. Main drivers.
4. Exceptions / anomalies.
5. Risks.
6. Recommended actions.
7. Limitations.
8. Appendix / evidence.
## Audience split
### Executive memo
- verdict;
- headline numbers;
- where the money is;
- main risks;
- decisions needed;
- actions;
- limitations.
```text
mart_main_tz / mart_main_compact
```
### Finance working package
- full evidence;
- DQ;
- timing logs;
- INOUT checks if valid;
- baseline;
- cards;
- backlog;
- reconciliation.
```text
mart_main_full
```
## Evidence rule
Every important sentence must be backed by:
- metric;
- table/mart;
- period;
- evidence card;
- or explicitly marked as interpretation.
## Memo QA
- [ ] Executive summary does not exceed evidence.
- [ ] Key numbers trace to mart.
- [ ] Drivers are ranked by impact.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner / due date / status.
- [ ] Limitations visible.
- [ ] Hypotheses are not presented as confirmed causes.


## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_MEMO_STRUCTURE.md`

# Analytical Memo Structure
## Purpose
Структура аналитической записки, которая отделяет обязательный управленческий слой от рабочего evidence-пакета.
## MVP memo standard
1. DQ status.
2. Plan / Fact / Delta / ABS Delta.
3. Top deviations by ABS Delta.
4. Row type.
5. Timing status.
6. Planning risk + risk basis.
7. Confidence + why not higher.
8. Confirmed cause vs hypothesis.
9. Required action + owner + due date.
## Must / Should / Conditional / Optional
| Block | Status | Notes |
| DQ status | Must | Без DQ нельзя публиковать сильный вывод |
| Plan / Fact / Delta / ABS Delta | Must | Базовый слой отклонений |
| Top deviations | Must | Ранжировать по ABS Delta или materiality |
| Row type | Must | Например: real variance / timing / data issue / mapping issue |
| Timing status | Must when relevant | candidate / confirmed / partial / not timing |
| Risk + risk basis | Must for management memo | Risk без basis не публиковать |
| Confidence + rationale | Must | Low Confidence не финальная причина |
| Confirmed cause vs hypothesis | Must | Не смешивать |
| Action + owner + due date | Must for управленческого действия | Иначе это observation |
## Stop conditions
| DQ Fail | Do not publish management conclusion |
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


## From: `ChatGPT/[Analytics]/Knowledge/WORD_REPORT_STANDARD.md`

# Word / DOCX Report Standard
## Purpose
Стандарт подготовки аналитических записок в Word без потери evidence.
## Source rule
DOCX must be based on verified data:
```text
executive memo content ← mart_main_tz / mart_main_compact
appendix / evidence ← mart_main_full
charts ← slices derived from mart_main_full
```
## Recommended document structure
1. Title.
2. Date / period / owner.
3. Executive summary.
4. Key numbers table.
5. Main deviations and drivers.
6. Risks and confidence.
7. Recommended actions.
8. Charts.
9. Limitations.
10. Appendix / evidence.
## Required metadata
```text
report_name:
period:
audience:
owner:
source_mart_full:
source_mart_compact:
qa_status:
accepted:
version:
```
## Word formatting principles
- Use short executive summary.
- Put numbers in tables, not only prose.
- Put limitations before appendix, not hidden at the end.
- Use chart captions that state the exact metric and period.
- Separate confirmed causes from hypotheses.
- Avoid decorative language.
## Executive language and evidence layer
- Все видимые элементы управленческой записки должны быть на русском языке.
- Executive memo body must stay management-readable; detailed evidence belongs to appendix / evidence layer.
- Technical IDs допускаются только в appendix / evidence layer.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart titles, labels, legends, axes and captions must use Russian business-readable labels.
- Appendix / evidence must be clearly separated from the executive memo body.
## DOCX acceptance
- [ ] Executive summary present.
- [ ] Key numbers trace to `mart_main_tz/compact`.
- [ ] Deep claims trace to `mart_main_full`.
- [ ] Charts have source and caption.
- [ ] Limitations visible.
- [ ] Confidence stated.
- [ ] No unsupported claims.
- [ ] Formatting does not change analytical meaning.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs only in appendix / evidence.
- [ ] Appendix is clearly separated from executive memo.
## Handoff to Codex
Only handoff DOCX generation to Codex if the task requires:
- automated `.docx` creation;
- template rendering;
- file conversion;
- reproducible report generator;
- tests or CI.


## From: `ChatGPT/[Analytics]/Knowledge/TEXT_QA_AND_STYLE.md`

# Text QA and Style
## Purpose
## Style principles
- Concrete over decorative.
- Numbers before adjectives.
- Evidence before recommendation.
- Limitation before confidence inflation.
- Hypothesis is not cause.
- Observation is not action.
## Language rules
```text
Данные показывают...
Расчёт по mart_main_full показывает...
Отклонение составляет...
Вероятная причина, требующая проверки...
Ограничение анализа...
```
```text
Очевидно...
Бесспорно...
Компания должна...
Причина точно в...
Данные полностью подтверждают...
```
unless QA and evidence support it.
## Executive report language standard
- Все видимые элементы управленческой записки должны быть на русском языке.
- Executive memo body must stay management-readable; evidence detail belongs to appendix / evidence layer.
- Technical IDs допускаются только в appendix / evidence layer.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Captions must not exceed evidence.
## Text QA checklist
- [ ] No unsupported claims.
- [ ] Every key conclusion has evidence.
- [ ] Low Confidence is not written as fact.
- [ ] Hypotheses are labeled.
- [ ] Risk has `risk_basis`.
- [ ] Action has owner / due date / status.
- [ ] INOUT not used without Definition Card.
- [ ] Chart captions not stronger than data.
- [ ] Limitations visible.
- [ ] Executive wording matches compact mart.
- [ ] Deep conclusions reference full mart/evidence.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs appear only in appendix / evidence.
## Formatting QA
- [ ] Headings reflect analytical structure.
- [ ] Tables are readable.
- [ ] Period and units visible.
- [ ] Numbers have consistent formatting.
- [ ] Same metric has same name everywhere.
- [ ] Appendix is clearly separated from executive memo.
- [ ] No hidden methodological caveats.
- [ ] Executive memo body is not overloaded with evidence detail.


## From: `ChatGPT/[Analytics]/Knowledge/MEMO_RUBRIC.md`

# Analytical Memo Rubric
## Purpose
## Rubric
| Area | Pass condition | Fail condition |
| Evidence | Key conclusions trace to mart/evidence | Unsupported claims |
| Action | Action has owner / due date / status | Observation called action |
| Confidence | Confidence and limitations visible | Low confidence as fact |
## Golden memo criteria
- executive summary is short and evidence-backed;
- numbers are in tables and prose;
- deviations are ranked by ABS Delta/materiality;
- confirmed causes and hypotheses are separated;
- limitations are visible before appendix;
- appendix / evidence layer supports deep claims.
