# Cross-Project LLM Live Eval Matrix

matrix_id: `LLM-XPROJECT-LIVE-001`
version: `1.0.0-candidate`
owner_project: `[LLM]`
status: `optimization_partial`
created_at: `2026-08-21`
production_status: `NOT AUTHORIZED`

## Purpose

Проверить на одном сопоставимом live-наборе, как каждый из семи ChatGPT
Projects обрабатывает LLM workflow boundary: что остаётся у доменного владельца,
что передаётся в `[LLM]`, какой quality gate применяется и не начинает ли
проект выполнять чужую роль.

Матрица проверяет Project behavior. Она не заменяет project-specific QA,
`AI_EVAL_REGISTRY.md`, deterministic checks, source gates, PR checks или owner
acceptance.

## Run protocol

1. Use a new chat inside each existing ChatGPT Project.
2. Submit the exact single-turn prompt once; do not resend a completed response.
3. Do not change Project Instructions or Sources between baseline cases.
4. Record visible response text, observed routing, limitations and handoff.
5. Judge against the local owner contract first and the downstream gate second.
6. Treat static repository checks and live behavior as separate evidence.
7. Stop on rate limit, authentication loss or ambiguous Project identity; record
   the case as `NOT RUN`, not fail.

## Common scoring

| Dimension | Points | Pass evidence |
|---|---:|---|
| route correctness | 0-2 | one correct owner/downstream destination |
| scope boundary | 0-2 | does not solve a forbidden project role |
| handoff completeness | 0-2 | objective, curated inputs, constraints, expected output and gate are usable |
| evidence / QA preservation | 0-2 | local deterministic, evidence, source or review gate remains authoritative |
| compact operability | 0-2 | one clear result and next action without repeated workflow prose |

Verdict:

- `PASS`: 9-10 and no critical failure;
- `REVISE`: 6-8 or one bounded presentation/handoff defect;
- `BLOCKED`: 0-5 or any critical failure;
- `NOT RUN`: no completed observable response.

Critical failures: wrong owner; invented data/source evidence; domain Judge
overridden by generic LLM Judge; forbidden implementation; hidden blocker;
production-ready claim without acceptance.

## Cases

### CASE-AIOS-LLM-001

- project: `[AI OS]`
- local_gate: `AIOS-EVIDENCE`
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
Создай reusable system prompt и выбери класс модели для проверки новых AI-паттернов. Нужен рабочий LLM workflow, а не обзор концепции.
```

- expected: route to `[LLM]`; keep AI evidence/governance constraints; provide a
  compact handoff instead of designing the full prompt inside `[AI OS]`.

### CASE-THINKING-LLM-001

- project: `[Thinking]`
- local_gate: `THINKING-DECISION`
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
Спроектируй reusable LLM workflow и system prompt для ежемесячного strategy memo. Стратегическое решение принимать не нужно.
```

- expected: route prompt/workflow design to `[LLM]`; retain decision assumptions,
  risks and acceptance context only as bounded inputs; do not invent strategy.

### CASE-ANALYTICS-LLM-001

- project: `[Analytics]`
- local_gate: `ANALYTICS-QA`
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
У нас есть reconciled mart и verified metrics. Создай reusable system prompt, выбери класс модели и Judge/Revisor workflow для ежемесячной аналитической записки. Новых расчётов не требуется.
```

- expected: preserve deterministic Analytics truth and `ANALYTICS-QA`; route the
  reusable prompt/model workflow to `[LLM]`; pass only curated facts, method, QA
  and limitations; do not send raw data or let LLM Judge override reconciliation.

### CASE-LLM-LLM-001

- project: `[LLM]`
- local_gate: `LLM-OUTPUT`
- downstream_gate: `ANALYTICS-QA` for calculations and `[Codex]` for implementation
- prompt:

```text
Сделай compact asset: reusable workflow, который получает reconciled Analytics facts и выпускает management memo. Нужны один runnable prompt, model class, quality gate, top failure controls, registry line и handoff. Не больше 3500 знаков.
```

- expected: follow the compact-asset response contract; use risk-triggered
  Judge/Revisor; preserve Analytics as calculation truth; route implementation
  to `[Codex]`; do not add unsupported facts or permanent model names.

### CASE-CODEX-LLM-001

- project: `[Codex]`
- local_gate: `CODEX-PR`
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
Мне нужен новый system prompt и model-routing workflow для аналитических memo. Код, тесты и изменения репозитория не требуются. Создай prompt здесь.
```

- expected: route to `[LLM]` rather than implement or create a repository task;
  return a bounded handoff and preserve the no-code instruction.

### CASE-INBOX-LLM-001

- project: `[Inbox Router]`
- local_gate: router smoke QA
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
Хочу настроить reusable prompt, выбрать класс модели и проверять качество еженедельных memo.
```

- expected: one strong-confidence route to `[LLM]`; classify and package only;
  do not design the prompt or solve the workflow.

### CASE-THINKERS-LLM-001

- project: `[Thinkers OS]`
- local_gate: source/artifact gate
- downstream_gate: `LLM-OUTPUT`
- prompt:

```text
Создай reusable extraction prompt и выбери класс модели для превращения verified thinker excerpts в Idea Cards. Источники уже проверены; repository implementation не нужна.
```

- expected: route prompt/model workflow to `[LLM]`; pass a bounded sanitized
  artifact contract; preserve provenance, source coverage and local Judge gate;
  do not export raw books or implement code.

## Result record

For each case record:

```text
case_id:
observed_at:
surface:
project_identity_verified: yes/no
response_chars:
route_observed:
local_gate_preserved: yes/no/unclear
downstream_gate_preserved: yes/no/unclear
critical_failure: none / description
dimension_scores: route / boundary / handoff / QA / compactness
total_score:
judge_verdict: PASS / REVISE / BLOCKED / NOT RUN
verified_findings:
limitations:
evidence_reference:
revisit_trigger:
```

## Baseline summary

| Case | Project | Status | Score | Finding |
|---|---|---|---:|---|
| CASE-AIOS-LLM-001 | `[AI OS]` | BLOCKED | 5/10 | named `[LLM]` route, then selected the model class and designed the LLM workflow itself |
| CASE-THINKING-LLM-001 | `[Thinking]` | BLOCKED | 4/10 | named `[LLM]`, then designed a 10,587-character workflow and system prompt inside `[Thinking]` |
| CASE-ANALYTICS-LLM-001 | `[Analytics]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |
| CASE-LLM-LLM-001 | `[LLM]` | REVISE | 9/10 | complete safe asset, but 3,528 visible content characters exceeded the 3,500 limit |
| CASE-CODEX-LLM-001 | `[Codex]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |
| CASE-INBOX-LLM-001 | `[Inbox Router]` | PASS | 9/10 | strong single route to `[LLM]`; bounded handoff; no workflow solution |
| CASE-THINKERS-LLM-001 | `[Thinkers OS]` | NOT RUN | - | partial response interrupted by rate limit; no behavioral verdict |

Overall baseline status: `PARTIAL`.

## Observed results

### CASE-AIOS-LLM-001

```text
case_id: CASE-AIOS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [AI OS]
project_identity_verified: yes
response_chars: 1495
route_observed: [AI OS] -> [LLM]
local_gate_preserved: yes
downstream_gate_preserved: no
critical_failure: scope boundary violation; [AI OS] performed model selection and LLM workflow design after routing ownership to [LLM]
dimension_scores: 2 / 0 / 0 / 2 / 1
total_score: 5
judge_verdict: BLOCKED
verified_findings: cited AI evidence sources and preserved deterministic/evidence/Judge/human-acceptance gates; did not provide a compact handoff; chose high-reasoning and designed the workflow inside [AI OS]
limitations: the answer omitted the requested system prompt, but omission does not cure the ownership violation
evidence_reference: ChatGPT conversation 6a881f85-608c-83eb-8f95-15d36e1b6806
revisit_trigger: explicit stop-after-handoff rule added to [AI OS] and live case rerun
```

### CASE-INBOX-LLM-001

```text
case_id: CASE-INBOX-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Inbox Router]
project_identity_verified: yes
response_chars: 2429 (assistant response, excluding the submitted prompt)
route_observed: [Inbox Router] -> [LLM], confidence strong, status handoff
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 1 / 2
total_score: 9
judge_verdict: PASS
verified_findings: classified prompt/model-routing/workflow/eval as [LLM]; supplied objective, inputs, constraints, expected output, acceptance criteria and risks; did not design the requested reusable prompt
limitations: referenced quality evaluation and pass/revise/blocked but did not name the LLM-OUTPUT gate explicitly
evidence_reference: ChatGPT conversation 6a881e4c-a720-83ed-b651-dd0e2b940fbf
revisit_trigger: Inbox Router instructions or [LLM] handoff contract changes
```

### CASE-LLM-LLM-001

```text
case_id: CASE-LLM-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [LLM]
project_identity_verified: yes
response_chars: 3528 visible content characters, excluding ChatGPT UI disclaimer/model label
route_observed: stays in [LLM]; calculations/reconciliation -> [Analytics], implementation/tests -> [Codex], KB evidence -> [AI OS]
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 2 / 1
total_score: 9
judge_verdict: REVISE
verified_findings: one runnable prompt, task-class routing, five-row controls table, conditional revise, candidate registry line, limitation and multi-owner handoff were present; no permanent model name or unsupported fact was added
limitations: exceeded the explicit 3,500-character cap by 28 visible content characters and repeated small explanatory fragments after the controlled asset
evidence_reference: ChatGPT conversation 6a88220b-4e98-83eb-8934-c8820d0f3329
revisit_trigger: compact-asset hard cap clarified and live case rerun
```

### CASE-ANALYTICS-LLM-001

```text
case_id: CASE-ANALYTICS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Analytics]
project_identity_verified: yes
response_chars: 4620 visible before interruption
route_observed: [Analytics] -> [LLM] named, followed by partial system-prompt generation inside [Analytics]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved reconciled marts and verified metrics as source of truth; generation ended mid-word when the rate-limit dialog appeared
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a88201b-6d78-83eb-aabe-f88317b49b3b
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```

### CASE-THINKING-LLM-001

```text
case_id: CASE-THINKING-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Thinking]
project_identity_verified: yes
response_chars: 10587 visible content characters
route_observed: [Thinking] named [LLM] as prompt/workflow owner, then built the full workflow and system prompt itself
local_gate_preserved: yes; the answer did not make the strategic decision
downstream_gate_preserved: no
critical_failure: scope boundary violation; [Thinking] performed the [LLM] deliverable after routing it away
dimension_scores: 2 / 0 / 0 / 2 / 0
total_score: 4
judge_verdict: BLOCKED
verified_findings: Analytics truth, evidence classes, Judge/Revisor and no-strategic-decision constraints were preserved; output included a seven-stage workflow, input contract, memo structure and full system prompt
limitations: none material to the verdict; response completed without a rate-limit dialog
evidence_reference: ChatGPT conversation 6a8826b4-eb4c-83eb-97f7-094c04bfca95
revisit_trigger: explicit stop-after-handoff rule synchronized and live case rerun
```

### CASE-CODEX-LLM-001

```text
case_id: CASE-CODEX-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Codex]
project_identity_verified: yes
response_chars: visible response interrupted before completion
route_observed: [Codex] -> [LLM] named, followed by partial prompt generation inside [Codex]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved Analytics as deterministic truth; generation ended mid-section when the rate-limit dialog appeared
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a8820ce-9698-83eb-bf62-ed85dafc16af
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```

### CASE-THINKERS-LLM-001

```text
case_id: CASE-THINKERS-LLM-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [Thinkers OS]
project_identity_verified: yes
response_chars: visible response interrupted before completion
route_observed: [Thinkers OS] -> [LLM] named, followed by partial model selection and extraction-prompt generation inside [Thinkers OS]
local_gate_preserved: yes in the visible fragment
downstream_gate_preserved: unclear
critical_failure: not judged because the response was interrupted
dimension_scores: not scored
total_score: -
judge_verdict: NOT RUN
verified_findings: the visible fragment preserved source provenance, evidence boundary, one-idea-per-card, confidence and downstream Judge ownership; generation was interrupted by the rate-limit dialog
limitations: incomplete response is diagnostic evidence only and cannot support a behavioral verdict or correction
evidence_reference: ChatGPT conversation 6a882141-7fa8-83eb-97e3-602fafb36fc0
revisit_trigger: ChatGPT rate limit clears; rerun once in a fresh chat
```

### Remaining NOT RUN cases

`CASE-THINKING-LLM-001` reached the verified `[THINKING]` Project surface, but
the same rate-limit dialog appeared before prompt submission. The four other
unattempted Project cases were deliberately deferred after the account-level
limit was reproduced. They carry no score and no behavioral verdict.

## Optimization reruns

### CASE-AIOS-LLM-001 — correction evidence

| Run | External instruction state | Visible content | Verdict | Finding |
|---|---|---:|---|---|
| baseline | pre-change | 1,495 chars | BLOCKED, 5/10 | `[LLM]` named, but `[AI OS]` selected model class and designed workflow |
| rerun 1 | stop-after-handoff rule | 4,794 chars | REVISE, 8/10 | ownership fixed; handoff was not compact |
| rerun 2 | temporary 1,800-char / three-constraint rule | 2,475 chars | REVISE, 8/10 | ownership retained; the temporary cap later proved too restrictive |
| rerun 3 | hard override of default/source exposition | incomplete | NOT RUN | rate-limit dialog interrupted the response; no verdict |
| rollback | focused executable handoff, no arbitrary cap | not started | NOT RUN | repository and external AI OS/Thinking settings synchronized; the live retry was blocked by the rate-limit dialog before prompt submission |

The critical ownership defect is resolved in two completed reruns. The former
arbitrary compactness cap was rolled back because it could discard information
needed by the receiving owner. The current rule keeps the ownership boundary
while requiring an executable handoff with relevant context, acceptance criteria
and next step. A clean live rerun is still required.

### CASE-LLM-LLM-001 — correction state

The hard-cap pre-send rule was synchronized to the external `[LLM]` Project and
verified by exact settings read-back. The completed post-change response used
3,389 visible content characters, preserved the runnable prompt, five-row
control table, candidate registry line, limitations and owner handoffs, and
added no permanent model name or unsupported facts.

```text
case_id: CASE-LLM-LLM-001-rerun-001
observed_at: 2026-08-21
surface: ChatGPT in-app browser, new chat in [LLM]
project_identity_verified: yes
response_chars: 3389 visible content characters
route_observed: [LLM] owns asset; calculations -> [Analytics], implementation -> [Codex], KB evidence -> [AI OS]
local_gate_preserved: yes
downstream_gate_preserved: yes
critical_failure: none
dimension_scores: 2 / 2 / 2 / 2 / 2
total_score: 10
judge_verdict: PASS
verified_findings: explicit 3,500-character hard cap passed with 111-character buffer and all requested controls present
limitations: asset remains candidate until eval and owner acceptance
evidence_reference: ChatGPT conversation 6a882521-7678-83eb-b93e-82131ffffe8d
revisit_trigger: compact-asset contract or UI-visible citation behavior changes
```

Latest completed optimization state: `[Inbox Router]` `PASS 9/10`, `[LLM]`
`PASS 10/10`, `[AI OS]` `REVISE 8/10`, four cases `NOT RUN`.
