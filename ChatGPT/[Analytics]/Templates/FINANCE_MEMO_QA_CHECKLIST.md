# Finance Memo QA Checklist

## Scope

Memo title:
Decision context:
Audience:
Owner:
Expected output:

## Data contract

- [ ] Source datasets are listed.
- [ ] Source owner and refresh timestamp are listed.
- [ ] Required columns and metric rules are listed.
- [ ] Currency / units are explicit.
- [ ] Source mart or compact mart is listed.

## Grain / period / filters

- [ ] Grain is explicit.
- [ ] Period and comparison period are explicit.
- [ ] Filters and exclusions are explicit.
- [ ] Segment or entity scope is explicit.

## Method

- [ ] Method is stated.
- [ ] Source layer and output layer are stated.
- [ ] Formula references are included where relevant.
- [ ] Numeric calculations were performed by Python, SQL, spreadsheet formulas, or another deterministic project-standard tool.
- [ ] LLM arithmetic was not used.

## Memo facts

- [ ] Key numbers trace to verified Analytics facts.
- [ ] Main deviations trace to mart rows, slices, or evidence cards.
- [ ] Drivers are separated into confirmed causes and hypotheses.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner, due date, and status.
- [ ] Recommendations do not exceed verified facts.

## QA

- [ ] Totals and reconciliations are documented or blockers are listed.
- [ ] Data quality status is visible.
- [ ] Confidence is stated for major claims.
- [ ] Executive language avoids technical IDs outside appendix / evidence.
- [ ] Appendix or evidence section is clearly separated from the memo body.

## Limitations

- [ ] Known blockers are listed.
- [ ] Coverage gaps are listed.
- [ ] Timing, mapping, or data quality issues are listed.
- [ ] Assumptions are labeled.

## Acceptance

- [ ] Memo narrative is based only on verified Analytics facts.
- [ ] Unsupported statements are marked as assumptions, hypotheses, limitations, or blockers.
- [ ] The memo is ready for judge / QA or clearly blocked.
