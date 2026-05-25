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
→ LLM context package, if needed
→ draft memo
→ judge review
→ revised memo
→ final report
```

## Memo structure

1. Executive summary.
2. Key numbers.
3. Main drivers.
4. Exceptions / anomalies.
5. Risks.
6. Recommended actions.
7. Limitations.
8. Appendix / evidence.

## Audience split

### Executive memo

For CFO / COO / руководители:

- verdict;
- headline numbers;
- where the money is;
- main risks;
- decisions needed;
- actions;
- limitations.

Uses:

```text
mart_main_tz / mart_main_compact
```

### Finance working package

For Sergey / Finance Team / deep review:

- full evidence;
- DQ;
- timing logs;
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

- [ ] Executive summary does not exceed evidence.
- [ ] Key numbers trace to mart.
- [ ] Drivers are ranked by impact.
- [ ] Risks have `risk_basis`.
- [ ] Actions have owner / due date / status.
- [ ] Limitations visible.
- [ ] Hypotheses are not presented as confirmed causes.
