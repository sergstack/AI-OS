# Routing and Handoff

## Project routing

```text
AI-концепция / supported KB pattern → [AI OS]
Стратегия / решение / риски → [Thinking]
Расчёты / данные / marts → [Analytics]
Prompts / model routing / LLM quality → [LLM]
Код / implementation / tests / release → [Codex]
```

## Standard handoff format

```text
# Handoff

From:
To:
Task type:
Objective:
Context:
Inputs:
Constraints:
Expected outputs:
Acceptance criteria:
Risks:
Evidence / confidence:
Open questions:
```

## Thinking → Analytics

Используй, когда decision или scenario требует расчётов.

Передать:
- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.

## Analytics → LLM

Используй, когда verified numbers нужно превратить в memo, summary или narrative.

Передать:
- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.

## LLM → Codex

Используй, когда нужен код для автоматизации prompt/memo/report workflow.

Передать:
- prompt spec;
- input/output contract;
- files to inspect;
- forbidden actions;
- tests;
- acceptance criteria.

## Codex → QA / Release

Передать:
- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.
