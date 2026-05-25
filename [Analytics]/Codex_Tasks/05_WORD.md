# Codex Task 05 — Word / DOCX

## Objective

Add Word/DOCX report standard.

## Requirements

- Executive content from `mart_main_tz/compact`.
- Appendix/evidence from `mart_main_full`.
- Charts from mart slices.
- Limitations visible.

## Acceptance criteria

- [x] Word structure documented.
- [x] Metadata documented.
- [x] DOCX QA documented.
- [x] Handoff to Codex only for automated generation.

## Visual and language standard for executive memo

- Все видимые элементы управленческой записки должны быть на русском языке.
- Technical IDs допускаются только в appendix / evidence layer и не должны перегружать основной текст записки.
- Графики для executive memo используют спокойную управленческую палитру: приглушённые, благородные цвета без ярких и кислотных оттенков.
- Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` must not appear in the main executive body unless placed in appendix / evidence context.
- Chart labels, legends, axes, titles and captions must use Russian business-readable labels.
- Captions must not exceed evidence.
- Executive memo body must stay management-readable; evidence detail belongs to appendix / evidence layer.
- Appendix / evidence must be clearly separated from the executive memo.

## Additional DOCX QA checks

- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical IDs appear only in appendix / evidence.
- [ ] Chart labels and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Appendix is clearly separated from executive memo.
