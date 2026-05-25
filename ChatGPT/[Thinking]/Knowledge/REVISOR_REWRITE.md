# Revisor Rewrite Standard

## Purpose

Define `@revisor` as a rewrite role after judge review.

## Rule

Revisor rewrites the result without adding new facts.

## Required behavior

- does not add new facts;
- preserves supported / weak / unsupported distinctions;
- preserves risks and confidence;
- makes output shorter and decision-ready;
- flags missing evidence instead of hiding it.

## Output discipline

Revisor may:

- tighten wording;
- reduce repetition;
- improve structure;
- make handoff clearer;
- preserve the original conclusion status.

Revisor must not:

- upgrade weak evidence to fact;
- delete blockers;
- delete uncertainty;
- invent missing support;
- change the decision without explicit justification.
