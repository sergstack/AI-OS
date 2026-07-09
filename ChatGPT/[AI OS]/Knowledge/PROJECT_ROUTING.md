# Project Routing

Назначение: определить, в каком ChatGPT Project должна решаться задача.

Scope note: this file is the `[AI OS]` project routing and handoff reference.
Canonical front-door routing lives in
`ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md`. If raw-input triage and
AI OS scoped routing differ, use Inbox Router for triage and this file for
AI OS evidence/governance scope.

## Главный принцип

Сначала routing, потом reasoning.

| Тип задачи | Куда направлять | Почему |
|---|---|---|
| Понять AI-концепцию | `[AI OS]` | Здесь KB по AI-трендам, моделям, паттернам |
| Найти AI-use case | `[AI OS]` | Здесь use cases и связь с работой Сергея |
| Сравнить AI-подходы | `[AI OS]` | Здесь pattern/evidence слой |
| Найти supported/weak evidence | `[AI OS]` | Здесь confidence/governance слой |
| Принять стратегическое решение | `[Thinking]` | Там сценарии, риски, decision memo, judge/revisor |
| Посчитать финансовую модель или метрики | `[Analytics]` | Там deterministic расчёты, marts, QA |
| Спроектировать prompt/workflow/model routing | `[LLM]` | Там prompt library и orchestration |
| Подготовить coding task | `[Codex]` или `[LLM]` | Там task packages и implementation workflow |
| Реализовать код | `[Codex]` | `[AI OS]` не пишет production-код |
| Проверить production readiness | `[Codex]` / `[LLM]` / `[AI OS]` | Зависит от типа evidence и реализации |

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

## Routing response pattern

```text
Маршрут: [AI OS] / [Thinking] / [Analytics] / [LLM] / [Codex]
Почему: ...
Что можно сделать здесь: ...
Что нужно передать дальше: ...
Evidence/confidence: ...
```

## Handoff rule

Если задача выходит за пределы `[AI OS]`, дай короткий handoff:

```text
Handoff to: [Project]
Goal: ...
Context from KB: ...
Inputs needed: ...
Expected output: ...
Risks / constraints: ...
```
