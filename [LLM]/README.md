# [LLM] Project Setup

## Что это

`[LLM]` — проект для prompting, model routing, orchestration, local/Ollama/OpenAI workflows, quality gates и memo generation.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
Project/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Загрузи все файлы из:

```text
Project/Knowledge/
```

## Файлы Knowledge

- `LLM_ROUTING.md` — выбор LLM workflow.
- `PROMPT_LIBRARY.md` — библиотека промптов.
- `MODEL_ROUTING.md` — выбор модели.
- `QUALITY_GATES.md` — проверки качества.
- `LOCAL_LLM_WORKFLOW.md` — local/Ollama/Open WebUI workflow.
- `MEMO_GENERATION_WORKFLOW.md` — draft → judge → revise.
- `ROUTING_AND_HANDOFF.md` — передача в другие проекты.
- `AI_OS_REFERENCE.md` — связь с существующей AI OS KB.

## Что не делать

Не превращать LLM в расчётный слой, не загружать raw dumps, не хранить API keys.
