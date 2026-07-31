# Artifact Contracts

## Traceable excerpt

Each excerpt identifies excerpt ID, source ID, author, work, normalized location, short paraphrase or compliant quotation, reason, target card, and confidence. Avoid long copyrighted quotation and ornamental excerpts.

## Author Card

Separate `FACT`, `INTERPRETATION`, `HYPOTHESIS`, `RECOMMENDATION`, `BLOCKER`, core problem, concepts, next extraction, and confidence. Partial coverage remains explicit.

## Idea Card

One source-backed idea per card with evidence reference, concrete application, anti-pattern, transfer risk, confidence, and bounded candidate status. Missing evidence, risk, or confidence blocks the card.

## Applied Pattern

Required fields:

- source ideas;
- input;
- workflow;
- output;
- QA check;
- rollback;
- failure modes;
- transfer risk;
- confidence;
- export status.

Do not create a pattern from an unsupported idea.

## Judge

Review unsupported claims, evidence strength, hidden assumptions, corpus completeness, transfer risk, routing, QA, rollback, and premature automation. Verdict is `pass`, `revise`, or `blocked`. Non-pass blocks export.

## Revisor

Run only after `revise`. Fix only Judge-required defects; do not add facts, upgrade evidence, or erase limitations, risks, blockers, or confidence.

## Export candidate

Export only after Judge pass. Required state:

- `owner_acceptance: pending`;
- `execution_status: not run` unless observed otherwise;
- `production_status: NOT AUTHORIZED`;
- `contains_raw_source_text: false`;
- evidence and transfer risk explicit.

Export one functionally relevant bounded output to one receiving project. Never export books, normalized text, excerpt dumps, source manifests, blocked/rejected artifacts, or local paths.
