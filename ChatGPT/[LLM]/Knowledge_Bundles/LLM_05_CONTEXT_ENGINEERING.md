# [LLM] — Context Engineering

## Purpose

Compact upload artifact for `[LLM]` covering context engineering, CTC prompts, context intake, and good/bad examples.

## Source files

- `docs/standards/CONTEXT_PACK_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/CONTEXT_ENGINEERING_PLAYBOOK.md`
- `ChatGPT/[LLM]/Knowledge/CTC_PROMPT_STANDARD.md`
- `ChatGPT/[LLM]/Knowledge/CONTEXT_INTAKE_CHECKLIST.md`
- `ChatGPT/[LLM]/Knowledge/GOOD_BAD_CONTEXT_EXAMPLES.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[LLM]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- autonomous_retrieval: no
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:93f876d6e36a1cf2427f6a1072a7cb35d3e57ac08ba009a6c4287c61d49f4094
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `docs/standards/CONTEXT_PACK_STANDARD.md`

# Context Pack Standard
Context Packs are compact inputs for AI-OS, LLM, Analytics, and Codex workflows. They should contain the context needed for the next decision or output, not every available file.
## Minimal Schema
```markdown
# Context Pack
## Goal
## Decision needed
## Relevant files
## Facts
## Authority provenance
## Constraints
## Forbidden
## Open questions
## Expected output
## Quality gate
```
## Guidance
- Do not dump all files.
- Use curated context.
- Separate facts from assumptions.
- For each decision-relevant claim, retain its authority class, source
  reference, and action eligibility. The same claim text can have different
  eligibility when its authority differs.
- Mark missing evidence and open questions.
- Route deterministic calculations to `[Analytics]`.
- Route implementation, repo changes, checks, and PR work to `[Codex]`.
- Route AI evidence, governance, and trend interpretation to `[AI OS]`.
- Keep raw source files in the repo or source system; reference them instead of copying large bodies of text.
## Quality Gate
A Context Pack is ready when:
- the goal is clear;
- relevant files or sources are named;
- facts and assumptions are separated;
- decision-relevant claims retain authority provenance and action eligibility;
- constraints and forbidden actions are visible;
- the expected output is specific;
- the receiving project can act without asking Sergey to write an atomic task package.

## From: `ChatGPT/[LLM]/Knowledge/CONTEXT_ENGINEERING_PLAYBOOK.md`

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

## From: `ChatGPT/[LLM]/Knowledge/CTC_PROMPT_STANDARD.md`

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

## From: `ChatGPT/[LLM]/Knowledge/CONTEXT_INTAKE_CHECKLIST.md`

# Context Intake Checklist
## Purpose
Check whether incoming context is safe and usable before prompting or building a Context Pack.
## Intake Questions
- What is the goal?
- What decision or output is needed?
- Which project owns the work?
- Which sources or files are relevant?
- Which facts are supported?
- Which items are assumptions?
- What evidence is missing?
- What must not be included?
- What output format is expected?
- What quality gate decides pass / revise / blocked?
## Routing Check
| Need | Route |
|---|---|
| AI concept, KB evidence, governance, AI pattern | `[AI OS]` |
| Prompt, model routing, LLM quality, context workflow | `[LLM]` |
| Data, metrics, marts, formulas, deterministic calculations | `[Analytics]` |
| Implementation, repo changes, tests, PR | `[Codex]` |
| Decision, strategy, options, risks | `[Thinking]` |
## Forbidden Inputs
Reject or remove:
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
## Pass / Revise / Blocked
`pass` when context is curated, sources are named, facts/assumptions are separated, forbidden inputs are absent, and the output quality gate is clear.
`revise` when the goal is clear but context needs trimming, source labels, missing evidence markers, or a better output format.
`blocked` when context includes secrets, unsafe raw dumps, production/runtime artifacts, no source trail, wrong owner project, or asks `[LLM]` to replace deterministic `[Analytics]` work.
## Output
```text
Context intake status:
Owner project:
Context mode: CTC / Context Pack / handoff
Missing evidence:
Forbidden inputs removed:
Quality gate:
Next step:
```

## From: `ChatGPT/[LLM]/Knowledge/GOOD_BAD_CONTEXT_EXAMPLES.md`

# Good / Bad Context Examples
## Purpose
Show compact examples of good and bad context engineering.
These are examples, not runtime logs or transcript storage.
## Good Context Pack
```markdown
# Context Pack
## Goal
Prepare a short memo from verified Analytics findings.
## Decision needed
Which findings are strong enough for the executive memo?
## Relevant files
- `mart_main_full`
- memo draft
- Analytics QA checklist
## Facts
- Revenue variance is calculated in `[Analytics]`.
- Period and grain are explicit.
- QA status is pass.
## Constraints
- Do not change formulas.
- Do not add unsupported causes.
## Forbidden
- raw data dump
- source-card dump
- secrets
- logs
- runtime artifacts
## Open questions
- Which recommendation owner should be named?
## Expected output
Memo-ready findings with limitations.
## Quality gate
Unsupported claims listed; recommendations do not exceed data.
```
Why it is good:
- goal is clear;
- sources are named;
- facts and limitations are separated;
- forbidden inputs are explicit;
- Analytics remains owner of calculations.
## Good CTC Prompt
```text
Context:
- We have a verified QA pass from Analytics.
- The memo must be concise and evidence-aware.
- Missing evidence: action owner is not confirmed.
Task:
- Rewrite the findings into a short executive paragraph.
Constraints:
- Do not add new facts.
- Mark missing owner as limitation.
- Keep formulas and numbers unchanged.
```
Why it is good:
- small enough for CTC;
- no raw dump;
- no hidden calculation request;
- constraints are explicit.
## Bad Raw Dump
```text
Here are all files, all notes, all chunks, raw transcript, logs, and source-card dumps.
Figure out what matters and write the final answer.
```
Why it is bad:
- no goal;
- no owner project;
- raw dump leakage;
- no source/evidence labels;
- no quality gate.
## Bad Prompt That Should Route To Analytics
```text
Calculate the totals, reconcile the data, decide the drivers, and write a memo from this pasted table.
```
Why it is bad:
- asks `[LLM]` to perform deterministic calculations;
- lacks data contract, grain, period, filters, and QA;
- should route calculations to `[Analytics]` first.
## Bad Prompt That Should Route To Codex
```text
Update the repo however you think is best.
```
Why it is bad:
- no scope;
- no files;
- no forbidden actions;
- no checks;
- should become a Codex-safe task package before repo changes.
## Bad Context Inputs
Do not include:
- raw dumps;
- source-card dumps;
- chunks;
- logs;
- runtime artifacts;
- secrets;
- `.env`;
- credentials;
- API keys;
- embeddings;
- vector DB files;
- semantic search indexes;
- web UI artifacts;
- autonomous retrieval output without source review.
