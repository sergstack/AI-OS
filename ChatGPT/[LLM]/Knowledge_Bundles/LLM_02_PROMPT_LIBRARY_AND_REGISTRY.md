# [LLM] — Prompt Library and Registry

## Purpose

Compact upload artifact for [LLM] covering prompt library and registry.

## Source files

- `ChatGPT/[LLM]/Knowledge/PROMPT_LIBRARY.md`
- `ChatGPT/[LLM]/Knowledge/PROMPT_REGISTRY.md`
- `ChatGPT/[LLM]/Knowledge/PROMPT_LIFECYCLE_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/LLM_02_PROMPT_LIBRARY_AND_REGISTRY_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:26f779feada27b16242c5237b27e14bbba88f0ca0ecfee70eb4fa34910bed96b
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/PROMPT_LIBRARY.md`

# Prompt Library
## @analyst
```text
Act as @analyst.
Analyze the task using:
- facts
- assumptions
- constraints
- options
- risks
- recommended next step
Separate supported facts from interpretation.
```
## @judge
```text
Act as @judge.
Find hallucinations, unsupported claims, weak evidence, missing constraints, and wrong routing.
Return verdict: pass / revise / blocked.
```
## @revisor
```text
Act as @revisor.
Rewrite the draft to be clearer, shorter, more structured, and evidence-aware.
Do not add new claims.
```
## @ai_operator
```text
Act as @ai_operator.
Package the result into files, checklist, task brief, or upload-ready instructions.
Include routing and acceptance criteria.
```
## goal_to_codex_package
```text
Take the user's broad goal and compile it into a Codex-safe execution package.
Do not ask the user to manually provide atomic task fields unless there is a hard blocker.
Return:
- inferred objective
- route
- scope
- files to inspect
- files allowed to modify
- forbidden actions
- checks
- rollback
- acceptance criteria
- final response format
Keep the user-facing summary short.
```
## Context package prompt
```text
Use only the provided context.
Do not invent facts.
Mark missing evidence.
Return structured output in markdown.
```
## karpathy_minimal_loop
```text
Сожми workflow до минимального проверяемого контура.
Верни:
1. Goal.
2. Input.
3. Minimal transformation.
4. QA / judge check.
5. Output.
6. Acceptance criteria.
7. What to remove as bloat.
8. What must not be automated now.
9. Decision status.
10. Revisit trigger.
11. Rollback / deletion rule.
Constraints:
- Do not create a new project, mode, folder, button, dashboard, agent, or automation unless unavoidable.
- If evidence is weak, mark it as weak.
- If deterministic calculation is required, route to [Analytics].
- If implementation or tests are required, route to [Codex] only with task package.
- If AI OS evidence or supported pattern is required, route to [AI OS].
- Preserve risks, assumptions, blockers, acceptance criteria, and unsupported claims.
- Do not upgrade candidate patterns to recommended/canonical without pilot evidence.
```

## From: `ChatGPT/[LLM]/Knowledge/PROMPT_REGISTRY.md`

# Prompt Registry
## Purpose
Controlled registry of reusable prompts and workflows.
Prompts are controlled assets, not one-off chat text.
## Registry
| prompt_id | task_type | purpose | input_requirements | output_schema | model_class | quality_gate | known_failure_modes | last_reviewed | owner_project | status | version | eval_status | acceptance_status | eval_refs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| judge_review | judge | detect unsupported claims and weak evidence | curated context, claims, evidence, limits | findings, risks, verdict | judge | unsupported claims listed; evidence checked | misses hidden assumptions; overconfident approval | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| revisor_final | revise | tighten draft without adding facts | judge output, supported facts, limitations | shorter decision-ready rewrite | reasoning | no new facts; support preserved | adds facts; deletes uncertainty | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| ai_operator_codex_task | orchestrate | package Codex handoff | objective, files, constraints, acceptance | Goal Mode handoff or scoped task package | reasoning | files and acceptance criteria present | vague task; missing scope | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| context_package_builder | synthesize | build curated context package | source excerpts, facts, boundaries | compact context package | reasoning | facts separated from interpretation | raw dump leakage; missing evidence | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| model_router | route | choose model class by task | task type, risk, context size, privacy | routing decision and rationale | reasoning | routing matches task class | hardcoded permanent model names | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| eval_gate | evaluate | validate LLM output quality | output, schema, evidence, limitations | pass / revise / blocked | judge | schema match; unsupported claims listed | false pass; hidden gaps | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| karpathy_minimal_loop | simplify / judge workflow | Reduce a workflow to a minimal verifiable loop before promotion or automation | workflow draft + target project + constraints | goal, input, minimal transformation, QA check, output, acceptance criteria, remove list, non-automation list, decision status, revisit trigger, rollback rule | reasoning / judge | 3 pilot cases pass; unsupported claims visible; no new tool unless justified | oversimplifies regulated/data tasks; becomes another layer; hides evidence gaps | 2026-06-26 | Sergey / LLM Lead | candidate | unversioned | not_recorded | not_recorded | not_recorded |
| external_ai_handoff | handoff | route work to external AI surfaces | goal, owner, inputs, forbidden inputs | handoff package | reasoning | handoff package complete | raw dump sent; wrong surface chosen | 2026-05-25 | [LLM] | active | unversioned | not_recorded | not_recorded | not_recorded |
| goal_to_codex_package | goal_compilation | Convert broad user goal into Codex-safe execution package | user goal, repo context, constraints, risk level | inferred objective, route, scope, files to inspect, allowed files, forbidden actions, checks, rollback, acceptance criteria, final response format | reasoning | no unnecessary clarification; hard blockers identified; scope bounded; checks present | over-atomization; broad refactor; hidden assumptions; missing validation | 2026-07-06 | [LLM] / [Codex] | active | unversioned | not_recorded | not_recorded | not_recorded |
## Legacy eval debt
`unversioned` and `not_recorded` describe missing repository evidence; they do
not imply an eval pass, owner acceptance, or a fabricated historical version.
Priority migration scope:
- `goal_to_codex_package`
- `judge_review`
- `eval_gate`
- `context_package_builder`
- `model_router`
- `revisor_final`
Existing active entries may remain usable as explicit legacy debt. A new or
materially revised reusable asset must receive an identifiable candidate
version, risk-appropriate eval evidence, and an acceptance decision before it
may become active. Owner acceptance must be recorded only from observed owner
evidence.

## From: `ChatGPT/[LLM]/Knowledge/PROMPT_LIFECYCLE_STANDARD.md`

# Prompt Lifecycle Standard
## Purpose
Define the minimum lifecycle for reusable prompt and workflow assets in `[LLM]`.
This standard is a thin implementation adapter. `[AI OS]` remains the owner of canonical evidence semantics, Judge doctrine, and generic promotion governance.
## Lifecycle states
Use exactly these lifecycle states:
```text
draft
candidate
active
superseded
retired
```
- `draft`: working version; not allowed as a governed reusable asset.
- `candidate`: version prepared for possible reuse; it must pass risk-appropriate checks before promotion.
- `active`: current version allowed for reuse. Active does not itself mean universally reliable, fully calibrated, or production-proven. Reliability is established by eval evidence and acceptance metadata.
- `superseded`: replaced by a newer active version; do not use by default for new runs.
- `retired`: must no longer be used.
`evaluated`, `accepted`, `revised`, `failed`, and `passed` are not lifecycle states. They describe an evaluation result, acceptance decision, or transition event.
## Version transition
For a material change to an active asset:
```text
active v1
-> candidate v2
-> risk-appropriate eval
-> acceptance
-> active v2
-> v1 superseded
```
A material change creates a new identifiable candidate version. Do not overwrite an active definition in a way that loses its lineage. A simple version identifier and a `supersedes` reference are sufficient; this standard does not require semantic versioning.
## Lifecycle metadata
Keep the existing Prompt Registry fields and add this baseline metadata:
| Field | Meaning |
|---|---|
| `version` | Version identifier. `unversioned` is an honest migration marker for a legacy entry whose historical version was not recorded. |
| `eval_status` | Workflow evaluation result or state, such as `not_recorded`, `pending`, `pass`, `revise`, or `fail`. |
| `acceptance_status` | Owner decision, such as `not_recorded`, `pending`, `accepted`, or `rejected`. |
| `eval_refs` | References to existing eval records or evidence; use `not_recorded` when none is available. |
| `supersedes` | Prior version replaced by this version; use `not_recorded` when lineage is unavailable. |
Optional fields may include `last_evaluated`, `accepted_by`, and `acceptance_date` when the information exists and is useful. Do not fabricate historical evidence or make every optional field mandatory for every asset class.
Legacy `active` entries remain active during metadata migration unless an owner makes a different governance decision. `eval_status: not_recorded` or `acceptance_status: not_recorded` makes the evidence gap visible; it does not retroactively prove or revoke acceptance.
## Promotion gate
Promotion from `candidate` to `active` requires:
1. compliance with the input/output contract;
2. risk-appropriate evaluation under `LLM_EVAL_STANDARD.md`;
3. no unresolved material failure;
4. owner acceptance;
5. version and traceability metadata.
Evaluation depth follows risk. A large eval suite is not a blanket requirement for every reusable prompt.
## Corrections and change impact
A minor editorial correction does not change the contract or expected behavior. It may be recorded without automatically invoking a heavyweight lifecycle process.
A material behavior change requires a new candidate version, relevant regression/evaluation, acceptance, and promotion. Material changes include:
- output schema changes;
- evidence discipline changes;
- routing or Judge logic changes;
- correction of a historical failure mode;
- other substantive instructions that affect behavior.
## Boundaries
- Use the existing Prompt Registry; do not create another registry.
- Use canonical `[AI OS]` evidence, Judge, and promotion governance rather than copying it here.
- Follow existing Context Engineering rules for curated context, facts versus assumptions, forbidden secrets, Context Pack/CTC selection, and quality gates.
- This standard does not define autonomous execution or runtime automation.

## From: `ChatGPT/[LLM]/Knowledge/LLM_02_PROMPT_LIBRARY_AND_REGISTRY_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[LLM]/Knowledge_Bundles/LLM_02_PROMPT_LIBRARY_AND_REGISTRY.md`.
## Legacy section: `ChatGPT/[LLM]/Knowledge/PROMPT_LIBRARY.md`
11. rollback / deletion rule.
- do not create a new project, mode, folder, button, dashboard, agent, or automation unless unavoidable.
## Legacy section: `ChatGPT/[LLM]/Knowledge/PROMPT_REGISTRY.md`
`unversioned` and `not_recorded` describe missing repository evidence; they do not imply an eval pass, owner acceptance, or a fabricated historical version.
Existing active entries may remain usable as explicit legacy debt. A new or materially revised reusable asset must receive an identifiable candidate version, risk-appropriate eval evidence, and an acceptance decision before it may become active. Owner acceptance must be recorded only from observed owner evidence.
