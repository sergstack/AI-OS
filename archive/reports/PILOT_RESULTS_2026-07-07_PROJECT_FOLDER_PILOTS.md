# Project Folder Pilot Results

Date: 2026-07-07
Issue: #63
Method: repository-file review plus existing 2026-07-06 runtime evidence review.
Execution context: repo-only Codex pass; no fresh live ChatGPT UI pilot was run in this PR.
Production promotion: no

## Scope

This report represents the six individual ChatGPT project pilots requested by
issue #63. It does not claim fresh runtime success. Existing live smoke evidence
from `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` remains useful
context, but the realistic pilot cases below still require live execution before
they can move from `not_run` to `candidate` or `accepted`.

## Questions Asked Metric

| Pilot scope | Questions asked by agent | Hard blocker? | Instruction gap | Change made / issue |
|---|---:|---|---|---|
| Project folder pilots repo-only pass | 0 | no | none observed | none |

## Pilot Results Matrix

| Pilot ID | Project | Input source | Expected behavior | Actual output / blocker | Verdict | Evidence link / repo path | Fix required | Residual risks | Next step |
|---|---|---|---|---|---|---|---|---|---|
| `PILOT-AIOS-001` | `[AI OS]` | `PILOT_CASES.md` | Assess an AI topic/pattern, separate supported / weak / unsupported evidence, avoid blocked promotion items, route and hand off clearly. | Fresh realistic pilot not run in live ChatGPT UI in this PR. | not_run | Existing smoke context: `SMOKE_QA_RESULTS.md`; runtime smoke context: `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | none in repo files | Live Project runtime may drift after manual sync. | Run the suggested AI OS pilot in ChatGPT UI and paste concise evidence into a future pilot result. |
| `PILOT-THINKING-001` | `[Thinking]` | `PILOT_CASES.md` | Produce a decision memo with options, facts/assumptions, risks, decision status, revisit trigger, and handoff if needed. | Fresh realistic pilot not run in live ChatGPT UI in this PR. | not_run | Existing runtime smoke context: `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | none in repo files | Smoke QA does not prove decision-memo pilot quality. | Run the Thinking pilot in ChatGPT UI and record the memo excerpt plus verdict. |
| `PILOT-ANALYTICS-001` | `[Analytics]` | `PILOT_CASES.md` | Define data contract, stage/mart, deterministic QA checks, findings, and limitations without LLM arithmetic. | Fresh realistic pilot not run in live ChatGPT UI in this PR. | not_run | Existing Analytics QA context: `ChatGPT/[Analytics]/PROJECT_FOLDER_QA_ANALYTICS_REPORT.md`; runtime smoke context: `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | none in repo files | Requires real or representative data prompt and output capture. | Run the Analytics pilot in ChatGPT UI and record data contract / mart / QA output. |
| `PILOT-LLM-001` | `[LLM]` | `PILOT_CASES.md` | Create a reusable prompt/workflow item with prompt_id, model class routing, quality gate, judge/revise handling, and failure modes. | Fresh realistic pilot not run in live ChatGPT UI in this PR. | not_run | Existing cross-project smoke context: `CROSS_PROJECT_SMOKE_QA_RESULTS.md`; runtime smoke context: `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` | none in repo files | Prompt registry behavior still needs a live reusable-prompt pilot. | Run the LLM pilot in ChatGPT UI and record the prompt registry item. |
| `PILOT-CODEX-001` | `[Codex]` | `PILOT_CASES.md` | Execute one docs-only issue-driven task through branch, checks, PR, human review, and no auto-merge. | This PR series demonstrates the branch/checks/PR/no-auto-merge workflow, but it is not a live `[Codex]` ChatGPT Project pilot output. | not_run | PRs opened in this issue queue; `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md` for runtime smoke context | none in repo files | A real ChatGPT Project `[Codex]` answer should still be captured. | Run the Codex pilot in ChatGPT UI or explicitly accept a repo PR as the pilot evidence. |
| `PILOT-INBOX-001` | `[Inbox Router]` | `PILOT_CASES.md` | Classify 20 mixed raw inputs with destination, reason, confidence, first safe action, and no target-project work. | Fresh realistic 20-input pilot not run in live ChatGPT UI in this PR. | not_run | Runtime smoke context: `PILOT_RESULTS_2026-07-06_RUNTIME_CHATGPT_AND_OLLAMA.md`; Router bundle consistency context: PR #113 | none in repo files | Requires a 20-input live classification output. | Run the Inbox Router pilot in ChatGPT UI and record the routing table. |

## Optional Pilots

| Pilot ID | Verdict | Reason |
|---|---|---|
| `PILOT-CROSS-001` | not_run | Should run only after individual pilots have live result evidence. |
| `PILOT-CODEXAPP-001` | not_run | Requires a local executor task package pilot; not run in this repo-only PR. |

## Acceptance Status

partial

All six individual pilots are represented with honest `not_run` blockers and
next steps. No production readiness is claimed. No `PILOT_CASES.md` status was
upgraded because this PR does not add fresh live pilot output evidence.

## Next Step

Run the six live ChatGPT Project pilots one by one and replace the `not_run`
rows with captured output summaries, verdicts, residual risks, and owner
acceptance status.
