# [AI OS] — Cross-Project AI Evals

## Purpose

Compact upload artifact for [AI OS] covering lightweight AI eval and LLM-as-a-Judge governance across projects.

## Source files

- `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`
- `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`
- `ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md`
- `ChatGPT/[AI OS]/Knowledge/CROSS_PROJECT_EVAL_PLAYBOOK.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[AI OS]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- runtime_eval_automation: no
- acceptance_status: candidate / ready for human review
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:8d29dad5e2e797e8acc64276ffadffd69537bcd339e3f2da1a516e0f423a7093
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`

# AI Eval Registry
## Purpose
Single lightweight registry of AI evals across AI-OS projects.
This registry defines eval standards only. It does not store run results, runtime logs, eval databases, or benchmark outputs.
## Eval Status Values
- `draft`
- `candidate`
- `active`
- `blocked`
- `deprecated`
## Verdict Values
- `pass`
- `revise`
- `blocked`
## Core Rule
LLM-as-a-Judge is a reviewer, not truth.
Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business rules.
## Registry
| eval_id | workflow | owner_project | task_type | eval_type | judge/check | pass criteria | revise criteria | blocked criteria | last_reviewed | status |
|---|---|---|---|---|---|---|---|---|---|---|
| `AIOS-EVIDENCE` | AI OS evidence answer | `[AI OS]` | claim / pattern / governance | evidence | confidence and source check | supported evidence or clearly marked weak/mixed/not found | missing confidence, weak sourcing, unclear routing | unsupported claim presented as fact or blocked promotion item recommended | 2026-07-06 | active |
| `LLM-OUTPUT` | output QA; memo review is risk-triggered | `[LLM]` | prompt output / memo text | deterministic QA + triggered judge | output contract passes; required Judge passes when triggered | explicit QA or Judge findings require a bounded revision | hallucinated sources, hidden blockers, no evidence path, or required Judge omitted | 2026-08-18 | active |
| `ANALYTICS-QA` | analytical memo / QA | `[Analytics]` | data / memo / mart | deterministic QA + narrative judge | data contract, source mart/table, metric, period, grain, QA status | deterministic QA passes and memo claims trace to evidence | fixable missing method, limitation, or traceability field | failed reconciliation, missing contract, unclear grain, or unapproved formula/schema change | 2026-07-06 | active |
| `CODEX-PR` | PR Judge | `[Codex]` / `[Thinking]` | repo change / PR | workflow eval | diff, checks, scope, rollback | goal match, checks observed, rollback and risks visible | bounded scope or documentation fixes needed | secrets, production risk, failing checks, unsafe scope, or missing acceptance | 2026-07-06 | active |
| `AGENT-LOOP` | supervised loop review | `[AI OS]` / `[Thinking]` | loop design | governance eval | loop acceptance checklist | supervised loop, bounded retry, stop conditions, human acceptance | missing owner, retry rule, or stop condition | autonomous retrieval, uncontrolled agents, runtime artifacts, or no validation | 2026-07-06 | active |
| `ACT-ABSTAIN` | act-or-abstain decision | `[AI OS]` / routed owner | supervised workflow | governance eval | deterministic authority/evidence/validation check | expected and actual decision match | bounded decision mismatch or incomplete evidence | hard-boundary violation or no validation path | 2026-08-27 | candidate |
| `GOAL-CLOSURE` | AES Closure Review view | routed owner / `[AI OS]` | candidate output or change | closure eval | final evidence against original goal, acceptance, and owner boundary | checks pass and all closure dimensions satisfied | repairable goal or acceptance gap | missing acceptance/evidence or owner-boundary violation | 2026-08-27 | candidate |
| `FAILURE-REGRESSION` | observed failure lifecycle | routed owner / `[AI OS]` | workflow failure | deterministic-first regression | failure evidence and explicit expected contract | confirmed failure has a bounded regression case where material | evidence or expected contract incomplete | hard boundary or no validation path | 2026-08-27 | candidate |
| `BASELINE-REGRESSION` | baseline vs candidate | routed owner / `[AI OS]` | configuration change | regression matrix | accepted baseline, same required cases, deterministic checks | no hard regression and complete comparison | repairable or inconclusive comparison | unknown baseline, hard regression, or authority expansion | 2026-08-27 | candidate |
| `INTERMEDIATE-ASSERTION` | analytical intermediate state | `[Analytics]` / `[Codex]` | stage/mart/evidence QA | deterministic assertion | accepted analytical contract | all applicable checks pass | contract needs clarification or check not run | failed reconciliation/cardinality or unknown contract | 2026-08-27 | candidate |
| `CANDIDATE-GATE-SAMPLED-QA` | Candidate Gate sampled QA | `[LLM]` | selected-result relevance | reviewed-sample precision + replay | owner/reviewer labels; same-sample replay | current-run sample is traceable, labels and scoped observed precision are recorded, false positives and available attribution are shown, replay and owner decision are complete | incomplete review evidence, comparison, or owner decision | no current-run sample provenance or reviewer labels; recall claimed without a labelled denominator; automatic Candidate Gate change | 2026-08-27 | candidate |
| `THINKING-DECISION` | decision review | `[Thinking]` | decision memo / strategy | judge | assumptions, downside, reversibility, revisit trigger | options, risks, confidence, and revisit trigger are explicit | weak assumptions or missing downside can be revised | one-option decision, hidden blocker, or unsupported recommendation | 2026-07-06 | active |
## Required Eval Types
### AI OS Evidence Eval
Checks whether claims are supported, weak, mixed, unsupported, or not found.
### LLM Output Eval
Checks schema, facts vs interpretation, unsupported claims, evidence references,
limitations, and risk-appropriate judge/revise. For memo generation, the active
specialization is deterministic QA first, Judge only when a documented trigger
applies, and revision only from explicit findings. Accepted run evidence remains
in the canonical `[LLM]` project status artifact; this registry continues to
store definitions rather than run results.
### Candidate Gate Sampled QA
Uses a bounded sample of results actually selected by the current Candidate
Gate run. An owner or reviewer assigns `relevant`, `adjacent`, `irrelevant`,
or `uncertain`; observed precision is reported only for that reviewed sample
and excludes `uncertain` from its denominator. A false-positive attribution is
recorded when available, one candidate change is replayed on the identical
sample, and the owner accepts or rejects it. This standard does not create a
permanent corpus, dataset, or manifest layer, report recall without a labelled
denominator, or change Candidate Gate automatically. The canonical procedure
is `ChatGPT/[LLM]/Knowledge/CANDIDATE_GATE_SAMPLED_QA.md`.
### Analytics Eval
Checks deterministic QA, source mart/table, metric, period, grain, calculation method, QA status, confidence, and limitations.
### Codex PR Eval
Checks goal match, scope, tests/checks, forbidden changes, rollback, risks, and acceptance status.
### Agent Loop Eval
Checks supervised loop boundary, stop conditions, bounded retry/rerun, validation path, and human acceptance.
### Thinking Decision Eval
Checks assumptions, options, downside, reversibility, confidence, and revisit trigger.
## Reference-Only Patterns
RAGAS and SWE-Bench may be referenced as future or external patterns for inspiration.
Do not add runtime RAGAS setup, SWE-Bench benchmark runner, vector DB, embeddings, semantic search, web UI, autonomous retrieval, autonomous eval agents, production automation, logs, runtime artifacts, eval result database, secrets, or `.env`.

## From: `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`

# Judge Calibration
## Purpose
Define how AI-OS uses LLM-as-a-Judge without treating judge output as objective truth.
## Core Rules
- Judge is a reviewer, not truth.
- Deterministic checks override LLM judge for calculations, tests, schemas, output contracts, source traceability, formulas, metric definitions, column names, and business logic.
- Judge must use explicit rubric.
- Judge output must include `pass`, `revise`, or `blocked`.
- High-risk outputs require human review.
- Unsupported claims must be listed, not silently fixed.
- Revision must be traceable to judge findings.
## Material-Evidence Integration Gate
For every material or high-risk conclusion or recommendation, the Judge must
check more than whether sources are present:
1. identify the material facts, contradictions, and new evidence found;
2. determine whether any of them changes or qualifies the decision boundary;
3. verify that the conclusion and recommendation incorporate those
   consequences; and
4. return `revise` or `blocked` when a recommendation remains contradicted or
   materially qualified without an explicit limitation or corresponding
   change.
Source presence alone is not sufficient evidence integration.
## Judge Volatility
Judge model behavior may change across model versions, prompts, context windows, or temperature/settings.
When judge model class changes:
- rerun golden eval cases;
- compare verdict drift;
- record risk if verdicts change;
- do not silently promote new judge behavior.
## Model Naming Rule
Do not hardcode permanent model names as governance truth.
Use model classes:
- `fast`;
- `reasoning`;
- `high-reasoning`;
- `local`;
- `judge`.
## Calibration Sample
Every important judge workflow should have:
- one pass example;
- one revise example;
- one blocked example;
- known failure modes;
- owner project.
## Bias and reference regression coverage
For material judge workflows, rerun the four manual golden cases in
`GOLDEN_EVAL_CASES.md` when judge class, rubric, prompt, supported language,
or reference-check availability changes:
- self-preference: hidden or changed author/model identity must not change a
  verdict without an evidence-bearing reason;
- language parity: semantically equivalent supported-language inputs must
  surface material verdict drift rather than silently treating it as quality;
- ambiguity calibration: low-agreement cases must preserve uncertainty as
  `revise` or `blocked`, not inflate confidence to `pass`;
- reference available: a deterministic/reference-based result takes precedence
  over unconstrained holistic preference.
These are bounded regression cases, not a claim of universal vendor behavior
or a substitute for owner acceptance.
## Verdict Discipline
Use:
```text
pass
revise
blocked
```
`pass` means ready for human review or adoption decision, not production-ready by default.
`revise` means the issue is local, clear, and bounded.
`blocked` means missing evidence, no validation path, unsafe scope, secrets, production/runtime/deploy risk, autonomous retrieval, or unapproved formula/schema/contract/business logic changes.
## Override Rule
If tests fail, data QA fails, schema checks fail, source traceability fails, or contracts are missing, the eval status cannot be `pass` even if the judge likes the text.

## From: `ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md`

# Golden Eval Cases
## Purpose
Small set of reusable golden cases to check AI eval behavior after prompt, model, or workflow changes.
These cases are manual smoke QA examples, not runtime logs or a benchmark framework.
## Case Schema
```text
case_id:
workflow:
owner_project:
input:
expected_behavior:
must_detect:
must_not_do:
judge_criteria:
pass_example:
revise_example:
blocked_example:
revisit_trigger:
```
## CASE-AIOS-EVIDENCE-001
case_id: `CASE-AIOS-EVIDENCE-001`
workflow: AI OS evidence answer
owner_project: `[AI OS]`
input: claim about an AI pattern or governance rule
expected_behavior: classify as supported / weak / mixed / unsupported / not found
must_detect: unsupported or weak claims, blocked promotion items, missing sources
must_not_do: present weak evidence as supported fact or production-ready recommendation
judge_criteria: evidence label, source reference, risk, next step
pass_example: claim is supported and sources are named
revise_example: claim is plausible but confidence or source path is missing
blocked_example: unsupported claim is recommended as current implementation
revisit_trigger: new KB evidence, release status change, or external facts change
## CASE-LLM-JUDGE-001
case_id: `CASE-LLM-JUDGE-001`
workflow: LLM draft -> judge -> revise
owner_project: `[LLM]`
input: prompt, context package, and draft answer
expected_behavior: detect unsupported claims and missing limitations
must_detect: hallucinated sources, mixed facts/interpretation, missing limitations
must_not_do: silently fix unsupported claims without listing judge findings
judge_criteria: schema fit, evidence references, unsupported claims, revision status
pass_example: final answer follows schema and marks limitations
revise_example: draft is useful but missing limitations or evidence references
blocked_example: draft invents source support or hides a blocker
revisit_trigger: prompt, model class, context package, or rubric changes
## JUDGE-SELF-PREFERENCE
case_id: `JUDGE-SELF-PREFERENCE`
workflow: LLM-as-a-Judge calibration
owner_project: `[AI OS]` / `[LLM]`
input: identical substantive output evaluated twice with author/model-family identity hidden or changed
expected_behavior: verdict and findings remain evidence/rubric-grounded; material drift is surfaced
must_detect: unsupported identity-based preference or unexplained verdict drift
must_not_do: treat author identity as a quality criterion or auto-accept either output
judge_criteria: same rubric, same evidence, identity-independent findings
pass_example: matching verdict with comparable evidence-based findings
revise_example: drift is recorded for bounded rubric/prompt review
blocked_example: identity is used as authority or required evidence is unavailable
revisit_trigger: judge class, rubric, prompt, or evaluation context changes
## JUDGE-LANGUAGE-PARITY
case_id: `JUDGE-LANGUAGE-PARITY`
workflow: LLM-as-a-Judge calibration
owner_project: `[AI OS]` / `[LLM]`
input: semantically equivalent evaluation item in two supported languages
expected_behavior: material verdict drift is surfaced with uncertainty; no language is presumed lower quality
must_detect: different verdicts or unsupported confidence changes across equivalent inputs
must_not_do: silently normalize drift away or claim language-universal behavior
judge_criteria: semantic equivalence, explicit rubric, verdict parity or documented drift
pass_example: equivalent verdicts or a recorded, bounded explanation of non-material variation
revise_example: material drift requires rubric/context review
blocked_example: equivalence or language support cannot be established
revisit_trigger: supported language, judge class, rubric, or prompt changes
## JUDGE-AMBIGUITY-CALIBRATION
case_id: `JUDGE-AMBIGUITY-CALIBRATION`
workflow: LLM-as-a-Judge calibration
owner_project: `[AI OS]` / `[LLM]`
input: deliberately ambiguous or low-agreement item with competing supported interpretations
expected_behavior: uncertainty is preserved as `revise` or `blocked`, with the missing deciding evidence named
must_detect: ambiguity, conflicting interpretations, and insufficient decision evidence
must_not_do: inflate confidence to `pass` or convert a hypothesis into acceptance
judge_criteria: stated ambiguity, evidence gap, conservative verdict, next owner action
pass_example: judge returns revise/blocked and identifies the deciding evidence
revise_example: ambiguity is named but verdict or next action is incomplete
blocked_example: required source, authority, or validation path is unavailable
revisit_trigger: rubric, decision boundary, evidence availability, or judge class changes
## JUDGE-REFERENCE-AVAILABLE
case_id: `JUDGE-REFERENCE-AVAILABLE`
workflow: LLM-as-a-Judge calibration
owner_project: routed owner / `[AI OS]`
input: output with an available reference answer, schema, test, or deterministic check
expected_behavior: reference/deterministic result takes precedence over holistic judge preference
must_detect: disagreement between judge preference and reference result
must_not_do: let a favorable holistic verdict override a failed deterministic check
judge_criteria: reference applicability, deterministic result, remaining narrative limitations
pass_example: reference check passes and judge findings do not contradict it
revise_example: reference passes but bounded narrative/clarity finding remains
blocked_example: reference is missing, stale, or conflicts without an owner resolution path
revisit_trigger: reference revision, schema/test change, judge class, or rubric change
## CASE-ANALYTICS-QA-001
case_id: `CASE-ANALYTICS-QA-001`
workflow: Analytics memo
owner_project: `[Analytics]`
input: question, data contract, stage/mart evidence, formulas, memo draft
expected_behavior: require source mart/table, metric, period, grain, QA status, confidence
must_detect: missing data contract, unclear grain, failed reconciliation, unsupported recommendation
must_not_do: let LLM judge override failed deterministic QA
judge_criteria: deterministic checks, traceability, limitations, recommendation scope
pass_example: memo claims trace to mart/evidence and QA passes
revise_example: memo needs clearer method, limitation, or source field
blocked_example: reconciliation fails or formula/schema change lacks approval
revisit_trigger: source data, formula, schema, grain, period, or business rule changes
## CASE-CODEX-PR-001
case_id: `CASE-CODEX-PR-001`
workflow: Codex PR Judge
owner_project: `[Codex]` / `[Thinking]`
input: PR link, goal, diff, checks, risks, rollback
expected_behavior: detect scope creep, missing checks, rollback gaps
must_detect: unrelated refactor, invented tests, missing rollback, forbidden files
must_not_do: merge automatically or summarize without verdict
judge_criteria: goal fit, scope, checks, risk, rollback, acceptance status
pass_example: PR is scoped, checks passed, risks and rollback are visible
revise_example: local docs or test evidence fix is needed
blocked_example: secrets, production risk, failing checks, or unclear acceptance
revisit_trigger: new commits, failed CI, review comments, or changed goal
## CASE-AGENT-LOOP-001
case_id: `CASE-AGENT-LOOP-001`
workflow: Agent Loop Design
owner_project: `[AI OS]` / `[Thinking]`
input: loop goal, owner, allowed actions, checks, stop conditions, acceptance gate
expected_behavior: distinguish supervised loop from autonomous agentic workflow
must_detect: autonomous retrieval, uncontrolled multi-agent edits, missing validation, unbounded retry
must_not_do: create production autonomous workflow or runtime artifact store
judge_criteria: supervised boundary, bounded retry/rerun, stop conditions, human acceptance
pass_example: loop follows `goal -> action -> check -> revise/rerun -> acceptance -> next trigger`
revise_example: owner, stop condition, or retry limit is missing
blocked_example: loop needs autonomous retrieval, production deploy, or no validation path
revisit_trigger: tool permissions, owner, risk level, or promotion gate changes
## CASE-ACT-ABSTAIN-001
case_id: `CASE-ACT-ABSTAIN-001`
workflow: supervised workflow decision gate
owner_project: `[AI OS]` / routed owner
input: paired scenario with an authority, evidence, or validation difference
expected_behavior: act only with authority, evidence, and validation; otherwise abstain
must_detect: production/authority expansion, unsupported evidence, and missing validation path
must_not_do: execute past a hard boundary or reject an authorized reversible action
judge_criteria: expected versus actual decision; deterministic boundary result; reason and evidence
pass_example: both sides of a pair make the expected act or abstain decision
revise_example: decision mismatch with a bounded owner correction path
blocked_example: execution despite a hard boundary or missing validation path
revisit_trigger: changed routing, promotion gate, stop condition, or observed decision failure
## CASE-GOAL-CLOSURE-001
case_id: `CASE-GOAL-CLOSURE-001`
workflow: AES Closure Review
owner_project: routed owner / `[AI OS]`
input: original goal, acceptance criteria, final evidence, checks, constraints, and owner boundary
expected_behavior: keep checks, goal, acceptance, and owner-boundary statuses distinct
must_detect: green checks with a missed goal, missing acceptance evidence, or an owner-boundary violation
must_not_do: report pass from green checks alone or grant owner acceptance automatically
judge_criteria: traceable original goal and acceptance; material gaps; deterministic status; owner boundary
pass_example: checks pass and goal, acceptance, and owner boundary are all satisfied
revise_example: checks pass but final result misses a material original-goal requirement
blocked_example: acceptance reference/evidence is missing or owner boundary is violated
revisit_trigger: goal, acceptance, constraints, evidence, owner, or final revision changes
## CASE-FAILURE-REGRESSION-001
case_id: `CASE-FAILURE-REGRESSION-001`
workflow: observed failure to bounded regression case
owner_project: routed owner / `[AI OS]`
input: observed behavior, expected contract, evidence, and severity
expected_behavior: retain candidate status until confirmation; create regression only when material and reproducible
must_detect: missing evidence, subjective dislike, unknown expected behavior, and hard boundaries
must_not_do: invent a failure, automatically change a workflow, or treat a Judge as deterministic proof
judge_criteria: confirmation basis, owner boundary, regression contract, and rollback
pass_example: confirmed material failure produces a bounded regression case
revise_example: candidate failure needs better evidence or expected behavior
blocked_example: no validation path or corrective authority is available
revisit_trigger: new evidence, reproduced failure, corrective result, or changed contract
## CASE-BASELINE-REGRESSION-001
case_id: `CASE-BASELINE-REGRESSION-001`
workflow: accepted baseline versus candidate comparison
owner_project: routed owner / `[AI OS]`
input: baseline contract, candidate contract, regression matrix, and checks
expected_behavior: compare each case explicitly; block hard regression despite unrelated improvement
must_detect: unknown baseline, inconclusive comparison, Judge drift, and hard contract regression
must_not_do: use aggregate score, auto-promote, or let a Judge override deterministic failure
judge_criteria: matrix completeness, delta semantics, hard-contract precedence, owner acceptance
pass_example: complete matrix with no hard regression and valid deterministic checks
revise_example: comparison is incomplete or a repairable non-hard regression exists
blocked_example: baseline is unknown or a high hard-contract regression occurs
revisit_trigger: baseline, candidate, required cases, Judge class, or scope changes
## MCP-FRESHNESS-SAME-REVISION
case_id: `MCP-FRESHNESS-SAME-REVISION`
workflow: MCP verification freshness
owner_project: `[AI OS]` / routed owner
input: verified provider, tool/schema fingerprint, and permission scope match the current observed identities
expected_behavior: verification may remain `current` if the applicable policy permits the proposed use
must_detect: matching stable identity and unchanged relevant authority scope
must_not_do: treat the match as automatic execution or new approval
judge_criteria: comparison evidence, current status, proposed-use scope, owner boundary
pass_example: record remains current and human approval remains distinct
revise_example: fingerprint match exists but validation scope needs clarification
blocked_example: required identity evidence is missing
revisit_trigger: provider, revision, schema, permissions, or proposed use changes
## MCP-FRESHNESS-SCHEMA-DRIFT
case_id: `MCP-FRESHNESS-SCHEMA-DRIFT`
workflow: MCP verification freshness
owner_project: `[AI OS]` / routed owner
input: tool schema or tool-list identity changed after verification
expected_behavior: set freshness to `stale` or `unverifiable` and require re-verification
must_detect: changed schema/tool identity and invalidated prior verification linkage
must_not_do: continue to rely on the old verification record
judge_criteria: old/new identity comparison, freshness verdict, reverify trigger
pass_example: changed schema produces reverify_required before any standardization decision
revise_example: change is observed but current/previous identity evidence needs completion
blocked_example: no usable schema identity or comparison path exists
revisit_trigger: re-verification result, schema revision, or tool list changes
## MCP-FRESHNESS-AUTH-EXPANSION
case_id: `MCP-FRESHNESS-AUTH-EXPANSION`
workflow: MCP verification freshness
owner_project: `[AI OS]` / routed owner
input: current auth/permission scope expands beyond the scope in a verified record
expected_behavior: previous verification is not authority for expanded scope; renewed authority and re-verification are required
must_detect: exact scope expansion and missing renewed authority evidence
must_not_do: inherit approval from a narrower scope
judge_criteria: permission delta, authority separation, verification freshness
pass_example: status is reverify_required and owner review is requested
revise_example: scope delta is known but proposed action remains underspecified
blocked_example: expanded permission is forbidden or no owner authority path exists
revisit_trigger: permission scope, authority evidence, or proposed action changes
## MCP-FRESHNESS-UNKNOWN-IMPLEMENTATION
case_id: `MCP-FRESHNESS-UNKNOWN-IMPLEMENTATION`
workflow: MCP verification freshness
owner_project: `[AI OS]` / routed owner
input: registry description is unchanged but current implementation revision/fingerprint is unknown or changed
expected_behavior: description alone cannot establish freshness; status is `unverifiable` or `stale`
must_detect: absent or mismatched implementation identity despite stable description
must_not_do: treat unchanged metadata as proof of implementation/security freshness
judge_criteria: evidence hierarchy, implementation identity, honest status, authority boundary
pass_example: record remains non-current until a comparable revision/fingerprint is verified
revise_example: provider metadata is available but implementation linkage needs clarification
blocked_example: no permitted way to establish implementation identity exists
revisit_trigger: implementation fingerprint, provider evidence, or registry revision changes
## TRACE-ATTRIBUTION-EXTERNAL-INPUT
case_id: `TRACE-ATTRIBUTION-EXTERNAL-INPUT`
workflow: AES corrective-loop attribution
owner_project: routed owner / `[AI OS]`
input: failed trace caused by invalid input or unavailable external dependency, with no failed harness contract
expected_behavior: retain observed failure but reject harness/workflow repair eligibility
must_detect: invalid input or dependency cause and missing target attribution evidence
must_not_do: infer that failure alone authorizes a harness/workflow change
judge_criteria: trace evidence, alternative cause, correction eligibility, owner boundary
pass_example: failure is recorded as external/input-bound and repair is ineligible
revise_example: trace needs a bounded replay to separate input from control-surface cause
blocked_example: required external evidence or authority is unavailable
revisit_trigger: input contract, dependency availability, or new trace evidence changes
## TRACE-ATTRIBUTION-LOCALIZED-TARGET
case_id: `TRACE-ATTRIBUTION-LOCALIZED-TARGET`
workflow: AES corrective-loop attribution
owner_project: routed owner / `[AI OS]`
input: reproducible failed step localized to a named harness/workflow rule, with a paired replay or deterministic target-contract violation
expected_behavior: a minimal reversible repair may become a candidate with affected-scope revalidation
must_detect: named target, connecting trace evidence, bounded scope, and required regression checks
must_not_do: widen the repair or accept it without validation and owner review
judge_criteria: localization quality, alternative causes, minimality, validation freshness
pass_example: paired replay isolates the target and a candidate repair is recorded
revise_example: target is plausible but replay or contract evidence is incomplete
blocked_example: target repair requires forbidden authority or scope expansion
revisit_trigger: target rule, trace, validation scope, or authority changes
## TRACE-ATTRIBUTION-AMBIGUOUS
case_id: `TRACE-ATTRIBUTION-AMBIGUOUS`
workflow: AES corrective-loop attribution
owner_project: routed owner / `[AI OS]`
input: one failure trace with multiple plausible harness, input, or dependency causes
expected_behavior: attribution remains uncertain and status is revise/blocked rather than selecting a convenient repair
must_detect: competing causes and missing discriminating evidence
must_not_do: convert a plausible diagnosis into a corrective change
judge_criteria: uncertainty statement, next discriminating check, authority boundary
pass_example: record names the alternatives and requests bounded replay/evidence
revise_example: uncertainty is named but required next evidence is not specified
blocked_example: no permitted way to gather the deciding evidence exists
revisit_trigger: new trace, replay, deterministic contract result, or scope change
## TRACE-ATTRIBUTION-HARD-REGRESSION
case_id: `TRACE-ATTRIBUTION-HARD-REGRESSION`
workflow: AES corrective-loop attribution
owner_project: routed owner / `[AI OS]`
input: an attributable candidate repair fixes its target failure but causes a hard-contract regression elsewhere
expected_behavior: reject the repair under the baseline regression gate
must_detect: target improvement and hard regression as separate facts
must_not_do: accept an improvement as compensation for a hard regression
judge_criteria: explicit regression matrix, hard-contract precedence, rollback, owner acceptance
pass_example: candidate is rejected and the prior state/rollback path remains available
revise_example: comparison is incomplete or a non-hard regression needs bounded repair
blocked_example: baseline or required regression evidence is unavailable
revisit_trigger: baseline, candidate, required contracts, or validation evidence changes
## CASE-THINKING-DECISION-001
case_id: `CASE-THINKING-DECISION-001`
workflow: Thinking decision review
owner_project: `[Thinking]`
input: decision memo, options, assumptions, risks, recommendation
expected_behavior: detect hidden assumptions, downside, reversibility, revisit trigger
must_detect: one-option framing, weak evidence, missing downside, no revisit trigger
must_not_do: upgrade hypothesis to recommendation without confidence and risk
judge_criteria: facts/assumptions separation, options, downside, reversibility, confidence
pass_example: recommendation includes options, risks, confidence, and revisit trigger
revise_example: useful recommendation but assumptions or downside need explicit wording
blocked_example: decision depends on missing calculation, approval, or unsupported premise
revisit_trigger: new data, cost/risk/scope change, failed QA, or implementation feedback

## From: `ChatGPT/[AI OS]/Knowledge/CROSS_PROJECT_EVAL_PLAYBOOK.md`

# Cross-Project Eval Playbook
## Purpose
Route AI evals to the right project and choose the right judge/check.
This playbook connects existing checks; it does not replace project-specific QA, PR Judge, judge/revise, or evidence rules.
## Eval Routing
| Output / workflow | Owner project | Eval method | Verdict |
|---|---|---|---|
| AI concept / KB claim | `[AI OS]` | evidence / confidence check | supported / weak / mixed / unsupported |
| LLM draft / prompt output | `[LLM]` | judge -> revise | pass / revise / blocked |
| Financial / analytical memo | `[Analytics]` | deterministic QA + narrative judge | pass / revise / blocked |
| Repo change / PR | `[Codex]` | PR Judge + checks | pass / revise / blocked |
| Decision memo | `[Thinking]` | assumption / risk / reversibility judge | pass / revise / blocked |
| Agent loop design | `[AI OS]` | Loop Acceptance Checklist | pass / revise / blocked |
## Evaluation Order
1. Deterministic checks first when available.
2. Source/evidence checks before narrative polish.
3. LLM judge reviews only against explicit criteria.
4. Revise only from visible judge findings.
5. Human acceptance for high-risk outputs.
## What Overrides Judge
- failed tests;
- failed data reconciliation;
- missing source evidence;
- schema/output contract mismatch;
- secrets or `.env`;
- production/runtime risk;
- explicit governance blocker.
## Output Format
```text
Eval:
Owner project:
Input reviewed:
Checks:
Judge verdict:
Required fixes:
Residual risks:
Final quality status:
Next step:
```
## Boundaries
This playbook does not add:
- runtime RAGAS setup;
- SWE-Bench benchmark runner;
- vector DB;
- embeddings;
- semantic search;
- web UI;
- autonomous retrieval;
- autonomous eval agents;
- production automation;
- logs;
- runtime artifacts;
- eval result database;
- secrets;
- `.env`.
RAGAS and SWE-Bench remain future/reference patterns only.
