# AIOS AutoResearch — MD-2 / Subject-Content Implementation — Closure Review — 2026-09-05

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409). Decision:
[#435](https://github.com/sergstack/AI-OS/issues/435) (owner decision,
2026-09-05, resolving the MD-2 and subject-content-propagation gates
directly, superseding the routed `[LLM]`/`[Analytics]`/`[AI OS]` review).
Base: `main`@`3b81126cb754a3b4021fa16666b418e62eda5c90`. This branch:
`codex/issue-435-md2-directional-observation`, built on top of the frozen
handoff commit `f87ea5f` (`codex/autoresearch-md2-handoff`, untouched).

Status: **deterministic implementation + four-control calibration
complete and passing. No live call made anywhere in this work. No merge,
no promotion.**

## Owner decision implemented

1. **MD-2 → Option A**, directional blind-Judge extension, blinding
   preserved.
2. **Subject-content propagation → Option 2**, bounded mutable-surface
   excerpt, not a full-repository dump.

## What changed

| File | Change |
|---|---|
| `schemas/autoresearch_live_semantic_finding.schema.json` | Additive `subject: "A"\|"B"\|"both"` field, required. `schema_version` bumped `0.2.0` → `0.3.0`. Positional only — never baseline/candidate identity. |
| `schemas/autoresearch_context_manifest.schema.json` | Additive `mutable_surface_excerpt` object (nullable), required (explicit `null` when not applicable, matching the schema's existing `candidate_patch_hash` convention). `context_manifest_version` bumped `0.2.0` → `0.3.0`. |
| `docs/standards/autoresearch_v02_evaluator_config.json` | `evaluator_contract_version`/`finding_schema_version` bumped to `0.3.0`; `prompt_family_text` extended to require `subject`; `evaluator_version_hash` recomputed via the real `EvaluatorConfig.frozen_hash()` (not hand-computed) — loads cleanly, no drift. |
| `scripts/autoresearch_live_judge.py` | `build_judge_prompt`'s TASK text requires `subject`. New `_verdict_for_side(records, side)` — worst verdict among findings whose positional `subject` matches, defaulting to `pass` when a side has no attributed finding. `run_blind_ab` now de-blinds per-order into `(baseline_verdict, candidate_verdict)` and checks BOTH orders agree on that de-blinded pair (previously it only compared an aggregate severity, which was vacuous under the old symmetric mapping). New `CaseSemanticEvidence.directional_verdicts` field carries the result (`None` on disagreement/failure). |
| `scripts/autoresearch_cli.py` | `_contributes_to_pair` removed; replaced with `_directional_pair(sem)`, a pure pass-through of `sem.directional_verdicts` — invents no direction of its own. `compile_subject_baseline` call now passes `research_surface=spec.research_surface`. Docstrings/limitations text updated to cite issue #435 instead of the superseded minimal-for-C1 framing. `adc.CaseObservation`, `adc.evaluate_case_material_improvement`, `adc.aggregate_decision`: **byte-for-byte unchanged**, per the owner's explicit instruction not to redefine comparator semantics. |
| `scripts/autoresearch_context_pack_compiler.py` | New `mutable_surface_excerpt(reader, research_surface)` — reuses `autoresearch_shadow_runner.mutable_surface_line_ranges` (the same anchor mechanism the hard scope gate already depends on), fail-closed (`None`) when no surface or unresolvable anchor. `compile_subject_baseline`/`compile_subject_candidate` now populate it (baseline reads pre-patch via `read_committed`, candidate reads post-patch via `read_working_tree` on the isolated shadow worktree — structurally prevents cross-contamination). `_assemble_manifest`/`equivalence_report`/`render_summary` extended additively. `CREATED_BY_VERSION` bumped to `0.3.0`. |
| `ChatGPT/[LLM]/Knowledge/AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` | Addendum documenting the live-extended schema's `subject` field; the v0.1 base schema section is unchanged. |
| `tests/test_autoresearch_live_judge.py`, `tests/test_autoresearch_coordinated_session.py`, `tests/test_autoresearch_c1r1_regression.py` | Existing fixtures updated for the new required `subject` field; two regression tests that documented the now-fixed gaps replaced with tests proving the fix (old ones are named in the new tests' docstrings for traceability). |
| `tests/fixtures/autoresearch/context_pack_examples/subject_baseline_ai_os_example.manifest.json` | Regenerated via the real, updated `compile_subject_baseline` (same source revision, same `context_hash` — only the new additive fields changed). |
| `tests/test_autoresearch_md2_calibration.py` | **New.** The four-control deterministic calibration (below). |

## A real bug found and fixed while implementing

`validate_live_finding`'s constructed `record` dict hardcoded
`"schema_version": "0.2.0"` and never copied a `subject` key from the raw
finding at all — so even after adding `subject` to the finding schema and
the prompt, every finding would have failed validation with `'subject' is
a required property`, regardless of what the Judge returned. Fixed
(`schema_version` now `"0.3.0"`, `"subject": finding.get("subject", "")`
added). Caught immediately by the existing test suite once `subject` was
required — exactly why the full suite is run after every change, not just
the new tests.

## Verification checklist (owner-specified)

| Item | Result |
|---|---|
| Actual mutated text reaches the subject transport payload | **Yes.** `test_case_payload_now_includes_the_bounded_mutable_surface_excerpt`, `test_baseline_and_candidate_excerpts_never_cross_contaminate` (anti-leakage). |
| Baseline/candidate immutable context remains equivalent | **Yes.** `equivalence_report` unchanged in its core logic, extended to also report `mutable_surface_excerpt` consistency; existing equivalence tests still pass; `test_mutable_surface_excerpt_reader_extracts_exact_anchored_text` confirms the excerpt itself excludes the protected destinations table. |
| Judge output is schema-valid or fails closed | **Yes.** All 3 malformed-shape regression fixtures from the real C1-R1 run (`tests/test_autoresearch_c1r1_regression.py`) still correctly rejected under the new schema. |
| Directional signal survives Judge → de-blinding → observation → comparator | **Yes — this is what the four-control calibration proves**, end-to-end, through the real `Controller.run_experiment` → `lj.run_blind_ab` → `adc.evaluate_case` → `adc.aggregate_decision` wiring, not isolated fixtures. See below. |
| Retries and all Judge/subject calls are counted correctly | **Yes, unchanged.** `test_bounded_retry_then_success_is_counted` and the budget-accounting tests in `test_autoresearch_live_judge.py`/`test_autoresearch_live_browser_adapter.py` pass unmodified — the counting mechanism (`BudgetState.reserve_call` inside `lba.invoke`) was not touched by this change. |
| 3→5 escalation implemented per the accepted method, or explicitly blocked | **Explicitly blocked, unchanged.** `Controller.run_experiment` still hard-guards `spec.run_count != adc.MIN_MATCHED_RERUNS` → `blocked`; no escalation path exists to silently take. This remains out of scope, per the owner's original MD-2 decision request. |
| Ledger/evidence hashes validate | **Yes.** `test_all_four_controls_ledger_hash_chain_verifies` runs all 4 calibration scenarios against one ledger file and confirms `av.verify_ledger` returns zero findings. |
| All evidence refers to the final tested revision | **Yes.** Every check below was run fresh, on this exact working tree, after all code changes landed — not reused from any prior session. |

## Four-control deterministic calibration (owner-required)

`tests/test_autoresearch_md2_calibration.py`, run through the real
`Controller.run_experiment` (only the transport and Judge are fakes —
deterministic, no I/O; every hard gate, blinding step, and comparator
function is the real, unmodified code):

| Control | Ground truth fed to the fake Judge | `raw_decision` | `pilot_decision` |
|---|---|---|---|
| Known beneficial | baseline=`blocked`, candidate=`pass` | `keep_candidate` | `candidate_for_owner_review` |
| Known harmful | baseline=`pass`, candidate=`blocked` | `discard` | `reject` |
| Semantic no-op | baseline=`pass`, candidate=`pass` | `inconclusive` | `inconclusive` |
| Mixed (gain + regression) | case A: `blocked`→`pass` (target family); case B: `pass`→`blocked` (any family) | `discard` (regression veto wins) | `reject` |

The "ground truth" fake Judge does not fabricate anything the real
pipeline wouldn't otherwise produce from a real Judge that happened to
agree with itself across both presentation orders — it independently
computes the same `primary_assignment`/`reversed_assignment` the real code
computes, and emits positional (`A`/`B`) findings that de-blind to the
intended pair consistently across both orders, exactly the shape a real,
reliable Judge would need to produce. This is calibration of the
*wiring*, not evidence about any real candidate's quality.

## Checks run fresh on this revision

```bash
python3 -m pytest tests/ -q
# 628 passed (623 baseline + 5 new calibration tests)

python3 scripts/check_manifest_paths.py       # 189/189
python3 scripts/check_repo_public_safety.py   # PASS
python3 scripts/check_index_coverage.py       # 9/9
python3 scripts/check_knowledge_bundles.py    # 0 failed
```

No live/network/model call was made anywhere in this implementation or
its verification.

## What this closure review does NOT claim

- **Not semantic readiness.** The calibration proves the wiring can
  correctly propagate a *known* ground-truth signal end-to-end. It says
  nothing about whether a real live Judge will reliably produce
  well-formed, order-consistent, correctly-attributed findings — C1-R1's
  own 5/6 malformed-output rate under the *simpler* pre-#435 schema is a
  live, unresolved reliability risk for the *new*, slightly more complex
  schema (one more required field). This is exactly the caveat flagged in
  the original MD-2 decision package's Option A recommendation.
- **Not a merge or promotion decision.** This is a local branch, not
  merged, not pushed to a PR that's been reviewed yet.
- **Not a live-call authorization.** The live batch preview (separate
  document, `AUTORESEARCH_LIVE_AUTOTUNE_BATCH_PREVIEW_2026-09-05.md`) is
  the next artifact, and is itself explicitly not authorization — it's the
  thing the owner reviews before granting one.
- **Not a claim that AutoResearch v0.2's semantic-optimization objective
  is fully realized.** It is a claim that the specific MD-2 and
  subject-content gaps identified in issue #435 are closed, deterministically
  verified, and ready for the next, separately-authorized live stage.

## Rollback

Revert this branch's commits; the frozen handoff commit `f87ea5f` and
everything on `main` are untouched. No schema on `main` is modified — the
version bumps here exist only on this unmerged branch.
