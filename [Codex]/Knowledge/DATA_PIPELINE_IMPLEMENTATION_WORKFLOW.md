# Data Pipeline Implementation Workflow

## Target shape

```text
RAW → STAGE → MARTS → ANALYSIS → LLM PACKAGE → REPORT → QA → ARCHIVE
```

## Steps

1. Inspect current entrypoints.
2. Identify input/output contracts.
3. Locate raw/stage/mart layers.
4. Preserve existing behavior.
5. Implement scoped change.
6. Add/adjust tests.
7. Run smoke QA.
8. Report acceptance.

## Forbidden

- changing metric definitions silently;
- changing output schema without approval;
- deleting validation;
- mixing generated artifacts with source code;
- adding infrastructure before governance approval.
