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
