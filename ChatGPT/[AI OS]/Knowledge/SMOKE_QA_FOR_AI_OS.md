# Smoke QA For AI OS

Назначение: проверить, что `[AI OS]` после обновления настроек использует KB и routing правильно.

## Минимальная проверка после загрузки

Задай проекту эти вопросы.

### 1. Navigation

```text
Какие два индекса есть в [AI OS] и чем они отличаются?
```

Pass condition:
- называет `KB__00_INDEX.md` как индекс базы знаний;
- называет `AI_OS_PROJECT_FILES_INDEX.md` как индекс рабочих файлов.

### 2. Scope

```text
Для чего использовать [AI OS], а что нужно отправлять в [LLM], [Analytics], [Thinking] и [Codex]?
```

Pass condition:
- не смешивает роли проектов;
- явно говорит, что `[AI OS]` не пишет код и не делает финансовые расчёты.

### 3. Evidence

```text
Объясни любой AI-паттерн из KB и укажи confidence/evidence.
```

Pass condition:
- проверяет KB;
- указывает источники;
- разделяет supported/weak/unsupported.

### 4. Governance

```text
Можно ли сейчас добавлять embeddings, semantic search или vector DB?
```

Pass condition:
- говорит, что это заблокировано до acceptance/promotion gate;
- не выдаёт как текущую рекомендацию;
- не формирует implementation-ready `[Codex]` handoff и не предлагает внедрение как текущий next step;
- разрешает conceptual discussion и оставляет следующий шаг на уровне governance review / promotion decision / evidence collection.

### 5. Handoff

```text
Мне нужно превратить найденный AI-паттерн в задачу для Codex. Что делать?
```

Pass condition:
- даёт handoff to `[Codex]`;
- включает goal, context, evidence, constraints, acceptance criteria.

## Acceptance note

Smoke QA не означает production readiness. Это только проверка, что проект следует routing, KB usage и governance.
