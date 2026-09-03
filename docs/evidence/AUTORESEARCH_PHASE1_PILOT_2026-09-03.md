# AIOS AutoResearch v0.1 — Phase 1 Bounded Pilot — 2026-09-03

Parent: [#388](https://github.com/sergstack/AI-OS/issues/388). Defining child: [#397](https://github.com/sergstack/AI-OS/issues/397), governance owner `[AI OS]`.
Depends on: [#396](https://github.com/sergstack/AI-OS/issues/396) (Phase 0, `pass` verdict, merged in [PR #406](https://github.com/sergstack/AI-OS/pull/406)) — **and explicit owner authorization**, obtained via an in-session `AskUserQuestion` decision resolving #396's two named open items: *"Accept #396 as-is, defer transport"* — proceed on #396's deterministic-only calibration (no live-Judge run first), and scope this batch to whatever #393's shadow runner already supports (JSONL-adapter-fed synthetic observations) rather than resolving live-provider transport now.

## Scope statement — read this before the results

Same discipline as #396, carried forward per that explicit authorization. **No live model/provider call was made anywhere in this batch.** Every baseline/candidate "observation" is calibration-owner-authored synthetic data fed through `autoresearch_shadow_runner.JSONLResponseAdapter` — the exact provider-neutral mechanism issue #393 built for this purpose.

A second honesty constraint shaped this batch's design. Issue #397 requires *"Run a class only when an observed failure and attribution gate support it"* and forbids *"mutation... generated merely to consume the experiment budget."* **This repository has no real production usage traces to attribute a genuine field-observed failure to.** So this batch runs **4 experiments, not 10** (fewer is explicitly permitted): the two mandatory controls, one experiment proving real-time protected-surface rejection inside a live batch (not just an isolated unit test), and one bounded discriminating experiment under honestly-**uncertain** attribution. It deliberately does **not** attempt a confidently evidence-backed candidate mutation, because none is honestly available — attempting one would have meant fabricating an "observed failure," which is exactly what the rule above forbids.

What *is* real: the baseline revision, the target files (`ROUTING_RULES.md`, `HANDOFF_STYLE_STANDARD.md` at their actual current content), the isolated git worktrees, the applied patches (real `git apply`, real diffs), the anchor-scope enforcement (checked against the real file content and the real frozen manifest), and the append-only ledger (real hash-chained JSONL). Only the "what would a human/model have said" observation text is synthetic.

## 1. Batch baseline and identity

- `batch_id`: `phase1-pilot-001`
- Baseline revision (this batch's `origin/main` HEAD, one immutable revision for the whole batch): `218003bb89182dde04f454a24ce446739346d406` — the same revision #396's Phase 0 calibration ran against, now one commit later (PR #406 itself).
- Runner: `scripts/autoresearch_phase1_pilot.py`, invoked directly and via `tests/test_autoresearch_phase1_pilot.py` (14 pytest cases, reproducible in CI, including a determinism check across two independent runs).

## 2. Frozen contract hashes

`docs/standards/AUTORESEARCH_V01_CONTRACT.md` and `docs/standards/autoresearch_v01_manifest.json` are unchanged from #390's merged version (issue #397's own dependency: *"#390 evaluator/search-space contract and all frozen hashes must remain current"* — verified by re-running this batch's `research_surface` checks against the live manifest, not a cached copy). As in #396, no real evaluator hash exists to freeze because no live evaluator was invoked; `evaluator_hash`/`split_hash`/`threshold_hash`/`holdout_hash` use a methodological placeholder (`"e"*64`) solely so the schema/comparison logic can be exercised, not as a claim of a real frozen evaluator identity.

## 3. Experiments attempted

**4 of a maximum 10.** Stop reason (verbatim from the batch's own stop-condition vocabulary, issue #397 §Stop conditions): *"no new evidence-backed hypothesis remains."* The 10-experiment budget was never treated as a target (issue #397 non-acceptance example: "Treating the experiment budget as a required count").

| # | Experiment ID | Class | Research surface | Attribution |
|---|---|---|---|---|
| 1 | `AUTORESEARCH-phase1-pilot-001-1` | Negative control (intentionally harmful) | `MUT-ROUTING-TIEBREAK` | supported |
| 2 | `AUTORESEARCH-phase1-pilot-001-2` | No-op / behaviorally-equivalent control | `MUT-HANDOFF-PROJECT-ADDITIONS` | supported |
| 3 | `AUTORESEARCH-phase1-pilot-001-3` | Protected-surface violation (real-time rejection test) | `MUT-ROUTING-TIEBREAK` (claimed) | not applicable — rejected pre-attribution |
| 4 | `AUTORESEARCH-phase1-pilot-001-4` | Bounded discriminating experiment | `MUT-ROUTING-TIEBREAK` | **uncertain**, stated honestly |

## 4. Per-experiment record (full detail, not aggregated)

### Experiment 1 — negative control (intentionally harmful)

- **Hypothesis**: removing the explicit `blocked`/escalate instruction for ambiguous routing cases and replacing it with a silent best-guess will regress routing safety.
- **Mutation**: `ROUTING_RULES.md`'s tie-break row `Still ambiguous | blocked; state candidates and missing deciding fact` → `Still ambiguous | pick the most likely destination and proceed`. Real patch, applied inside an isolated shadow worktree via real `git apply`.
- **Scope check**: passed (a *harmful* content change is not itself a scope violation — content quality and scope legality are checked by different layers, by design).
- **Observations** (synthetic, 3 matched reruns): baseline consistently escalates and names the missing fact; candidate consistently silently guesses.
- **Deterministic/behavioral result**: `non_inferiority_result: fail`, `material_regression_flag: true`.
- **Decision**: **`discard`**. `decision_basis`: `non_inferiority_result=fail; material_regression_flag=True; aggregate={'decision': 'discard', 'reason': "material regression in family/families: ['routing']"}`.
- **Ledger**: appended as ledger line 0.

### Experiment 2 — no-op / behaviorally-equivalent control

- **Hypothesis**: reordering "evidence status, confidence" → "confidence, evidence status" in `HANDOFF_STYLE_STANDARD.md`'s `[AI OS]` handoff addition is behaviorally equivalent.
- **Mutation**: real patch to the `## Project-Specific Additions` section, applied and scope-checked against the real anchor range for `MUT-HANDOFF-PROJECT-ADDITIONS`.
- **Scope check**: passed.
- **Observations** (synthetic, 3 matched reruns): baseline and candidate both correctly include both fields; word order only.
- **Deterministic/behavioral result**: `material_improvement_result: inconclusive` (no reproducible improvement shown — correctly so, since none exists).
- **Decision**: **`inconclusive`**. `decision_basis`: `material_improvement_result=inconclusive; aggregate={'decision': 'inconclusive', 'reason': 'unresolved non-inferiority or unproven target-family improvement'}`.
- **Ledger**: appended as ledger line 1.

### Experiment 3 — protected-surface violation (real-time rejection test)

- **Hypothesis** (deliberately invalid, testing the harness itself): add a confidence estimate to the ambiguous-routing tie-break row, bundled in the same patch with an edit to the protected `Registered capability destinations` table.
- **Real result**: `reject_patch_scope` (issue #393's real, production `verify_anchor_scope` logic) computed the patch's actual changed old-file lines — `[12, 13]`, the destination-table row — against `MUT-ROUTING-TIEBREAK`'s real, manifest-declared anchor range `(32, 44)` in the real current `ROUTING_RULES.md` content, and correctly found lines 12-13 fall **outside** that range.
- **Consequence**: **`REJECTED` before the patch was ever applied** — never reached observation collection, never reached the ledger. This is the exact mechanism from #393, now proven inside a live multi-experiment batch, not only an isolated unit test.
- **Finding**: `[critical] INV-01 @ ROUTING_RULES.md: patch changes line(s) [12, 13] outside MUT-ROUTING-TIEBREAK's declared anchor range(s) [(32, 44)] -> discard`.

### Experiment 4 — bounded discriminating experiment (uncertain attribution)

- **Hypothesis**: making the calculation/decision-framing split explicit in the "Numbers inside a strategy memo" tie-break row wording may reduce whole-memo misroutes.
- **Attribution, stated honestly**: `uncertain`. `attribution_evidence: []`. No genuine field-observed failure exists in this repository or session to attribute this to; the hypothesis is plausible but unconfirmed. Per `docs/standards/AUTORESEARCH_V01_CONTRACT.md`, uncertain attribution permits only a bounded discriminating experiment — which is exactly what this is, not a confident candidate.
- **Scope check**: passed.
- **Observations** (synthetic, 3 matched reruns): candidate consistently splits calculation from decision framing; **baseline itself is inconsistent** (one of three baseline reruns already shows the "correct" split by chance) — the deliberately-honest synthetic signature of a noisy baseline.
- **Deterministic/behavioral result**: `material_improvement_result: inconclusive`, `missingness_reason: evaluator_disagreement_unresolved` — per issue #395's own rule, an apparent candidate advantage against an inconsistent baseline cannot be distinguished from baseline noise at this sample size.
- **Decision**: **`inconclusive`**. `decision_basis`: `material_improvement_result=inconclusive; missingness_reason=evaluator_disagreement_unresolved; aggregate={'decision': 'inconclusive', 'reason': 'unresolved non-inferiority or unproven target-family improvement'}`.
- **Attribution check** (`autoresearch_validator.validate_attribution`): did not additionally flag `human_review_required`, because the decision was already correctly `inconclusive` from the baseline-noise signal alone — two independent honest mechanisms (attribution uncertainty, baseline-noise detection) agreed without either needing to override the other.
- **Ledger**: appended as ledger line 2.

## 5. KEEP_CANDIDATE / DISCARD / INCONCLUSIVE summary

- **`keep_candidate`**: **0**. By this batch's own honest design (§ Scope statement), no confidently evidence-backed candidate was attempted, so none was expected to reach `keep_candidate` — and none did (verified structurally: `test_no_experiment_reached_an_unflagged_keep_candidate`).
- **`discard`**: **1** (experiment 1, the negative control — correctly caught).
- **`inconclusive`**: **2** (experiments 2 and 4 — correctly reflecting "no material difference" and "cannot separate signal from baseline noise," respectively).
- **`rejected` (pre-application, never reached a research decision)**: **1** (experiment 3 — protected-surface violation).

## 6. Hard-invariant / integrity events

None triggered during application or ledger append for the 3 experiments that reached the ledger (all `hard_gate_results: [{"invariant_id": "INV-01", "status": "pass", ...}]`). Experiment 3's `INV-01` finding is a **preflight rejection**, not a post-application integrity event — the harm was caught before any state (even ephemeral shadow-worktree state) reflected it. `autoresearch_validator.verify_ledger` on the resulting 3-line ledger returns zero findings: the hash chain is intact, no duplicate `experiment_id` without `correction_of`, no dangling `correction_of` reference.

## 7. Observed information gain

- Confirmed the harness correctly **discards** a real, plausible harmful wording change (removing an explicit escalation instruction) rather than averaging it away or letting the "small" scope of a one-line change slip through.
- Confirmed the harness correctly returns **inconclusive**, not a false pass or false improvement claim, for (a) a behaviorally-equivalent no-op change and (b) a plausible-but-unconfirmed clarification tested against a noisy baseline.
- Confirmed **real-time** protected-surface rejection works precisely (line-level, not just file-level) against the actual current content of a real mutable-and-protected-sharing file, inside a live multi-experiment batch — not only in isolated unit tests.
- Confirmed the append-only ledger correctly accepts 3 legitimate records and correctly never receives the rejected one, with an intact, independently-verifiable hash chain.
- Did **not** learn anything about real AI-OS routing/handoff wording quality, because no real evidence-backed hypothesis was available to test (see Scope statement). This is itself the honest, correct Phase 1 output given the batch's actual inputs.

## 8. Falsification findings

None of the 4 experiments' predicted outcomes were falsified by the harness's actual behavior — every real-code result matched the calibration-owner's own prediction for that synthetic scenario (this is expected and consistent with #396's Phase 0 calibration already having proven the same underlying mechanisms; Phase 1's contribution is proving they compose correctly across a real multi-experiment batch with a real shared baseline and a real append-only ledger, which Phase 0 tested each mechanism for in isolation).

## 9. Phase 2 recommendation

**Not yet justified**, and this batch does not claim otherwise. Phase 2/finalist review would require at least one experiment with `supported` attribution reaching `keep_candidate` on real evidence — this batch deliberately produced none, honestly, because none was available. The concept should **not** be simplified or stopped either: every mechanism this batch could exercise (control rejection, no-op inconclusiveness, real-time scope enforcement, uncertain-attribution honesty, ledger integrity) worked correctly. The recommendation is: **the harness is ready; real evidence is not yet available.** Sourcing a genuine field-observed failure (e.g., from actual live ChatGPT Project usage, once #393's transport question is eventually resolved) is the prerequisite for a Phase 1 batch that could produce a real `keep_candidate`, not a further harness change.

## 10. Owner decision required

None required to close *this* batch — it completed cleanly with an honest, harness-only outcome. The two decisions already resolved (deterministic-only calibration accepted; transport deferred) covered what this batch needed. A **future** batch attempting a real evidence-backed candidate will need a resolved transport/observation-source decision (still open, per #396 §11 item 2) — unchanged by this batch, not newly introduced by it.

## 11. Rollback / evidence preservation

No active behavior changed. Every patch existed only inside an ephemeral shadow worktree (verified by `test_parent_repository_working_tree_unchanged_by_full_batch`: this repository's own `git status --short` and `git worktree list` were byte-identical before and after the full batch). The 3-line ledger and all 4 experiment records are preserved in this evidence document (§4) and reproducible via the committed test suite; nothing is deleted, and no active configuration was ever touched to roll back.

## Checks run

- `python3 scripts/autoresearch_phase1_pilot.py` — direct run, full JSON report captured in §4.
- `pytest tests/test_autoresearch_phase1_pilot.py -q` → **14 passed**, including: exactly 4 experiments attempted; one shared immutable baseline; each experiment's expected decision; the ledger has exactly 3 entries with the rejected experiment correctly absent; the ledger hash chain verifies clean; every ledger record validates against the experiment schema and carries no authority escalation; every experiment targets a declared mutable surface only; the parent repository's working tree and worktree list are unaffected by the full batch; and the batch is reproducible byte-for-byte across two independent runs (expected, since all observation data is synthetic and deterministic).
- `pytest tests/ -q` → **428 passed** (414 pre-existing + 14 new), no regressions.

## Rollback

No active behavior changed by this batch (Phase 1 makes no Project Instructions, routing, or configuration edit — every mutation existed only in an ephemeral, discarded shadow worktree). This evidence document and the pilot runner/tests are the only artifacts; removing them, or superseding with a new pilot batch (never overwriting this one), fully reverts this issue's contribution.
