# [LLM] — Workflows and Handoff

## Purpose

Compact upload artifact for [LLM] covering workflows and handoff.

## Source files

- `ChatGPT/[LLM]/Knowledge/LOCAL_LLM_WORKFLOW.md`
- `ChatGPT/[LLM]/Knowledge/MEMO_GENERATION_WORKFLOW.md`
- `ChatGPT/[LLM]/Knowledge/EXTERNAL_AI_HANDOFF_PROTOCOL.md`
- `ChatGPT/[LLM]/Knowledge/GEMINI_DEEP_RESEARCH__KB_HUNTER.md`
- `ChatGPT/[LLM]/Knowledge/AI_OS_REFERENCE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[LLM]/Knowledge/LOCAL_LLM_WORKFLOW.md`

# Local LLM Workflow
## Purpose
## Workflow
1. Prepare compact context.
2. Run retrieval or draft locally.
3. Copy relevant retrieved excerpts.
4. Send curated excerpts to ChatGPT for reasoning/synthesis if needed.
5. Judge output.
6. Record limitations.
## Do not
- treat local retrieval as final truth;
- upload secrets;
- rely on raw dump;
- skip source grounding;
- use local output as production fact without QA.


## From: `ChatGPT/[LLM]/Knowledge/MEMO_GENERATION_WORKFLOW.md`

# Memo Generation Workflow
## Pipeline
```text
curated context
→ draft
→ judge
→ revise
→ final memo
→ QA
```
## Inputs
- verified numbers;
- evidence cards;
- required sections;
- audience;
- tone;
- constraints.
## Required sections
1. Executive summary.
2. Key facts.
3. Analysis.
4. Risks.
5. Recommendations.
6. Limitations.
7. Evidence appendix.
## Judge criteria
- unsupported claims;
- missing evidence;
- overconfident recommendations;
- unclear numbers;
- weak structure;
- wrong audience.


## From: `ChatGPT/[LLM]/Knowledge/EXTERNAL_AI_HANDOFF_PROTOCOL.md`

# External AI Handoff Protocol
## Purpose
## Rule
Do not choose a tool because it is fashionable.
## Surfaces
| Surface | Use when | Inputs | Outputs | Owner project | QA gate |
| Ollama | local memo reasoning over prepared payloads | metrics, signals, evidence cards, prompts | draft memo, local judgement | [Analytics] / [LLM] | deterministic facts preserved |
## Never send
- secrets;
- `.env`;
- API keys;
- raw financial dumps unless explicitly approved;
- source-card dumps;
- raw transcripts;
- chunks;
- vector DB files;
- private client data;
- production credentials.
## Handoff package
Every handoff should include:
- goal;
- owner project;
- context summary;
- allowed inputs;
- forbidden inputs;
- expected output;
- evidence rules;
- acceptance criteria;
- rollback / stop condition.
## Failure modes
- tool chosen before task;
- raw dump sent instead of curated context;
- coding agent given vague wish without Goal Mode constraints or safe scoped task package;
- research result accepted without source filtering;
- orchestration marked successful without business validation.


## From: `ChatGPT/[LLM]/Knowledge/GEMINI_DEEP_RESEARCH__KB_HUNTER.md`

# Gemini Deep Research — KB Hunter
## Purpose
## Best use cases
- YouTube workflow discovery;
- AI power-user subscription workflows;
- creator / repo / article scouting;
- comparison of fresh AI tools;
- finding repeatable workflows, not hype.
## Avoid
- generic subscription reviews;
- pricing-only comparisons;
- generic AI news;
- “10 tools” listicles;
- opinion videos without workflow demo;
- clickbait;
- unsupported claims.
## Research input package
- topic;
- scope;
- must-have criteria;
- avoid list;
- scoring rubric;
- output schema;
- Sergey relevance criteria.
## Scoring rubric
- signal score;
- operational depth;
- novelty;
- practicality;
- subscription leverage;
- evidence quality;
- hype risk;
- Sergey relevance.
## Second-pass filter
- reproducible workflow;
- concrete tools;
- visible steps;
- output artifact;
- quality check;
- repeatability.
- pure reviews;
- news;
- opinions;
- shallow demos;
- no source trail.
## Output to AI OS
Gemini output must be converted into:
- candidate source list;
- workflow candidates;
- patterns;
- anti-patterns;
- recommended KB ingestion items;
- unsupported / weak claims.
## Acceptance criteria
Pass if:
- sources are listed;
- hype is filtered;
- reusable workflows are extracted;
- Sergey relevance is scored;
- claims are separated from interpretation.


## From: `ChatGPT/[LLM]/Knowledge/AI_OS_REFERENCE.md`

# AI OS Reference
## Purpose
- понять новую AI-концепцию;
- найти supported pattern;
- проверить confidence / evidence;
- связать AI-тренд с работой Сергея;
- найти governance rule;
- отличить supported / weak / unsupported claim.
## Не копировать
- весь compact KB package;
- raw transcripts;
- source cards;
- chunks;
- temp files;
- logs;
- embeddings;
- vector DB;
- web UI artifacts.
## Как ссылаться
Когда нужен KB-backed вывод, формулируй handoff в `[AI OS]` так:
```text
Используй AI OS KB. Найди supported/weak/unsupported evidence по теме:
<topic>

Верни:
- найдено в KB: да/нет/частично
- sources
- confidence
- supported claims
- weak/unsupported claims
- practical use for Sergey
```
## Rule
AI OS даёт evidence и patterns. Текущий проект применяет их в своей области, не смешивая роли.
