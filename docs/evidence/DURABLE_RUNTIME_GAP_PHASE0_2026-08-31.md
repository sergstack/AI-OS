# Durable Runtime Gap Review — Phase 0

- date: 2026-08-31
- issue: [#342](https://github.com/sergstack/AI-OS/issues/342)
- owner project: `[AI OS]`
- execution scope: Phase 0 evidence review only
- decision: `blocked` — durable-runtime gap not proven
- Restate implementation path: `not_planned`
- production status: `not_authorized`

## Question and evidence boundary

This review asks whether observed AI-OS/AES use proves a recurring, material
gap that requires a durable runtime rather than a smaller correction to the
current Dual Surface and AES model. It uses repository-recorded live evidence
available on `origin/main` at `4ef92ba`; it does not treat specifications,
acceptance cases, expected behavior, or framework capabilities as observed
runtime evidence.

No Restate integration, dependency, service, external live run, routing change,
or AES semantic change was performed.

## Observed cases

| Case ID | Observed failure or friction | Frequency / recurrence | Material impact | Current workaround | Can Dual Surface / AES or a smaller fix address it? | Evidence refs | Owner intervention required | Candidate minimal fix | Why a durable runtime would materially improve it |
|---|---|---|---|---|---|---|---|---|---|
| `DRG-001` | No failure: three real Dual Surface Live Tests completed with cross-project continuity and zero manual orchestration. | 3 tested routes | None observed | None | Yes; current path passed the tested cases. | `CURRENT_STATUS.md`, "Dual Surface operational acceptance" | No | Continue observation; record only material friction. | Not demonstrated. |
| `DRG-002` | No failure: `PILOT-CROSS-001` preserved the goal, constraints, owner boundaries, and return path across `[AI OS] -> [Thinking] -> [AI OS]`. | 1 bounded route | None observed | None | Yes; the existing handoff path completed the case. | `docs/evidence/PILOT_RESULTS_2026-08-27_CROSS.md` | No | Capture the next real failure without changing architecture. | Not demonstrated. |
| `DRG-003` | ChatGPT request limits interrupted or prevented live eval cases. Four matrix cases remained unscored and a clean retry remained `NOT RUN`; other recorded work waited for the limit to clear. | Recurs in multiple live-eval records; the exact number of independent incidents is not recoverable from the retained evidence. | Partial or blocked validation, delayed reruns, and an operator return to fresh chats. No lost AES IDs, duplicated side effect, invalid closure, or semantic-state drift was recorded. | Wait for the limit to clear; rerun only incomplete cases; do not resend completed independent cases. | A bounded request cadence, smaller batches, and the existing recorded continuation can address the observed workflow without a runtime layer. The provider UI limit itself is outside Dual Surface. | `docs/llm_cross_project_live_eval/LIVE_EVAL_REPORT.md`; `docs/chatgpt_system_live_optimization/LIVE_EVAL_REPORT.md`; `docs/pilots/AIOS_G2_G3_MEASUREMENT_TASK.md` | Operator action was required to return and submit fresh chats; no material owner decision was required. | Add measured request pacing/batch limits to the next live-eval execution and retain exact incomplete-case state. | A durable timer could theoretically resume an authorized machine-callable operation, but no such execution boundary or measured recovery benefit is evidenced here. Restate cannot by itself remove or safely automate the signed-in ChatGPT UI limit. |
| `DRG-004` | Historical ChatGPT conversation references later opened as empty, disabled views, leaving no admissible input for independent Judge review because raw responses were intentionally not retained. | 2 material `001` cases in one pilot; fresh same-session reruns later passed. | Historical cases remained blocked; no false Judge verdict was created. | Rerun material cases and Judge them in the same supervised session. | Yes. This is an access/evidence-retention boundary, not loss of canonical AES state. A smaller evidence-capture policy is the relevant control. | `docs/response_quality_evals/LIVE_PILOT_REPORT.md` | Operator rerun was required; owner decision is needed only if retention policy changes. | Keep same-session Judge execution and preserve the minimum sanitized Judge input or an explicit non-retention blocker under existing policy. | Not demonstrated. A runtime journal cannot reconstruct provider content that policy intentionally did not retain. |
| `DRG-005` | Earlier project-specific handoffs did not natively carry all eight AES identity items. | 1 cross-project pilot finding | Potential traceability gap; no item was lost in the executed pilot. | The AES handoff envelope carries the items and the pilot verified them by source match. | Yes; the existing AES envelope resolved the observed contract gap without a new runtime. | `docs/pilots/AES_CROSS_PROJECT_PILOT_RESULTS.md`, "Gap report" | No | Keep AES as the single semantic and identity owner. | Not demonstrated. |

## Phase 0 gate

| Criterion | Result | Evidence-based finding |
|---|---|---|
| At least one material durable-runtime gap is directly observed | `fail` | Rate-limit and inaccessible-chat friction is observed, but no evidence shows crash-state loss, retry-state loss, duplicate effects, invalid closure, or another failure that requires durable runtime mechanics. |
| The gap is recurring or has material downside | `partial` | Provider/UI interruption recurs and delays validation, but independent-incident frequency, recovery effort, and owner-time cost were not measured. |
| It is not merely a UI, prompt, routing, or documentation defect | `fail` | The unresolved candidates are provider UI/access and evidence-retention boundaries. Routing/continuity cases passed. |
| A simpler bounded fix is insufficient or clearly inferior | `fail` | Pacing/batching, incomplete-case recording, same-session Judge review, and the existing AES continuation/handoff envelope remain viable smaller controls. |
| Restate capabilities map directly to the observed gap | `fail` | No authorized machine-callable operation was identified for Restate to resume; the signed-in provider UI and retention policy remain external boundaries. |
| Expected benefit is measurable | `fail` | The records do not contain a baseline for manual recovery actions, elapsed recovery time, duplicate effects, or unnecessary owner interventions. |
| Rollback remains local | `pass` | An isolated future adapter could be removable, but this condition alone cannot authorize Phase 1. |

## Judge verdict

`blocked`: Phase 0 does not pass all mandatory criteria. The observed evidence
supports continued use of the current Dual Surface/AES path and targeted
measurement of interruptions; it does not support a Restate fit test.

Accordingly:

- do not start Phase 1 or Phase 2;
- do not add Restate code, configuration, deployment, or a competing state model;
- retain this record as the Issue #342 Phase 0 result;
- keep architecture adoption and production promotion unauthorized.

## Revisit trigger and next evidence

Reopen the fit gate only after a real execution records at least one of the
following with an execution ID and evidence references: crash/restart state
loss, repeated manual reconstruction of the same AES state, durable-wait
failure on a machine-callable boundary, duplicated side effects, lost retry
state, or invalid closure caused by lost runtime state.

For that case, record the number of manual recovery actions, owner
interventions, elapsed recovery time, state/ID mismatches, duplicate effects,
the smallest non-runtime alternative, and an explicit Restate capability map.

## Rollback

Remove this evidence record and its two index/status references, or close the
pull request without merging. No runtime or canonical AES state requires
rollback.
