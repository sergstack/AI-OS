# Native Subagent Dispatch — Commissioning Memo — 2026-09-02

- Continues `NATIVE_SUBAGENT_DISPATCH_STANDARDIZATION_2026-09-02.md` (PR #356, merged `5a115c9`).
- Owner decision on record: **STANDARDIZE BOUNDED** — architectural direction owner-approved; the mechanism does not become unconditional/default standard until this commissioning punch-list is 4/4 closed and a Judge review passes.
- Scope of this PR: close only the commissioning gaps. No architecture change, no new authority, no AES-schema / ROUTING_RULES change, no framework/runtime/DB, no child→child, no write-capable children.

## Target standard

```text
root -> bounded routed slice -> Plan child + isolation:"worktree" -> evidence/patch -> root -> validation / AES continuation
```

Hard boundaries kept: child does not write the repo; child cannot use the native `Agent` tool; root is the only router and the only writer; no child→child; no shared-worktree dispatch; no parallel state/AES model; authority / merge / deploy / production gates unchanged.

## 1. Deterministic dispatch-evidence schema + linter — CLOSED

- `schemas/subagent_dispatch_evidence.schema.json` — one record per executed dispatch; required: `agent_type` (`Plan`/`Explore` only), `isolation` (`worktree` only), `workspace_observation` {`path` matching `.claude/worktrees/agent-`, `clean_tree`, `head`}, `execution_id` + `owner_capability` linkage, `telemetry` {`duration_ms`, `subagent_tokens`, `tool_uses` — each a number **or the literal `not_captured`**; no other value, so a missing runtime metric must be declared, never omitted or invented}, `outcome` (`completed`/`refused`/`defect`), `defect_ref` (non-null when `outcome: defect`), `scenario_tags`.
- `scripts/check_subagent_dispatch_evidence.py` — schema-validates each `docs/evidence/subagent_dispatch_records*.json`, then cross-checks every record against `PROJECT_CAPABILITIES.yaml`: `owner_capability` is a real capability; `agent_type` equals that capability's `executor.agent_type`; the executor is `workspace: isolated_worktree`, `write_capable: false`, `child_dispatch: forbidden`. For any file matched by the `subagent_dispatch_records*.json` name (or whose `generated_for` names it a commissioning record) it also enforces the acceptance gate: ≥15 records, ≥3 distinct owners, all four required scenario tags present.
- Wired into `.github/workflows/docs-safety.yml` as the last check step (blocking on PR + push to main).
- `tests/test_subagent_dispatch_evidence.py` — 15 tests: schema is valid Draft-7; minimal valid doc passes; missing `agent_type` fails; `general-purpose` rejected by enum; non-worktree isolation rejected; parent-tree path rejected; `telemetry` `null` rejected but `not_captured` and numbers accepted; arbitrary telemetry string rejected; unknown owner fails cross-check; `agent_type` mismatch vs registry fails; `defect` outcome without `defect_ref` fails; commissioning doc enforces min records/owners/scenarios; the acceptance gate applies by filename not only free text; `check_file` returns `(problems, doc)`; **the committed commissioning evidence file passes the full linter**.

## 2. Mandatory per-dispatch telemetry — CLOSED (as an enforced contract; capture is runtime-limited)

The schema makes `telemetry.duration_ms` / `subagent_tokens` / `tool_uses` **required keys**, each constrained to a number or `not_captured`. This forces every record to state, per metric, whether it was captured — a silent omission is a schema failure.

Honest capture status: the Claude Code `Agent` result emits a `usage` footer inconsistently. In this commissioning campaign (18 dispatches) **1/18 emitted a footer** — the Judge re-review J2 (`41801` subagent tokens, `15` tool uses, `84062` ms); the other 17 are recorded `not_captured`. In the prior hardening session two `Plan`+`isolation:"worktree"` dispatches also emitted footers (`41558` / `54468` tokens, `11` / `15` tool uses, `93091` / `148546` ms). So the runtime *can* provide these; the repo cannot force it to. `owner`, `outcome`, `refusal`/`defect`, and workspace facts are always capturable and are captured 18/18.

## 3. Sample: ≥15 hardened dispatches, ≥3 owners, required scenarios — CLOSED

`docs/evidence/subagent_dispatch_records_2026-09-02.json` — **18 records**, every one `agent_type: Plan` + `isolation: "worktree"`.

| Execution | Dispatches | Owners | Scenario |
|---|---|---|---|
| `exec-commissiong-2026-09-02` | G1–G6 (6) | ai_os, llm, thinking, analytics, codex | **long multi-hop** (6 owner transitions) + **repeat-route guard** |
| `exec-commissionh-2026-09-02` | H1–H3 (3) | codex, analytics | **deliberate failure** ×2 + **patch-return write** |
| `exec-commissioni-2026-09-02` | I1–I6 (6) | inbox_router, thinkers_os, ai_os, thinking, codex, analytics | per-capability coverage (routing) |
| `exec-commissionj-2026-09-02` | J1–J2 (2) | thinking | adversarial **Judge review** (round 1 `revise`, round 2 `pass`) |
| `exec-commission-2026-09-02` | C-PROBE-1 (1) | ai_os | runtime re-verification |

- **Distinct owner capabilities exercised: 7 / 7** (all of `PROJECT_CAPABILITIES.yaml`).
- **Deliberate failures (2), both honest, no workaround, recorded in the dispatch-evidence JSON:**
  - `def-commission-h-001` (`external_dependency` / capability-missing) — codex `Plan` child asked to write; it has no `Write`/`Edit` and Bash was read-only; it refused plainly, did not `sed -i` / heredoc / `git apply`, returned the exact diff. **Recovery:** re-formed as patch-return; H2 produced the patch; the root applied and validated it (this PR's `docs-safety.yml` wiring).
  - `def-commission-h-002` (`external_dependency` / missing input) — analytics `Plan` child asked to read a non-existent CSV; it reported "slice blocked / file not found" with `ls`/`find`/`git ls-files` evidence, **did not fabricate** a row count or headers, **did not substitute** another file.
  - Both are recorded in `subagent_dispatch_records_2026-09-02.json` as `outcome: refused` with a `defect_ref` and a described failure. They are **deliberate probes of the failure-handling path** (honest refusal, no silent retry, bounded recovery), not workflow defects that require a regression case under `ChatGPT/[AI OS]/Knowledge/FAILURE_REGISTRY.md`. `FAILURE_REGISTRY.md` and the AES record schema are unchanged.
- **Repeat-route guard (execution G):** the root first attempted a bare repeat route to `[LLM]` with no `evidence_delta` → recorded `repeat_route_refused_missing_evidence_delta`, **not dispatched**. After G3+G4+G5 produced a material `evidence_delta`, the repeat route to `[LLM]` (G6) was allowed and dispatched. Both branches observed.
- **Long multi-hop (execution G):** `root → ai_os → root → llm → root → thinking → root → analytics → root → codex → root → (refused llm) → root → llm → root`. One `execution_id` throughout; root chose every hop via `ROUTING_RULES.md`; children returned only `cross_domain_need`; original acceptance criteria re-checked before each next route; Closure Review produced the single final result.

### Guard-threshold calibration — POPULATION + PROPOSAL (not applied)

Per `AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md`, guard thresholds are calibrated only after real multi-project executions, recording the population and an owner decision. The four `continuation.guards` remain `null` (unset) in `schemas/autonomous_execution_record.schema.json` — **this PR does not change them.**

Observed population (real multi-project executions to date: pilots A/B/C/F + commission G/H):
- continuation hop counts: {3, 3, ~4, 5, 6} — **max observed 6**;
- repeat visits per owner: **max 2**, always with a material `evidence_delta`; 1 bare repeat refused;
- consecutive no-progress hops: **0 observed**;
- route-signature cycles: **1 attempted, 1 refused** (the bare repeat).

Proposal for owner decision (evidence-backed, **not** written to the schema):
`max_continuation_hops: 10` (≈1.6× observed max) · `max_retries_per_owner: 3` (observed 2 + 1 headroom) · `max_no_progress_hops: 2` (observed 0; a 2nd no-progress hop is a strong loop signal) · `route_signature_history_window: 6` (covers one long route).

## 4. Cost / latency owner — ASSIGNED

**Owner: `[AI OS]`** — it already owns `AGENT_LOOP_PLAYBOOK.md`, the supervised-loop governance, and the AES continuation contract; the dispatch cost/latency budget sits with the same owner. Recorded in `AGENT_LOOP_PLAYBOOK.md`.

**When a subagent dispatch is justified over inline root execution** (all-of nothing → inline):
dispatch a slice only when at least one holds — (a) the slice is independent of other in-flight slices (parallelizable), (b) its bounded `project-context` is materially smaller than the root's working context and isolation reduces cross-contamination, or (c) it needs a clean worktree at a specific revision. Otherwise the root executes the slice inline.

**Observed cost** (where captured): ~90–150 s wall-clock and ~40–55 k subagent tokens per dispatch, plus one git worktree (create + auto-cleanup). A 5–6 hop execution ≈ minutes and ≈ 200 k+ subagent tokens on top of the root. This is materially slower and costlier than inline; the justification rule above is the gate.

## Evidence → residual risks

**Closed by this PR:** deterministic evidence linter (blocking CI); enforced telemetry contract; ≥15-dispatch sample across 7 owners with all four required scenarios; cost/latency owner named; guard population recorded with a proposal; exact no-nesting wording; runtime re-verification (C-PROBE-1 confirmed `Plan` has no `Agent`/`Write` and `isolation:"worktree"` yields a clean linked worktree, unchanged).

**Remaining (carried, reviewed):**

| # | Risk | Status |
|---|---|---|
| R1 | **Unverified live spawn arguments.** The orchestrator is a prompt-level skill; no repo check observes that a *live* dispatch actually passed `isolation:"worktree"` / `agent_type: Plan`. Mitigated: registry-owned values, fail-closed SKILL wording, and the evidence linter now *rejects* any recorded dispatch that is not isolated/Plan — so a non-conforming dispatch cannot be entered as valid evidence. Not eliminable for a prompt-level controller. | accepted, reviewed |
| R2 | **Telemetry capture is runtime-dependent** (0/16 this campaign). The contract forces `not_captured` to be explicit; it cannot force the runtime to emit the footer. | accepted; revisit if the runtime adds reliable usage reporting |
| R3 | **`isolation:"worktree"` isolates VCS state only** — untracked / `.gitignore`d / env / cache / absolute-path reads are not isolated. Contract clause: such reads are out-of-contract. | accepted |
| R4 | **Bash-mediated external agent spawn.** A `Plan` child keeps `Bash`; spawning an external agent process via shell is not structurally blocked — **residual risk pending separate evidence**, made impractical (not impossible) by `write_capable: false` + worktree isolation. Not observed in 18 dispatches. | residual, documented |
| R5 | **External-runtime dependency.** "`Plan` cannot use `Agent`" and worktree semantics are Claude Code facts the repo restates but cannot test — re-verify on any runtime upgrade (now a written bound). | accepted with re-verify trigger |
| R6 | **No subagent timeout primitive** — only `TaskStop` + guard limits. | accepted, recorded |

## Cost / latency trade-off (summary)

Dispatch buys bounded context, isolated blast radius, parallelizable independent slices, and an auditable route trace, at ~90–150 s + ~40–55 k tokens + one worktree per hop. It is worth it only under the §4 justification rule; for coupled or context-light slices the root works inline. `[AI OS]` owns this budget.

## Rollback

`git revert` this PR's commit(s). New files (`schemas/subagent_dispatch_evidence.schema.json`, `scripts/check_subagent_dispatch_evidence.py`, `tests/test_subagent_dispatch_evidence.py`, the two evidence files) delete cleanly; the one-line `docs-safety.yml` step and the wording edits revert in place; regenerated bundle + provenance revert with them. No AES-record schema migration, no runtime store, no `.gitignore` change. Prompt-level `Invoke AI-OS`, Goal Mode, AES records, routing, and authority gates are unaffected by a revert.

## AES statuses (reported separately)

```yaml
execution_state: completed
overall_delivery: pass
qa_status: pass          # 6 canonical checks + provenance + dispatch-evidence linter + pytest 229
judge_verdict: pass       # round 1 revise (status-inflation wording), fixed; round 2 pass
authority_status: owner_review_pending
merge_status: not_opened
production_status: not_applicable
```

## Acceptance (owner's criteria for flipping conditional → `STANDARDIZED BOUNDED`)

| Criterion | Status |
|---|---|
| punch-list 4/4 closed | **yes** — §1 linter, §2 telemetry contract, §3 sample + guard population, §4 cost owner |
| ≥15 hardened dispatches with a valid evidence record | **yes** — 18 records, linter PASS, `test_committed_commissioning_evidence_passes_full_linter` green |
| no silent retry / no status inflation | **yes** — the 2 deliberate induced failures are recorded in `subagent_dispatch_records_2026-09-02.json` (`outcome: refused` + `defect_ref`) with honest refusal and bounded recovery, not claimed as `FAILURE_REGISTRY.md` entries; telemetry gaps declared `not_captured` (16/16); guard thresholds unchanged (schema not touched) |
| root-only routing and one `execution_id` preserved | **yes** — execution G (6 hops) and the prior long multi-hop both hold one id, root-only routing |
| no new architectural layers | **yes** — evidence file + linter + one CI step + wording; no router / state machine / DB / framework / schema change |
| rollback remains scoped | **yes** — see Rollback |
| Judge verdict = pass | **see Judge review** |

## Judge review

Two passes.

**Round 1 — `revise`** (`exec-commissionj-2026-09-02` J1, adversarial). Criteria 1, 2, 4, 5, 6 passed with cited evidence (18 records trace clean through schema → cross-check → acceptance gate; one `execution_id` per execution; root-only routing; no schema/router/authority change; scoped rollback). One blocking gap on criterion 3 (status inflation): the memo and status line said the two deliberate-failure defects were "registered" / "in the AES defect lifecycle", but no `FAILURE_REGISTRY.md` entry or AES record existed — the IDs lived only in the JSON `notes` and prose — and `def-`/`DEF-` casing was inconsistent with `defect_ref`.

**Fix applied:** IDs normalised to `def-commission-h-001` / `def-commission-h-002` in the JSON `defect_ref`, JSON `notes`, and the memo. Language corrected: the two induced failures are stated precisely as **recorded in `subagent_dispatch_records_2026-09-02.json` (`outcome: refused` + `defect_ref`)**, deliberate probes of the failure-handling path (honest refusal, no silent retry, bounded recovery), **not** `FAILURE_REGISTRY.md` regression cases. `FAILURE_REGISTRY.md` and the AES record schema remain unchanged. No other criterion was affected.

**Round 2 — `pass`** (`exec-commissionj-2026-09-02` J2, re-review of the corrected diff at `7b1f2c4`, `subagent_tokens: 41801`, `tool_uses: 15`, `duration_ms: 84062`). Observed result: the round-1 gap is **CLOSED** — H1/H3 carry `defect_ref` `def-commission-h-001` / `def-commission-h-002` (lowercase, matching prose); `notes` and memo state the failures are recorded in the dispatch-evidence JSON as `outcome: refused`, deliberate probes of the failure path, explicitly **not** `FAILURE_REGISTRY.md` / AES-lifecycle entries; `git diff --stat origin/main...HEAD` confirms `FAILURE_REGISTRY.md` and `schemas/autonomous_execution_record.schema.json` are **not** in the diff. No regression on criteria 1, 2, 4, 5, 6. Verdict: **`pass`**.

**Result: `judge_verdict: pass`, all six acceptance rows `yes`.** Per the flip rule the status line moves from `STANDARDIZE BOUNDED (conditional)` to **`STANDARDIZED BOUNDED`** — bounded, pilot-scoped, read-plus-patch-return, hub-and-spoke, `[AI OS]`-owned cost budget. It does **not** become a default or unrestricted standard; general/default promotion and the guard-threshold proposal above each remain a separate owner decision.
