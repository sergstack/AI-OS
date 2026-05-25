# [LLM] Project Setup

## Что это

`[LLM]` — проект для prompting, model routing, orchestration, local/Ollama/OpenAI workflows, quality gates и memo generation.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Загрузи все файлы из:

```text
ChatGPT/[LLM]/Knowledge/
```

## Файлы Knowledge

- `AI_OS_REFERENCE.md` — связь с существующей AI OS KB.
- `EXTERNAL_AI_HANDOFF_PROTOCOL.md` — external AI handoff protocol.
- `GEMINI_DEEP_RESEARCH__KB_HUNTER.md` — Gemini KB hunter workflow.
- `LLM_ROUTING.md` — выбор LLM workflow.
- `LOCAL_LLM_WORKFLOW.md` — local/Ollama/Open WebUI workflow.
- `MEMO_GENERATION_WORKFLOW.md` — draft → judge → revise.
- `MODEL_ROUTING.md` — выбор модели.
- `PROMPT_LIBRARY.md` — библиотека промптов.
- `PROMPT_REGISTRY.md` — controlled registry for reusable prompts.
- `QUALITY_GATES.md` — проверки качества.
- `ROUTING_AND_HANDOFF.md` — передача в другие проекты.
- `SMOKE_QA_FOR_LLM.md` — smoke QA checklist.
- `LLM_PROJECT_STATUS.md` — current project status.
- `EVAL_RUN_TEMPLATE.md` — eval run template.

## Что не делать

Не превращать LLM в расчётный слой, не загружать raw dumps, не хранить API keys.
