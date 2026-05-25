# Analytics QA Checklist

## Data QA

- [ ] Required files exist.
- [ ] Required columns exist.
- [ ] Data types valid.
- [ ] Dates parsed correctly.
- [ ] Currency / units normalized.
- [ ] Null policy applied.
- [ ] Duplicate policy applied.
- [ ] Freshness checked.
- [ ] Mapping tables checked.
- [ ] Unmatched rows listed.

## Main files QA

- [ ] `stage_main_full` exists or is designed.
- [ ] `stage_main_full` has no business metrics.
- [ ] `stage_main_full` has no analytical classifiers.
- [ ] `stage_main_full` is portable to DB / BI / Excel.
- [ ] `mart_main_full` exists or is designed.
- [ ] `mart_main_full` contains metrics and formulas.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is designed.
- [ ] Mart slices are derived from `mart_main_full`.

## Calculation QA

- [ ] RAW totals reconciled.
- [ ] STAGE totals reconciled.
- [ ] MART totals reconciled.
- [ ] Metric formulas documented.
- [ ] Edge cases tested or listed.
- [ ] Outliers reviewed.
- [ ] Thresholds explicit.
- [ ] Grain explicit.
- [ ] Period explicit.

## Analysis QA

- [ ] Method stated.
- [ ] Source mart stated.
- [ ] Top deviations ranked by materiality / ABS Delta.
- [ ] Driver logic documented.
- [ ] Timing status not overstated.
- [ ] Confirmed cause separated from hypothesis.
- [ ] Confidence rationale stated.

## Chart QA

- [ ] Chart source mart/slice listed.
- [ ] Metric listed.
- [ ] Grain listed.
- [ ] Period listed.
- [ ] Caption does not exceed data.
- [ ] Chart adds insight.
- [ ] Chart labels, legends, axes, titles and captions are Russian / business-readable.
- [ ] Executive chart palette uses muted executive colors.
- [ ] Technical IDs are absent from executive chart body unless the chart is appendix / evidence.

## Memo QA

- [ ] No unsupported claims.
- [ ] Every key conclusion has evidence.
- [ ] Limitations visible.
- [ ] Recommendations do not exceed data.
- [ ] Confidence stated.
- [ ] Risk has `risk_basis`.
- [ ] Action has owner / due date / status.
- [ ] Visible report language is Russian.
- [ ] No technical IDs in executive body.
- [ ] Technical values such as `fact_only`, `plan_only`, `p_fact_adjusted`, `refund_only`, `source_mix`, `slice_*`, `mart_*`, `EV-*`, `CH_EXEC_*` appear only in appendix / evidence context.
- [ ] Appendix is clearly separated from executive memo.

## Handoff QA

- [ ] Handoff only if another project is needed.
- [ ] Expected output clear.
- [ ] Acceptance criteria clear.
- [ ] Inputs listed.
- [ ] Risks listed.
- [ ] No unresolved analysis hidden in Codex task.
