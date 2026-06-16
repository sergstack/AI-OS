# Routing and Handoff

## Project routing

```text
AI-концепция / supported KB pattern → [AI OS]
Стратегия / решение / риски → [Thinking]
Расчёты / данные / marts → [Analytics]
Prompts / model routing / LLM quality → [LLM]
Код / implementation / tests / release → [Codex]
```

## Analytics default

For metrics, marts, data contracts, QA, calculations, deviations, charts and analytical memo structure: stay in `[Analytics]`.

## Analytical Memo Factory via Codex APP

If the user asks to create an analytical memo as an executable artifact, use:

```text
[Analytics] for analytical task framing
-> [Codex] for ultra-long Codex APP task package
-> Codex APP for execution
```

Keep `[Analytics]` responsible for methodology, data contracts, assumptions, limitations, and acceptance criteria. `[Codex]` designs the task package; Codex APP executes locally.

Do not force an interactive loop where `[Analytics]` asks for Python outputs back and forth unless the user explicitly wants manual exploration.

## Do not hand off too early

Before handoff, provide:

- analytical framing;
- data contract or missing fields;
- main files standard;
- expected metrics;
- QA requirements;
- acceptance criteria.

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

Use when decision/scenario requires calculations.

Pass:

- question;
- metrics;
- period;
- assumptions;
- options to test;
- expected analytical output.

## Analytics → LLM

Use when verified numbers need narrative, prompt workflow or model routing.

Pass:

- curated facts;
- tables or marts;
- reconciled metrics;
- limitations;
- tone and output format.

## Analytics → Codex

Use when implementation is needed.

Pass:

- files to inspect/change;
- input/output contract;
- main files rules;
- task packet;
- forbidden actions;
- tests;
- acceptance criteria.

## Codex → QA / Release

Pass:

- changed files;
- tests run;
- smoke QA;
- acceptance status;
- residual risks;
- rollback notes.
