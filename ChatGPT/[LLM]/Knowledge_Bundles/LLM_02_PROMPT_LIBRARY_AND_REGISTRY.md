# [LLM] — Prompt Library and Registry

## Purpose

Compact upload artifact for [LLM] covering prompt library and registry.

## Source files

- `ChatGPT/[LLM]/Knowledge/PROMPT_LIBRARY.md`
- `ChatGPT/[LLM]/Knowledge/PROMPT_REGISTRY.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:3fabfff0fd33f77c43bacb97d230ea06ee1fc7feda66b1329f2afe081b68a65c

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
11. rollback / deletion rule.

Constraints:
- do not create a new project, mode, folder, button, dashboard, agent, or automation unless unavoidable.
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
## Registry
| prompt_id | task_type | purpose | input_requirements | output_schema | model_class | quality_gate | known_failure_modes | last_reviewed | owner_project | status |
| judge_review | judge | detect unsupported claims and weak evidence | curated context, claims, evidence, limits | findings, risks, verdict | judge | unsupported claims listed; evidence checked | misses hidden assumptions; overconfident approval | 2026-05-25 | [LLM] | active |
| ai_operator_codex_task | orchestrate | package Codex handoff | objective, files, constraints, acceptance | Goal Mode handoff or scoped task package | reasoning | files and acceptance criteria present | vague task; missing scope | 2026-05-25 | [LLM] | active |
| context_package_builder | synthesize | build curated context package | source excerpts, facts, boundaries | compact context package | reasoning | facts separated from interpretation | raw dump leakage; missing evidence | 2026-05-25 | [LLM] | active |
| model_router | route | choose model class by task | task type, risk, context size, privacy | routing decision and rationale | reasoning | routing matches task class | hardcoded permanent model names | 2026-05-25 | [LLM] | active |
| eval_gate | evaluate | validate LLM output quality | output, schema, evidence, limitations | pass / revise / blocked | judge | schema match; unsupported claims listed | false pass; hidden gaps | 2026-05-25 | [LLM] | active |
| karpathy_minimal_loop | simplify / judge workflow | Reduce a workflow to a minimal verifiable loop before promotion or automation | workflow draft + target project + constraints | goal, input, minimal transformation, QA check, output, acceptance criteria, remove list, non-automation list, decision status, revisit trigger, rollback rule | reasoning / judge | 3 pilot cases pass; unsupported claims visible; no new tool unless justified | oversimplifies regulated/data tasks; becomes another layer; hides evidence gaps | 2026-06-26 | Sergey / LLM Lead | candidate |
| external_ai_handoff | handoff | route work to external AI surfaces | goal, owner, inputs, forbidden inputs | handoff package | reasoning | handoff package complete | raw dump sent; wrong surface chosen | 2026-05-25 | [LLM] | active |
| goal_to_codex_package | goal_compilation | Convert broad user goal into Codex-safe execution package | user goal, repo context, constraints, risk level | inferred objective, route, scope, files to inspect, allowed files, forbidden actions, checks, rollback, acceptance criteria, final response format | reasoning | no unnecessary clarification; hard blockers identified; scope bounded; checks present | over-atomization; broad refactor; hidden assumptions; missing validation | 2026-07-06 | [LLM] / [Codex] | active |
