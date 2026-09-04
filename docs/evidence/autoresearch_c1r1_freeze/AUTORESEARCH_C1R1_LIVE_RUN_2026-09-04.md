# AIOS AutoResearch v0.2 — C1-R1 Live `manual_candidate_evaluation` — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Runtime: PR
[#434](https://github.com/sergstack/AI-OS/pull/434) (issue #433), merged to
`main` as `3b81126cb754a3b4021fa16666b418e62eda5c90`.

Status: **one bounded live `manual_candidate_evaluation` executed and
completed.** `pilot_decision: inconclusive`. No merge, no promotion, no
Phase 1, no active Project/routing change.

**Branch-placement note:** this document and the rest of the freeze package
in this directory were written into the working tree of a Codex session
whose then-checked-out branch (`codex/chatgpt-project-live-optimization-source`,
head `cf294f3`) does **not** descend from `3b81126` and has no AutoResearch
scripts at all (confirmed via `git merge-base`). They are plain files on
disk, not committed to any branch. Before this evidence is committed, move
these files onto a branch actually based on `main`@`3b81126` (or later).

---

## Why C1-R1, not C1

The frozen candidate C1 (`ROUTING_RULES.md` → `## Tie-break rules` →
"Coding task preparation" row, `a prompt or workflow deliverable` → `a
prompt/workflow deliverable`, baseline `0b1ce29386342ef4e1884d8a58b574445572575e`)
had its exact patch bytes and case text recorded only in a prior session's
ephemeral temp-directory worktree (`scratchpad/arpilot/`), which was never
committed and no longer exists. The declared patch hash
`44505534bf2f910e70725a4244f98347324a7cb1d4af00d8120e501e643c3c87` could not
be recovered from git history or the test suite (`git grep` across all
tracked history returns nothing).

Per owner decision 2026-09-04, the same semantic mutation was regenerated
from the frozen description as a **distinct candidate identity, C1-R1** —
not a claimed restoration of the original C1 — with its own hash and its
own newly-authored case text, both explicitly owner-confirmed before any
live call.

## C1-R1 identity

| Field | Value |
|---|---|
| `candidate_id` | `C1-R1` |
| `baseline_revision` | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| `research_surface` | `MUT-ROUTING-TIEBREAK` (declared in `docs/standards/autoresearch_v01_manifest.json`) |
| `mutation_class` | `wording_clarification` |
| `candidate_patch_hash` | `9e7d0a1ea07f4b626b7be9a5bbd42b3df950b3481016fddf43d86d26bc45509c` |
| `case_id` | `c1-routing-tiebreak-coding-task-prep` (`case_family: routing`) |

Freeze package: `ROUTING_RULES.baseline.md`, `ROUTING_RULES.candidate.md`,
`candidate.patch`, `batch_config.json`, `spec.json` (all in this directory).
`candidate.patch` applies cleanly via `git apply --check` against the
baseline revision and was re-verified byte-identical (same sha256)
immediately before the live run.

## Execution method: disposable manual bridge

`Controller.run_experiment` (the real, unmodified #433 sequencer) needs a
live `mcp_call` bound inside one Python process. This session's tool
architecture cannot interleave live `mcp__playwright__browser_*` calls into
a running Python subprocess — there is no way for a spawned Python process to
drive the same signed-in browser instance (`--remote-debugging-pipe`, no CDP
port to attach a second automation client to). Per owner-authorized
execution strategy, a **disposable, scratch-only bridge**
(`scratchpad/arpilot/c1_bridge.py`, not committed) was used instead:

1. Pure functions already in the frozen code (`_case_payload`,
   `cli._transport_policy`, `lj.primary_assignment` /
   `reversed_assignment` / `build_judge_prompt`) computed the exact subject
   and Judge payload text deterministically, with no live call.
2. The operator (this session, holding real `mcp__playwright__browser_*`
   tool access) drove each of the 12 real live submissions by hand, in a
   fresh `chatgpt.com` conversation each time (dedicated signed-in profile,
   `session_policy: fresh_conversation`), capturing the genuine response
   text, model identity (`data-message-model-slug`), URL, and timestamps.
3. A `RecordedBrowserTransport` (satisfying the existing
   `BrowserSessionTransport` protocol used by `lba.invoke`, `FakeBrowserTransport`'s
   sibling) replayed those genuine captures keyed by **exact payload text**,
   with strict equality — no queued item for a requested payload raises
   `LiveTransportError` rather than fabricating a response.
4. The Judge side reused the real, unmodified `lj.BrowserJudgeModel` (not a
   custom stand-in) wired to the same transport, so budget accounting,
   `LiveTransportError` handling, hashing, and sanitization all run through
   the real `lba.invoke()` exactly as `autoresearch_coordinated_session.py`
   wires it.
5. `Controller.run_experiment(spec, batch_config, budget, evidence_dir)` was
   then called once, for real, consuming only the pre-captured genuine data.
   Every hard gate, the blind-A/B Judge sequencing, `adc.aggregate_decision`,
   the MD-4 relabeling, schema validation, and the ledger append are the
   real, unmodified functions from commit `3b81126` — nothing in this
   pipeline stage was reimplemented.

The bridge script and captured-response files are disposable scratch
(`scratchpad/arpilot/`, untracked) and are being left as non-canonical
scratch evidence rather than deleted, per the owner's stated option.

## What actually happened, live

- **6/6 real subject calls** made and captured (3 baseline + 3 candidate,
  each a fresh conversation). Model identity `ui_observed:
  gpt-5-6-thinking` on every call.
- The subject prompt is a **manifest** (file names + byte counts via
  `cpc.render_summary`), not literal `ROUTING_RULES.md` content — by the
  real, unmodified `compile_subject_baseline`/`render_summary` design, not a
  bridge defect. The model answered from its own prior knowledge of the
  routing table rather than from injected text; both conditions produced
  near-identical answers, and one candidate rerun (rerun 1) explicitly
  refused to fabricate an exact quote it could not see in context — a
  genuine, honest live-model behavior difference the harness's own bounded
  retries and Judge did not need to paper over.
- **6/6 real Judge calls** made. 5 of the 6 raw responses were
  schema-noncompliant on their one live attempt (unescaped quotes inside a
  JSON string value in 3 cases; `evidence` supplied as an object instead of
  the required string in 2 cases) — genuine live-model formatting failures,
  captured and fed through unedited. With `retry_limit: 1` and only one
  genuine capture per (rerun, order) slot, each retry-exhaustion resolved
  through the harness's own real, already-coded fallback
  (`LiveTransportError` → `validation_error` → bounded-retry exhaustion →
  `contributes: inconclusive`) — never a fabricated pass, never an extra
  live call. Because `run_blind_ab` returns on the first order's failure
  without evaluating the second, 2 of the 6 real Judge calls I drove
  (rerun 0 order 1, rerun 2 order 1) were never actually reached by that
  code path; they are genuine live captures, just logically unconsumed.
  Exactly one rerun (rerun 1, order 0) produced a schema-valid finding:
  verdict `revise`, flagging the candidate's quote-refusal as a hand-off
  gap relative to baseline.

## Result

```
Hard gates:              pass (patch applies cleanly; scope gate over
                         MUT-ROUTING-TIEBREAK holds)
Context equivalence:     equivalent=true; differences=["ROUTING_RULES.md"]
                         only (matches the declared mutable surface)
Per-rerun consistency:   judge_disagreement (Judge failure, not order
                         disagreement) for all 3 reruns; contributes=
                         inconclusive for all 3
Comparator raw decision: {"decision": "inconclusive", "reason":
                         "unresolved non-inferiority or unproven
                         target-family improvement"}
Pilot decision:          inconclusive
```

`inconclusive` was the pre-declared expected, accepted outcome for this
near-cosmetic candidate. It carries no acceptance, merge, or promotion
authority.

## Evidence artifacts (scratch, non-canonical, untracked)

- `scratchpad/arpilot/evidence/c1r1-routing-tiebreak-2026-09-04_evidence.json`
- `scratchpad/arpilot/evidence/c1r1-routing-tiebreak-2026-09-04_record.json`
  (schema-valid `manual_candidate_evaluation`)
- `scratchpad/arpilot/evidence/autoresearch_manual_evaluations.jsonl`
  (hash-chained ledger; integrity verified via the real `av.verify_ledger`
  — 0 findings)
- `evidence_package_sha256: 33cdacb74c5f1f61340b65f54ce133110e1bd1effe926066c7c635f4959d6975`

## Active-state proof / cleanup

No commit, no push, no merge. The execution worktree (a detached checkout of
`3b81126` used only to import the real modules and run them) was removed
after the run. `main` and the checked-out branch's `HEAD` were unaffected
throughout. The disposable bridge remains as non-canonical scratch per the
owner's instruction, not deleted.

## Follow-ups this run surfaces (not fixed here — out of scope)

- `scripts/autoresearch_live_browser_adapter.py`'s `_timeout_seconds()`
  hardcoded-180 fallback (tracked separately, pre-existing, chip
  `task_9db59036`) — untouched.
- The Judge's own output format reliability (5/6 schema-noncompliant raw
  responses in this one run) may warrant a future look at the frozen
  prompt/schema pairing under `AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md`
  — noted as an observation, not acted on; changing the evaluator contract
  is explicitly out of scope for this run.
- This freeze package currently lives on a branch unrelated to the
  AutoResearch line of work (see branch-placement note above) and should be
  relocated before being committed.
