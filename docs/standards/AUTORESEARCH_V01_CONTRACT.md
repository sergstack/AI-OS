# AIOS AutoResearch v0.1 — Controlled Research Contract

- Status: candidate contract; frozen pending explicit owner authorization at each phase gate.
- Canonical owner: `[AI OS]` / `[Codex]` jointly, per `ROUTING_RULES.md` (governance promotion questions route to `[AI OS]`; implementation routes to `[Codex]`).
- Production promotion: not authorized. No child issue may cite this contract as authorization to merge, deploy, or promote a candidate.
- Parent: [#388](https://github.com/sergstack/AI-OS/issues/388). Defining child: [#390](https://github.com/sergstack/AI-OS/issues/390). Baseline: [#389](https://github.com/sergstack/AI-OS/issues/389), `docs/evidence/AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md`.
- Machine-readable companion: [`autoresearch_v01_manifest.json`](autoresearch_v01_manifest.json).

## Purpose

Freeze the exact research boundary for AIOS AutoResearch v0.1 before any code, schema, runner, or experiment is allowed. This is a **bounded extension** of existing AI-OS governance, not a second governance framework: every rule below cites its canonical owner instead of restating it. Where this document and an existing standard appear to overlap, the existing standard governs and this document only narrows scope for the AutoResearch case.

This contract implements #388's directive: *"AI-OS already contains routing, AES, eval definitions, supervised-loop governance, behavioral benchmarks, validators, fixtures, and evidence conventions. The proposed AutoResearch capability must reuse these components rather than create a second governance or execution framework."*

## What this is not

Per #388's own "Forbidden actions" (owner reference, not restated in full here): no `LOOP FOREVER` or unattended self-improvement; no automatic candidate promotion, commit, PR, merge, deploy, or production change; no candidate modifying its own evaluator, cases, thresholds, split, holdout, history, or protected surfaces; no opaque weighted quality score; no benchmark cherry-picking or post-hoc label/threshold changes; no broad refactor or multiple independent mechanisms in one experiment; no weakening of evidence, safety, authority, ownership, or routing semantics to improve a score; no vector DB, embeddings, semantic search, dashboard, runtime database, generic agent platform, or second governance framework; no secrets, `.env`, credentials, unapproved provider/API calls, or hidden external side effects.

## 1. Frozen, mutable, and forbidden surfaces

The full, machine-addressable allowlist is [`autoresearch_v01_manifest.json`](autoresearch_v01_manifest.json)'s `mutable_surfaces` and `protected_surfaces` arrays. Summary:

**Mutable (v0.1 search space, default-deny outside these four surfaces):**

| Surface | File | Scope |
|---|---|---|
| `MUT-ROUTING-TIEBREAK` | `ROUTING_RULES.md` | Tie-break rules table wording, including the "Still ambiguous" row |
| `MUT-AIOS-CONTEXT-PRIORITY` | `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` | §2 "Индексы и источники" (context-selection / KB-priority wording) |
| `MUT-AIOS-HANDOFF-WORDING` | `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md` | §7 "Goal Mode handoff" and "Quick Goal Mode" subsections only |
| `MUT-HANDOFF-PROJECT-ADDITIONS` | `HANDOFF_STYLE_STANDARD.md` | "Project-Specific Additions" section only |

**Explicitly protected even within a mutable file** (not an exhaustive restatement — see manifest): routing destination tables, the `[AI OS]` governance/promotion-gate section, the mandatory response-header/evidence-label/standard-section output-contract sections, `HANDOFF_STYLE_STANDARD.md`'s Default Style/Merge/Forbidden-Inputs sections, AES, the eval registry, `REGRESSION_GATE.md`, `FAILURE_REGISTRY.md`, existing benchmark freeze manifests and holdouts, Judge calibration cases, `main`, the live ChatGPT Project configuration, the future experiment ledger, and this contract/manifest pair itself.

**Rationale for the narrow cut**: #388 says "selected wording," not "the whole file." Per this contract's own acceptance bar, *unknown mutable clauses stay blocked rather than guessed* — sections that read as an output contract, an authority/safety gate, or a duplicated routing table are protected by default even inside an otherwise-mutable file. The owner may widen `mutable_surfaces` later; that is itself a protected-surface change to this manifest, reviewed the same way as any other.

## 2. Allowed mutation classes

`semantic_change`, `wording_clarification`, `deletion`, `ordering`, `consolidation` — defined and enforced per mutable-surface entry in the manifest (`allowed_mutation_classes`). A diff whose actual shape does not match its declared mutation class is `INV-05`.

## 3. One-experiment identity rule

Owned by #388's "Grain" section (not restated here): one observed failure class + one candidate cause + one falsifiable hypothesis + one mutation class + one target file + one minimal reversible logical diff. This contract operationalizes it as `AUTORESEARCH-<batch_id>-<sequence>` with the required-field set in the manifest's `one_experiment_identity`. A batch has one immutable baseline revision (§7).

## 4. Hard invariants

Ten hard invariants (`INV-01`..`INV-10`) are defined in the manifest with `detection_owner` (`deterministic` or `hybrid`), `severity`, and `consequence`. They cover: mutating outside the allowlist, targeting `main`/the live Project directly, evaluator/split/holdout/threshold hash drift, ledger append-only violations, multi-mechanism or mislabeled-class diffs, missing or ineligible causal attribution, opaque scalar scoring, `keep_candidate` mislabeled as acceptance, mid-batch baseline drift, and Researcher role overreach.

Required rule, verbatim from #390: **any material hard-invariant violation forces `discard`**; evaluator/split/holdout/threshold/history integrity violations **invalidate the batch** (not just the one experiment).

## 5. Decision semantics: `keep_candidate` / `discard` / `inconclusive`

Full definitions in the manifest's `decision_semantics`. Summary of the required rules this contract enforces verbatim:

- `keep_candidate` **never** means accepted, active, merge-ready, or production-authorized (`INV-08`). It only advances a candidate inside `PROMPT_QA_FACTORY.md`'s existing lifecycle (§9), pending owner review.
- `inconclusive` is **mandatory**, not optional, whenever the frozen eval and the batch's statistical method cannot distinguish candidate from baseline. It must never be silently rounded to `keep_candidate` or `discard`.
- `discard` covers any hard-invariant violation, a supported harmful/regression result under `REGRESSION_GATE.md`'s existing matrix, or attribution that is `ineligible`/`uncertain` per `FAILURE_REGISTRY.md` without a valid bounded-discriminating-experiment frame.

This contract deliberately does **not** pick the statistical/non-inferiority method (owned by child #395) or the shadow-runner transport (owned by child #393) — #390's own "Forbidden actions" exclude implementing runner, validator, schemas, fixtures, or provider integration here. Those children must satisfy the rules above; they do not get to redefine them.

## 6. Batch baseline immutability

One accepted baseline per batch, reusing `REGRESSION_GATE.md`'s `baseline_id` / `configuration_ref` / `source_revision` / `accepted_by` / `acceptance_status` contract **verbatim** — this contract defines no second baseline schema. The baseline cannot change mid-batch (`INV-09`); a new baseline starts a new batch.

## 7. Authority, merge, and production separation

No new authority is created. Reused verbatim from existing canonical owners:

- `GOAL_MODE.md` Merge Policy: "Codex and agents must not manually merge pull requests or decide final mergeability by themselves... Tier 2 protected changes require owner review."
- `HANDOFF_STYLE_STANDARD.md` "Merge And Acceptance": "Codex / Codex APP must not manually merge PRs or decide final mergeability by themselves."
- AES §2 (canonical ownership) and §13 (external authority separation) govern who may declare an external effect authorized.

Role separation (Researcher / Evaluator / Owner) is detailed in the manifest's `authority_separation`, following `benchmarks/supermanager/`'s existing Runner/Evaluator/Final-Judge role split (per the #389 audit). A kept candidate is exactly a Codex-style "candidate / ready for owner review" PR — nothing more.

## 8. Stop conditions and rollback ownership

Stop conditions are not restated: they are `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`'s existing "Stop Conditions" list, plus #388's own "Forbidden actions" and "Revisit triggers", all cited by reference in the manifest's `stop_conditions_reference`.

Rollback: each experiment is a single revertible diff to one declared mutable surface. Rollback authority is the human owner, never AutoResearch itself. `keep_candidate` changes no baseline, active Project configuration, merge state, or production state, so it needs no rollback beyond reverting the candidate branch (#388 Grain section).

## 9. Research / evaluator / owner role separation and Prompt QA Factory relationship

This resolves the #389-audit open question explicitly (audit §3, finding 2): **AutoResearch v0.1 does not define a second candidate-lifecycle status vocabulary.** `docs/standards/PROMPT_QA_FACTORY.md` already owns the `candidate → test → judge → revise → selected` lifecycle for "ChatGPT Project prompts," which is exactly this contract's mutation class. AutoResearch supplies added rigor — frozen eval, hard invariants, blind comparison, causal attribution, statistical distinguishability — that feeds Prompt QA Factory's `test` and `judge` stages; it does not replace, parallel, or duplicate that lifecycle. A kept candidate is reported using Prompt QA Factory's existing statuses.

Prompt QA Factory's 1–5 UX Score, if carried at all, is descriptive metadata only, never a decision input (`INV-07` forbids any scalar score as the basis for `keep_candidate`/`discard`).

Any AutoResearch `eval_id` added to `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md` must be a **definition row only**, matching the shape of the existing `BASELINE-REGRESSION` / `FAILURE-REGRESSION` / `GOAL-CLOSURE` rows. Run results belong only in the separate experiment ledger that #391/#392 will build — the registry stays "a registry of eval standards only... [that] does not store run results" (its own words, unchanged).

## 10. Phase 0 / Phase 1 boundary and Phase 3 exclusion

- **Phase 0** (calibration, child #396) requires #391–#395 accepted or merged first.
- **Phase 1** (up to 10 bounded one-mutation experiments, child #397) requires **explicit owner authorization** after Phase 0, per #388's dependency graph.
- **Phase 3** (broader search across other projects) is explicitly out of scope for parent #388 and requires a separate parent issue and a separate owner decision (#388 Scope boundaries, not repeated here).

This contract governs Phase 0 and Phase 1 only. It authorizes neither.

## Revisit triggers

Same as #388's own "Revisit triggers" (owner reference, not restated): evaluator calibration fails; candidate rankings are unstable across reruns; improvements do not generalize to holdout; most failures cannot be attributed to the mutable surface; manual bounded review provides equivalent gains at materially lower complexity; governance regressions occur; model/provider/runtime changes invalidate matched comparison; holdout secrecy cannot be enforced; scope, cost, risk, or owner decision changes.
