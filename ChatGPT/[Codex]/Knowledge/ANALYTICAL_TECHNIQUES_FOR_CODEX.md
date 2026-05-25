# Analytical Techniques for Codex

Codex may implement analytical workflows, but must not invent business logic.

## Techniques to implement

- variance analysis;
- driver analysis;
- bridge tables;
- cohort summaries;
- anomaly flags;
- reconciliation totals;
- mart generation;
- evidence cards;
- memo context packages.

## Implementation rules

- formulas must be explicit;
- grain must be explicit;
- outputs must have tests;
- business definitions must come from Analytics task package;
- LLM narrative must be separate from deterministic calculation.
