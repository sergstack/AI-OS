# Ollama / Open WebUI Pilot

## Purpose

Define safe pilot use of Ollama and Open WebUI.

Owner project: `[LLM]`
Pilot status: `candidate`
Manifest/upload status: source file for `ChatGPT/[LLM]/Knowledge_Bundles/LLM_06_LOCAL_AI_EXPERIMENTS.md`.
Residual risk: repository-file guidance only; local tool behavior still needs a recorded pilot result.

Ollama and Open WebUI are allowed as local experiment surfaces for draft generation, local model comparison, and curated excerpt exploration. They are not production systems and do not replace source review, judge/revise, Analytics QA, or AI-OS evidence checks.

## Pilot Scope

Allowed:

- load local model;
- test prompt behavior;
- draft from curated excerpts;
- compare local model outputs;
- explore approved local notes;
- prepare candidate text for `[LLM]` judge/revise.

Not allowed:

- autonomous retrieval;
- vector DB;
- embeddings;
- semantic search;
- web UI production workflow;
- production automation;
- MCP tools;
- unattended agent loop;
- source-of-truth decision without review.

## Input Rule

Use only curated excerpts and compact context.

Do not paste:

- secrets;
- `.env`;
- credentials;
- API keys;
- production data;
- raw financial dumps without explicit approval;
- raw logs;
- runtime artifacts;
- raw transcripts unless explicitly scoped and sanitized;
- source-card dumps;
- chunks.

## Pilot Loop

```text
prepare curated context
-> run local draft / retrieval pilot
-> keep relevant excerpts only
-> compare against source context
-> judge / revise
-> state limitations
-> decide pass / revise / blocked
```

## Acceptance Gate

Pilot output is usable only when:

- source context is named;
- output is marked draft or candidate;
- unsupported claims are listed;
- limitations are visible;
- judge/revise has been applied;
- deterministic claims have been routed to `[Analytics]`;
- production/repo work has been routed to `[Codex]`.

## Stop Conditions

Stop if:

- sources are not traceable;
- local retrieval contradicts source context;
- output is used as final truth;
- forbidden inputs are needed;
- production data or credentials are involved;
- the workflow requires autonomous retrieval, vector DB, embeddings, semantic search, MCP tools, or production automation.
