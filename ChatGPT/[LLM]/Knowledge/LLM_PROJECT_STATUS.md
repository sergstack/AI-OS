# [LLM] Project Status

status: controlled legacy eval debt
last_reviewed: 2026-08-21
current score: 8.6/10

## Accepted memo workflow evidence

- workflow: risk-triggered memo review;
- registry status: active;
- owner acceptance: accepted on 2026-08-18;
- corpus: 10 real memo cases from one workbook and period `2026-05`;
- case mix: routine 4, material 2, evidence-sensitive 2, QA-defect 1,
  Judge-defect 1;
- quality: OLD 154/160; NEW 154/160;
- blind verdict: equivalent 10/10;
- false bypass count: 0;
- Judge runs: 10 -> 6 (40% reduction);
- Revise runs: 10 -> 2 (80% reduction);
- semantic LLM stages: 30 -> 18 (40% reduction).

Verdicts:

- workflow quality: PASS;
- safety: PASS;
- logical execution efficiency: PASS;
- token savings: NOT PROVEN;
- billing savings: NOT PROVEN;
- generalization beyond the current corpus: NOT PROVEN.

Evidence boundaries:

- the corpus covers one real workbook and one period, `2026-05`;
- drafts were frozen, so the eval tested the review loop rather than draft
  generation variability;
- the blind Judge used the current environment model, not an independent model;
- provider-level token usage was unavailable;
- elapsed-time attribution was unavailable.

These results accept the current memo review workflow without changing the
project's overall `controlled legacy eval debt` status or resolving the separate
prompt-registry debt below.

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
- `Knowledge/CANDIDATE_GATE_SAMPLED_QA.md`
- `Knowledge/ROUTING_AND_HANDOFF.md`
- `Knowledge/SMOKE_QA_FOR_LLM.md`
- `Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- `Knowledge/LLM_PROJECT_STATUS.md`
- `Knowledge/EVAL_RUN_TEMPLATE.md`
- `Knowledge/LLM_EVAL_STANDARD.md`
- `Knowledge/PROMPT_LIFECYCLE_STANDARD.md`
- `Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`

## Known gaps

- README still remains a lightweight setup file rather than a full operating manual.
- No formal decision archive exists in `[LLM]`; that should stay in the relevant project or handoff record.
- No production automation or CI is defined here.
- Relationship Effectiveness templates are candidate / ready for human review, not a CRM project, outreach pipeline, or automation.
- Communication Pack templates are candidate / ready for human review, not production reporting automation.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or
  owner-acceptance evidence. Priority migration debt is listed in
  `PROMPT_REGISTRY.md`; no eval pass is inferred.
- Cross-project live coverage is partial: `[Inbox Router]` passed; `[AI OS]`
  reproduced a scope-boundary defect by performing model selection and workflow
  design after routing ownership to `[LLM]`; `[LLM]` produced a safe complete
  asset but exceeded its hard 3,500-character cap by 28 characters; four cases
  remain `NOT RUN` under a temporary ChatGPT account-level request limit.
- AI OS corrective evidence: ownership was fixed in two completed reruns. The
  temporary 1,800-character handoff target was rolled back because it could
  remove necessary execution context; the current rule requires a focused,
  executable handoff without an arbitrary length cap. A clean rerun is blocked
  by the ChatGPT rate limit.
- External AI OS, Thinking and LLM Project Instructions match the corrected
  repository files by exact settings read-back.
- LLM post-change validation passed 10/10 at 3,389 visible content characters,
  preserving the prompt, gates, registry and handoffs with 111 characters of
  buffer under the explicit maximum.

## Next fix

- Rerun the synchronized `[AI OS]` compact override after a clean cooldown;
  do not widen it after three correction attempts.
- Complete the four `NOT RUN` cases in `CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
  after the ChatGPT rate limit clears; use only completed responses to justify
  additional Project Instruction changes.
- Migrate priority reusable prompts to identifiable candidate revisions and run
  risk-appropriate evals before any new activation decision.

## Acceptance checklist

- [x] README matches actual Knowledge files
- [x] prompt registry exists
- [x] smoke QA file exists
- [x] cross-project live-eval matrix exists
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

## Bundle semantic migration sources

- `LLM_02_PROMPT_LIBRARY_AND_REGISTRY_BUNDLE_SEMANTICS.md`
- `LLM_03_QUALITY_GATES_AND_EVAL_BUNDLE_SEMANTICS.md`
