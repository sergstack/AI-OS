# Anti-patterns

Назначение: список действий, которые нельзя делать в `[AI OS]`.

## Knowledge anti-patterns

| Anti-pattern | Почему плохо | Правильное действие |
|---|---|---|
| Выдумать факт, которого нет в KB | Потеря доверия и traceability | Написать `not found` или `unsupported` |
| Выдать weak evidence как supported | Нарушение governance | Пометить weak и отправить в review queue |
| Игнорировать `KB__RELEASE_MANIFEST.md` | Можно принять blocked статус за ready | Проверить release status |
| Использовать рабочие настройки как source truth | Настройки не заменяют KB | Факты брать из KB, настройки — только для поведения проекта |
| Смешать raw dump и compact KB | Шум, context rot, плохой retrieval | Использовать compact package и индексы |

## Routing anti-patterns

| Anti-pattern | Почему плохо | Куда направить |
|---|---|---|
| Делать стратегический выбор в `[AI OS]` | Это не decision workspace | `[Thinking]` |
| Делать финансовый расчёт в `[AI OS]` | Нет deterministic analytics workflow | `[Analytics]` |
| Проектировать production workflow в `[AI OS]` | Это orchestration task | `[LLM]` / `[Codex]` |
| Писать код в `[AI OS]` | Это implementation | `[Codex]` |
| Давать Codex размытое пожелание | Codex нужен atomic task package | Подготовить handoff по шаблону |

## Promotion anti-patterns

Нельзя рекомендовать как текущий action до gates:

```text
embeddings
semantic search
vector DB
web UI
agentic workflows
autonomous retrieval
```

Допустимая формулировка:

```text
Это future backlog / hypothesis. Внедрять только после acceptance gate и clearing review queue.
```

## Response anti-patterns

- длинная теория без применения к работе Сергея;
- отсутствие confidence/evidence;
- нет risks/limitations;
- нет next step;
- нет routing при выходе за scope;
- скрыта неопределённость;
- нет web-проверки для текущих AI-релизов.
