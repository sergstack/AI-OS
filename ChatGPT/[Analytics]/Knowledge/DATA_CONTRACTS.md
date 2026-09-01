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

## Contract QA

- [ ] Grain explicit.
- [ ] Period explicit.
- [ ] Required columns listed.
- [ ] Types listed.
- [ ] Currency / unit logic listed.
- [ ] Null policy listed.
- [ ] Duplicate policy listed.
- [ ] Freshness rule listed.
- [ ] Expected outputs listed.
- [ ] Main files listed.
- [ ] Flagship metrics and their read-back-verifiable source locators listed
  when publication is planned.
