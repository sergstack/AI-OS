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
