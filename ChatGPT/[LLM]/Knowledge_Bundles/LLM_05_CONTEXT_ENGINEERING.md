# [LLM] — Context Engineering

## Purpose

Compact upload artifact for `[LLM]` covering context engineering, CTC prompts, context intake, and good/bad examples.

## Source files

- `CONTEXT_PACK_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/CONTEXT_ENGINEERING_PLAYBOOK.md`
- `ChatGPT/[LLM]/Knowledge/CTC_PROMPT_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/CONTEXT_INTAKE_CHECKLIST.md`
- `ChatGPT/[LLM]/Knowledge/GOOD_BAD_CONTEXT_EXAMPLES.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- bundle_type: compact upload artifact
- source_of_truth: granular files listed above
- production_promotion: no, unless explicitly accepted elsewhere
- autonomous_retrieval: no

---

# Content

## Context Engineering Playbook

`CONTEXT_PACK_STANDARD.md` remains the reusable root standard. `[LLM]` owns prompt/context workflows and prepares prompt-ready context without raw dumps.

Workflow:

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

Ownership:

- `[LLM]`: prompt/context workflows, prompt registry, CTC prompts, context packs.
- `[AI OS]`: KB evidence, governance, supported / weak / unsupported labels.
- `[Analytics]`: data, marts, deterministic calculations, formulas, analytical QA.
- `[Codex]`: implementation, repo changes, tests, checks, PRs.

## Context Pack

Use a full Context Pack when another project needs reusable context, implementation scope, analytics, evidence-sensitive reasoning, handoff, acceptance criteria, or rollback.

Minimum sections:

- Goal
- Decision needed
- Relevant files
- Facts
- Constraints
- Forbidden
- Open questions
- Expected output
- Quality gate

## CTC Prompt Standard

CTC means:

```text
Context
Task
Constraints
```

Use CTC for small, low-risk, one-shot prompts with curated context.

CTC is not a replacement for a full Context Pack when risk, reuse, implementation, analytics, or evidence traceability matters.

## Context Intake Checklist

Before prompting:

- identify goal and decision needed;
- route to owner project;
- name relevant sources;
- separate facts from assumptions;
- mark missing evidence;
- reject forbidden inputs;
- define expected output;
- define quality gate.

Status:

```text
pass / revise / blocked
```

## Good / Bad Examples

Good context names the goal, sources, facts, constraints, forbidden inputs, open questions, expected output, and quality gate.

Bad context is a raw dump, asks `[LLM]` to do deterministic `[Analytics]` work, asks Codex to update a repo without scope, or hides missing evidence.

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

## Non-Goals

This layer does not add production automation, autonomous retrieval, vector DB, embeddings, semantic search, web UI, runtime artifacts, or new agent workflows.
