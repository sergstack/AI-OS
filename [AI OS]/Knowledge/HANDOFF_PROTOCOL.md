# Handoff Protocol

Назначение: как `[AI OS]` передаёт результат в другие Project-папки.

## Когда делать handoff

| Ситуация | Куда |
|---|---|
| Нужно принять решение или выбрать стратегию | `[Thinking]` |
| Нужно посчитать, построить mart, проверить данные | `[Analytics]` |
| Нужно собрать prompt/workflow/model routing | `[LLM]` |
| Нужно написать код, тесты, refactor, bugfix | `[Codex]` |
| Нужно внедрять production workflow | `[Codex]` / `[LLM]` |

## Handoff template

```text
Handoff to: [Project]
Task type: concept / workflow / analytics / implementation / QA / release
Goal:
Context from AI OS:
KB evidence used:
Confidence:
Inputs required:
Expected output:
Constraints:
Risks:
Acceptance criteria:
Suggested first step:
```

## Thinking → Analytics → LLM → Codex → QA → Release

1. `[Thinking]` формулирует решение, сценарии, риски, assumptions.
2. `[Analytics]` считает deterministic часть: data contracts, marts, metrics, QA.
3. `[LLM]` собирает context package, prompts, model routing, memo workflow.
4. `[Codex]` реализует только по atomic task package с tests/acceptance.
5. QA проверяет evidence, tests, artifacts, regression, smoke checks.
6. Release фиксирует status, residual risks, rollback и changelog.

## Что передавать из [AI OS]

- краткое объяснение концепции;
- relevant KB files;
- supported / weak / unsupported distinction;
- risks;
- recommended project;
- first safe task.

## Что не передавать как факт

- weak evidence без пометки;
- unsupported claims;
- “production ready” без acceptance;
- новые инструменты без свежей проверки;
- implementation details, если они не подтверждены.
