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
| Управлять thinker corpus, source requests, author artifacts и cross-author synthesis | `[Thinkers OS]` | Там source-backed author pipeline и portfolio state |
| Применить thinker patterns к реальному решению | `[Thinking]` | Thinker artifacts — evidence input; decision ownership остаётся в `[Thinking]` |
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

Если задача выходит за пределы `[AI OS]`, дай короткий handoff:

```text
Handoff to: [Project]
Goal: ...
Context from KB: ...
Inputs needed: ...
Expected output: ...
Risks / constraints: ...
```
