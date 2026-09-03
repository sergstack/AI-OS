# [SELF_LEARNING] Post-Fix Review

## Назначение

Этот промпт используется после каждого нетривиального фикса, чтобы проект превращал исправления в повторяемое знание:

- что реально привело к успеху;
- что не сработало или было лишним;
- какие гипотезы подтвердились или не подтвердились;
- какие правила нужно сохранить;
- какие тесты и документы нужно обновить;
- какие регрессии теперь нужно контролировать.

Цель: не просто закрыть фикс, а сохранить операционное знание для будущих задач.

---

# Prompt

```text
@postfix-review

Сделай Post-Fix Learning Review по последнему фиксу.

## 0. Mode

Use compact mode by default.

Use deep mode only if the fix is:
- high-risk;
- production-facing;
- finance-related;
- security-related;
- related to public/user-facing behavior;
- related to data correctness;
- related to model routing, prompt behavior, judge/revisor behavior, or evidence discipline;
- explicitly requested as deep review.

Compact mode:
1. Status
2. What worked
3. What failed / unclear
4. Regression risks
5. Tests/docs to update
6. One learning rule

Deep mode:
Use the full 12-section format below.

## Goal

Determine:
- what really led to success;
- what did not work or was unnecessary;
- which hypotheses were confirmed / rejected / remain unclear;
- what knowledge should be saved in the project;
- what tests and docs should be updated;
- what regressions must now be monitored.

## Allowed evidence

Work only from:
- summary;
- changed files;
- commands run;
- test results;
- observed behavior;
- diff, if available.

Do not invent causes.
Do not infer root cause without evidence.
Do not recommend tests unless they map to a concrete observed risk, changed behavior, or missing contract.

Separate:
- fact;
- hypothesis;
- inference;
- missing evidence.

Do not rewrite code.
Do not propose large refactoring unless clearly required by the evidence.
Do not evaluate what was not tested.
If evidence is insufficient, say exactly what is missing.

## Route

Classify the review target:

- Bug/code fix review → Codex / QA
- Prompt/model behavior fix → LLM
- Data/mart/reconciliation fix → Analytics
- Governance/evidence rule → AI OS
- Strategic process change → Thinking

## Acceptance criteria

The review is acceptable only if:

- no unsupported root-cause claims are made;
- every success factor references evidence;
- every recommended test maps to a regression risk;
- docs updates are specific and actionable;
- missing evidence is explicitly marked;
- final learning rule is short and reusable.

---

# Compact Mode Format

## 1. Status

Status: success / partial / fail / blocked

Briefly state:
- what was fixed;
- why the fix is considered successful / partial / failed / blocked;
- what evidence supports this status;
- what evidence is missing, if any.

## 2. What Worked

| Factor | Why it helped | Evidence |
|---|---|---|
| [factor] | [reason] | [test / log / file / observed behavior] |

## 3. What Failed / Unclear

| Action / Hypothesis | Status | Why |
|---|---|---|
| [action or hypothesis] | failed / useless / unclear / insufficient evidence | [reason] |

If no failed paths are visible, write:
"Явно неуспешных действий по предоставленным данным не выявлено."

If evidence is insufficient, write:
"Insufficient evidence."

## 4. Regression Risks

| Possible regression | Why possible | How to catch | Test needed? |
|---|---|---|---|
| [risk] | [reason] | smoke / unit / integration / contract / manual check | yes/no |

## 5. Tests / Docs to Update

| Area | Update | Priority | Why |
|---|---|---|---|
| tests / README.md / RUNBOOK.md / AGENTS.md / SPEC.md / docs | [specific update] | high / medium / low | [reason] |

If no updates are needed, explain why.

## 6. Learning Rule

```text
Learning Rule:
[one short reusable rule]

Why:
[why this matters]

Save to:
learning_log / RUNBOOK.md / AGENTS.md / SPEC.md / tests / README.md