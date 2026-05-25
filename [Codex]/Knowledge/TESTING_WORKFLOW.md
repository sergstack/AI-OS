# Testing Workflow

## Test types

- unit tests;
- integration tests;
- contract tests;
- smoke tests;
- golden output regression;
- data quality checks;
- artifact validation.

## Steps

1. Identify risk.
2. Choose smallest useful test.
3. Run existing tests first if possible.
4. Add tests only where useful.
5. Report pass/fail/blocked.

## Smoke test command format

```bash
# example
pytest tests/
python scripts/validate_artifact_outputs.py
```

Use actual repo commands from the task package.
