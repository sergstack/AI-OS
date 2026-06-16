# Analytical Memo Automation Workflow

## Canonical route

Use the Analytical Memo Factory via Codex APP pattern:

```text
Analyst defines the task
-> [Analytics] structures methodology
-> [Codex] prepares an ultra-long Codex APP task package
-> Codex APP executes
-> Python calculates
-> LLM writes from evidence
-> Judge/QA checks
-> Human accepts
```

`[Codex]` is the task package design layer in this route. Codex APP is the executor layer.

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
