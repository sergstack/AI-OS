# Context Engineering Playbook

## Purpose

Define the lightweight context engineering workflow for `[LLM]`.

`docs/standards/CONTEXT_PACK_STANDARD.md` remains the reusable root standard. This playbook explains how `[LLM]` prepares prompt-ready context without turning raw material into a dump.

## Ownership

- `[LLM]` owns prompt/context workflows, prompt registry, CTC prompts, and context pack preparation.
- `[AI OS]` owns KB evidence, governance, supported / weak / unsupported labels, and AI pattern checks.
- `[Analytics]` owns data contracts, marts, deterministic calculations, reconciliations, formulas, and analytical QA.
- `[Codex]` owns implementation, repo changes, tests, checks, branches, PRs, and local files.
- GitHub remains the source of truth for repository files.

## Workflow

```text
goal
-> route owner project
-> identify decision needed
-> gather relevant sources
-> extract curated facts
-> separate facts / assumptions / open questions
-> define constraints and forbidden inputs
-> choose Context Pack or CTC
-> set output format and quality gate
-> hand off or run prompt
-> judge / revise if needed
```

## Context Pack Use

Use a full Context Pack when the receiving project needs reusable context, multi-step work, implementation, evidence-sensitive reasoning, or handoff.

Minimum sections stay aligned with `docs/standards/CONTEXT_PACK_STANDARD.md`:

- Goal
- Decision needed
- Relevant files
- Facts
- Constraints
- Forbidden
- Open questions
- Expected output
- Quality gate

## CTC Use

Use CTC for quick prompts and small one-shot tasks.

CTC is not a replacement for a full Context Pack when risk, reuse, implementation, analytics, or evidence traceability matters.

## Forbidden Context Inputs

Do not use as prompt/context inputs:

- raw dumps;
- source-card dumps;
- chunks;
- logs;
- runtime artifacts;
- raw transcripts unless explicitly scoped and sanitized;
- secrets;
- `.env`;
- credentials;
- API keys;
- embeddings;
- vector DB files;
- semantic search indexes;
- web UI artifacts;
- autonomous retrieval output without source review.

## Quality Gate

Context is ready when:

- the goal and decision are clear;
- owner project is correct;
- facts and assumptions are separated;
- relevant sources are named;
- missing evidence is visible;
- forbidden inputs are excluded;
- output format and quality gate are explicit;
- deterministic work is routed to `[Analytics]`;
- implementation work is routed to `[Codex]`;
- KB evidence/governance is routed to `[AI OS]`.

## Non-Goals

This layer does not add production automation, autonomous retrieval, vector DB, embeddings, semantic search, web UI, runtime artifacts, or new agent workflows.
