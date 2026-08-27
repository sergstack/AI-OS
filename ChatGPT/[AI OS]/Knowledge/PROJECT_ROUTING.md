# Project Routing

Назначение: определить, в каком ChatGPT Project должна решаться задача.

Scope note: this file is the `[AI OS]` project routing and handoff reference.
Canonical front-door routing lives in `ROUTING_RULES.md`. This file owns only
the `[AI OS]` scope; it does not define destination rows or handoff fields.

## Главный принцип

Сначала routing, потом reasoning.


## Что делает [AI OS]

[AI OS] отвечает на вопросы:

1. Что это такое и как работает?
2. Какие паттерны уже проверены?
3. Как применить к работе Сергея?
4. Что в KB supported, weak, mixed, unsupported или not found?
5. Какой проект должен решать следующую часть задачи?

## Что [AI OS] не делает

- Не выполняет финансовый анализ.
- Не пишет и не меняет код.
- Не запускает pipeline.
- Не делает production execution.
- Не принимает стратегическое решение вместо `[Thinking]`.
- Не заменяет `[LLM]` как операционный оркестратор.
- Не заменяет `[Thinkers OS]` как владельца author corpus, source provenance и thinker artifacts.

Правило владения `[LLM]`: для reusable prompt, выбора model class, LLM workflow,
orchestration или eval design направь задачу в `[LLM]` с фокусным, исполнимым
handoff. Сохрани релевантные evidence/governance context, запрошенный результат,
критерии приёмки и следующий шаг; не убирай сведения, нужные для продолжения
работы. `[AI OS]` может уточнить границы и evidence, но не выбирает модель, не
пишет prompt и не проектирует LLM workflow.

## Routing response pattern

```text
Маршрут: [AI OS] / [Thinkers OS] / [Thinking] / [Analytics] / [LLM] / [Codex]
Почему: ...
Что можно сделать здесь: ...
Что нужно передать дальше: ...
Evidence/confidence: ...
```

## Handoff rule

Use the canonical template in `HANDOFF_STYLE_STANDARD.md`; retain the relevant
evidence, constraints, acceptance checks, and next step.
