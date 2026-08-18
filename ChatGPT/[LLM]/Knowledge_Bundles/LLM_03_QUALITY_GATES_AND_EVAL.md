# [LLM] — Quality Gates and Eval

## Purpose

Compact upload artifact for [LLM] covering quality gates and eval.

## Source files

- `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`
- `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`
- `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`
- `AUTONOMOUS_EXECUTION_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:909bccea4b1950ddfa592a472c49ac57d840fb7c8b62d1388b243005fca41015

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`

# LLM Quality Gates
## Output QA
- [ ] Does the output answer the task?
- [ ] Are facts separated from interpretations?
- [ ] Are unsupported claims marked?
- [ ] Is confidence stated?
- [ ] Are sources/evidence referenced when available?
- [ ] Are limitations visible?
- [ ] Is routing correct?
- [ ] Is the output actionable?
## Hallucination checks
1. Ask: what claims are not supported?
2. Remove or mark them.
3. Check against AI OS or source context when needed.
4. For memo generation, apply the Judge triggers and no-Judge acceptance rule in `MEMO_GENERATION_WORKFLOW.md`.
5. Revise only from explicit findings; a `pass` result does not trigger a rewrite.
## Verdict
```text
quality_status: pass / revise / blocked
reason:
unsupported_claims:
required_revision:
```


## From: `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`

# Eval Run Template
## eval_id
## date
## task_type
## input_summary
## context_package_used
## model_class
## output_type
## evidence_status
## unsupported_claims
## judge_verdict
pass / revise / blocked
## revision_required
## revision_applied
## final_quality_status
## limitations
## owner_project
## next_step


## From: `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`

# [LLM] Smoke QA
Verdict: pass
## Checks
| Test | Expected | Result | Status |
| Routing test | calculation goes to [Analytics] | LLM routing rules send deterministic calculation to `[Analytics]` | pass |
| Implementation test | implementation goes to [Codex] | handoff rules route code and repo changes to `[Codex]` | pass |
| AI OS evidence test | use [AI OS] for KB evidence | evidence rules point to `[AI OS]` for KB-backed claims | pass |
| Fact / interpretation test | facts separated from interpretation | evidence rules require explicit separation | pass |
| Unsupported claims test | unsupported claims are marked | judge and eval gate require unsupported claims listing | pass |
| Secrets / raw dumps test | reject raw dumps / secrets / .env | context rules forbid them | pass |
| Model class test | choose class by task, not permanent model name | routing matrix uses task class | pass |
| Judge/revise test | high-risk outputs run judge then revise | workflow includes judge and revise before final | pass |
| Codex handoff test | package handoff with acceptance criteria | task package requires objective, files, acceptance, rollback | pass |
| Gemini test | treat Gemini output as candidate sources | KB hunter rules treat Gemini output as candidate sources only | pass |
## Issues found
- none
## Required fixes
- none
## Acceptance status
pass


## Autonomous Execution Standard

Execution in `[LLM]` now also follows the canonical Autonomous Execution
Standard defined in `AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above the output QA, hallucination
checks, and judge/eval workflow above as a shared execution/validation/
defect/acceptance loop, without replacing them or the merge policy in
`GOAL_MODE.md`. No `[LLM]`-specific AES extension exists yet; only the
canonical standard is in scope here.

## From: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

# [LLM] Project Status
status: controlled legacy eval debt
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
- Reusable prompt entries are legacy/unversioned and have no recorded eval or owner-acceptance evidence. Priority migration debt is listed in `PROMPT_REGISTRY.md`; no eval pass is inferred.
## Next fix
- Migrate priority reusable prompts to identifiable candidate revisions and run risk-appropriate evals before any new activation decision.
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
