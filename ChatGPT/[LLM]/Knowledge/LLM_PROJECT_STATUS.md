# [LLM] Project Status

status: minor fix
last_reviewed: 2026-05-25
current score: 8.6/10

## Files present

- `PROJECT_INSTRUCTIONS.md`
- `README.md`
- `Knowledge/AI_OS_REFERENCE.md`
- `Knowledge/EXTERNAL_AI_HANDOFF_PROTOCOL.md`
- `Knowledge/GEMINI_DEEP_RESEARCH__KB_HUNTER.md`
- `Knowledge/LLM_ROUTING.md`
- `Knowledge/LOCAL_LLM_WORKFLOW.md`
- `Knowledge/MEMO_GENERATION_WORKFLOW.md`
- `Knowledge/MODEL_ROUTING.md`
- `Knowledge/PROMPT_LIBRARY.md`
- `Knowledge/PROMPT_REGISTRY.md`
- `Knowledge/QUALITY_GATES.md`
- `Knowledge/ROUTING_AND_HANDOFF.md`
- `Knowledge/SMOKE_QA_FOR_LLM.md`
- `Knowledge/LLM_PROJECT_STATUS.md`
- `Knowledge/EVAL_RUN_TEMPLATE.md`

## Known gaps

- README still remains a lightweight setup file rather than a full operating manual.
- No formal decision archive exists in `[LLM]`; that should stay in the relevant project or handoff record.
- No production automation or CI is defined here.

## Next fix

- Keep README aligned with actual Knowledge files after future additions.

## Acceptance checklist

- [x] README matches actual Knowledge files
- [x] prompt registry exists
- [x] smoke QA file exists
- [x] status file exists
- [x] eval template exists
- [x] no production feature added
- [x] no hardcoded permanent model names added

## Blocked items

- secrets
- raw logs
- full dumps
- vector DB
- embeddings
- autonomous workflows
- web UI as current recommendation
- production-ready claims without acceptance
