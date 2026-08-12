# [LLM] Project Status

status: controlled legacy eval debt
last_reviewed: 2026-08-12
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
- `Knowledge/RELATIONSHIP_CRM_LITE_TEMPLATE.md`
- `Knowledge/WEEKLY_RELATIONSHIP_REVIEW_BLOCK.md`
- `Knowledge/VALUE_FIRST_OUTREACH_TEMPLATE.md`
- `Knowledge/MEETING_RECAP_TEMPLATE.md`
- `Knowledge/ASK_FOR_ADVICE_TEMPLATE.md`
- `Knowledge/NO_SPAM_HUMAN_REVIEW_RULE.md`
- `Knowledge/EXECUTIVE_SUMMARY_TEMPLATE.md`
- `Knowledge/COMMUNICATION_QA_CHECKLIST.md`
- `Knowledge/CHART_COMMENTARY_STANDARD.md`
- `Knowledge/AUDIT_FINDING_WORDING_TEMPLATE.md`
- `Knowledge/SLIDE_STORYLINE_TEMPLATE.md`
- `Knowledge/CONTEXT_ENGINEERING_PLAYBOOK.md`
- `Knowledge/CONTEXT_INTAKE_CHECKLIST.md`
- `Knowledge/CTC_PROMPT_STANDARD.md`
- `Knowledge/GOOD_BAD_CONTEXT_EXAMPLES.md`
- `Knowledge/LOCAL_AI_EXPERIMENT_PLAYBOOK.md`
- `Knowledge/LOCAL_AI_SECURITY_BOUNDARY.md`
- `Knowledge/LOCAL_MODEL_EVAL_MATRIX.md`
- `Knowledge/OLLAMA_OPENWEBUI_PILOT.md`
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
- Relationship Effectiveness templates are candidate / ready for human review, not a CRM project, outreach pipeline, or automation.
- Communication Pack templates are candidate / ready for human review, not production reporting automation.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or
  owner-acceptance evidence. Priority migration debt is listed in
  `PROMPT_REGISTRY.md`; no eval pass is inferred.

## Next fix

- Migrate priority reusable prompts to identifiable candidate revisions and run
  risk-appropriate evals before any new activation decision.

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
