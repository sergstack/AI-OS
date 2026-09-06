# [Analytics] — Data Contracts and Marts

## Purpose

Compact upload artifact for [Analytics] covering data contracts and marts.

## Source files

- `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`
- `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`
- `ChatGPT/[Analytics]/Knowledge/ANALYTICS_02_DATA_CONTRACTS_AND_MARTS_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:60008b6f0c42e17e0c4840105f63f699a3957fb105576332778fce801015df68
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`

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
`UNMATCHED` rows feed the `RECONCILIATION_CONTRACT` control, promoted to
standard, active status (`ANALYTICAL_REASONING_STANDARD.md` §15.2,
CONTROL/CONTRACT, issue #445): a material `UNMATCHED` population must be
carried into `matched_population` / `only_in_left` / `only_in_right` rather
than collapsed into an aggregate reconciliation pass. This does not add a
reconciliation method or a new `METHOD_ID`; it makes explicit which existing
methods and `VALUE_STATE` evidence back which integrity dimension.
Promoted 2026-09-06 (owner-authorized); see
`docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md` for the promotion
decision and `../Knowledge/P1_PILOT_EVIDENCE_2026-09-06.md` for the original
pilot evidence.
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

## From: `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`

# Marts Design
## Purpose
Mart is an analysis-ready table. It is not raw data and not final narrative.
## Layers
```text
RAW: original inputs, minimally touched.
STAGE: cleaned, normalized, typed.
MARTS: business-ready metrics by grain.
ANALYSIS: variance, drivers, exceptions, risks, confidence.
REPORT: memo/chart/docx/pptx/dashboard/output.
```
## Mandatory design
Every mart design must include:
```text
mart_name:
business purpose:
audience:
grain:
period:
keys:
source stage files:
metrics:
formulas:
dimensions:
classifiers:
filters:
QA totals:
limitations:
```
## Main mart rule
Always design two levels:
```text
mart_main_full
mart_main_tz / mart_main_compact
```
`mart_main_full` is the source of truth for analytical slices, charts and evidence.
`mart_main_tz/compact` is the shortened management-ready view.
## mart size guardrails
A mart must be useful to read, not just complete.
Default visible field budget:
| Mode | Metrics | Visible columns | Sheets / views |
|---|---:|---:|---:|
| quick | 3-5 | 8-12 | 0-1 |
| standard | 5-10 | 15-30 | 3-5 |
| full | as needed | as needed | as needed, but requires index and compact front sheet |
Rules:
- Do not create 40 sheets or 200 columns unless user explicitly requests `full` mode / reusable model / dashboard-ready package.
- If more than 30 columns are needed, split fields into groups:
  - identity;
  - core metrics;
  - variance;
  - risk/confidence;
  - QA/evidence;
  - technical lineage.
- User-facing compact mart must show only decision-relevant fields.
- Technical QA/evidence fields should be hidden in appendix/evidence view unless requested.
## Mart checklist
- name explains business purpose;
- grain is explicit;
- keys are stable;
- metric formulas documented;
- source tables listed;
- refresh logic defined;
- QA totals available;
- limitations recorded;
- evidence fields available for key conclusions;
- compact layer references full layer.
## Recommended mart fields
### Identity
```text
row_id
period
entity_id
entity_name
source_system
source_file
stage_row_id
```
### Metrics
```text
plan_value
fact_value
delta_value
delta_pct
abs_delta
share_of_total
```
### Analysis
```text
row_type
materiality_flag
materiality_reason
driver_candidate
driver_confirmed
timing_status
inout_status
risk_level
risk_basis
confidence_level
confidence_reason
```
### Action
```text
action_required
action_owner
action_due_date
action_status
```
### QA
```text
dq_status
qa_status
reconciliation_status
limitation_flag
limitation_text
```
## Forbidden
- Do not put raw files into marts.
- Do not hide business logic in LLM prompts.
- Do not change formula definitions silently.
- Do not make isolated mini-marts from raw slices when a main mart is required.
- Do not build chart slices from raw if mart exists or is required.

## From: `ChatGPT/[Analytics]/Knowledge/ANALYTICS_02_DATA_CONTRACTS_AND_MARTS_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Analytics]/Knowledge_Bundles/ANALYTICS_02_DATA_CONTRACTS_AND_MARTS.md`.
## Legacy section: `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`
- If more than 30 columns are needed, split fields into identity, core metrics, variance, risk/confidence, QA/evidence and technical lineage.
