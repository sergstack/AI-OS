# Analytics Context Pack Template

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
Primary keys:
Join keys:
Currency / units:
Metric rules:

## Grain / period / filters

Grain:
Period:
Comparison period:
Filters:
Exclusions:
Segmentation:

## Method

Workflow step:
Source layer:
Output layer:
Calculation tool:
Method summary:
Formula references:

## Verified facts

| fact_id | fact | metric | period | grain | source_mart | evidence_id | QA status |
|---|---|---|---|---|---|---|---|

## QA

- [ ] Data contract is complete enough for the requested output.
- [ ] Grain, period, filters, and exclusions are explicit.
- [ ] Numeric calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Findings trace to verified facts, source mart, and evidence.

## Limitations

Known blockers:
Coverage gaps:
Data quality notes:
Assumptions:

## Acceptance

- [ ] Context pack can support the requested analysis or memo.
- [ ] Unsupported claims are marked as assumptions, hypotheses, limitations, or blockers.
- [ ] Next run trigger is clear.
