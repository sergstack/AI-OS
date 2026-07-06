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
