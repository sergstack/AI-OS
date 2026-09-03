# AIOS AutoResearch v0.1 — Baseline & Collision Audit — 2026-09-03

Parent: [#388](https://github.com/sergstack/AI-OS/issues/388) ([Goal] AIOS AutoResearch v0.1).
Child: [#389](https://github.com/sergstack/AI-OS/issues/389) (Baseline and collision audit of existing eval/AES infrastructure) — mandatory baseline gate, no dependencies.

This is a **read-only inventory**, not an implementation. It does not create a harness, database, agent, dashboard, provider call, experiment, or candidate mutation, and it does not touch active Project Instructions, routing, AES, eval semantics, benchmarks, schemas, scripts, tests, or workflows.

## 0. Revision and inspected paths

- Baseline revision: `3f3a6b6a4a11c62b0ba70a9dccee5878a40e3ff6` (`origin/main`, observed 2026-09-03).
- `git status --short`: clean (no uncommitted changes at audit time).
- Full applicable test suite at this revision: `pytest tests/ -q` → **243 passed** (observed, this audit).
- Inspected paths (superset of #388/#389's required input layer):
  `ROUTING_RULES.md`, `HANDOFF_STYLE_STANDARD.md`, `GOAL_MODE.md`,
  `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`,
  `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md`,
  `docs/standards/PROMPT_QA_FACTORY.md`,
  `docs/standards/LOCAL_FIRST_COMPUTE_POLICY.md`,
  `docs/standards/BOUNDED_PROJECT_CONTEXT_FRESHNESS.md`,
  `ChatGPT/[AI OS]/PROJECT_INSTRUCTIONS.md`,
  `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md`,
  `ChatGPT/[AI OS]/Knowledge/ACT_OR_ABSTAIN_EVAL_GATE.md`,
  `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`,
  `ChatGPT/[AI OS]/Knowledge/REGRESSION_GATE.md`,
  `ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md`,
  `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md`,
  `ChatGPT/[AI OS]/Knowledge/GOLDEN_EVAL_CASES.md`,
  `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md`,
  `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`,
  `PROJECT_CAPABILITIES.yaml`, `schemas/`, `scripts/`, `tests/`,
  `benchmarks/live_behavioral/`, `benchmarks/supermanager/`, `docs/evidence/`.

## 1. Capability inventory

| # | Artifact / capability | Path | State |
|---|---|---|---|
| 1 | Routing ownership | `ROUTING_RULES.md` | existing |
| 2 | Handoff field set + merge policy pointer | `HANDOFF_STYLE_STANDARD.md` | existing |
| 3 | Goal Mode contract + merge policy | `GOAL_MODE.md` | existing |
| 4 | Execution/authority/acceptance state machine | `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` (AES v2.0.0) | existing |
| 5 | Parent/child issue + PR gate pattern | `docs/standards/PARENT_CHILD_ISSUE_GATE_STANDARD.md` | existing (this audit follows it) |
| 6 | Prompt/instruction candidate lifecycle | `docs/standards/PROMPT_QA_FACTORY.md` | existing |
| 7 | Local-model eligibility/fallback policy | `docs/standards/LOCAL_FIRST_COMPUTE_POLICY.md` | existing, candidate/not production-authorized |
| 8 | Status-anchor freshness contract | `docs/standards/BOUNDED_PROJECT_CONTEXT_FRESHNESS.md` | existing |
| 9 | Eval definition registry (no run results) | `ChatGPT/[AI OS]/Knowledge/AI_EVAL_REGISTRY.md` | existing |
| 10 | Act/abstain decision gate + paired smoke cases | `ChatGPT/[AI OS]/Knowledge/ACT_OR_ABSTAIN_EVAL_GATE.md` | existing |
| 11 | Supervised loop catalogue + native-subagent worktree-isolation pilot | `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md` | existing |
| 12 | Baseline-vs-candidate regression contract + matrix | `ChatGPT/[AI OS]/Knowledge/REGRESSION_GATE.md` | existing |
| 13 | Observed-failure → attribution → regression-case lifecycle | `ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md` | existing |
| 14 | Judge bias calibration cases | `ChatGPT/[AI OS]/Knowledge/JUDGE_CALIBRATION.md` + `GOLDEN_EVAL_CASES.md` | existing |
| 15 | Dispatch evidence schema + linter (append-only, worktree-isolated) | `schemas/subagent_dispatch_evidence.schema.json`, `scripts/check_subagent_dispatch_evidence.py` | existing |
| 16 | Capability registry incl. `executor.workspace: isolated_worktree`, `write_capable` | `PROJECT_CAPABILITIES.yaml` | existing |
| 17 | Repo-contract frozen benchmark: Runner/Evaluator/Final-Judge role split, `SCOPE_LOCK.json`, `freeze_manifest.json`, baseline/candidate comparison over a worktree | `benchmarks/supermanager/` | existing |
| 18 | Live-Project frozen benchmark: freeze manifest, sealed holdout, hard-fail/variance/tie-break rules | `benchmarks/live_behavioral/` | existing |
| 19 | Deterministic response-quality/Judge-verdict contract over curated fixtures | `scripts/response_quality_evaluator.py` | existing |
| 20 | Transport-neutral live-Project capture verifier (no direct Project API) | `scripts/live_project_verifier.py` | existing |
| 21 | AES record validators (identity, corrective loop, freshness) | `schemas/autonomous_execution_record*.schema.json`, `scripts/validate_autonomous_execution_record.py` | existing |
| 22 | Deterministic content-hash generate/check fixture pattern | `scripts/pilot_generate_artifact_fixture.py` | existing (narrowly pilot-scoped) |
| 23 | Statistical significance / non-inferiority / stochasticity method | — | **missing** |
| 24 | Append-only, cross-batch experiment ledger (run-results store) | — | **missing** |
| 25 | Blind randomized A/B comparison mechanism (vs. single-sample judge) | — | **missing** |
| 26 | Automated, provider-invoking shadow runner for Project-Instructions wording variants | — | **missing** |
| 27 | Protected-surface / hard-invariant manifest scoped to `PROJECT_INSTRUCTIONS.md` wording | — | **missing** (pattern exists: `SCOPE_LOCK.json`) |

## 2. Reuse / extend / add / protected matrix

Classification legend: **reuse** = adopt the existing contract/mechanism as-is for this purpose; **extend** = existing mechanism covers the shape but needs a bounded addition for AutoResearch's specific case; **add** = no existing equivalent, new artifact required; **protected** = must not be modified by AutoResearch.

| AutoResearch v0.1 need (from #388) | Classification | Basis |
|---|---|---|
| Observed failure → causal attribution → falsifiable hypothesis | **reuse** | `FAILURE_REGISTRY.md`'s `attribution_status: attributable\|uncertain\|ineligible` + `attribution_statement` + "Harness and workflow repair attribution" section already require reproducible localization, paired/counterfactual replay, or deterministic contract violation before a repair candidate is eligible — this is the causal-attribution bar #388 asks for, not a new one. |
| One minimal reversible mutation, one target file | **reuse** | `GOAL_MODE.md` "smallest useful working version" + `PARENT_CHILD_ISSUE_GATE_STANDARD.md` grain discipline + `REGRESSION_GATE.md` candidate contract (`change_type`, `change_summary`, `affected_workflows`, `source_revision`). |
| Frozen evaluator / eval-case / split manifests, verified before each batch | **extend** | `benchmarks/supermanager/freeze_manifest.json` + `verify_freeze()` and `benchmarks/live_behavioral/freeze_manifest.json` + `verify_freeze.py` already hash-freeze spec/rubric/cases/evaluator and fail closed on drift. Neither is scoped to Project-Instructions/routing wording; a new `freeze_manifest` for the AutoResearch search space is `add`, but it should reuse this exact hash-and-verify shape rather than invent one. |
| Protected-surface / hard-invariant manifest | **extend** | `benchmarks/supermanager/SCOPE_LOCK.json` (`initial_allowed_roots`, `specific_file_allowlist`, `forbidden_files`, `expected_blast_radius`) is a direct structural precedent. A new manifest scoped to `PROJECT_INSTRUCTIONS.md` wording + routing/tie-break/ambiguity/handoff/context-selection wording is `add`, following this shape. |
| Read-only deterministic validator + hard-veto logic | **reuse pattern / add instance** | `benchmarks/supermanager/evaluator.py` (immutable deterministic evaluator) + `REGRESSION_GATE.md`'s rule "improvement never compensates for a hard regression" + AES §13.2 effect-boundary invariant already define the hard-veto semantics AutoResearch needs. A new validator instance targeting the AutoResearch search space is `add`, using this contract. |
| Behavioral / candidate comparison, `keep_candidate`/`discard`/`inconclusive` | **reuse pattern / add instance** | `REGRESSION_GATE.md` regression matrix already has exactly this verdict shape (`pass`/`revise`/`blocked`, deltas `improvement`/`unchanged`/`regression`/`inconclusive`) and `benchmarks/supermanager/final_judge.py` already implements a Final-Judge role that compares immutable baseline/candidate results. Map AutoResearch's `keep_candidate`/`discard`/`inconclusive` onto this vocabulary rather than inventing a parallel one. |
| Efficiency comparison | **add** | No existing cost/latency comparator. `AGENT_LOOP_PLAYBOOK.md`'s "Cost / latency budget owner: `[AI OS]`" note and its observed dispatch-cost figures are the only precedent (a budget owner and an example of recording cost, not a comparator). |
| Provider-neutral shadow runner using isolated worktrees | **reuse pattern / add instance** | Isolation mechanics are a direct reuse: `PROJECT_CAPABILITIES.yaml`'s `executor.workspace: isolated_worktree` + `write_capable: false`, `AGENT_LOOP_PLAYBOOK.md`'s worktree-isolation pilot bounds, and `benchmarks/supermanager/run_benchmark.py --repo-root <worktree>` all already run isolated, non-authoritative execution against a worktree. The *invocation* half is `add` and has a real open design question (see §3): `scripts/live_project_verifier.py` documents that ChatGPT Projects have **no direct API** — it is explicitly "transport-neutral," binding to a manually supplied capture rather than calling a Project. "Provider-neutral" for AutoResearch cannot mean automating the ChatGPT Project UI; it means selecting among API-callable models (or `LOCAL_FIRST_COMPUTE_POLICY.md`'s local-Ollama path) under the same eligibility/fallback framework, testing wording variants outside the live Project. |
| Frozen semantic evaluator / blind A/B Judge contract | **reuse pattern / add instance** | `scripts/response_quality_evaluator.py`'s deterministic-plus-observed-Judge-verdict contract (`pass`/`revise`/`blocked`/`not_run`, explicit unsupported-claim findings, no factual inference from prose) and `JUDGE_CALIBRATION.md` + `GOLDEN_EVAL_CASES.md`'s bias cases (`JUDGE-SELF-PREFERENCE`, `JUDGE-LANGUAGE-PARITY`, `JUDGE-AMBIGUITY-CALIBRATION`, `JUDGE-REFERENCE-AVAILABLE`) are the calibration bar. Blind, randomized A/B presentation order is genuinely new (`add`). |
| Deterministic stochasticity / non-inferiority method | **add** | No statistical significance/non-inferiority tooling exists anywhere in the repo (checked `ChatGPT/[Analytics]/Knowledge/ANALYTICAL_TECHNIQUES.md`'s 22 methods and grepped the repo for `t-test`/`confidence interval`/`p-value`/`standard error`/`sample size` — no hits). `benchmarks/live_behavioral/benchmark_spec.json`'s `variance_rule` field is the closest partial precedent (a rerun-variance rule, not a formal non-inferiority test) and should inform the method's shape. **Caution**: `ChatGPT/[Analytics]/Knowledge/VARIANCE_DIAGNOSTIC_CONTRACT.md` matches on the word "variance" but is Plan/Fact **financial** variance (management-direction sign convention for budget bridges) — unrelated to statistical variance/stochasticity. Recorded here explicitly as a rejected false match, per #389's own non-acceptance example ("treating a filename match as proof of equivalent behavior"). |
| Append-only experiment ledger and candidate-comparison artifact | **add** | No run-results ledger exists; `AI_EVAL_REGISTRY.md` is explicitly "a registry of eval standards only... does not store run results" and must stay that way (see §3). AES §9 (defect record) and `subagent_dispatch_evidence.schema.json`'s append-only, machine-checkable evidence convention are the closest structural precedent for shape (immutable, schema-validated, linted in CI) and should be followed rather than a new free-form log. |
| Phase 0 calibration / readiness gate | **reuse pattern** | `benchmark_spec.json`'s `variance_rule`, `minimal_meaningful_improvement`, `tie_break_rule`, `hard_fail_rules` and `REGRESSION_GATE.md`'s smoke scenario (`REGRESSION-001`) are direct structural precedent for a calibration gate that must separate an obvious-good and an obvious-bad variant before real experiments run. |
| Phase 1 bounded pilot recording every attempt incl. negative/inconclusive | **reuse pattern** | `benchmarks/live_behavioral/README.md`'s numbered workflow (freeze → sync → run → capture → evaluate → bounded iterations → open holdout only after selection → frozen final gate → separate non-merging PR) is close to a working template for a bounded pilot; the ledger it writes to is `add` (see above). |
| Holdout inaccessible to Researcher until predeclared checkpoint | **reuse pattern** | `benchmarks/live_behavioral/freeze_manifest.json`'s `sealed_holdout_sha256` + `HOLDOUT_MANIFEST.json` + the README's "open the sealed holdout only after candidate selection" is a direct, already-working precedent for holdout secrecy. |
| Owner/researcher/evaluator/merge/production authority separation | **protected / reuse** | AES §2 (canonical ownership), §13 (external authority separation), `GOAL_MODE.md` Merge Policy ("Codex and agents must not manually merge... Tier 2 protected changes require owner review"), `HANDOFF_STYLE_STANDARD.md` "Merge And Acceptance". These are the existing authority boundaries AutoResearch must sit inside, not extend. |
| `main`, active Project Instructions, AES/eval semantics, protected files | **protected** | Explicit in #388's own "Safety boundaries" and "Forbidden actions"; also independently protected by `GOAL_MODE.md` Merge Policy, `.github/CODEOWNERS` Tier-2 list, and the Merge Gate allowlist (`.github/workflows/auto-merge.yml`). No child issue may weaken these. |

## 3. Duplicate or conflicting semantic owners

1. **`AI_EVAL_REGISTRY.md` vs. an AutoResearch experiment ledger.** The registry is explicitly definitions-only ("does not store run results, runtime logs, eval databases, or benchmark outputs"). AutoResearch's ledger is a run-results store. These must stay two different artifacts with two different owners — the ledger must not be folded into `AI_EVAL_REGISTRY.md`, and the registry must not grow a "recent runs" section for AutoResearch. If AutoResearch needs a registry row at all, it is a *definition* row (`eval_id`, `owner_project`, criteria) pointing at the separate ledger, following the existing `BASELINE-REGRESSION` / `FAILURE-REGRESSION` / `GOAL-CLOSURE` row shape.
2. **`PROMPT_QA_FACTORY.md`'s `candidate → test → judge → revise → selected` loop vs. AutoResearch's `hypothesis → mutation → eval → keep_candidate/discard/inconclusive` loop.** These are the same shape applied to overlapping material: Prompt QA Factory's own table already lists "ChatGPT Project prompts" (owner: the owning project) with test criterion "Project follows source, routing, and output rules" — i.e., it is already the nominal governance owner for changes to Project Instructions wording, which is exactly the mutable search surface `[AI OS]` PROJECT_INSTRUCTIONS.md wording, routing/tie-break wording, ambiguity-handling wording, handoff wording, context-selection wording named in #388. **Recommendation for #390**: frame AutoResearch v0.1 as a rigor-upgraded, bounded specialization that *runs inside* the Prompt QA Factory lifecycle (its `candidate`/`test`/`judge`/`revise`/`selected` statuses and supervision boundary) for this one mutation class, rather than a second parallel prompt-change governance framework. This directly satisfies #388's own instruction to reuse rather than duplicate governance.
3. **UX Score (Prompt QA Factory) vs. AutoResearch's explicit ban on "opaque weighted AIOS Quality Score."** Prompt QA Factory's 1–5 subjective UX Score must **not** be reused as (or folded into) AutoResearch's keep/discard decision — #388 explicitly forbids exactly this shape of aggregate. If Prompt QA Factory fields are reused per finding 2, the UX Score field should be carried only as descriptive metadata, never as a decision input.
4. **`REGRESSION_GATE.md` vs. a new AutoResearch-specific regression gate.** `REGRESSION_GATE.md` already owns baseline-vs-candidate regression semantics repo-wide (`pass`/`revise`/`blocked`, delta vocabulary, "improvement never compensates for a hard regression"). AutoResearch's hard-veto/`discard` logic must cite and reuse this contract, not define a second regression vocabulary.
5. **`live_project_verifier.py` vs. an AutoResearch shadow runner.** Both bind an evaluation to a captured response under a canonical contract, but `live_project_verifier.py` is explicitly "transport-neutral" because no ChatGPT Project API exists, and requires a controlled browser or manual operator to supply the capture. Any shadow runner that claims to "run" a Project-Instructions variant automatically would conflict with this documented constraint unless it is scoped to API-callable models rather than the live Project UI — see §2's "provider-neutral shadow runner" row. This is a design question for #390/#393, not resolved by this audit.
6. **`AES artifact_freshness_status` (§4.10/§11) vs. AutoResearch's frozen-eval hash verification.** Both are "has the input changed since it was verified" mechanisms, but at different grains (AES: hand-written status prose vs. git revision; benchmark freeze manifests: file content SHA-256). No conflict observed — they solve adjacent problems with intentionally different mechanisms (see `docs/evidence/AUTORESEARCH...` n/a; cf. this session's own recent fix in `docs/evidence/` for why a revision-anchor and a content-hash have different failure modes) — but #390 should not merge them into one mechanism.

## 4. Existing tests and validators relevant to the parent

| Test / validator | Path | Status (this audit) |
|---|---|---|
| Full repository test suite | `tests/` (27 files) | **PASS** — `pytest tests/ -q` → 243 passed, observed this audit at `3f3a6b6` |
| Supermanager benchmark contract | `tests/test_supermanager_benchmark.py` | not independently re-run beyond the full-suite pass above; covered by it |
| Live-behavioral benchmark contract | `tests/test_live_behavioral_benchmark.py` | covered by full-suite pass |
| Response-quality evaluator contract | `tests/test_response_quality_evaluator.py` | covered by full-suite pass |
| Judge calibration contract | `tests/test_judge_calibration_contract.py` | covered by full-suite pass |
| Live project verifier contract | `tests/test_live_project_verifier.py` | covered by full-suite pass |
| Subagent dispatch evidence contract | `tests/test_subagent_dispatch_evidence.py` | covered by full-suite pass |
| Project context / status-freshness contract | `tests/test_project_context_contract.py` | covered by full-suite pass |
| AES record schema + validator | `tests/test_autonomous_execution_schema.py`, `tests/test_autonomous_execution_validator.py` | covered by full-suite pass |
| Merge Gate protection | `tests/test_merge_gate_protection.py` | covered by full-suite pass |
| Analytics variance-diagnostic contract (financial, unrelated to §2's statistical-variance gap) | `tests/test_analytics_variance_diagnostic_contract.py` | covered by full-suite pass; flagged in §3 as a non-match for AutoResearch's stochasticity need |
| `check_knowledge_bundles.py` | `scripts/check_knowledge_bundles.py` | **NOT RUN** in this audit (no bundle-declaring file was touched; out of scope for a read-only audit) |
| `audit_bundle_provenance.py --check` | `scripts/audit_bundle_provenance.py` | **NOT RUN** in this audit, same reason |
| `check_manifest_paths.py` | `scripts/check_manifest_paths.py` | **NOT RUN** in this audit, same reason |
| `check_project_context_contract.py --advisory` | `scripts/check_project_context_contract.py` | **NOT RUN** in this audit; not required to establish this baseline |
| Any live-model / live-Project execution | n/a | **NOT RUN** — this audit performs no provider calls and no Project invocation |

## 5. Gaps blocking child #2 onward

None of these block #390 from *starting* (#390 only needs to consume this audit), but #390 must resolve them before downstream children can proceed without rediscovery:

1. **Shadow-runner transport decision** (feeds #393, referenced by #390's "protected surfaces" and by #392/#395's comparator design): no ChatGPT Project API exists (§2, §3 finding 5). #390 must decide whether AutoResearch v0.1's shadow runner targets API-callable models only (and if so, which provider(s) are already approved for this repo — none observed as pre-approved for AutoResearch specifically) or is deferred/scoped out for v0.1, with Project-Instructions-wording experiments run through the existing manual `live_project_verifier.py`-style capture path instead.
2. **Statistical method choice** (feeds #395): no existing non-inferiority/stochasticity method to reuse (§2). #390/#395 must pick a specific deterministic method (e.g., paired bootstrap, exact binomial test, a fixed-threshold rule) rather than leaving it open, consistent with "deterministic checks override semantic Judge."
3. **Ledger schema ownership** (feeds #391/#392): confirmed as new (`add`), but its relationship to `AI_EVAL_REGISTRY.md` (must stay separate, §3 finding 1) and to AES §9's defect-record/append-only conventions (should follow the same shape) needs to be explicit in #390's contract so #391's schema doesn't reinvent either.
4. **Prompt QA Factory relationship** (feeds #390 directly): §3 finding 2 is a scope/ownership decision, not a technical blocker — #390 should explicitly state whether AutoResearch v0.1 is positioned as running inside Prompt QA Factory's lifecycle or as a separate bounded track, so later children don't drift into a second parallel governance framework.
5. No repository-fact gap prevents #390 from proceeding; all four items above are **design decisions for #390 to make explicit**, not missing infrastructure that blocks starting.

## 6. Recommended minimal implementation map

Ranked single path (not an unranked list of ideas):

1. **#390** should write the v0.1 contract as an explicit specialization that cites and reuses, by name: `FAILURE_REGISTRY.md` (attribution), `REGRESSION_GATE.md` (regression/veto vocabulary), `PROMPT_QA_FACTORY.md` (candidate lifecycle — resolve §3 finding 2 explicitly), `benchmarks/supermanager/SCOPE_LOCK.json` shape (protected-surface manifest), `benchmarks/*/freeze_manifest.json` shape (frozen-eval hash-and-verify), and `PROJECT_CAPABILITIES.yaml` isolation fields (worktree isolation) — and resolve the two open design decisions in §5 (#1 shadow-runner transport, #2 statistical method) before #391 defines schemas around them.
2. **#391** schemas should be additive siblings to existing schemas (`schemas/autoresearch_eval_case.schema.json`, `schemas/autoresearch_experiment_record.schema.json`, `schemas/autoresearch_manifest.schema.json` or similar), matching the field-naming and validation style of `schemas/subagent_dispatch_evidence.schema.json`, not a redesign of it.
3. **#392** validator/hard-veto/ledger/comparator should be implemented as a new `benchmarks/autoresearch/` sibling to `benchmarks/supermanager/` and `benchmarks/live_behavioral/`, reusing their Runner/Evaluator/Final-Judge role separation and freeze-verification pattern rather than a new architecture.
4. **#393** shadow runner should reuse `executor.workspace: isolated_worktree` + `write_capable: false` semantics already in `PROJECT_CAPABILITIES.yaml`/`AGENT_LOOP_PLAYBOOK.md`, and must implement whatever transport #390 decided in §5 item 1.
5. **#394** frozen semantic evaluator/blind-A/B-Judge should extend `scripts/response_quality_evaluator.py`'s contract shape and be calibrated against `JUDGE_CALIBRATION.md`/`GOLDEN_EVAL_CASES.md`'s existing bias cases before use, adding blind-order presentation as the one genuinely new mechanism.
6. **#395** stochasticity/non-inferiority method is the one component with no in-repo precedent at all; implement the specific method #390 selected (§5 item 2), owned by `[Analytics]`, explicitly not reusing `VARIANCE_DIAGNOSTIC_CONTRACT.md` (§3 caution).
7. **#396–#398** (calibration, pilot, final QA) can largely follow `benchmarks/live_behavioral/README.md`'s existing numbered workflow shape (freeze → run → evaluate → bounded iterations → sealed-holdout-after-selection → frozen final gate → non-merging PR) adapted to the new `benchmarks/autoresearch/` ledger.

## 7. Explicit NOT RUN markers

- No provider/API call of any kind was made.
- No ChatGPT Project was invoked, synced, or read live.
- No benchmark (`benchmarks/live_behavioral/`, `benchmarks/supermanager/`) was executed — their contracts and manifests were read, not run.
- `check_knowledge_bundles.py`, `audit_bundle_provenance.py --check`, `check_manifest_paths.py`, `check_project_context_contract.py --advisory` were **NOT RUN** (no in-scope file changed; not required to establish this baseline).
- No performance, cost, or token-saving claim is made or implied anywhere in this report.
- No pilot, benchmark result, or behavioral claim beyond "these artifacts exist and read as described" is made.

## 8. Files changed by this audit

- `docs/evidence/AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md` (new — this report).
- `docs/evidence/README.md` (new index bullet, existing repository convention for this directory).

No other file is touched. No Project Instructions, routing, AES, eval semantics, benchmark, schema, script, test, or workflow file is modified.

## 9. Commands run

```bash
git status --short
git rev-parse HEAD
python3 -m pytest tests/ -q
```

## 10. Rollback

Revert this commit, or close the PR without merging. No schema, contract, business-logic, or protected-path change is included; nothing else requires rollback.

---

## Final response format

```text
What exists: 27 relevant existing artifacts inventoried (§1); the closest
  direct precedents are FAILURE_REGISTRY.md (causal attribution),
  REGRESSION_GATE.md (regression/veto vocabulary), PROMPT_QA_FACTORY.md
  (candidate lifecycle for Project-Instructions wording specifically),
  benchmarks/supermanager/ and benchmarks/live_behavioral/ (frozen eval,
  SCOPE_LOCK-style protected-surface manifest, sealed holdout, Runner/
  Evaluator/Final-Judge role split), response_quality_evaluator.py +
  JUDGE_CALIBRATION.md (semantic-evaluator contract and bias calibration),
  and PROJECT_CAPABILITIES.yaml / AGENT_LOOP_PLAYBOOK.md (isolated-worktree
  execution semantics).
Reuse: causal attribution, regression/veto vocabulary, candidate lifecycle
  (pending #390's explicit Prompt QA Factory scope decision), worktree
  isolation semantics, authority/merge boundaries (AES, GOAL_MODE.md).
Extend: frozen-eval/freeze-manifest mechanics, protected-surface manifest
  shape, deterministic validator + Final-Judge pattern, semantic-evaluator
  contract — all have a working shape but need a new instance scoped to the
  AutoResearch search space.
Add: statistical non-inferiority/stochasticity method (no precedent at all),
  append-only experiment ledger (run-results store, deliberately separate
  from AI_EVAL_REGISTRY.md), blind randomized A/B presentation, efficiency
  comparator, and the model-invocation half of the shadow runner (transport
  choice is an open #390 decision, §5).
Protected: main, active Project Instructions, AES/eval semantics, .github/
  CODEOWNERS Tier-2 paths, Merge Gate allowlist, existing benchmark freeze
  manifests and holdouts, AI_EVAL_REGISTRY.md's definitions-only scope.
Checks run: git status --short; git rev-parse HEAD; pytest tests/ -q (243
  passed at 3f3a6b6).
Evidence: this report, docs/evidence/AUTORESEARCH_V01_BASELINE_AUDIT_2026-09-03.md.
Acceptance status: candidate — ready for owner/#390 review; this audit makes
  no acceptance claim of its own.
Blockers for child 2: none block starting #390; two design decisions (shadow-
  runner transport, statistical method choice — §5) should be resolved inside
  #390's contract rather than left implicit, so #391 onward do not rediscover
  or redecide them.
Rollback: revert this commit or close the PR without merging; no protected
  path touched.
```
