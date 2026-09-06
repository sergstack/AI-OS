# Data Contracts

## Purpose

Data contract фиксирует, какие данные нужны, на каком grain, с какими типами, правилами качества и ограничениями.

## Minimum contract

```markdown
# Data Contract

Dataset:
Owner:
Business owner:
Technical owner:
Source:
Source file / system:
Refresh frequency:
Load timestamp:
Period:
Grain:
Primary keys:
Foreign keys:
Required columns:
Optional columns:
Column types:
Allowed values:
Date logic:
Currency / units:
Null policy:
Duplicate policy:
Freshness rule:
Mapping rules:
Join rules:
Metric rules:
Flagship metrics:
Source locators:
Independent recalculation source locators:
Classification rules:
Validation checks:
Known limitations:
Expected outputs:
```

## Main file additions

For every case, define:

```text
stage_main_full:
- expected grain
- required columns
- no metrics / no classifiers rule
- portability target: DB / dashboard / Excel / BI

mart_main_full:
- expected grain
- metrics
- dimensions
- classifiers
- QA fields
- evidence fields

mart_main_tz / compact:
- audience
- shortened field list
- source reference to mart_main_full
```

## Rules

- No analysis without grain.
- No memo without calculation method.
- No mart without owner and expected output.
- No LLM package without curated facts.
- No chart without source mart or mart slice.
- No executive conclusion from raw data.
- For a publishable quantitative conclusion, identify flagship metrics and
  provide the reported-value and independent source-level locators required by
  `QUANTITATIVE_SANITY_GATE.md`.
- For a material/flagship/ratio-like metric, a `METRIC_DEFINITION_CARD` with
  `status: approved` is required before a strong management conclusion; see
  `../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md`.
- Preserve `VALUE_STATE` distinctions end to end when they are material; do
  not collapse `UNKNOWN`, `NOT_REPORTED`, `PARSE_FAILED`, `MISSING_SOURCE`,
  `UNMATCHED`, or `BLOCKED` into one generic null.

## Compact/full input

When only `compact` exists:

```text
contract_status: partial
missing_full_context: yes
assumptions_required: yes
```

When both `compact` and `full` exist:

```text
contract_status: complete_or_reviewable
compact_used_for: executive scope
full_used_for: data contract and full mart
```

## Canonical VALUE_STATE

Single semantic contract for materially different missing/uncertainty
states. It is not a second data-quality framework: it defines the vocabulary
that `Null policy`, `stage_main_full`, `mart_main_full`, and Analysis QA
already reference.

```text
VALUE_STATE
KNOWN
UNKNOWN
NOT_REPORTED
NOT_APPLICABLE
PARSE_FAILED
MISSING_SOURCE
UNMATCHED
BLOCKED
```

Invariants:

```text
UNKNOWN != 0
UNKNOWN != NOT_REPORTED
PARSE_FAILED != MISSING_SOURCE
NOT_APPLICABLE != FALSE
```

Semantics:

- `KNOWN` - a valid observed value exists.
- `UNKNOWN` - the value exists conceptually but is not determined; never
  substitute `0` or a generic null.
- `NOT_REPORTED` - the source was expected to report the value and did not;
  distinct from `UNKNOWN` (which may have no expectation of reporting).
- `NOT_APPLICABLE` - the field has no meaning for this row; never treat as
  `FALSE` or a negative/zero business result.
- `PARSE_FAILED` - a source value existed but could not be parsed/typed;
  distinct from `MISSING_SOURCE` (no source value existed to parse).
- `MISSING_SOURCE` - no source record/field was available.
- `UNMATCHED` - a join/reconciliation key had no counterpart in the expected
  population.
- `BLOCKED` - the value cannot be determined because a required upstream
  step is blocked.

Required behavior: `RAW -> STAGE -> MART` must not collapse materially
different `VALUE_STATE` values into a generic null if doing so could change
denominator, population, reconciliation, classification coverage, metric
result, claim strength, or management conclusion. `stage_main_full` carries
the row-level `VALUE_STATE` (see `MAIN_FILES_STANDARD.md`); `mart_main_full`
preserves it in coverage/denominator fields rather than silently dropping
affected rows. Use `VALUE_STATE` in `Null policy`, `zero_denominator_rule`,
and `null_semantics` on `METRIC_DEFINITION_CARD_TEMPLATE.md`.

`UNMATCHED` rows feed the activated `RECONCILIATION_CONTRACT` bounded pilot
control (`ANALYTICAL_REASONING_STANDARD.md` §15.2, CONTROL/CONTRACT, issue
#445): a material `UNMATCHED` population must be carried into
`matched_population` / `only_in_left` / `only_in_right` rather than
collapsed into an aggregate reconciliation pass. This does not add a
reconciliation method or a new `METHOD_ID`; it makes explicit which existing
methods and `VALUE_STATE` evidence back which integrity dimension.
`owner review required` before promotion beyond the bounded pilot; see
`../Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md`.

## Canonical METRIC_DEFINITION_CARD

For material, flagship, or ratio-like metrics, a formula alone is not a
sufficient metric definition. Use
`../Templates/METRIC_DEFINITION_CARD_TEMPLATE.md` to fix numerator,
denominator, aggregation semantics, population, units/currency,
sign/direction, zero-denominator behavior, allowed comparison scope, and
forbidden interpretations before a material conclusion is published. An
unresolved material metric definition (`status: provisional / blocked`)
blocks a strong management conclusion; see `ANALYTICAL_REASONING_STANDARD.md`
and `ACCEPTANCE_CRITERIA.md`. This is an extension of the existing
`Metric rules` / `Flagship metrics` contract fields, not a parallel
framework.

## Contract QA

- [ ] Grain explicit.
- [ ] Period explicit.
- [ ] Required columns listed.
- [ ] Types listed.
- [ ] Currency / unit logic listed.
- [ ] Null policy listed, using canonical `VALUE_STATE` where states are
  materially different.
- [ ] Duplicate policy listed.
- [ ] Freshness rule listed.
- [ ] Expected outputs listed.
- [ ] Main files listed.
- [ ] Flagship metrics and their read-back-verifiable source locators listed
  when publication is planned.
- [ ] Material/flagship/ratio-like metrics have a `METRIC_DEFINITION_CARD`
  with `status: approved`, or the conclusion is limited/blocked.
