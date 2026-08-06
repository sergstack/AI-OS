# AES Phase 5 — Cross-Project Handoff Pilot: Results

Status: executed (real evidence, not narrative). Spec:
`docs/pilots/AES_CROSS_PROJECT_PILOT.md`. Standard reference:
`AUTONOMOUS_EXECUTION_STANDARD.md` Section 15 (cross-project handoff
persistence) and Section 15.1 (reverse handoff).

Evidence artifact: `docs/autonomous_execution/examples/pilot_evidence/cross_project_handoff_pilot.json`.

## Chain executed

```text
[Thinking] (exec-aes-crossproject-pilot-001, new root)
   -> [Analytics] (exec-aes-phase4-analytics-pilot-001, real Phase 4 pilot execution)
      -> [Codex] (exec-aes-codex-pilot-001, real Phase 2 pilot execution)
         -> Judge (reverse handoff, judge_verdict: not_run)
```

This branch was built by merging `origin/codex/autonomous-execution-standard-v1`
(Phase 1) with `origin/codex/aes-phase2-codex-pilot` (Phase 2, PR #228) and
`origin/codex/aes-phase4-analytics-pilot` (Phase 4, PR #229), plus
`origin/codex/aes-phase6-semantic-validator` (Phase 6, PR #226) so the
semantic validator was available to check this pilot's output. All three
merges were fast-forward/clean, additive, non-overlapping paths; no
conflicts were hit.

## Hop-by-hop verification

For each hop, the eight items `docs/pilots/AES_CROSS_PROJECT_PILOT.md`
requires tracking (execution ID, parent execution ID, requirement IDs,
defect IDs, iteration references, evidence references, acceptance
scopes/snapshot, authority status) were checked against the source
records.

### Hop 1: `[Thinking] -> [Analytics]` (`handoff-crossproject-pilot-001`)

| Item | Value | Source |
|---|---|---|
| execution_id | `exec-aes-crossproject-pilot-001` | new root, this pilot |
| parent_execution_id | `null` (root) | this pilot |
| requirement_ids | `req-crossproject-thinking-001` (handoff scope) + `req-001` carried forward | `analytics_pilot.json` requirements[0].requirement_id |
| defect_ids | none open at handoff time | n/a |
| iteration refs | `null` at handoff time (work not yet started) | n/a |
| evidence_refs | `[]` at handoff time; fulfilling execution's `ev-002` cited via `fulfillment_note` | `analytics_pilot.json` |
| acceptance snapshot | `overall_delivery: not_started` at handoff time | this pilot |
| authority_status | `not_required` | this pilot |

**Preserved:** execution_id, requirement_ids (req-001, real, verified
present verbatim in `analytics_pilot.json`), evidence_refs (ev-002,
real).

**Lineage update (adoption cleanup, resolved):** at the time this pilot
was originally run, `analytics_pilot.json`'s own `parent_execution_id`
field was `null`, since it was authored in Phase 4 before this root
execution existed. Since none of the PRs in this stack (#225-#230) are
merged, that "frozen" evidence was not actually immutable pre-merge:
during pre-merge adoption cleanup, `analytics_pilot.json` (PR #229) had
`parent_execution_id: "exec-aes-crossproject-pilot-001"` added as an
additive field, and this branch's own merged-in copy of that file was
updated to match. Lineage for this hop is now bidirectional (asserted
here in the handoff record, and present on the child record itself) —
see the Cross-check summary and Gap report below, which previously
described this as an open, one-directional gap.

### Hop 2: `[Analytics] -> [Codex]` (`handoff-crossproject-pilot-002`)

| Item | Value | Source |
|---|---|---|
| execution_id | `exec-aes-phase4-analytics-pilot-001` | `analytics_pilot.json` |
| parent_execution_id | `exec-aes-crossproject-pilot-001` (asserted by this pilot) | this pilot |
| requirement_ids | `req-001` | `analytics_pilot.json` requirements[0].requirement_id (verbatim) |
| defect_ids | `def-001` (open at handoff, resolved within the Analytics execution itself) | `analytics_pilot.json` defects[0].defect_id (verbatim) |
| iteration refs | `iter-002` (Analytics final iteration) | `analytics_pilot.json` source_revision.final_iteration_id |
| evidence_refs | `ev-002` | `analytics_pilot.json` requirements[0].evidence_refs |
| acceptance snapshot | `overall_delivery: pass` | `analytics_pilot.json` top-level `overall_delivery` |
| authority_status | `owner_review_pending` | `analytics_pilot.json` top-level `authority_status` (verbatim) |

**Preserved:** execution_id, requirement_id (req-001), defect_id
(def-001), iteration_id (iter-002), evidence_refs (ev-002),
authority_status (owner_review_pending) — all copied verbatim from the
real, frozen `analytics_pilot.json`, none invented.
**Fulfilled by:** the real Phase 2 Codex pilot execution
`exec-aes-codex-pilot-001`, whose `def-pilot-001` is carried forward as
the code-side fix. **Honesty note / gap:** `def-pilot-001` (Codex,
`clamp_percentage` missing lower-bound clamp) is **not** causally derived
from `def-001` (Analytics, MART revenue leakage) — they are two
independently-fixtured pilot defects on unrelated branches. This handoff
links them only to exercise the identity-preservation mechanics Section
15 requires, as instructed by the Phase 5 task; the record says this
explicitly rather than implying a fabricated causal chain. **Lineage
update (adoption cleanup, resolved):** the same parent-link gap
originally noted for Hop 1 applied here too (`exec-aes-codex-pilot-001`'s
own `parent_execution_id` was `null`). It has been closed the same way:
`codex_corrective_loop_pilot.json` (PR #228) now carries
`parent_execution_id: "exec-aes-crossproject-pilot-001"`, additively,
and this branch's merged-in copy matches.

### Hop 3 (reverse): `[Codex] -> Judge` (`handoff-crossproject-pilot-003`)

| Item | Value | Source |
|---|---|---|
| execution_id | `exec-aes-codex-pilot-001` | `codex_corrective_loop_pilot.json` |
| parent_execution_id | `exec-aes-crossproject-pilot-001` (asserted by this pilot, additive field) | this pilot |
| requirements_affected | `req-pilot-001` | `codex_corrective_loop_pilot.json` requirements[0].requirement_id (verbatim) |
| defects resolved (carried forward) | `def-pilot-001` | `codex_corrective_loop_pilot.json` defects[0].defect_id, status: `resolved` (verbatim) |
| iteration refs | `iter-002` (Codex final iteration) | `codex_corrective_loop_pilot.json` source_revision.final_iteration_id |
| evidence_refs | `ev-pilot-002`, `ev-pilot-003`, `ev-pilot-004` | `codex_corrective_loop_pilot.json` acceptance_scopes / validation_runs (verbatim) |
| qa_status | `not_run` | `codex_corrective_loop_pilot.json` top-level `qa_status` (verbatim) |
| judge_verdict | `not_run` | `codex_corrective_loop_pilot.json` top-level `judge_verdict` (verbatim) |
| authority_status | `owner_review_pending` | `codex_corrective_loop_pilot.json` top-level `authority_status` (verbatim) |

**Preserved:** execution_id, requirement_id, defect_id, iteration
reference, evidence_refs, and — critically — `qa_status` /
`judge_verdict` = `not_run` were **not** collapsed into a fabricated
pass. No live Judge pass occurred during this pilot; the reverse handoff
honestly reports `not_run`, matching the source record's own value, per
`AUTONOMOUS_EXECUTION_STANDARD.md` Section 15.1 ("a handoff must never
drop ... authority status").

## Cross-check summary (all eight tracked items, all three hops)

| Item | Hop 1 | Hop 2 | Hop 3 |
|---|---|---|---|
| execution_id | preserved | preserved | preserved |
| parent_execution_id | preserved (root) | bidirectional (asserted here; also now present on child record) | bidirectional (asserted here; also now present on child record) |
| requirement_ids | preserved (req-001 carried forward) | preserved (req-001, verbatim) | preserved (req-pilot-001, verbatim) |
| defect_ids | n/a (none yet) | preserved (def-001, verbatim) | preserved (def-pilot-001, verbatim, status resolved) |
| iteration references | n/a (none yet) | preserved (iter-002) | preserved (iter-002) |
| evidence_refs | n/a at handoff time; cited in fulfillment_note | preserved (ev-002) | preserved (ev-pilot-002/003/004) |
| acceptance scope/snapshot | not_started (accurate) | pass (verbatim) | not_run qa_status / judge_verdict reported separately, not collapsed |
| authority_status | not_required (accurate for an unstarted handoff) | owner_review_pending (verbatim) | owner_review_pending (verbatim), judge_verdict kept separately as not_run |

No item was dropped at any hop. Two identity items (`requirement_ids`,
`defect_ids`) that had to be "real, not invented" per the task were
verified by direct text match against the frozen Phase 2/4 JSON files
(quoted in the tables above), not re-derived from memory.

## Gap report (deliverable 3 of the pilot spec)

1. **Parent-link direction — RESOLVED during pre-merge adoption cleanup.**
   The canonical contract (Section 15) puts `parent_execution_id` on the
   child execution record. The "child" executions (Phase 2 Codex, Phase 4
   Analytics) were originally authored and evidenced *before* this Phase 5
   root execution existed, so their own `parent_execution_id` fields were
   `null` at that time, and the link could only be asserted forward, from
   this pilot's own handoff array (`fulfilled_by_execution_id`).
   Since none of PRs #225-#230 are merged yet, that evidence was not
   actually append-only/frozen in the sense that would make option (b)
   below unsafe: during pre-merge adoption cleanup, `parent_execution_id`
   was added to both `codex_corrective_loop_pilot.json` (PR #228) and
   `analytics_pilot.json` (PR #229) as an additive field only — no test
   result, defect description, hash, or command output in either record
   was altered — and this branch's merged-in copies of both files were
   updated to match. Lineage is now bidirectional: discoverable from the
   handoff record (as before) and from each child record directly.
   The general caution below (option (a) vs. (b)) still applies to any
   *post-merge* case, where amending a frozen, already-merged record would
   indeed conflict with append-only evidence: (a) create child executions
   after the parent handoff is issued (the ordering Section 15 implicitly
   assumes), or (b) amend the child record post hoc, which is only safe
   pre-merge, as an additive field, as done here.
2. **No single existing handoff mechanism natively carries all eight
   items.** `ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`,
   `ChatGPT/[Analytics]/Knowledge/ROUTING_AND_HANDOFF.md`, and
   `ChatGPT/[Thinking]/Knowledge/ROUTING_AND_HANDOFF.md` each describe
   project-specific routing, not a shared identity envelope; the AES
   handoff record (this file) is what supplies that envelope on top,
   exactly as Section 15 intends ("AES adds tracking, not a new
   workflow").
3. **`judge_verdict` / `qa_status` staying `not_run` is itself evidence
   the separation works**, not a shortfall: the reverse handoff (hop 3)
   demonstrates that an unfinished authority step is representable and
   distinguishable from a real pass, rather than being silently defaulted
   to one.

## Commands run and results

```text
git fetch origin
git checkout -b codex/aes-phase5-cross-project-pilot origin/codex/autonomous-execution-standard-v1
git merge --no-edit origin/codex/aes-phase2-codex-pilot        # fast-forward, clean
git merge --no-edit origin/codex/aes-phase4-analytics-pilot    # clean merge, no conflicts
git merge --no-edit origin/codex/aes-phase6-semantic-validator # clean merge, no conflicts (needed for step 6)

python3 -m json.tool docs/autonomous_execution/examples/pilot_evidence/cross_project_handoff_pilot.json
# -> valid JSON

python3 scripts/validate_autonomous_execution_record.py \
  docs/autonomous_execution/examples/pilot_evidence/analytics_pilot.json \
  docs/autonomous_execution/examples/pilot_evidence/codex_corrective_loop_pilot.json
# -> PASS analytics_pilot.json: 0 violations
# -> PASS codex_corrective_loop_pilot.json: 0 violations
# confirms this pilot's new file did not disturb the Phase 2/4 records' validity.

python3 scripts/validate_autonomous_execution_record.py
# default glob (docs/autonomous_execution/examples/**/*.json) also picks up
# cross_project_handoff_pilot.json and reports "PASS ... 0 violations" for
# it, but this is a vacuous pass, not a meaningful validation: the script's
# SEM-001..SEM-008 checks read fields like `requirements`, `overall_delivery`,
# `defects` via .get(..., []) and simply find nothing to flag, because this
# file is a handoff-chain artifact (object with a `handoffs` array), not a
# full AES execution record. The validator was written for the single
# top-level execution-record shape; it does not meaningfully apply to this
# pilot's output shape, and the "0 violations" result should not be read as
# a semantic endorsement of the handoff-chain content -- it just means the
# validator found nothing to check. Noted per the Phase 5 task instructions
# rather than forcing the file into an execution-record shape it isn't.

python3 -m pytest tests/ -q
# -> 92 passed in 1.40s (full merged tree: Phase 1 + Phase 2 + Phase 4 + Phase 6 tests together)

python3 scripts/check_manifest_paths.py
python3 scripts/check_index_coverage.py
python3 scripts/check_knowledge_bundles.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_codex_goal_mode_defaults.py
python3 scripts/check_project_instructions_length.py
# -> all pass (see command list in the PR body / final report)
```

## Verdict

The pilot ran for real, on the merged Phase 1+2+4(+6) tree, and
demonstrably preserved execution_id, requirement_ids, defect_ids,
iteration references, and evidence_refs across all three hops using ids
copied verbatim from frozen Phase 2/4 evidence — no placeholder or
invented ids were used for those fields. `judge_verdict` is honestly
`not_run` throughout; no Judge or QA pass is claimed. One genuine
contract-vs-practice gap was found and reported (parent-link direction on
frozen child records), matching the pilot spec's deliverable 3
requirement to report such gaps rather than paper over them.
