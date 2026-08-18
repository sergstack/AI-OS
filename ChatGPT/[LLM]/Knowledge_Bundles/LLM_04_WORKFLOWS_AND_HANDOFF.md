# [LLM] — Workflows and Handoff

## Purpose

Compact upload artifact for [LLM] covering workflows and handoff.

## Source files

- `ChatGPT/[LLM]/Knowledge/LOCAL_LLM_WORKFLOW.md`
- `ChatGPT/[LLM]/Knowledge/MEMO_GENERATION_WORKFLOW.md`
- `ChatGPT/[LLM]/Knowledge/RELATIONSHIP_CRM_LITE_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/WEEKLY_RELATIONSHIP_REVIEW_BLOCK.md`
- `ChatGPT/[LLM]/Knowledge/VALUE_FIRST_OUTREACH_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/MEETING_RECAP_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/ASK_FOR_ADVICE_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/NO_SPAM_HUMAN_REVIEW_RULE.md`
- `ChatGPT/[LLM]/Knowledge/EXECUTIVE_SUMMARY_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/COMMUNICATION_QA_CHECKLIST.md`
- `ChatGPT/[LLM]/Knowledge/CHART_COMMENTARY_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/AUDIT_FINDING_WORDING_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/SLIDE_STORYLINE_TEMPLATE.md`
- `ChatGPT/[LLM]/Knowledge/EXTERNAL_AI_HANDOFF_PROTOCOL.md`
- `ChatGPT/[LLM]/Knowledge/GEMINI_DEEP_RESEARCH__KB_HUNTER.md`
- `ChatGPT/[LLM]/Knowledge/AI_OS_REFERENCE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- source_fingerprint: sha256:236291cadfdfc4f7d733e1ba622744632cdb7611b156f68e42ec1ffaf63d2f8f

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
curated context snapshot
→ draft
→ deterministic output QA
→ judge when a trigger applies
→ revise only from explicit findings
→ targeted recheck
→ final memo
```
## Inputs
- verified numbers;
- evidence cards;
- required sections;
- audience;
- tone;
- constraints.
## Minimal run contract
1. Build one curated context snapshot and assign a `context_id`. Reuse it for draft, judge, and revise; rebuild it only when sources change or QA identifies missing evidence.
2. Before an LLM Judge, check deterministic items first: required sections, source/evidence labels, visible limitations, and the requested output schema.
3. Run Judge when the output is material or decision-critical, evidence-sensitive, fails deterministic QA, uses an unreviewed workflow/model path, or a human explicitly requests review.
4. Bypass Judge only when every trigger in step 3 is false and deterministic QA passes. If QA/Judge returns `pass`, publish the draft without rewriting it. If it returns `revise`, change only the listed findings and rerun the affected checks. If a material finding remains after one revision, return `blocked` for human review instead of starting an open-ended loop.
Do not treat fewer calls as proof of token savings. Record available per-run evidence (`context_id`, generation steps, Judge trigger, revision count, and provider-reported input/output tokens when available); otherwise mark token cost `not measured`.
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
Material or evidence-sensitive output cannot pass deterministic QA alone; Judge remains required. Revise remains findings-driven.


## From: `ChatGPT/[LLM]/Knowledge/RELATIONSHIP_CRM_LITE_TEMPLATE.md`

# Relationship CRM Lite Template
Status: candidate / ready for human review.
Purpose: lightweight relationship effectiveness note, not a CRM project, outreach pipeline, or automation.
## Contact
Name:
Role:
Organization:
Relationship type:
Topic of mutual interest:
## Context
Last contact date:
Last context:
Promised follow-up:
Value I can offer:
Ask / opportunity:
Next touch:
Status:
Notes:
## Guardrails
- Empty fields only; do not store real contact data in public repo templates.
- No emails, phone numbers, addresses, private relationship notes, client/vendor/employee data, secrets, raw dumps, or runtime artifacts.
- No mass outreach, auto-send, autonomous follow-up, production automation, autonomous agents, retrieval, vector DB, embeddings, semantic search, or web UI.
- All outbound messages require human review before sending.
- Prompt QA is required before promoting outreach prompts or Stream Deck commands.


## From: `ChatGPT/[LLM]/Knowledge/WEEKLY_RELATIONSHIP_REVIEW_BLOCK.md`

# Weekly Relationship Review Block
Status: candidate / ready for human review.
Purpose: small weekly relationship block connected to Weekly AI-OS Review, not a status ledger or CRM workflow.
## Review
Who can benefit from current AI-OS / audit / finance artifact:
Who I owe a follow-up to:
What value I can send this week:
One relationship next action:
## Next action
Person / group:
Value to send:
Owner:
Draft needed: yes / no
Human review before sending: yes
Acceptance criteria:
## Guardrails
- End with one relationship next action.
- No mass messaging.
- No auto-send.
- No autonomous follow-up.
- No real contact data or private notes in repo files.
- Stream Deck relationship commands remain candidate until Prompt QA, testing, and owner acceptance.


## From: `ChatGPT/[LLM]/Knowledge/VALUE_FIRST_OUTREACH_TEMPLATE.md`

# Value-First Outreach Template
Status: candidate / ready for human review.
Purpose: draft one human-reviewed outbound message based on useful context or artifact.
## Inputs
Context:
Useful artifact / idea:
Why it may help:
Low-pressure next step:
Human review before sending: required
## Draft
Hi [name],
[context]
[useful artifact / idea]
[why it may help]
[low-pressure next step]
## QA
- [ ] Message is one-to-one, not mass outreach.
- [ ] Value comes before ask.
- [ ] No fake praise.
- [ ] No unsupported claims.
- [ ] No private data, contact details, secrets, raw dumps, or runtime artifacts.
- [ ] Human reviewed before sending.
- [ ] No auto-send or autonomous follow-up.


## From: `ChatGPT/[LLM]/Knowledge/MEETING_RECAP_TEMPLATE.md`

# Meeting Recap Template
Status: candidate / ready for human review.
Purpose: concise meeting recap and follow-up note, not a CRM log or automated follow-up system.
## Meeting
Meeting:
Date:
Context:
## Recap
Key points:
Commitments from me:
Commitments from them:
Useful follow-up:
Next touch:
Risks / sensitivities:
## Follow-up guardrails
- Human review before any outbound message.
- No auto-send.
- No autonomous follow-up.
- Do not store real private notes, emails, phone numbers, addresses, or personal data in repo templates.
- Keep sensitive context out of public repo files.


## From: `ChatGPT/[LLM]/Knowledge/ASK_FOR_ADVICE_TEMPLATE.md`

# Ask For Advice Template
Status: candidate / ready for human review.
Purpose: low-pressure request for advice, not mass outreach or automated networking.
## Inputs
Context:
Why this person:
Specific advice requested:
Useful artifact / context offered:
Low-pressure next step:
Human review before sending: required
## Draft
Hi [name],
[brief context]
[specific advice requested]
[useful artifact / context offered, if relevant]
[low-pressure next step]
## QA
- [ ] The ask is specific and respectful.
- [ ] Message is not mass outreach.
- [ ] No fake praise.
- [ ] No pressure language.
- [ ] No private data or contact details in repo files.
- [ ] Human reviewed before sending.
- [ ] No auto-send or autonomous follow-up.


## From: `ChatGPT/[LLM]/Knowledge/NO_SPAM_HUMAN_REVIEW_RULE.md`

# No-Spam / Human-Review Rule
Status: candidate / ready for human review.
Purpose: safety boundary for Relationship Effectiveness templates and outreach prompts.
## Rules
- No mass messaging.
- No auto-send.
- No autonomous follow-up.
- No fake praise.
- No private data in repo files.
- No real contact data, emails, phone numbers, addresses, private relationship notes, client/vendor/employee data, secrets, raw dumps, or runtime artifacts.
- Human review is required before any outbound message.
- Prompt QA is required before promoting outreach prompts or Stream Deck commands.
- Stream Deck commands remain candidate until tested and accepted.
## Human review checklist
- [ ] Recipient and context are correct.
- [ ] Message is useful to the recipient.
- [ ] Message is one-to-one.
- [ ] Ask is low pressure.
- [ ] No private data is exposed.
- [ ] Follow-up, if any, is human-owned.
- [ ] No automation or production promotion is implied.


## From: `ChatGPT/[LLM]/Knowledge/EXECUTIVE_SUMMARY_TEMPLATE.md`

# Executive Summary Template
Status: candidate / ready for human review.
Purpose: concise executive communication after Analytics facts, deterministic checks, and QA.
## Inputs
Audience:
Decision context:
Verified Analytics facts:
Evidence cards / source marts:
Period:
Scope / population:
Currency / units:
Known limitations:
## Executive summary
Main message:
What changed:
Why it matters:
Evidence:
- source:
- period:
- scope / population:
- metric / amount / fact:
Risk / opportunity:
Recommended action:
Owner / next step:
Confidence:
Limitations:
## Guardrails
- Analytics facts first, LLM narrative second.
- Deterministic checks first.
- No LLM arithmetic.
- No LLM variance, driver, exposure, or root-cause calculation.
- Root cause must be evidenced or marked `requires management confirmation`.
- Recommendations must trace to verified facts.


## From: `ChatGPT/[LLM]/Knowledge/COMMUNICATION_QA_CHECKLIST.md`

# Communication QA Checklist
Status: candidate / ready for human review.
## Source and scope
- [ ] Main message exists.
- [ ] Source exists.
- [ ] Period exists.
- [ ] Scope / population exists.
- [ ] Metric / amount / fact exists where applicable.
- [ ] Evidence cards, source mart, or accepted source references are listed.
## Evidence and claims
- [ ] Facts are separated from interpretation.
- [ ] Limitations are visible.
- [ ] Confidence is visible.
- [ ] Unsupported claims are removed or marked.
- [ ] Root cause is evidenced or marked `requires management confirmation`.
- [ ] Recommendation traces to verified facts.
- [ ] Recommendation is actionable.
- [ ] Owner / next step is visible.
## Analytics-first guardrails
- [ ] Analytics facts came before LLM narrative.
- [ ] Deterministic checks came before narrative.
- [ ] LLM arithmetic was not used.
- [ ] LLM variance, driver, exposure, or root-cause calculation was not used.
## Verdict
QA verdict: pass / revise / blocked


## From: `ChatGPT/[LLM]/Knowledge/CHART_COMMENTARY_STANDARD.md`

# Chart Commentary Standard
Status: candidate / ready for human review.
## Required inputs
Chart ID:
Chart source:
Source mart / slice:
Period:
Scope / population:
Metric / amount / fact:
Grain:
Filters:
QA status:
Limitations:
## Commentary structure
What it shows:
What changed:
Why it matters:
What to do next:
## Guardrails
- Do not infer unsupported causes from visual shape.
- Do not calculate variance, exposure, driver impact, or root cause by LLM.
- If cause is not evidenced, write `requires management confirmation`.
- Recommendation must trace to verified chart facts or accepted Analytics findings.


## From: `ChatGPT/[LLM]/Knowledge/AUDIT_FINDING_WORDING_TEMPLATE.md`

# Audit Finding Wording Template
Status: candidate / ready for human review.
## Finding structure
Finding:
Criteria:
Evidence:
Risk:
Cause: [Known cause or requires management confirmation]
Recommendation:
Confidence:
Limitations:
## Traceability
Source:
Period:
Scope / population:
Metric / amount / fact:
Source mart / evidence ID:
Reviewer:
## Wording rules
- Use cautious wording.
- Do not label fraud, misconduct, manipulation, or confirmed breach unless separately evidenced and accepted by the human reviewer.
- Root cause must be evidenced or marked `requires management confirmation`.
- Recommendation must trace to verified facts.


## From: `ChatGPT/[LLM]/Knowledge/SLIDE_STORYLINE_TEMPLATE.md`

# Slide Storyline Template
Status: candidate / ready for human review.
Purpose: optional storyline outline for approved facts. This is not a Presentation project, deck generator, raw-data-to-deck workflow, or production reporting automation.
## Inputs
Audience:
Decision needed:
Verified facts:
Evidence sources:
Period:
Scope / population:
Limitations:
Confidence:
## Storyline
Slide 1 - Main message:
Slide 2 - What changed:
Slide 3 - Evidence:
Slide 4 - Risk / opportunity:
Slide 5 - Recommended action:
## Guardrails
- Optional and candidate-only.
- Do not generate a deck.
- Do not create a new Presentation project.
- Do not create a raw-data-to-deck workflow.
- Do not add facts, causes, metrics, or recommendations.


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
