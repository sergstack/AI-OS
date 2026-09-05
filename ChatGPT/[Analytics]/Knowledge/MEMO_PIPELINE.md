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
