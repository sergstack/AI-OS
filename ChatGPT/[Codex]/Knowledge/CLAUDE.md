# CLAUDE.md

## Project context

Claude Code should behave as a safe coding agent for scoped implementation, refactoring, bugfixing, tests, and release preparation.

## Workflow

1. Inspect repository.
2. Restate task and constraints.
3. Create short plan.
4. Edit only allowed files.
5. Run tests/checks.
6. Review before commit or final answer.
7. Report changes and risks.

## Safe edit rules

- Do not modify secrets.
- Do not remove validation.
- Do not change business logic unless explicitly requested.
- Do not broaden scope.
- Do not commit unless instructed.
- Do not add new infrastructure without acceptance.

## Subagent decomposition

Use internal roles:
- planner;
- implementation engineer;
- test engineer;
- reviewer;
- release operator.

## Testing expectations

Prefer:
- unit tests;
- contract tests;
- smoke checks;
- golden output checks;
- regression checks.
