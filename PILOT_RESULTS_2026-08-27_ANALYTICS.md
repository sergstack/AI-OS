# Pilot Result

Pilot ID: `PILOT-ANALYTICS-001`
Date: 2026-08-27
Project: `[Analytics]`
Owner project: `[Analytics]`
Pilot status: candidate
Manifest/upload status: existing `[Analytics]` sync evidence retained; this pilot used only an artificial three-row prompt dataset
Owner: Sergey

Input:

> Quick-analyse three artificial plan/fact rows for 2026-08: A/acquisition 100→120, B/retention 150→120, and C/acquisition 0→30. Define the data contract and `RAW → stage_main_full → mart_main_full`; show deterministic calculations, QA, findings, and limitations without causal claims or a Codex handoff.

Expected behavior:

- state grain, period, filters, units, formulas, and data layers;
- perform traceable calculations and reconciliation;
- handle the zero-plan row without an invented percentage;
- show QA, findings, and limitations without causal claims.

Actual behavior:

- defined grain as `period × entity × channel`, period `2026-08`, and units as unspecified currency;
- designed raw, stage, and mart layers with documented `delta`, `abs_delta`, and conditional `delta_pct` formulas;
- calculated totals of plan `250`, fact `270`, delta `+20`, and `+8%` at total level;
- marked the zero-plan row as percentage not applicable, reconciled all totals, and stated causes as unsupported.

Evidence:

- direct live response: <https://chatgpt.com/g/g-p-69e9f058f22481918c854fffa86335ec-analytics/c/6a902031-8d40-83eb-97c9-995fcdd157ca>;
- no user data, file upload, settings change, implementation, or production action occurred.

Checks run:

- manual review against all `PILOT-ANALYTICS-001` success and failure criteria: pass;
- grain, period, filters, and units explicit: pass;
- data contract and main layers designed: pass;
- calculations traceable and reconciled: pass;
- zero-plan edge case handled without invented percentage: pass;
- limitations visible; no causal claim or Codex handoff: pass.

Questions asked:

| Question text | Hard blocker? | Instruction gap | Change made / issue |
|---|---|---|
| None | no | none observed in this run | none |

Pass / fail: pass
Confidence: medium
Risks / limitations:

- one artificial, three-row case does not prove behavior on real datasets;
- currency, history, and operational drivers were intentionally absent;
- owner acceptance, cross-project evidence, and production promotion remain separate gates.

Blockers:

- no promotion or production authorization exists.

Decision status: candidate; owner review pending
Revisit trigger: new pilot evidence, changed Analytics instructions, a recurring QA failure, or an owner decision.
Next step: owner reviews this candidate result; then run the bounded cross-project pilot and record it separately.
Link: <https://chatgpt.com/g/g-p-69e9f058f22481918c854fffa86335ec-analytics/c/6a902031-8d40-83eb-97c9-995fcdd157ca>
