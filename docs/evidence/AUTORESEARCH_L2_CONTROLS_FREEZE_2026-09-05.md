# AIOS AutoResearch — L2 Four-Control Freeze — 2026-09-05

Status: **FROZEN, PRE-LIVE. No live model/browser call was made producing
this document.** All content below was verified against the real,
unmodified repository code (`autoresearch_shadow_runner`,
`autoresearch_context_pack_compiler`, `autoresearch_live_judge`,
`autoresearch_validator`) — no fake-Judge fixture, no fabricated gate
result. Every mutation is a real, bounded text change inside a declared
mutable surface, presentable to a real subject/Judge pipeline as-is.

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Decision:
[#435](https://github.com/sergstack/AI-OS/issues/435). Supersedes the
fake-Judge-fixture four-control calibration in
`tests/test_autoresearch_md2_calibration.py` for live-authorization
purposes — that suite remains valid for what it proves (the comparator
wiring), but its four scenarios all reuse one candidate/patch and hardcode
Judge output, so it cannot stand in for a live four-control run (this is
the same distinction the live contract's §9 draws between
`calibration_deterministic_layer` and `live_evidence_required`).

**Shared baseline revision for all four controls (and for L1's own
candidate)**: `0b1ce29386342ef4e1884d8a58b574445572575e` — identical to
C1-R1's own baseline, and verified byte-identical against current
`origin/main` (`281585ddde18010238ff7fb22a21a2a528391d18`) for every file
any of these five candidates touches (`ROUTING_RULES.md`,
`ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`, `HANDOFF_STYLE_STANDARD.md`) —
`git diff` between the two revisions on these three paths is empty. Reusing
one shared baseline across all five case-runs keeps this consistent with
manifest invariant INV-09 (baseline must not change inside one program).

**Pipeline runtime revision these controls are built against**:
`281585ddde18010238ff7fb22a21a2a528391d18` (current tip of `origin/main`,
PR [#436](https://github.com/sergstack/AI-OS/pull/436) merged).

## What was actually run, per control (no live call in any step)

For each of the four controls below, the following ran against the real
code, not a mock:

1. **Patch built for real** inside a disposable, git-isolated shadow
   worktree at the shared baseline revision (`autoresearch_shadow_runner.create_shadow_worktree`
   / `remove_shadow_worktree`) — the literal `git diff` of the actual
   mutation, not hand-typed patch text.
2. **Patch-fingerprint gate** (`verify_patch_fingerprint`): declared
   `candidate_patch_hash` matches the actual patch bytes' sha256.
3. **Patch-scope gate** (`reject_patch_scope` / `verify_anchor_scope`, via
   `compile_subject_candidate`): the patch touches only its declared
   mutable surface's own file, only within that surface's own declared
   anchor heading range, and no protected surface — enforced by the real
   deterministic code, not asserted by hand.
4. **Context-equivalence gate** (`equivalence_report`): baseline and
   candidate context packs have identical source sets, ordering, and
   rendering rules; the only content-changed source is the declared target
   file; the mutable-surface excerpt's identity (surface/path) matches
   across baseline and candidate.
5. **Literal subject-content propagation gate**: the compiled
   `mutable_surface_excerpt` for baseline and candidate have different
   `excerpt_hash` values and carry the literal changed text (not just a
   byte-count line) — this is the exact gap PR #436 closed; re-verified
   here for four new candidates, not just re-asserted from that PR's own
   tests.
6. **Schema validation**: a full `autoresearch_v02_live_batch_config`
   document for the control validates clean against
   `schemas/autoresearch_v02_live_batch_config.schema.json`
   (`authority_status: owner_review_pending`, `max_cost_amount: null` —
   honest pre-authorization values, not a placeholder positive number).
7. **Evaluator hash re-verification**: `EvaluatorConfig.load(...)` on
   `docs/standards/autoresearch_v02_evaluator_config.json` recomputes
   `evaluator_version_hash` and finds no drift from the frozen
   `960e1408c58e97d9fab1aa19c62147dbfa20de2839f90e86a7f0236ad8bdb853`.
8. **Baseline/candidate isolation** (`reject_config_mismatch`): flagged as
   a **precondition only** at this stage — this check compares the actual
   `runtime_model_configuration` captured from real subject responses, so
   it can only be meaningfully exercised once real captures exist. Not
   fabricated here. What is verified now: both conditions declare the same
   case IDs and are planned under the same transport/model/runtime
   identity, so the check is *satisfiable*, not yet *satisfied*.
9. **Ledger/evidence preparation**: each control's `spec.json`,
   `batch_config.json`, `candidate.patch`, baseline/candidate excerpt
   texts, both context manifests, and the full `gate_results.json` are
   committed under its own evidence subdirectory (paths below) — nothing
   is held only in this document's prose.

Full machine-readable gate output for each control is in that control's
own `gate_results.json`; this document is a human-readable summary of it,
not a restatement that could drift from it.

## Control 1 — Beneficial (`L2-BEN-1`)

| Field | Value |
|---|---|
| Candidate ID | `L2-BEN-1` |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Mutable surface | `MUT-ROUTING-TIEBREAK` (`ROUTING_RULES.md`) — distinct row from C1-R1's own (`Coding task preparation`), no collision with L1 |
| Mutation class | `semantic_change` (adds a previously-absent tie-break rule for a genuinely undefined case, mirroring the sibling `Production readiness` row's own "earliest unfinished stage wins" pattern — allowed for this surface) |
| Exact patch | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_beneficial/candidate.patch` |
| Patch SHA-256 | `7941ec48800b5ebb751b491bd9154a344d1ba1e5b5e766ebdfa7bc4e024f0506` |
| Case ID / family | `l2-ben-1-rollout-tiebreak` / `routing` |
| Target/non-target | target (`target_family_flag: true`) — single case |
| Expected directional outcome | `keep_candidate` / `candidate_for_owner_review` — the "Production workflow rollout" row previously had no stated tie-break for the mixed-stage case (a completed `[Codex]` implementation vs. an unfinished `[LLM]` design); the candidate adds "earliest unfinished stage wins," letting a subject give a definitive, rule-grounded answer it could not give before |
| Forbidden outcome | `discard` / `reject` |
| Rollback | no active state touched by freezing; if executed and discarded, discard the ephemeral shadow worktree only (automatic) |
| Evidence path | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_beneficial/` |

## Control 2 — Harmful (`L2-HARM-1`)

| Field | Value |
|---|---|
| Candidate ID | `L2-HARM-1` |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Mutable surface | `MUT-AIOS-HANDOFF-WORDING` (`ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`, `### Goal Mode handoff`) |
| Mutation class | `consolidation` (merges the distinct "risks" field into "acceptance criteria," producing the garbled phrase "the criteria to accept the risk" — a real information-loss defect, not a hidden semantic redefinition; `consolidation` is an allowed class for this surface, `semantic_change` is not) |
| Exact patch | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_harmful/candidate.patch` |
| Patch SHA-256 | `ea0084bfe80c25f56fd4b2c952e941ad022e61d6c67a130bd5e78e7e02834a9c` |
| Case ID / family | `l2-harm-1-codex-handoff-fields` / `handoff` |
| Target/non-target | target (`target_family_flag: true`) — single case |
| Expected directional outcome | `discard` / `reject` — baseline correctly lists 5 required fields (goal, context, constraints, **risks**, acceptance criteria); candidate's garbled wording drops the distinct "risks" disclosure requirement, a real dropped-field regression analogous to the `handoff_fidelity` rubric's own "penalize dropped IDs, lost provenance" |
| Forbidden outcome | `keep_candidate` / `candidate_for_owner_review` |
| Rollback | no active state touched by freezing; if executed and discarded, discard the ephemeral shadow worktree only (automatic) |
| Evidence path | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_harmful/` |

## Control 3 — Semantic no-op (`L2-NOOP-1`)

| Field | Value |
|---|---|
| Candidate ID | `L2-NOOP-1` |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Mutable surface | `MUT-HANDOFF-PROJECT-ADDITIONS` (`HANDOFF_STYLE_STANDARD.md`, `## Project-Specific Additions`) |
| Mutation class | `ordering` (swaps the listed order of "rollback" and "PR summary needs" in the `[Codex]` bullet; same 6 fields, same set, pure order change) |
| Exact patch | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_noop/candidate.patch` |
| Patch SHA-256 | `3132ecf427996be18987b5a9261e68d45805d61a0f32bafd256a8e3d4c7a1586` |
| Case ID / family | `l2-noop-1-codex-fields-list` / `handoff` |
| Target/non-target | target (`target_family_flag: true`) — single case |
| Expected directional outcome | `inconclusive` — the field *set* a subject should report is identical before and after; a real Judge should find no material behavioral difference. This is a genuine byte-level diff (unlike this repo's own deterministic fixtures, which reuse one unrelated patch for every control) — the hypothesis under test is specifically whether the pipeline can correctly recognize a real but meaning-preserving change as a non-improvement, rather than manufacturing a false positive from wording noise |
| Forbidden outcome | `keep_candidate` or `discard` decided on the strength of this candidate alone (a stable-but-wrong verdict here is exactly what this control exists to catch) |
| Rollback | no active state touched by freezing; if executed and discarded, discard the ephemeral shadow worktree only (automatic) |
| Evidence path | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_noop/` |

## Control 4 — Mixed: local improvement + material regression (`L2-MIXED-1`)

| Field | Value |
|---|---|
| Candidate ID | `L2-MIXED-1` |
| Baseline revision | `0b1ce29386342ef4e1884d8a58b574445572575e` |
| Mutable surface | `MUT-AIOS-CONTEXT-PRIORITY` (`ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`, `## 2. Индексы и источники`) |
| Mutation class | `consolidation` (adds one genuine conflict-priority clarification, and separately drops one entry — `ANTI_PATTERNS.md` — while editing the adjacent checklist; a single patch with two distinct real effects, by design, since that is what a "mixed" control is for) |
| Exact patch | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_mixed/candidate.patch` |
| Patch SHA-256 | `c88596959994f4aeca3a079156080475c28d40ed10b6fc05bbf31a69d37d4976` |
| Case ID / family | `l2-mixed-1-conflict-priority` (target) + `l2-mixed-1-checklist-completeness` (non-target), both `scope_execution` |
| Target/non-target | `l2-mixed-1-conflict-priority`: target (`target_family_flag: true`); `l2-mixed-1-checklist-completeness`: non-target (`target_family_flag: false`) — "elsewhere," per the task's own definition of a mixed control |
| Expected directional outcome | target case shows a `keep_candidate`-shaped local improvement (candidate now states `GOVERNANCE_RULES.md` wins over `PROJECT_ROUTING.md` on conflict, where baseline states no such rule); non-target case shows a real regression (candidate's checklist silently drops `ANTI_PATTERNS.md`, so a subject asked to list every file to also check will under-report); **the regression veto in `adc.aggregate_decision` (unchanged by PR #436, per owner instruction) should force the overall result to `discard`/`reject` despite the local target-case gain** |
| Forbidden outcome | `keep_candidate` / `candidate_for_owner_review` — this control exists specifically to prove the regression veto is not silently outvoted by a simultaneous local improvement, live, not only under the fixture in `tests/test_autoresearch_md2_calibration.py::test_control_mixed_candidate_regression_vetoes_local_gain` |
| Rollback | no active state touched by freezing; if executed and discarded, discard the ephemeral shadow worktree only (automatic) |
| Evidence path | `docs/evidence/autoresearch_live_l1_l2_2026-09-05/l2_mixed/` |

## Honesty note on directional predictions

Every "expected directional outcome" above is a predeclared hypothesis
about what a correctly-functioning pipeline plus a competent live Judge
*should* produce, reasoned from the actual content of each real mutation —
not a guaranteed result. That is the entire purpose of running these
controls live rather than trusting the deterministic fixture suite alone:
a real Judge could still disagree, format-fail past its retry ceiling, or
find something in the wording this document did not anticipate. Any of
those outcomes is itself informative and must be reported honestly
(including as a finding against this freeze's own case design), never
silently reclassified to match the prediction.

## Case-family-to-rubric mapping used

`routing` → `routing_correctness`; `handoff` → `handoff_fidelity`;
`scope_execution` → `scope_discipline` — all three are existing frozen
rubric blocks in `docs/standards/autoresearch_v02_evaluator_config.json`
(unchanged by this freeze). No new case family or rubric block was
introduced.

## What is not claimed by this document

- No live call has been made for any of these four controls.
- No candidate is authorized, accepted, or promoted by this freeze — that
  remains a separate, later owner decision, unconditionally, regardless of
  which way a live run eventually points.
- `baseline/candidate isolation` (gate 8 above) is confirmed satisfiable,
  not yet satisfied — it closes only once real captures exist.
- This freeze does not itself grant `live_call_authority` or
  `usage_budget_authority` for any envelope; see
  `AUTORESEARCH_LIVE_AUTHORIZATION_PACKET_2026-09-05.md` for the one
  document that consolidates the actual ask.
