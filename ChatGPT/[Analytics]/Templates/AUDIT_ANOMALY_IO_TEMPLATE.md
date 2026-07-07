# Audit Anomaly Input / Output Template

## Input

Anomaly ID:
Question:
Decision context:
Owner:
Expected output:

## Data contract

Source datasets:
Source owner:
Refresh timestamp:
Required columns:
Primary keys:
Join keys:
Expected behavior:
Metric rules:
Currency / units:

## Grain / period / filters

Grain:
Period:
Comparison period:
Filters:
Exclusions:
Anomaly threshold:

## Method

Source layer:
Output layer:
Detection method:
Comparison method:
Calculation tool:
Formula references:

## Output

Finding:
Evidence:
Likely cause:
Risk:
Recommended action:
Owner:
Due date:
Confidence:

## Anomaly evidence table

| anomaly_id | entity | metric | observed_value | expected_value | delta | period | grain | source_mart | evidence_id | QA status |
|---|---|---|---:|---:|---:|---|---|---|---|---|

## QA

- [ ] Expected behavior is explicit.
- [ ] Period, grain, filters, and threshold are explicit.
- [ ] Detection calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.
- [ ] Finding is separated from likely cause and hypothesis.
- [ ] Risk has a risk basis and evidence.

## Limitations

Known blockers:
Coverage gaps:
False-positive risks:
Assumptions:

## Acceptance

- [ ] Anomaly output can be traced to source mart, evidence, period, and grain.
- [ ] Unsupported causes remain hypotheses.
- [ ] Recommended action is bounded by verified evidence.
