# Text QA and Style

## Purpose

Отладка текстов и оформления аналитических записок так, чтобы текст не становился сильнее данных.

## Style principles

- Concrete over decorative.
- Numbers before adjectives.
- Evidence before recommendation.
- Limitation before confidence inflation.
- Hypothesis is not cause.
- Observation is not action.

## Language rules

Use:

```text
Данные показывают...
Расчёт по mart_main_full показывает...
Отклонение составляет...
Вероятная причина, требующая проверки...
Ограничение анализа...
```

Avoid:

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
