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
