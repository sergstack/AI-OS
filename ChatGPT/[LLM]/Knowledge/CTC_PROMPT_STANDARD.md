# CTC Prompt Standard

## Purpose

Define CTC as a quick prompt structure for small tasks.

CTC means:

```text
Context
Task
Constraints
```

## When To Use

Use CTC when:

- the task is short;
- context is small and curated;
- output is one-shot;
- risk is low;
- no repo implementation is required;
- no deterministic calculation is required;
- no governed KB evidence decision is required.

## CTC Template

```text
Context:
- relevant facts:
- source / file:
- assumptions:
- missing evidence:

Task:
- requested output:
- audience:
- format:

Constraints:
- forbidden inputs:
- forbidden claims:
- routing:
- quality gate:
```

## When To Escalate To Context Pack

Use a full Context Pack instead of CTC when:

- another project must act on the context;
- Codex needs implementation scope;
- Analytics needs data contracts, marts, formulas, or QA;
- AI OS needs KB evidence/governance;
- output will be reused;
- risk is high;
- missing evidence changes the answer;
- the prompt needs handoff, acceptance criteria, or rollback.

## Guardrails

CTC must not include raw dumps, source-card dumps, chunks, logs, runtime artifacts, secrets, `.env`, credentials, API keys, embeddings, vector DB files, semantic search indexes, web UI artifacts, or autonomous retrieval output without source review.

CTC must not ask the LLM to perform deterministic calculations that belong in `[Analytics]`.

CTC must not replace human review for high-risk output.
