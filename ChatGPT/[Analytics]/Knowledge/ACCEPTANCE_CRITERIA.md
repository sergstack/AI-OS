# Analytics Acceptance Criteria

A result is accepted when:

1. Question and scope are clear.
2. Inputs are listed.
3. Data contract exists or missing fields are explicit.
4. Grain, period and filters are documented.
5. Stage and mart main files are created or designed.
6. Calculation method is documented.
7. QA checks passed or failed with explanation.
8. Findings are traceable to data.
9. Limitations are explicit.
10. Handoff package is complete if another project is needed.
11. Before publication, every flagship metric in a quantitative report passes
    `QUANTITATIVE_SANITY_GATE.md`; otherwise the result is `revise` or
    `blocked` and is not published as a final quantitative conclusion.
12. For `analytical_depth = material / decision_critical`, the Analytical Judge
    gate (`ANALYTICAL_REASONING_STANDARD.md` §8) ran after findings and before
    memo / report generation, and an `ANALYTICAL_JUDGE` result is recorded with
    `status: pass` (or a `revise` resolved by one bounded correction and a
    passing re-check). A `blocked` Judge status means the final management
    conclusion is not published. `maximum_claim_strength` does not exceed
    `FINAL_EVIDENCE_SUFFICIENCY`; `driver != root cause` and
    `correlation != causation` hold. Routine / no-trigger cases satisfy this
    through the compact QA note without a full Judge record.
13. Material/flagship/ratio-like metrics have an approved
    `METRIC_DEFINITION_CARD` (`ANALYTICAL_REASONING_STANDARD.md` §11); an
    unresolved material metric definition blocks a strong management
    conclusion.
14. `VALUE_STATE` distinctions are not collapsed into a generic null where
    material (§12); a claim built on unresolved material uncertainty coverage
    is at most `PARTIALLY_SUPPORTED`, unless the uncertainty is quantified and
    demonstrably does not change the conclusion.
15. For `analytical_depth = material / decision_critical`, every headline
    claim has complete Claim/Evidence Registry lineage (§13); missing
    lineage sets `allowed_in_executive = no` and the claim does not appear
    in the executive layer.

## Main file acceptance

```text
stage_main_full: pass/fail/blocked/not_applicable
mart_main_full: pass/fail/blocked/not_applicable
mart_main_tz_or_compact: pass/fail/blocked/not_applicable
slices_from_mart_main_full: pass/fail/blocked/not_applicable
```

## Acceptance status

```text
accepted: yes/no
qa_status: pass/fail/blocked
quantitative_sanity_gate_status: pass/revise/blocked/not_applicable
analytical_judge_status: pass/revise/blocked/not_applicable
metric_definition_status: approved/provisional/blocked/not_applicable
value_state_coverage_status: pass/revise/blocked/not_applicable
headline_claim_gate_status: pass/blocked/not_applicable
confidence: high/medium/low
residual_risks:
known_limitations:
next_step:
```

## Usability acceptance

A result is not accepted if it is technically complete but unusable for the requested task.

For `quick` mode:

- max 1 user-facing table;
- max 5 metrics;
- max 12 visible columns;
- no workbook unless explicitly requested;
- no hidden expansion into `full` package.

For `standard` mode:

- compact front view required;
- no more than 3-5 sheets unless justified;
- every extra sheet must have a business purpose.

For `full` mode:

- workbook may be large, but must include:
  - README / index;
  - compact front sheet;
  - data dictionary;
  - field groups;
  - evidence appendix.

## Material management synthesis acceptance

For `analytical_depth = material / decision_critical` and management-facing output:

- the business question is answered by an executive verdict;
- the smallest sufficient set of material findings is prioritized by a supported business criterion;
- headline business meaning is supported or its evidence gap is explicit;
- materially different performance dimensions and data/control artefacts remain distinct where relevant;
- management implication and decision/action if any do not exceed verified evidence;
- material uncertainty remains visible, with what would change the view where applicable;
- strategic choice is routed to `[Thinking]` when it depends on trade-offs, risk appetite, or preferences;
- the executive layer is materially shorter than the supporting evidence.

Routine compact tasks are excluded from expanded synthesis acceptance.

## Material Plan/Fact variance acceptance

For cases governed by `VARIANCE_DIAGNOSTIC_CONTRACT.md`:

- reported and normalized management views are both traceable and use explicit, non-mixed sign conventions;
- gross adverse/favorable movement, normalized net variance, and primary attribution reconcile deterministically;
- gross classification coverage declares population, denominator, classified/unclassified movement, and unknown rows separately from net reconciliation;
- materiality basis and selected/excluded population are explicit;
- controllability, recurrence, generalization, and accountability claims have required evidence or remain unknown/not established;
- adjusted view is supplementary, reconciled, and uses explicit adjustment polarity;
- management synthesis follows the contract semantically without expanding routine output.

## Blocked status

Use `blocked` when:

- required data is missing;
- grain is unknown;
- DQ Fail;
- no reconciliation possible;
- metric formulas undefined;
- compact-only input is insufficient for requested conclusion;
- implementation is required before result can be produced.
- a required flagship metric has a blocked quantitative sanity gate.
- the Analytical Judge gate returns `blocked` (required prerequisite,
  reconciliation, grain, validation path, or discriminating evidence
  unavailable).
- a material/flagship/ratio-like metric has no approved
  `METRIC_DEFINITION_CARD` and the conclusion depends on it.
- a headline claim for `analytical_depth = material / decision_critical` has
  no complete Claim/Evidence Registry lineage (`allowed_in_executive = no`).

## Not production-ready rule

Smoke QA or a good memo does not equal production readiness. Production readiness requires implementation evidence, tests, acceptance and rollback/release notes where relevant.
