# [LLM] — Quality Gates and Eval

## Purpose

Compact upload artifact for [LLM] covering quality gates and eval.

## Source files

- `ChatGPT/[LLM]/Knowledge/QUALITY_GATES.md`
- `ChatGPT/[LLM]/Knowledge/EVAL_RUN_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/SMOKE_QA_FOR_LLM.md`
- `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`
- `AUTONOMOUS_EXECUTION_STANDARD.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:38c514b92bd318b17ddcfba330fffade19e31c985558623e9337f6510477ff43

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
Date: 2026-08-21
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

## Cross-project live coverage

Matrix: `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` (`LLM-XPROJECT-LIVE-001`,
`1.0.0-candidate`).

| Live case | Result | Evidence |
|---|---|---|
| `[Inbox Router]` → `[LLM]` | pass, 9/10 | strong single route, bounded handoff, target workflow not solved in the router |
| `[AI OS]` → `[LLM]` | blocked, 5/10 | route named correctly, but `[AI OS]` selected the model class and designed the workflow instead of handing off |
| `[LLM]` compact asset | revise, 9/10 | safe complete asset exceeded the 3,500-character cap by 28 visible content characters |
| `[Thinking]`, `[Analytics]`, `[Codex]`, `[Thinkers OS]` | not run | ChatGPT rate limit prevented completed observable responses |

Static smoke QA remains `pass`. Cross-project live coverage is `partial`; a
rate-limited case is not a product failure and is not evidence for changing
Project Instructions.

## Issues found
- the reproduced AI OS/LLM scope-boundary defect is resolved in two completed reruns;
- the temporary AI OS compactness cap was rolled back; the replacement preserves
  executable handoff context without an arbitrary length limit, pending a clean live rerun;
- one reproduced LLM compactness defect;
- four live cases remain unobserved because of an external ChatGPT rate limit.

## Required fixes
- rerun the synchronized AI OS compact override after a clean cooldown; do not widen it after three correction attempts;
- rerun only the four `NOT RUN` cases after the rate limit clears;
- make no other Project behavior change without a reproduced defect.

## Acceptance status
static pass; cross-project live coverage partial


## From: `ChatGPT/[LLM]/Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`

# Cross-Project LLM Live Eval Matrix

- matrix_id: `LLM-XPROJECT-LIVE-001`
- version: `1.0.0-candidate`
- owner_project: `[LLM]`
- status: `optimization_partial`
- production_status: `NOT AUTHORIZED`

The matrix uses one exact prompt for each of the seven ChatGPT Projects and
scores route correctness, scope boundary, handoff completeness, evidence/QA
preservation and compact operability. A rate limit, authentication loss or
ambiguous Project identity is recorded as `NOT RUN`, not fail.

Observed baseline: `[Inbox Router]` passed 9/10 with one strong route to
`[LLM]`, a bounded handoff and no target-workflow solution. `[AI OS]` scored
5/10: it named `[LLM]` as owner, then selected the model class and designed the
workflow itself. `[Analytics]`, `[Codex]` and `[Thinkers OS]` produced partial
diagnostic fragments before the rate-limit dialog interrupted generation;
`[Thinking]` did not produce a response. `[LLM]` completed at 3,528 visible
content characters and remains `REVISE` against its 3,500 cap. The four
incomplete cases remain `NOT RUN`. Overall baseline status: `PARTIAL`.

AI OS corrective evidence: two completed reruns fixed ownership; response size
fell from 4,794 to 2,475 characters but remains above the compact target. A
third rerun was interrupted and is `NOT RUN`. The synchronized `[LLM]` hard-cap
rule passed its completed post-change rerun at 3,389 visible characters with
all requested controls preserved.


## Autonomous Execution Standard

Execution in `[LLM]` now also follows the canonical Autonomous Execution
Standard defined in `AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above the output QA, hallucination
checks, and judge/eval workflow above as a shared execution/validation/
defect/acceptance loop, without replacing them or the merge policy in
`GOAL_MODE.md`. No `[LLM]`-specific AES extension exists yet; only the
canonical standard is in scope here. Closure Review rechecks prompt and
input-context contracts, output schema, unsupported claims, eval regressions,
and routing ownership before acceptance.

After routing resolves a material decision or deliverable owner, `[LLM]` may
preserve evidence, contradictions, constraints, and a bounded handoff, but it
must not silently substitute its judgment for the resolved owner.

## From: `ChatGPT/[LLM]/Knowledge/LLM_PROJECT_STATUS.md`

# [LLM] Project Status
status: controlled legacy eval debt
last_reviewed: 2026-08-21

## Accepted memo workflow evidence
- workflow: risk-triggered memo review
- registry status: active
- owner acceptance: accepted on 2026-08-18
- corpus: 10 real memo cases from one workbook and period `2026-05`
- case mix: routine 4, material 2, evidence-sensitive 2, QA-defect 1, Judge-defect 1
- quality: OLD 154/160; NEW 154/160
- blind verdict: equivalent 10/10
- false bypass count: 0
- Judge runs: 10 -> 6 (40% reduction)
- Revise runs: 10 -> 2 (80% reduction)
- semantic LLM stages: 30 -> 18 (40% reduction)

Verdicts:
- workflow quality: PASS
- safety: PASS
- logical execution efficiency: PASS
- token savings: NOT PROVEN
- billing savings: NOT PROVEN
- generalization beyond the current corpus: NOT PROVEN

Evidence boundaries:
- one real workbook and one period, `2026-05`
- frozen drafts; review-loop tested, not draft-generation variability
- blind Judge used the current environment model, not an independent model
- provider-level token usage unavailable
- elapsed-time attribution unavailable

The accepted memo workflow does not resolve the separate legacy prompt-eval debt.

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
- `Knowledge/CROSS_PROJECT_LIVE_EVAL_MATRIX.md`
- `Knowledge/LLM_PROJECT_STATUS.md`
- `Knowledge/EVAL_RUN_TEMPLATE.md`
## Known gaps
- README still remains a lightweight setup file rather than a full operating manual.
- No formal decision archive exists in `[LLM]`; that should stay in the relevant project or handoff record.
- No production automation or CI is defined here.
- Relationship Effectiveness templates are candidate / ready for human review, not a CRM project, outreach pipeline, or automation.
- Communication Pack templates are candidate / ready for human review, not production reporting automation.
- Reusable prompt entries are legacy/unversioned and have no recorded eval or owner-acceptance evidence. Priority migration debt is listed in `PROMPT_REGISTRY.md`; no eval pass is inferred.
- Cross-project live coverage is partial: `[Inbox Router]` passed; `[AI OS]` reproduced a scope-boundary defect that was fixed in two completed reruns. Its later arbitrary compactness cap was rolled back in favour of a focused executable handoff; the clean rerun is `NOT RUN` under the ChatGPT account-level request limit. `[LLM]` passed the corrected explicit hard cap at 3,389 visible characters; four baseline cases remain `NOT RUN`.
- External AI OS, Thinking and LLM Project Instructions match the corrected repository files by exact settings read-back.
- LLM post-change validation passed 10/10 at 3,389 visible content characters, preserving the prompt, gates, registry and handoffs with 111 characters of buffer under the explicit maximum.
## Next fix
- Rerun the synchronized `[AI OS]` focused-handoff rule after a clean cooldown; do not change it without a completed reproduced defect.
- Complete the four `NOT RUN` cases in `CROSS_PROJECT_LIVE_EVAL_MATRIX.md` after the ChatGPT rate limit clears; use only completed responses to justify additional Project Instruction changes.
- Migrate priority reusable prompts to identifiable candidate revisions and run risk-appropriate evals before any new activation decision.
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
