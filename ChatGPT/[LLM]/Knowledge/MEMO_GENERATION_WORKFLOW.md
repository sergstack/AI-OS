# Memo Generation Workflow

## Pipeline

```text
curated context snapshot
→ draft
→ deterministic output QA
→ judge when a trigger applies
→ revise only from explicit findings
→ targeted recheck
→ final memo
```

## Inputs

- verified numbers;
- evidence cards;
- required sections;
- audience;
- tone;
- constraints.

## Minimal run contract

1. Build one curated context snapshot and assign a `context_id`. Reuse it for draft, judge, and revise; rebuild it only when sources change or QA identifies missing evidence.
2. Before an LLM Judge, check deterministic items first: required sections, source/evidence labels, visible limitations, and the requested output schema.
3. Run Judge when the output is material or decision-critical, evidence-sensitive, fails deterministic QA, uses an unreviewed workflow/model path, or a human explicitly requests review.
4. Bypass Judge only when every trigger in step 3 is false and deterministic QA passes. If QA/Judge returns `pass`, publish the draft without rewriting it. If it returns `revise`, change only the listed findings and rerun the affected checks. If a material finding remains after one revision, return `blocked` for human review instead of starting an open-ended loop.

Do not treat fewer calls as proof of token savings. Record available per-run evidence (`context_id`, generation steps, Judge trigger, revision count, and provider-reported input/output tokens when available); otherwise mark token cost `not measured`.

## Required sections

1. Executive summary.
2. Key facts.
3. Analysis.
4. Risks.
5. Recommendations.
6. Limitations.
7. Evidence appendix.

## Judge criteria

- unsupported claims;
- missing evidence;
- overconfident recommendations;
- unclear numbers;
- weak structure;
- wrong audience.

Material or evidence-sensitive output cannot pass deterministic QA alone; Judge remains required. Revise remains findings-driven.
