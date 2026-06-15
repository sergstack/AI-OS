# [Analytics] — Data Contracts and Marts

## Purpose

Compact upload artifact for [Analytics] covering data contracts and marts.

## Source files

- `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`
- `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Analytics]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`

# Data Contracts
## Purpose
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
```
## Main file additions
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
## Compact/full input
```text
contract_status: partial
missing_full_context: yes
assumptions_required: yes
```
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


## From: `ChatGPT/[Analytics]/Knowledge/MARTS_DESIGN.md`

# Marts Design
## Purpose
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
```text
mart_main_full
mart_main_tz / mart_main_compact
```
`mart_main_full` is the source of truth for analytical slices, charts and evidence.
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
