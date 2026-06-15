# [Thinking] — Workflow and Decisions

## Purpose

Compact upload artifact for [Thinking] covering workflow and decisions.

## Source files

- `ChatGPT/[Thinking]/Knowledge/INDEX.md`
- `ChatGPT/[Thinking]/Knowledge/THINKING_WORKFLOW.md`
- `ChatGPT/[Thinking]/Knowledge/DECISION_STATUS_AND_REVISIT.md`
- `ChatGPT/[Thinking]/Knowledge/DECISION_MEMO_TEMPLATE.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Thinking]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere

---

# Content

## From: `ChatGPT/[Thinking]/Knowledge/INDEX.md`

# [Thinking] Knowledge Index
## Canonical path
## Active files
- `PROJECT_INSTRUCTIONS.md`
- `README.md`
- `CURRENT_STATUS.md`
- `SMOKE_QA_RESULTS.md`
- `DECISION_LOG.md`
- `Knowledge/INDEX.md`
- `Knowledge/REVISOR_REWRITE.md`
- `Knowledge/DECISION_STATUS_AND_REVISIT.md`
## Optional support files
- `Knowledge/THINKING_WORKFLOW.md`
- `Knowledge/DECISION_MEMO_TEMPLATE.md`
- `Knowledge/RISK_REVIEW.md`
- `Knowledge/JUDGE_REVIEW.md`
- `Knowledge/STRATEGY_OPTIONS_TEMPLATE.md`
- `Knowledge/SCENARIO_ANALYSIS_TEMPLATE.md`
- `Knowledge/ROUTING_AND_HANDOFF.md`
- `Knowledge/AI_OS_REFERENCE.md`
## Status file
- `CURRENT_STATUS.md` is the live status source.
## Smoke QA file
- `SMOKE_QA_RESULTS.md` records the latest smoke QA.
## Decision log
- `DECISION_LOG.md` records reusable decisions.
## Revisor file
- `Knowledge/REVISOR_REWRITE.md` defines the rewrite role.
## Routing note
It must not absorb their responsibilities.


## From: `ChatGPT/[Thinking]/Knowledge/THINKING_WORKFLOW.md`

# Thinking Workflow
## Purpose
## Workflow
1. **Frame**
   - Какой вопрос решаем?
   - Какой decision/output нужен?
   - Кто пользователь результата?
2. **Facts**
   - Что известно?
   - Какие источники есть?
   - Что подтверждено, а что предположение?
3. **Options**
   - 2–4 варианта.
   - Для каждого: upside, downside, cost, reversibility.
4. **Criteria**
   - speed;
   - risk;
   - cost;
   - evidence strength;
   - operational complexity;
   - dependency on other projects.
5. **Risk review**
   - hidden assumptions;
   - failure modes;
   - what can go wrong;
   - how to detect failure.
6. **Decision**
   - recommendation;
   - why now;
   - what not to do;
   - what to defer.
7. **Handoff**
   - Analytics for calculations.
   - LLM for prompts/memo generation.
   - Codex for implementation.
   - AI OS for supported KB pattern.
## Output format
```text
Decision:
Reason:
Options considered:
Risks:
Assumptions:
Confidence:
Next step:
```


## From: `ChatGPT/[Thinking]/Knowledge/DECISION_STATUS_AND_REVISIT.md`

# Decision Status and Revisit Trigger
## Purpose
Define the standard for decision status tracking and revisit conditions.
## Decision statuses
- `draft`
- `candidate decision`
- `recommended`
- `blocked`
- `handoff required`
- `accepted`
- `deprecated`
## Revisit triggers
- new data;
- changed cost, risk, timing, or scope;
- QA fail;
- assumption invalidated;
- implementation feedback contradicts decision;
- owner rejects hypothesis;
- decision becomes irreversible.
## Requirement
Require status plus revisit trigger for:
- strategic decisions;
- budget or process decisions;
- handoff tasks;
- anything saved as a reusable decision record.
## Minimum record
- decision;
- status;
- confidence;
- owner;
- revisit trigger;
- next review;
- handoff;
- link or source.


## From: `ChatGPT/[Thinking]/Knowledge/DECISION_MEMO_TEMPLATE.md`

# Decision Memo Template
```markdown
# Decision Memo

## 1. Decision

Что предлагается решить.

## 2. Context

Факты, ограничения, фон.

## 3. Options

| Option | Description | Pros | Cons | Risk | Reversibility |
|---|---|---|---|---|---|

## 4. Criteria

| Criterion | Weight | Notes |
|---|---:|---|

## 5. Recommendation

Рекомендуемый вариант и почему.

```
