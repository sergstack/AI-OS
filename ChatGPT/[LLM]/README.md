# [LLM] Project Setup

## Что это

`[LLM]` — проект для prompting, model routing, orchestration, local/Ollama/OpenAI workflows, quality gates и memo generation.

## Что копировать в Project Instructions

Скопируй содержимое:

```text
ChatGPT/[LLM]/PROJECT_INSTRUCTIONS.md
```

## Что загружать в Knowledge

Default upload mode: compact bundles. Загружай bundle files из:

```text
ChatGPT/[LLM]/Knowledge_Bundles/UPLOAD_LIST.md
```

Granular файлы из `ChatGPT/[LLM]/Knowledge/` загружай только в advanced/debug режиме.

## Файлы Knowledge

- `AI_OS_REFERENCE.md` — связь с существующей AI OS KB.
- `EXTERNAL_AI_HANDOFF_PROTOCOL.md` — external AI handoff protocol.
- `GEMINI_DEEP_RESEARCH__KB_HUNTER.md` — Gemini KB hunter workflow.
- `LLM_ROUTING.md` — выбор LLM workflow.
- `LOCAL_LLM_WORKFLOW.md` — local/Ollama/Open WebUI workflow.
- `MEMO_GENERATION_WORKFLOW.md` — draft → judge → revise.
- `RELATIONSHIP_CRM_LITE_TEMPLATE.md` — candidate relationship CRM-lite fields, no real contact data.
- `WEEKLY_RELATIONSHIP_REVIEW_BLOCK.md` — candidate weekly relationship review block.
- `VALUE_FIRST_OUTREACH_TEMPLATE.md` — candidate value-first outreach draft.
- `MEETING_RECAP_TEMPLATE.md` — candidate meeting recap template.
- `ASK_FOR_ADVICE_TEMPLATE.md` — candidate ask-for-advice template.
- `NO_SPAM_HUMAN_REVIEW_RULE.md` — no-spam and human-review guardrail.
- `EXECUTIVE_SUMMARY_TEMPLATE.md` — candidate executive summary from approved facts.
- `COMMUNICATION_QA_CHECKLIST.md` — candidate QA for communication outputs.
- `CHART_COMMENTARY_STANDARD.md` — candidate chart commentary standard.
- `AUDIT_FINDING_WORDING_TEMPLATE.md` — candidate cautious audit finding wording.
- `SLIDE_STORYLINE_TEMPLATE.md` — optional candidate storyline outline, not a deck generator.
- `CONTEXT_ENGINEERING_PLAYBOOK.md` — lightweight context engineering workflow.
- `CONTEXT_INTAKE_CHECKLIST.md` — проверка входящего контекста перед prompting/Context Pack.
- `CTC_PROMPT_STANDARD.md` — CTC quick prompt structure для мелких задач.
- `GOOD_BAD_CONTEXT_EXAMPLES.md` — примеры хорошего и плохого context engineering.
- `LOCAL_AI_EXPERIMENT_PLAYBOOK.md` — controlled local AI / home server experiment layer.
- `LOCAL_AI_SECURITY_BOUNDARY.md` — security boundary для local AI экспериментов.
- `LOCAL_MODEL_EVAL_MATRIX.md` — checklist evals полезности локальных моделей.
- `OLLAMA_OPENWEBUI_PILOT.md` — safe pilot Ollama / Open WebUI.
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
