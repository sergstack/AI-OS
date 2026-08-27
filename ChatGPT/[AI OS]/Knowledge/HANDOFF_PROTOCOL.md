# Handoff Protocol

Назначение: как `[AI OS]` передаёт результат в другие Project-папки.

## Continuation contract

Handoff — это внутренний переход между владельцами внутри исходной цели. Handoff completion is not goal completion.

- Поле `Objective` сохраняет исходную цель и не заменяется локальной подзадачей.
- `Expected output` описывает результат текущего этапа, а `Acceptance criteria` сохраняет релевантную часть исходной приёмки.
- Handoff сохраняет evidence, constraints, risks, authority/execution status и путь возврата к текущему владельцу.
- Если capability доступна в текущей среде, а следующий шаг reversible, policy-permitted и уже authorized, вызови capability, проверь её результат и верни его текущему владельцу.
- Если capability недоступна, верни terminal handoff с точной причиной, а не выдавай подготовку handoff за completion.

Вовлекай owner только когда нужно изменить owner-frozen policy, получить explicit governance approval, выбрать между материально разными вариантами без детерминированного предпочтения или выполнить действие с материальным downside/низкой обратимостью. Также эскалируй при недоступных credentials, permissions, money, legal authority, physical action или когда все authorized recovery paths исчерпаны.

Destination вне `PROJECT_CAPABILITIES.yaml`: сначала проверь class в
`ROUTING_RULES.md`: `external` остаётся explicit terminal handoff — не создавай
capability, не вызывай `project-context` и не расширяй полномочия;
`internal_non_capability` продолжай только через названную границу;
`owner_escalation` требует решения владельца.

## Когда делать handoff

Destination выбирается только по `ROUTING_RULES.md`. Если выбран `[Codex]` для
repository work, предпочтительно оформить handoff как GitHub Issue-driven task
package с явным scope, allowed files, checks и acceptance criteria.

## Handoff template

Use the canonical template in `HANDOFF_STYLE_STANDARD.md`. Preserve the
continuation, evidence, confidence, and destination rules in this protocol.

## Thinking → Analytics → LLM → Codex → QA → Release

1. `[Thinking]` формулирует решение, сценарии, риски, assumptions.
2. `[Analytics]` считает deterministic часть: data contracts, marts, metrics, QA.
3. `[LLM]` собирает context package, prompts, model routing, memo workflow.
4. `[Codex]` реализует через Goal Mode handoff или strict task package со scope, checks, rollback и acceptance.
5. QA проверяет evidence, tests, artifacts, regression, smoke checks.
6. Release фиксирует status, residual risks, rollback и changelog.

Для user-facing artifact или business deliverable handoff должен явно отделять business acceptance и artifact/content checks от технических проверок. Технические checks, созданный файл или PR не означают acceptance, если deliverable не удовлетворяет business outcome.

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
