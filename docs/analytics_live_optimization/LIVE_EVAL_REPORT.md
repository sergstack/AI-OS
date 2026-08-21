# Analytics Live Response Optimization

- date: 2026-08-21
- owner project: `[Analytics]`
- implementation owner: `[Codex]`
- branch: `codex/analytics-live-optimization`
- method: baseline → defect → minimal contract correction → external sync → same-prompt rerun → regression check
- production status: `NOT AUTHORIZED`

## Scope and handoff

From `[Analytics]` to `[Codex]`: improve answer compactness without changing formulas, metric definitions, schemas, deterministic-calculation rules, evidence classes, QA gates, routing, or production authority. Allowed scope is Analytics Project Instructions, its smoke contract/result, focused tests, and this evidence record. Rollback is a scoped restore plus replacement of external Project Instructions with the baseline version.

## Baseline

| Case | Observed result | Verdict |
|---|---|---|
| no-data Top-3 request | 1,850 visible characters; correct `NOT CALCULABLE`, but an empty three-row ranking and repeated blocker sections | `REVISE` |
| supplied Plan/Fact fixture | correct ranking, aggregate arithmetic, zero-denominator handling, root-cause guard, QA/limitations, and Codex boundary | `PASS` |
| strict seven-line weak-evidence request | one compact paragraph; fact/hypothesis separation, one action, limitation, QA, and weak confidence | `PASS` |

Defect `ANALYTICS-LIVE-001`: the default no-data quick path could add placeholder output and repeat one limitation under several labels. Classification: `contract`; severity: `recoverable`; affected scope: response presentation only.

## Correction

- `quick` now uses the smallest evidence-bearing form and at most one table containing actual inputs or calculated rows;
- the missing-data fast path forbids placeholder rankings, empty Top-N tables, invented examples, and full-workflow expansion;
- the response retains `NOT CALCULABLE`, minimum missing input, one supported observation or bounded hypothesis, confidence, and one next action;
- repeated `QA` / `LIMITATION` / `GATE` blocker sections collapse into one combined line.

No calculation, mart, sign-normalization, reconciliation, metric, evidence, Judge, routing, or handoff rule was weakened.

## Corrective rerun

| Case | Before | After | Result |
|---|---:|---:|---|
| same no-data Top-3 prompt | 1,850 chars | 1,034 chars | 44.1% shorter; placeholder table removed; semantic gates preserved |
| same supplied Plan/Fact prompt | 2,070 chars | 1,515 chars | 26.8% shorter; ranking, zero-denominator, root-cause and Codex-boundary checks preserved |

The second response omitted an unrequested aggregate-total paragraph while preserving every explicitly requested output. This is treated as compactness, not a semantic regression. A future prompt that explicitly requests totals remains a separate test candidate.

## External state

The `[ANALYTICS]` Project Instructions were saved through the Codex in-app Browser and verified after reload. The persisted value contains the new quick and missing-data contracts and is 7,703 characters. The refreshed `ANALYTICS_05_QA_GOVERNANCE_ROUTING.md` source was uploaded; the older same-name source remains visible because removing an existing external source was not inferred from the optimization request. ChatGPT temporarily displayed its rapid-request rate limit between cases; completed responses were not resent.

## Validation

- focused repository suite: 38 passed;
- Local Developer Worker parse: `RUN-7f1bcfa5e1e24979`, `run_status: passed`, exit code `0`, `command_observed: true`;
- live no-data corrective rerun: pass;
- live supplied-data regression rerun: pass;
- full real-data pilot: `NOT RUN`;
- full external Analytics smoke suite: `NOT RUN`.

## Acceptance

| Scope | Status |
|---|---|
| compact no-data behavior | PASS |
| supplied-data calculation behavior | PASS |
| evidence, QA, routing, and handoff preservation | PASS |
| external instruction sync | PASS |
| external bundle 05 upload | PASS_WITH_DUPLICATE_SOURCE_LIMITATION |
| rollback readiness | PASS |
| real source-backed pilot | NOT RUN |
| production | NOT AUTHORIZED |

Overall delivery: `PASS_WITH_LIMITATIONS`. The focused live cases passed, but a real owner dataset and the full external suite were not run; the external Project also retains the prior same-name bundle until its removal is explicitly authorized.
