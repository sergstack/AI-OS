# Quantitative Sanity Gate

## Purpose and boundary

`quantitative_sanity_gate` is the mandatory pre-publish control for a
quantitative Analytics report. It proves that a decision-bearing number is
plausible, correctly represented, precisely traceable, method-appropriate,
and independently reproducible. It is an extension of existing Analytics QA
and acceptance; it does not replace QA, Judge, reconciliation, or AES.

The gate is required only when a report is being published or presented as a
publishable management-facing result and contains one or more
`flagship_metric`s. A `flagship_metric` is a number shown in an executive
summary, heading, key finding, decision/recommendation basis, or otherwise
used to determine the report conclusion.

Do not create a gate record for private scratch calculations, exploratory
work, or an unpublished draft that is explicitly not offered as a result. If
such material becomes publishable, assess the gate before publication. A
report with no quantitative conclusion records `quantitative_sanity_gate_status:
not_applicable` with its reason.

Gate records are evidence artifacts or an appendix, not required executive
output. `quick` and routine compact reports retain their existing visible
format; publication still requires the internal gate evidence when they make a
quantitative decision-bearing claim.

## Canonical gate record

Create one record for every `flagship_metric`:

```text
metric_id:
metric_name:
reported_value:
unit:
population:
period:
grain:
filters:
source_locator:
representation_check:
plausibility_expectation:
plausibility_result: pass / fail / blocked
method:
method_applicability:
censoring_status: none / present / unknown
independent_source_locator:
independent_recalculation_method:
independent_recalculated_value:
tolerance:
reproduction_result: pass / fail / blocked
reviewer_or_execution_id:
evidence_reference:
resolution:
```

`source_locator` identifies where the reported metric is read back.
`independent_source_locator` identifies the source-level fields/evidence used
by the independent recalculation; it must not point only to the same derived
cells, formula output, copied aggregate, or calculated metric column.

Both locators must be read-back-verifiable:

- spreadsheet: file/workbook, sheet, and cell/range or structured table/column;
- database: dataset/schema/table, fields, and query/filter reference;
- mart: exact mart, row/key/filter, and metric/formula field; the independent
  locator still names the source-level inputs;
- another source: an equivalently precise, readable location.

General names such as `source workbook`, `raw data`, or `mart_main_full` are
not locators by themselves.

## Gate rules

- Check order of magnitude, sign, units, feasible range, and relevant
  cross-field/domain invariants.
- Validate storage semantics for duration metrics. When raw timestamps exist,
  cross-check the derived duration against their difference. Excel time-of-day
  values must not silently represent elapsed durations above 24 hours.
- For time-to-event metrics, state whether observations are open, closed, or
  right-censored. A closed-only percentile is not a complete-population
  duration when censoring is material. Use an appropriate survival method such
  as Kaplan–Meier, or mark the metric limited/blocked with the method gap.
- Independent reproduction starts from the `independent_source_locator`, uses
  an explicit path and tolerance, and cannot reuse the reported derived result.
- Taxonomy, formatting, arithmetic consistency, or reconciliation alone never
  prove gate passage.

## Aggregate status

```text
quantitative_sanity_gate_status: pass / revise / blocked / not_applicable
```

- `pass`: every flagship record has both checks passing, complete evidence and
  locators, an applicable method, and an explicit reproduction within tolerance.
- `revise`: one or more records fail, but a bounded remediation path is known;
  publication is prohibited until the affected records pass.
- `blocked`: required evidence, a read-back locator, source-level reproduction,
  or an applicable method is unavailable or unresolved; publication is
  prohibited.
- `not_applicable`: no published quantitative conclusion is present; state the
  reason. It is not a substitute for a failed or missing flagship record.

For `revise` or `blocked`, name each failed metric, evidence, owner/reviewer,
required remediation, and publication status in `resolution`.

## Non-acceptance

- A generic “sanity checked” item without the record and stop behavior.
- A report-level `pass` when any flagship metric is failed, blocked, missing
  evidence, or has an unresolved locator.
- Successful reconciliation presented as proof of correct units or duration
  representation.
- Recalculation from the same erroneous calculated cells or derived column.
- Kaplan–Meier mentioned as optional prose while a materially censored
  closed-only percentile passes.
- Copying this full contract into global system instructions or a second
  Analytics QA framework.

## Integration

`QA_CHECKLIST.md` owns the operational checklist, `ACCEPTANCE_CRITERIA.md`
owns result acceptance, and `DATA_CONTRACTS.md` owns source/evidence inputs.
Those files reference this contract rather than duplicate it. Method registry
ownership remains in `ANALYTICAL_TECHNIQUES.md`; this gate adds no method ID.
