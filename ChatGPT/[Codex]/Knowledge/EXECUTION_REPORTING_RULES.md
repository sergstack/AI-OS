# Codex Execution And Reporting Rules

## Execution modes

- inspect-only: изучи repo, верни files/entrypoints/risks/plan, не редактируй.
- implement: минимально измени allowed files, запусти checks.
- bugfix: reproduce/define failure -> root cause -> minimal patch -> regression check.
- refactor: зафиксируй текущее behavior -> minimal refactor -> regression/golden check.
- test/QA: выбери smallest useful test, запусти/добавь checks, верни pass/fail.
- data pipeline: проверь contracts, grain, raw/stage/marts, reconciliation, artifacts.
- release: acceptance, tests, release notes, rollback, residual risks.

## Planning

Перед edit дай короткий action-oriented plan:

- scope;
- files to inspect/modify;
- assumptions;
- risks;
- tests to run.

Не раскрывай лишнюю internal reasoning.

## Testing

После изменений запусти доступные проверки:

- unit / integration / contract / smoke / golden / data quality / artifact validation;
- build / type check / lint, если они есть и релевантны;
- repo-specific commands из README, package files или task package.

Если тесты не запускались, явно напиши почему и какой минимальный check нужен.

## Review

Перед финальным ответом проверь:

- diff соответствует scope;
- forbidden actions не выполнены;
- output contracts сохранены;
- tests/checks понятны;
- risks и assumptions названы;
- rollback/next step есть.

## Blocker format

```text
blocked_reason:
missing_input:
risk_if_continue:
safe_next_step:
files_inspected:
```

## Final response format

Canonical final report schema:

```text
Summary:
Branch:
Files inspected:
Files changed:
Commands run:
Test results:
Evidence / artifacts:
Assumptions:
Blockers:
Risks:
Rollback:
PR:
Acceptance status:
Merge / gate status:
```

Mode-specific reports may be shorter, but they must not conflict with this schema.

Пиши как инженер: конкретно, проверяемо, без воды.
