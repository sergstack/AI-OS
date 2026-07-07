# Variance Analysis Pack Template

## Scope

Question:
Decision context:
Audience:
Owner:
Expected output:

## Data contract

Source datasets:
Source owner:
Refresh timestamp:
Required columns:
Metric rules:
Plan / baseline source:
Fact source:
Currency / units:

## Grain / period / filters

Grain:
Period:
Comparison period:
Filters:
Exclusions:
Materiality threshold:

## Method

Source layer:
Output layer:
Variance method:
Ranking method:
Calculation tool:
Formula references:

## Variance table

| item | plan | fact | delta | abs_delta | delta_pct | period | grain | source_mart | QA status |
|---|---:|---:|---:|---:|---:|---|---|---|---|

## Drivers

Confirmed drivers:
Hypotheses:
Unexplained variance:

## QA

- [ ] Plan and fact sources are identified.
- [ ] Period, grain, filters, and exclusions match across plan and fact.
- [ ] Totals reconcile before variance interpretation.
- [ ] Variance, absolute variance, and percentage variance were calculated by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Confirmed drivers are separated from hypotheses.

## Limitations

Known blockers:
Coverage gaps:
Timing issues:
Mapping issues:
Assumptions:

## Acceptance

- [ ] Top deviations are ranked by materiality.
- [ ] Every driver or risk has evidence.
- [ ] Recommendations do not exceed verified variance facts.
