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
Relative threshold and denominator:
Zero-plan rule:
Contribution basis and threshold:
Selected / excluded population:
Selection coverage:

## Method

Source layer:
Output layer:
Variance method:
Ranking method:
Calculation tool:
Formula references:

## Sign convention

Source variance formula:
Source sign convention:
Economic direction rule (`higher_is`):
Raw variance:
Normalized management variance (`positive = adverse`, `negative = favorable`):
Normalization status (`resolved / unresolved`):

## Variance table

| item | plan | fact | source_variance | normalized_management_variance | abs_movement | delta_pct | primary_attribution | budget_status | controllability | recurrence | evidence_status | period | grain | source_mart | QA status |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|---|---|---|

## Gross bridge and attribution

Gross adverse movement:
Gross favorable movement:
Normalized net management variance:
Economic effect:
Timing / cutoff effect:
Data / mapping effect:
Unresolved effect:
Reconciliation residual:
Reconciliation status:

## Classification coverage

Population basis:
Eligible gross movement:
Classified gross movement:
Unclassified gross movement:
Coverage percentage:
Total / classified / unknown row counts:

## Drivers

Confirmed drivers:
Hypotheses:
Unexplained variance:
Generalization scope and evidence:

## Reported / adjusted view

Official Plan / Fact / variance:
Reported normalized management variance:
Adjustments with explicit `increases_adverse / reduces_adverse` direction:
Adjusted management variance:

## QA

- [ ] Plan and fact sources are identified.
- [ ] Period, grain, filters, and exclusions match across plan and fact.
- [ ] Totals reconcile before variance interpretation.
- [ ] Variance, absolute variance, and percentage variance were calculated by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Confirmed drivers are separated from hypotheses.
- [ ] Source/raw sign and normalized management direction are explicit and not mixed.
- [ ] Gross adverse plus gross favorable reconciles to normalized net variance.
- [ ] Primary attribution is mutually exclusive, exhaustive within scope, and reconciled.
- [ ] Classification coverage uses eligible gross absolute movement, not net variance.
- [ ] Controllability and recurrence have traceable evidence or remain `unknown`.
- [ ] Single-period evidence is not generalized as systemic/non-systemic.
- [ ] Reported result remains visible; adjusted polarity is explicit.

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
- [ ] Secondary management attributes are not summed as causes.
- [ ] A material driver exceeding net variance has an explicit favorable offset.
