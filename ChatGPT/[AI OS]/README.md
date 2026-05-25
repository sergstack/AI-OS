# [AI OS] Project Setup

Назначение: отдельная настройка существующего ChatGPT Project `[AI OS]`.

Этот пакет **не заменяет** уже загруженную governed KB. Он добавляет рабочие настройки проекта: routing, правила использования KB, governance, workflow, handoff и smoke QA.

## Структура

```text
[AI OS]/
└── Project/
    ├── README.md
    ├── PROJECT_INSTRUCTIONS.md
    └── Knowledge/
        ├── AI_OS_PROJECT_FILES_INDEX.md
        ├── PROJECT_ROUTING.md
        ├── KB_USAGE_RULES.md
        ├── GOVERNANCE_RULES.md
        ├── AI_OS_WORKFLOW.md
        ├── HANDOFF_PROTOCOL.md
        ├── SMOKE_QA_FOR_AI_OS.md
        └── ANTI_PATTERNS.md
```

## Что делать

1. Открой существующий ChatGPT Project `[AI OS]`.
2. Скопируй содержимое `PROJECT_INSTRUCTIONS.md` в поле Project Instructions.
3. Загрузи в Project Knowledge только файлы из папки `Knowledge/`.
4. Не удаляй существующие KB-файлы.
5. Используй два индекса:
   - `KB__00_INDEX.md` — индекс базы знаний;
   - `AI_OS_PROJECT_FILES_INDEX.md` — индекс рабочих файлов этого пакета.

## Что не загружать повторно

Не загружай заново всю KB, если она уже есть в проекте.
Не загружай архивы, raw transcripts, source cards, clean notes, chunks, temp, logs, embeddings, vector DB или runtime artifacts.

## Статус

- Тип пакета: project settings / lightweight operational memory.
- Production status: не production-promotion.
- Evidence: mixed — проектная настройка опирается на supported KB governance, но сами новые файлы являются configuration synthesis.
