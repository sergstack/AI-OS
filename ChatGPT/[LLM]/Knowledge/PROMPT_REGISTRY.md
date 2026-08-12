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
