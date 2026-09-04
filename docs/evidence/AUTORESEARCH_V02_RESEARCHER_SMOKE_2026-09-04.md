# AIOS AutoResearch v0.2 — Failure Intake, Attribution & Bounded Researcher Proposal — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409).
Child: [#415](https://github.com/sergstack/AI-OS/issues/415) (Real failure intake, attribution,
and bounded Researcher proposal flow).

Status: **implementation + automated checks complete; the live Researcher smoke is `blocked`**
pending the coordinated live session. Per #415's Stop/blocker rule, a manually written patch
reported as Researcher-generated is a named non-acceptance; the child is not accepted as complete
until one actual Researcher invocation returns a structured proposal (against a **calibration-only**
fixture — that patch is never promoted or counted as a Phase 1 real candidate).

No live model/provider/Researcher call was made in producing this document. No raw sensitive
field trace is committed.

---

## Owner authorization envelope

Same envelope as the #413 smoke doc (owner instruction 2026-09-04, Option 1): dedicated
persistent Playwright profile; shared **~40** Phase-0 live-call ceiling; **$0 / plan-included**.
Owner acceptance of sensitive field-trace handling is a separate, still-pending item (§ Blockers).

---

## Final response format (per #415)

```text
Parent:                    #409. Child #415.
Dependencies:              #411 controlling; #412 available; #413 in review (PR #423); FAILURE_REGISTRY.md attribution vocabulary reused unchanged ('supported' == 'attributable').
Failure input modes:       field_observation (sanitized, provenance-checked, never 'reproduced' on intake); live_baseline (must carry real invocation/context/model/evaluator evidence); calibration_fixture (Researcher-contract testing only, never satisfies the real-failure bar).
Failure/reproduction records: schemas/autoresearch_failure_record.schema.json — observation / reproduction / attribution / eligibility are separate machine-checkable states; unknown revision/model/context stay null; 'reproduced' needs >= 2 matched repo-replay runs with real context_hash + model_hash + failure signal.
Attribution decisions:     assess_attribution -> supported | uncertain | rejected. Reproduced-without-causal-evidence stays uncertain; empty/explicitly-ruled-out cause is rejected; supported needs reproduced + trace-grounded evidence + a mutable cause_target + every alternative marked [addressed] + a discriminating test.
Researcher model/prompt hash: docs/standards/autoresearch_v02_researcher_contract.json — contract_hash 3904b515661ad2a553310fd934dfd0c442c2ae95f9ab6a40609902e73098f13c (sha256 over {prompt_text, context_boundary_allow, context_boundary_forbid, output_schema_version, model_class_pin}); drift rejected by ResearcherContract.load(). Model class pinned "researcher".
Live Researcher smoke:     0 calls so far — BLOCKED. Predeclared: exactly 1 Researcher invocation (+ <= 1 bounded retry) against a calibration_fixture failure, inside the shared 40-call / $0 Phase-0 envelope.
Proposal/preflight result: deterministic_preflight reuses the v0.1 shadow runner's fingerprint / worktree / patch-scope machinery unchanged; proves one file + one anchor + one mutation class, clean apply at baseline revision, protected content untouched, patch_hash match, mandatory rollback + regression families; returns ready_for_experiment | rejected. It does NOT decide the candidate is good. Test-proven: a valid in-anchor patch reaches ready_for_experiment; a multi-file / non-applying / hash-mismatched / rollback-missing proposal is rejected; active repo state is unchanged by preflight.
Privacy checks:            fail-closed field-trace sanitisation (reuses #413's secret-shape set); raw_restricted never committed; secret-shaped record content blocks intake; the Researcher context forbidden-token/secret scan targets only the externally-sourced regions (train_diagnostics, baseline_excerpt, failure_record) and not the manifest, which legitimately names protected surfaces.
Checks run:                22 focused #415 tests; full suite 572 passed (550 + 22); check_manifest_paths 189/189; check_repo_public_safety PASS; check_index_coverage 9/9; both new schemas valid draft-07. No live network/model/Researcher call in any test.
Acceptance status:         BLOCKED. Artifact/code acceptance met; business acceptance (one actual live Researcher proposal from bounded evidence) not met until the smoke runs.
Residual limitations:      a browser-UI Researcher exposes no model identity; the smoke's calibration_fixture patch has no evidential weight beyond proving the workflow/schema; sensitive field-trace handling still needs explicit owner acceptance before any real field_observation is ingested.
Rollback:                  remove scripts/autoresearch_failure_intake.py, schemas/autoresearch_failure_record.schema.json, schemas/autoresearch_researcher_proposal.schema.json, docs/standards/autoresearch_v02_researcher_contract.json, tests/test_autoresearch_failure_intake.py, this doc, and the README line. Immutable failure/proposal records (none yet) are preserved. No active AI-OS behaviour changes.
```

---

## What was built

- **`scripts/autoresearch_failure_intake.py`** — `intake_field_observation`, `assess_reproduction`,
  `assess_attribution`, `eligibility_for`, `build_researcher_context` (+ `researcher_context_findings`
  boundary guard), `ResearcherContract` (frozen, drift-checked), `FakeResearcherModel` (no I/O,
  `provenance = "calibration_fixture"`), `BrowserResearcherModel` (routes the one call through
  `lba.invoke`, shares the batch `BudgetState`), `parse_researcher_proposal`,
  `deterministic_preflight` (reuses `autoresearch_shadow_runner` unchanged), `run_researcher`
  (one call + one retry; fails closed on `rejected`/`ineligible` and on repeated invalid output).
- **`schemas/autoresearch_failure_record.schema.json`** and
  **`schemas/autoresearch_researcher_proposal.schema.json`** — additive; no v0.1 schema modified.
  Conditionals enforce the state separation (field observation + null context ⇒ not `reproduced`;
  `reproduced` ⇒ real hashes; `rejected` attribution ⇒ `ineligible`; `uncertain` proposal ⇒
  `discriminating_experiment_only: true`). `additionalProperties:false` + `not/anyOf` keep
  authority / merge / production / `keep_candidate` / score fields structurally impossible.
- **`docs/standards/autoresearch_v02_researcher_contract.json`** — `[LLM]`-owned frozen prompt +
  context boundary, self-consistent `contract_hash`.
- **`tests/test_autoresearch_failure_intake.py`** — 22 tests.

---

## Blockers

1. Owner sign-in to the dedicated Playwright MCP profile + a live `mcp_call` binding (shared
   with #413 / #414 / #417).
2. A frozen Researcher-role context pack from `scripts/autoresearch_context_pack_compiler.py`.
3. A predeclared harmless `calibration_fixture` failure record for the smoke.
4. Explicit owner acceptance of sensitive field-trace handling before any real `field_observation`
   is ingested (not required for the calibration smoke, required for Phase 1).

Until items 1–3 are done and one real Researcher invocation ID + response hash exist, #415 stays
`blocked`.

---

## Rollback

Remove the six child-owned files above plus the one `docs/evidence/README.md` index line. No v0.1
artifact, `FAILURE_REGISTRY.md`, Project configuration, or active AI-OS behaviour is touched.

---

## Checks run

```bash
python3 -m pytest tests/test_autoresearch_failure_intake.py -q                    # 22 passed
python3 -m pytest tests/ -q                                                       # 572 passed
python3 -m json.tool schemas/autoresearch_failure_record.schema.json              # parses
python3 -m json.tool schemas/autoresearch_researcher_proposal.schema.json         # parses
python3 scripts/check_manifest_paths.py                                           # 189/189
python3 scripts/check_repo_public_safety.py                                       # PASS
python3 scripts/check_index_coverage.py                                           # 9/9
```

This document was scanned for secrets, raw credentials, personal data, raw field traces, and
unsupported live-run claims before commit: none found. No live Researcher call has occurred.
