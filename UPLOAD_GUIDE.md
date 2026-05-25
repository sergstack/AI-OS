# Upload Guide — [AI OS]

## 1. Project Instructions

Скопируй весь текст из:

```text
[AI OS]/Project/PROJECT_INSTRUCTIONS.md
```

в поле **Project Instructions** существующего ChatGPT Project `[AI OS]`.

## 2. Project Knowledge

Загрузи только эти файлы:

```text
[AI OS]/Project/Knowledge/AI_OS_PROJECT_FILES_INDEX.md
[AI OS]/Project/Knowledge/PROJECT_ROUTING.md
[AI OS]/Project/Knowledge/KB_USAGE_RULES.md
[AI OS]/Project/Knowledge/GOVERNANCE_RULES.md
[AI OS]/Project/Knowledge/AI_OS_WORKFLOW.md
[AI OS]/Project/Knowledge/HANDOFF_PROTOCOL.md
[AI OS]/Project/Knowledge/SMOKE_QA_FOR_AI_OS.md
[AI OS]/Project/Knowledge/ANTI_PATTERNS.md
```

## 3. Не загружать

Не загружай повторно весь KB package, если он уже есть.
Не загружай:

```text
zip archives
raw transcripts
source-card dumps
clean-note dumps
chunks
temp files
logs
runtime artifacts
embeddings
vector DB
secrets
.env
```

## 4. После загрузки

Задай smoke questions из:

```text
SMOKE_QA_FOR_AI_OS.md
```

Минимально проверить:

1. Проект различает `KB__00_INDEX.md` и `AI_OS_PROJECT_FILES_INDEX.md`.
2. Проект маршрутизирует задачи в правильные папки.
3. Проект не выдаёт weak evidence как supported.
4. Проект не рекомендует blocked promotion items.

## 5. Статус

Этот пакет не делает `[AI OS]` production-promoted. Он только обновляет project behavior и operational memory.
