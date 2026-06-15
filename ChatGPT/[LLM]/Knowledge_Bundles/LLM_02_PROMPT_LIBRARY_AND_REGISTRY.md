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
## Context package prompt
```text
Use only the provided context.
Do not invent facts.
Mark missing evidence.
Return structured output in markdown.
```


## From: `ChatGPT/[LLM]/Knowledge/PROMPT_REGISTRY.md`

# Prompt Registry
## Purpose
## Registry
| prompt_id | task_type | purpose | input_requirements | output_schema | model_class | quality_gate | known_failure_modes | last_reviewed | owner_project | status |
| judge_review | judge | detect unsupported claims and weak evidence | curated context, claims, evidence, limits | findings, risks, verdict | judge | unsupported claims listed; evidence checked | misses hidden assumptions; overconfident approval | 2026-05-25 | [LLM] | active |
| ai_operator_codex_task | orchestrate | package Codex handoff | objective, files, constraints, acceptance | atomic task package | reasoning | files and acceptance criteria present | vague task; missing scope | 2026-05-25 | [LLM] | active |
| context_package_builder | synthesize | build curated context package | source excerpts, facts, boundaries | compact context package | reasoning | facts separated from interpretation | raw dump leakage; missing evidence | 2026-05-25 | [LLM] | active |
| model_router | route | choose model class by task | task type, risk, context size, privacy | routing decision and rationale | reasoning | routing matches task class | hardcoded permanent model names | 2026-05-25 | [LLM] | active |
| eval_gate | evaluate | validate LLM output quality | output, schema, evidence, limitations | pass / revise / blocked | judge | schema match; unsupported claims listed | false pass; hidden gaps | 2026-05-25 | [LLM] | active |
| external_ai_handoff | handoff | route work to external AI surfaces | goal, owner, inputs, forbidden inputs | handoff package | reasoning | handoff package complete | raw dump sent; wrong surface chosen | 2026-05-25 | [LLM] | active |
