# [LLM] — Quality Gates and Eval

## Purpose

Compact upload artifact for [LLM] covering quality gates and eval.

## Source files

- `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`
- `ChatGPT/[LLM]/Knowledge/LLM_EVAL_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`
- `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:1b50d1a723ee49a6726f350ab424371b3f77c058dd0b06b12879ec8063a0f6aa

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`

# LLM Quality Gates
Reusable asset promotion and regression depth follow `LLM_EVAL_STANDARD.md`. Prompt and workflow version status follows `PROMPT_LIFECYCLE_STANDARD.md`.
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
4. Run Judge when the output is material, evidence-sensitive, fails deterministic QA, follows an unreviewed path, or a human requests review.
5. Revise only from explicit findings; a `pass` result does not trigger a rewrite.
## Verdict
```text
quality_status: pass / revise / blocked
reason:
unsupported_claims:
required_revision:
```


## From: `ChatGPT/[LLM]/Knowledge/LLM_EVAL_STANDARD.md`

# LLM Eval Standard
## Purpose
Define minimum, risk-proportional evaluation for reusable `[LLM]` prompt and workflow assets. Evaluation must be sufficient for the cost of error without turning `[LLM]` into an MLOps platform.
## Risk classification
Choose the evaluation level from four primary considerations:
- error cost;
- evidence sensitivity;
- reversibility;
- verification path.
Downstream consequence may also raise the level. Do not use a mandatory numerical risk formula.
## Evaluation levels
### LIGHT
Use for low-risk, reversible workflows whose output is easy to verify, such as formatting, simple rewriting, structure transformation, or low-risk extraction with easy manual verification.
Minimum:
- schema or smoke check;
- 1-3 representative cases;
- owner check.
LIGHT does not require a full regression suite or heavyweight eval suite.
### CONTROLLED
Use for reusable workflows where an error may affect downstream analysis, decision support, or a repeated process.
Minimum:
- representative cases;
- negative and boundary cases;
- materially relevant historical failures;
- regression protection;
- Judge/revise where appropriate;
- owner acceptance.
### HIGH-RISK
Use for evidence-sensitive or consequential workflows.
Minimum:
- extended representative set;
- boundary and adversarial cases;
- historical failure cases;
- workflow-specific Judge fixtures;
- deterministic verification where applicable;
- explicit human acceptance;
- visible limitations.
HIGH-RISK does not authorize an LLM to perform deterministic calculations. Route `[Analytics]` calculations and analytical work to `[Analytics]`.
## Evaluation types
### Pre-promotion / offline eval
Checks a candidate before promotion and governed reuse.
### Regression eval
Checks that a material change has not reintroduced known failure modes. Regression cases should primarily come from materially relevant historical failures or corrections; not every comment needs to become a regression test.
### Runtime/output QA
Checks a specific output produced during workflow use. Runtime QA does not by itself prove the quality of the reusable asset.
## Deterministic before Judge
If a criterion can be checked deterministically, perform that check before relying on an LLM Judge. Examples include:
- required sections and schema fields;
- enum and exact status values;
- file presence;
- routing owner;
- forbidden field detection;
- simple contract validation.
Use Judge evaluation for semantic or evidence-sensitive criteria. A Judge is not absolute truth.
## Ownership boundary
`[AI OS]` owns:
- canonical Judge doctrine;
- evaluator governance and calibration principles;
- generic evidence/confidence semantics;
- generic promotion governance.
`[LLM]` owns:
- workflow-specific rubrics;
- domain, negative, and boundary cases;
- expected outcomes;
- historical regression fixtures.
`[LLM]` provides workflow-specific test fixtures for the canonical Judge mechanism. It does not own a separate generic Judge calibration standard.
## Evidence, evaluation, and acceptance
Keep these operational concepts separate:
```text
evidence_status -> follows canonical [AI OS] semantics
workflow_eval -> result for a specific LLM asset or workflow
acceptance_status -> owner or human-gate decision
```
Do not introduce model confidence, Judge confidence, a workflow-confidence score, or a multi-level confidence architecture. Self-reported LLM confidence is not a governance metric or a calibrated probability. Model uncertainty may be recorded as a textual limitation.
## Failure to regression
When a failure materially affected output, can recur, and belongs to reusable behavior, consider its case as a candidate regression fixture. Keep the reference in existing eval records; do not create a separate Failure Registry.
## Local AI boundary
Existing `LOCAL_AI_EXPERIMENT_PLAYBOOK.md`, `LOCAL_AI_SECURITY_BOUNDARY.md`, and local pilot rules remain authoritative:
- local output is draft/candidate evidence;
- local retrieval is not final truth;
- only curated context is allowed;
- limitations are required;
- production truth is prohibited without appropriate QA.
Risk-aware use:
- low risk: a local result may be sufficient after deterministic/schema verification passes;
- controlled: use a local draft with stronger or Judge verification where needed;
- high-risk or evidence-sensitive: local processing may prepare a draft, but consequential conclusions require stronger verification and a human gate.
This is an operational interpretation, not a separate permanent escalation architecture.
## Context boundary
Follow the existing Context Engineering standards for curated context, facts versus assumptions, forbidden secrets, Context Pack/CTC selection, and quality gates. Do not duplicate the Context Pack schema here.


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


## From: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

# [LLM] Project Status
status: minor fix
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
- `Knowledge/LLM_EVAL_STANDARD.md`
- `Knowledge/MODEL_ROUTING.md`
- `Knowledge/PROMPT_LIFECYCLE_STANDARD.md`
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
