# Analytical Memo Automation Workflow

## Pipeline

```text
data contracts
→ marts
→ insight cards
→ evidence cards
→ LLM context package
→ draft
→ judge
→ revise
→ final memo
```

## Codex responsibility

Implement deterministic parts:
- data extraction;
- mart generation;
- evidence card creation;
- context package assembly;
- output validation;
- tests.

## Not Codex responsibility

- deciding business recommendation;
- inventing metric definitions;
- treating LLM text as data truth.
