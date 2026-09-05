# Metric Definition Card Template

## Purpose

A formula alone is not a sufficient metric definition. Use this card for
material, flagship, or ratio-like metrics before a strong management
conclusion is published. It extends the existing Data Contract / mart
metric-formula rule (`DATA_CONTRACTS.md`, `MAIN_FILES_STANDARD.md`); it is not
a parallel metric framework and does not replace `QUANTITATIVE_SANITY_GATE.md`
or the 22-method registry.

## Card

```text
METRIC_DEFINITION_CARD

metric_id:
metric_name:
business_question:
metric_type: amount / count / ratio / rate / duration / share / index
formula:
numerator:
denominator:
aggregation_rule:
higher_is: favorable / adverse / context_dependent
unit:
currency:
time_basis:
population:
inclusions:
exclusions:
zero_denominator_rule:
null_semantics:
sign_convention:
allowed_comparisons:
forbidden_interpretations:
source_fields:
owner:
status: approved / provisional / blocked
```

## Field notes

- `numerator` / `denominator` are required whenever `metric_type` is `ratio`,
  `rate`, or `share`; otherwise record `not_applicable`.
- `aggregation_rule` states how the metric aggregates across grain (sum,
  weighted average, last value, distinct count, etc.); it is never inferred
  from the formula alone.
- `population` states the entity/record population the metric is computed
  over, consistent with `MAIN_FILES_STANDARD.md` grain and `DATA_CONTRACTS.md`
  scope rules. Population comparability across periods is the responsibility
  of this field, not a separate framework.
- `zero_denominator_rule` and `null_semantics` must use the canonical
  `VALUE_STATE` vocabulary (`DATA_CONTRACTS.md`) where the null/undefined case
  is materially different from zero.
- `allowed_comparisons` states permitted comparison scope (e.g. same
  population, same period type, same denominator definition).
  `forbidden_interpretations` states conclusions the metric must not be used
  to support (e.g. "not a causal driver", "not comparable across the
  population change on <date>").
- `status: approved` is required before the metric supports a material or
  flagship management conclusion. `provisional` or `blocked` metrics may be
  shown with an explicit limitation but cannot anchor a strong conclusion.

## Required behavior

- A formula alone (`formula:` populated, remaining fields empty) is not a
  sufficient metric definition for a material/flagship/ratio-like metric.
- Before any material conclusion, numerator/denominator, aggregation
  semantics, population, units/currency, sign/direction, zero-denominator
  behavior, allowed comparison scope, and forbidden interpretations must be
  defined where applicable to the `metric_type`.
- An unresolved material metric definition (`status: provisional / blocked`,
  or a required field left undefined) blocks a strong management conclusion:
  the claim is limited to `HYPOTHESIS` / `LIMITATION`, not a flagship finding.

## Acceptance

- [ ] Metric semantics documented separately from formula.
- [ ] Aggregation rule explicit.
- [ ] Numerator / denominator explicit when applicable.
- [ ] Population explicit.
- [ ] Zero-denominator rule explicit.
- [ ] Forbidden interpretations stated.
- [ ] Unresolved material metric definition blocks a strong management
  conclusion.

## P1 extension point (not implemented in this version)

`POPULATION_CONTRACT` — a future, more detailed population/denominator
comparability contract for ratio/rate/share/average/margin/conversion/
productivity/frequency metrics:

```text
population_definition
numerator_population
denominator_population
period
grain
filters
exclusions
population_changed_vs_baseline
denominator_changed_vs_baseline
scope_change_amount
scope_change_pct
interpretation_allowed
```

P1, not active in this version. Until it lands, `population`, `inclusions`,
`exclusions`, and the existing `population_constant_or_explained?` /
`denominator_constant_or_explained?` / `scope_change_quantified?` controls in
`ANALYTICAL_REASONING_STANDARD.md` §5 remain the active mechanism.
