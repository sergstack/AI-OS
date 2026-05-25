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

Otherwise, structure and content can be prepared inside `[Analytics]`.
