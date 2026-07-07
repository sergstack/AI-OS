# [AI OS] Project Setup

Назначение: отдельная настройка существующего ChatGPT Project `[AI OS]`.

Этот пакет **не заменяет** уже загруженную governed KB. Он добавляет рабочие настройки проекта: routing, правила использования KB, governance, workflow, handoff и smoke QA.

## Структура

```text
ChatGPT/[AI OS]/
├── PROJECT_INSTRUCTIONS.md
├── README.md
├── Knowledge/
└── Knowledge_Bundles/
```

## Что делать

1. Открой существующий ChatGPT Project `[AI OS]`.
2. Скопируй содержимое `PROJECT_INSTRUCTIONS.md` в поле Project Instructions.
3. Для обычного sync используй compact bundles из `Knowledge_Bundles/UPLOAD_LIST.md`.
4. Загружай granular `Knowledge/` files только в advanced/debug режиме.
5. Не удаляй существующие KB-файлы.
6. Используй два индекса:
   - `KB__00_INDEX.md` — индекс базы знаний;
   - `AI_OS_PROJECT_FILES_INDEX.md` — индекс рабочих файлов этого пакета.

## Что не загружать повторно

Не загружай заново всю KB, если она уже есть в проекте.
Не загружай архивы, raw transcripts, source cards, clean notes, chunks, temp, logs, embeddings, vector DB или runtime artifacts.

## Статус

- Тип пакета: project settings / lightweight operational memory.
- Production status: не production-promotion.
- Evidence: mixed — проектная настройка опирается на supported KB governance, но сами новые файлы являются configuration synthesis.
