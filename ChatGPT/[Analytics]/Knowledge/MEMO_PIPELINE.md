# Analytical Memo Pipeline

## Purpose

Convert verified analysis into a memo without losing evidence.

## Pipeline

```text
mart_main_full
→ analysis tables
→ insight cards
→ evidence cards
→ mart_main_tz / compact
→ management synthesis when material and management-facing
→ LLM context package, if needed
→ draft memo
→ deterministic memo QA
→ LLM Judge according to the canonical [LLM] memo gate
→ revision only from explicit findings
→ final report
```

`[Analytics]` owns verified inputs and deterministic memo QA. `[LLM]` owns Judge/revise triggers in `ChatGPT/[LLM]/Knowledge/MEMO_GENERATION_WORKFLOW.md`; this pipeline references that contract rather than redefining it.

This pipeline is the Gate 3 (narrative) checkpoint (`ANALYTICAL_REASONING_STANDARD.md` §14): it controls that memo wording is no stronger than the verified claim from Gate 2. A headline conclusion with `allowed_in_executive = no` (missing Claim/Evidence Registry lineage, or `analytical_depth = material/decision_critical` without a resolved `METRIC_DEFINITION_CARD`) does not enter the memo/executive layer; state the limitation instead.

## Memo structure

1. Executive summary.
2. Key numbers.
3. Main drivers.
4. Exceptions / anomalies.
5. Risks.
6. Management implication / decision or action if any.
7. Limitations.
8. Appendix / evidence.

### Management implication section (P1-B, issue #449, standard, active)

For `analytical_depth = material / decision_critical`, the management
implication section (item 6) reads the `ANALYTICAL_REASONING_STANDARD.md`
§16 controls rather than redefining them:

- `recommendation_status` (supported / pilot_candidate / hypothesis) from
  `RECOMMENDATION_EVIDENCE` (§16.2) governs the strength of the wording used;
  a `pilot_candidate` or `hypothesis` recommendation is worded as such, not
  as a settled management decision.
- `what_would_change_the_view` (§16.6) is stated as one compact line when a
  material evidence gap exists (§16.2–§16.5, `FINAL_EVIDENCE_SUFFICIENCY`, or
  unresolved `CONTRADICTING_EVIDENCE`); it is omitted when no such gap
  exists.

Routine/quick output does not instantiate these fields absent a material
trigger (§9 runtime collapse).

## Audience split

### Executive memo

For CFO / COO / руководители:

- verdict;
- headline numbers;
- where the money is;
- main risks;
- decisions or actions if supported;
- limitations.

Uses:

```text
mart_main_tz / mart_main_compact
```

### Finance working package

For Sergey / Finance Team / deep review:

- full evidence;
- DQ;
- timing notes;
- INOUT checks if valid;
- baseline;
- cards;
- backlog;
- reconciliation.

Uses:

```text
mart_main_full
```

## Evidence rule

Every important sentence must be backed by:

- metric;
- table/mart;
- period;
- evidence card;
- or explicitly marked as interpretation.

## Memo QA

- [ ] Executive summary is materially shorter than supporting evidence and does not exceed it.
- [ ] Key numbers trace to mart.
- [ ] Drivers are ranked by impact.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner / due date / status.
- [ ] Limitations visible.
- [ ] Hypotheses are not presented as confirmed causes.
- [ ] No headline claim with `allowed_in_executive = no` appears in the
  executive body.
- [ ] Ambiguous or unresolved metric definitions (no `METRIC_DEFINITION_CARD`)
  are not presented as flagship conclusions.
- [ ] A management recommendation is not presented as `supported` when
  `RECOMMENDATION_EVIDENCE.recommendation_status` is `pilot_candidate` or
  `hypothesis` (§16.2, standard/active, issue #449; promoted 2026-09-06, see
  `docs/evidence/ANALYTICS_P1_PROMOTION_2026-09-06.md`).
- [ ] `what_would_change_the_view` is present when a material evidence gap
  exists for material/decision-critical output, and absent otherwise (§16.6).
