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
