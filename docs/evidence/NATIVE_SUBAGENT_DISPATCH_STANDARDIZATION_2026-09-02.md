# Native Subagent Dispatch — Standardization Decision Memo — 2026-09-02

- Continues `docs/evidence/NATIVE_SUBAGENT_DISPATCH_PILOT_2026-09-02.md` (PR #355).
- Branch: `codex/native-subagent-dispatch-mvp`, hardening on commit `fe24c04`.
- Scope of this stage: no new functionality — close the two standardization blockers, run 3 more observed executions, add measurement evidence, decide.
- Evidence status: observed; no owner acceptance, no merge, no production authorization.
- Not changed: AES state machine, `ROUTING_RULES.md` ownership, `PROJECT_CAPABILITIES.yaml` as sole registry, root-only routing, authority/merge/deploy/production gates, child→child ban, framework ban. No Temporal/LangGraph/CrewAI/AutoGen/Mastra, no runtime DB/service, no `.gitignore` change.

## 1. Native enforcement audit (done before any change)

| Question | Method | Finding |
|---|---|---|
| Does `Agent isolation: "worktree"` give a deterministic isolated workspace? | Spawned a probe child with `isolation: "worktree"`; it reported `pwd`, `git` state. | **Yes.** Child landed in `.claude/worktrees/agent-<id>` on its own branch, **clean tree**, HEAD `5ea37b6` — the session base, *not* the stale parent working-tree branch (`08b0989` on `codex/chatgpt-project-live-optimization-source`). Full repo checkout. |
| Can a `general-purpose` child spawn a nested sub-agent? | Spawned a `general-purpose` child; told it to enumerate tools and attempt one nested `Agent` call. | **Yes — it did it** (nested `Explore` child returned "PONG"). `general-purpose` / `claude` carry the `Agent` tool; only prompt text stops nesting. **Insufficient for standardization.** |
| Is there an agent type that can write but not nest? | System-reminder agent-type definitions. | **No.** `Plan` / `Explore` are `All tools except Agent, …, Write, Edit` (no nest, no write). No built-in has Write without Agent. A tracked custom type is impossible (`.claude/agents` is gitignored and out of scope). |
| Per-call tool restriction? | `Agent` tool schema. | **No** `allowed_tools` / `disallowed_tools` parameter. |

**Conclusion of the audit:** blocker 1 is closable with a real native mechanism. Blocker 2 is closable only by **removing the write-capable child** — no `general-purpose` executor, implementation slices return a patch, the root applies it.

## 2. Changes made (minimal)

| File | Change |
|---|---|
| `PROJECT_CAPABILITIES.yaml` | every `executor`: `agent_type: Plan` (was `general-purpose` for `codex`), `write_capable: false` (all), new `workspace: isolated_worktree` (all), `child_dispatch: forbidden` retained |
| `.agents/skills/ai-os-orchestrator/SKILL.md` | "Native subagent dispatch (pilot)": two **structural invariants** (no `Agent` tool → no nesting; no `Write`/`Edit` → no child writes, patch-return + root applies); mandatory `isolation: "worktree"`; **fail-closed** spawn wording (a dispatch that would omit isolation/agent_type is an AES `contract` defect, not a silent default; a dispatch with no recorded workspace observation is not counted as executed) |
| `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md` | "Supervised AI-OS Subagent Dispatch (Pilot)" bounds: hub-and-spoke "structurally enforced"; mandatory worktree isolation; root is the only writer. Regenerated `AIOS_05` bundle + provenance audit. |
| `tests/test_project_capabilities_executor.py` | `workspace: isolated_worktree` required for every capability (DEF-001 regression); `agent_type ∈ {Plan, Explore}` (non-nesting); no executor `write_capable: true`; fail-closed backend test retained |
| `docs/evidence/README.md`, `MASTER_STATUS.md`, `CURRENT_STATUS.md` | pointers + status line |

Checks: 6 canonical scripts + `audit_bundle_provenance.py --check` + `pytest tests/ -q` (**216 passed**).

## 3. Three additional observed executions

Continuation records `exec-pilotD/E/F-2026-09-02`, one `execution_id` each, every dispatch with `isolation: "worktree"`.

### Pilot D — runtime-failure case

- Goal (deliberately impossible for the executor): "modify and save `docs/evidence/README.md`".
- D1 (`Plan`, isolated worktree `agent-a49eee332e91ffee0`, clean, HEAD `5ea37b6`): the child **structurally could not write** ("I have no Edit, Write, apply_patch … this is a tooling limitation, not a transient error") and **did not work around it** (no `sed -i`, no heredoc). It returned the exact unified diff instead.
- Root: registered **DEF-P D-001** (`classification: external_dependency` / capability-missing, `severity: needs_check`). **Bounded recovery, no silent retry:** root applied the child's returned patch, ran `check_repo_public_safety` (PASS), then reverted the marker (it was a test artifact). Failure entered the AES defect lifecycle and was resolved by the patch-return path.
- Result: failure not lost; recovery is the designed mechanism.

### Pilot E — write-path case (patch-return)

- Goal: add the pointer for this memo to `docs/evidence/README.md` and `MASTER_STATUS.md`.
- E1 (`Plan`, isolated worktree `agent-a9e4feca1d6998835`): ran `git fetch` + `checkout` inside its worktree to reach the branch tip, **flagged honestly** that the requested base SHA was not yet pushed, produced a clean 2-file unified diff matching existing style, and listed the validation commands. `subagent_tokens: 41558`, `tool_uses: 11`, `duration_ms: 93091`.
- Root applied the patch to the branch and validated (checks below). Return-to-root + validation + one `execution_id`.

### Pilot F — long multi-hop (5 owner transitions)

- Goal: "is the hardened pilot ready to STANDARDIZE BOUNDED? one yes/no + the single biggest residual risk + one-line justification."
- Route: **root → ai_os → root → thinking → root → analytics → root → codex → root → ai_os → root**. 5 dispatches, one `execution_id` `exec-pilotF-2026-09-02`, each hop returned to root, original acceptance re-checked each hop; the repeat visit to `ai_os` (hop 5) was allowed only because hops 2–4 supplied a material `evidence_delta` (`new_evidence` / `implementation_feedback`).
  | hop | owner | isolated worktree | tokens | duration_ms | finding |
  |---|---|---|---|---|---|
  | F1 | ai_os | `agent-a56b34878a401c00f` | 54468 | 148546 | mechanisms sound in design; residual doubt: nothing statically asserts the root passes the args at spawn time; worktree isolates only VCS state |
  | F2 | thinking | `agent-a77cc4bea6a6c377b` | not shown | not captured | reliability **sufficient-with-conditions** for bounded scope; biggest risk = unverified root spawn arguments; 5 conditions |
  | F3 | analytics | `agent-ac65f6849891d57c5` | not shown | not captured | measurement base **pilot-only / insufficient**: n=5 hardened, telemetry 2/5, clean-tree 2/5 |
  | F4 | codex | `agent-a7f0db0ededb7a595` | not shown | not captured | no repo check can observe a *live* dispatch's args (prompt-level skill); can bind registry-owned args + fail-closed wording + an evidence-doc linter; a `dispatch` sub-object in the AES `route_trace` is **out of scope** (schema frozen) |
  | F5 | ai_os | `agent-<id>` | not shown | not captured | **STANDARDIZE BOUNDED WITH CONDITIONS** — "ready now: NO"; conditional yes on a 4-item punch-list; criterion (4) one-execution_id confirmed |
- Guard behavior: the hop-5 repeat route to `ai_os` was gated on an `evidence_delta` (present → allowed); a bare repeat would have been `repeat_route_refused_missing_evidence_delta`.
- Observation (honest): worktree branch-checkout behaviour was **inconsistent** across children — E1/F1 completed `git fetch` + `checkout FETCH_HEAD`; F4 reported the isolation guard *refused* `git checkout FETCH_HEAD`. The isolation boundary has teeth but its exact rules were not fully characterised.

## 4. Measurement evidence

Grain: one row per dispatch where individual, aggregate where only a range exists. Method: direct count / min-median-max on captured values only. **Every non-captured quantity is marked `not captured` — nothing invented.**

| Metric | Value | Notes |
|---|---|---|
| Total dispatches (this MVP) | **16** | A/B/C = 9 (un-hardened, no isolation); D1, E1, F1–F5 = 7 (hardened, `isolation: "worktree"`) |
| Successful multi-agent executions | **6** | A, B, C, E, F reached their goal end-to-end; D reached a bounded terminal state via recovery |
| Hardened dispatches landing in an isolated worktree | **7 / 7 = 100%** | every hardened child reported `.claude/worktrees/agent-<id>` |
| Clean-tree-on-entry confirmed (hardened) | **4 / 7** | Probe, D1, E1, F1 explicit; F2–F5 not re-stated |
| Structural write refusal observed | **1 / 1** | D1 — child had no Write tool, refused, no workaround |
| Nested-spawn by a non-nesting executor | **0** | `Plan` children cannot; not attempted |
| Defects registered | **3** | DEF-001, DEF-002 (pilot memo) + DEF-P D-001 (this memo) — all handled, none hidden |
| Silent retries | **0** | |
| Latency, hardened, captured | E1 93.1 s, F1 148.5 s (n=2); median n/a | D1, F2–F5, Probe `not captured` |
| Latency, un-hardened A/B/C | 39–64 s range (n=9); individual values `not captured` | |
| `subagent_tokens`, captured | A/B ~48k–69k; E1 41 558; F1 54 468 | most rows `not captured` |
| `tool_uses`, captured | E1 11; F1 15; some A/B/C | rest `not captured` |
| Cost/latency owner | **none assigned** | |

**Measurement sufficiency:** the *isolation* claim is well-supported (7/7). The *reliability / cost* base is thin — telemetry was captured opportunistically from `Agent` result footers, not by a mandatory schema.

## 5. Risks closed / remaining

**Closed (structurally, native mechanism, not prompt text):**

1. **DEF-001 — stale parent state.** Every dispatch uses `isolation: "worktree"`; registry-enforced (`workspace: isolated_worktree`) + contract test + SKILL fail-closed wording. Behavioural proof: 7/7 hardened children in isolated clean worktrees at a deterministic revision.
2. **Nested delegation on the write path.** No write-capable child exists. All executors are `Plan` (tool set excludes `Agent`) → a child **cannot** spawn a sub-agent. Implementation slices return a patch; the root (sole router, sole writer) applies it. The one nest-capable executor (`general-purpose`) is removed.

**Remaining:**

| # | Risk | Severity | Can it be fully closed? |
|---|---|---|---|
| R1 | **Unverified live spawn arguments.** The orchestrator is a prompt-level skill; no repo check can observe that the *live* root actually passed `isolation`/`agent_type`. Fail-closed SKILL wording + registry-owned values + recorded workspace observation reduce it; it stays partly behavioural. | medium | No — inherent to a prompt-level controller. Mitigation = evidence-doc linter (punch-list #2) + owner/Judge review. |
| R2 | **Thin measurement base.** n=7 hardened, full telemetry on 2, no mandatory schema, no min sample. | medium | Yes — punch-list #2/#3. |
| R3 | **Worktree isolates only VCS state.** Untracked / `.gitignore`d / env / cache / absolute-path reads are not isolated. | low–medium | Partly — contract clause "such reads are out-of-contract" + review. |
| R4 | **`Plan` keeps `Bash`.** Indirect nesting via a shell-spawned agent CLI is not structurally blocked (but `write_capable: false` + isolation make it impractical and pointless). | low | Partly — documented; not observed. |
| R5 | **External-runtime dependency.** "`Plan` excludes `Agent`" and "`isolation: worktree` is clean/locked" are Claude Code properties the repo restates but cannot test. | low | No — re-check trigger on any runtime upgrade. |
| R6 | **No timeout primitive.** Only `TaskStop` (manual cancel) + guard limits. | low | No — runtime limitation, recorded. |
| R7 | **No cost/latency owner.** | low | Yes — punch-list #4. |

## 6. Reliability assessment

- **Isolation mechanism:** reliable within its defined scope (VCS state), 7/7 behavioural, registry+test+skill enforced. R3/R5 bound the scope.
- **No-nesting / no-write:** reliable — enforced by the runtime tool set, not instruction; the removed `general-purpose` executor was the only hole.
- **Failure handling:** reliable — D1 shows an honest structural failure entering the AES defect lifecycle with a bounded, non-silent recovery.
- **Routing integrity:** reliable — Pilot F kept one `execution_id` across 5 hops, root-only routing, guard-gated repeat, Closure Review against the original goal.
- **Overall:** adequate for a **bounded** scope (read/analysis slices + patch-return writes, named dispatch types, hub-and-spoke). **Not** adequate for general use: R1 is irreducible for a prompt-level controller and the measurement base is thin.

## 7. Operational cost / latency trade-off

- Per hardened dispatch: ~90–150 s wall-clock (n=2), ~40–55 k subagent tokens (n=2), plus a fresh git worktree (disk + create/cleanup). Each spawn starts cold and re-derives context.
- A 5-hop execution (Pilot F) ≈ several minutes and ≈ 200 k+ subagent tokens on top of the root.
- Benefit: bounded context per slice, isolated blast radius, parallelizable read slices, auditable route trace.
- Trade: materially slower and more expensive than the root doing the work inline; only worth it when slices are genuinely independent and context-isolation matters. **No owner is accountable for this budget** (punch-list #4).

## 8. Assessment against the strict `STANDARDIZE BOUNDED` criteria

| # | Criterion | Status |
|---|---|---|
| 1 | deterministic isolated child workspace proven | **met** — `isolation: "worktree"` mandatory + registry + test; 7/7 behavioural; caveat R3 (VCS-only) |
| 2 | write-capable child structurally cannot nested-delegate | **met** — by removing the write-capable child; all executors `Plan` (no `Agent`, no `Write`); patch-return + root applies |
| 3 | runtime failure not lost, enters AES defect lifecycle | **met** — DEF-P D-001 (Pilot D) + DEF-001/002; bounded recovery, no silent retry |
| 4 | ≥6 total successful observed multi-agent executions | **met (borderline)** — 6 executions reached a bounded terminal state (A,B,C,E,F clean; D via recovery); 16 dispatches total |
| 5 | long multi-hop keeps one `execution_id`, requirements, evidence, authority provenance | **met** — Pilot F, 5 hops, `exec-pilotF-2026-09-02` throughout |
| 6 | root remains the only router | **met** — every hop; children structurally cannot route |
| 7 | Closure Review checks the original user goal | **met** — each pilot's final hop |
| 8 | no silent retry / no status inflation | **met** — F3 stated "insufficient", F5 stated "NO / conditional"; all defects registered |
| 9 | rollback remains bounded | **met** — `git revert` 3 commits; executor block inert; no schema / `.gitignore` change; no runtime store |
| 10 | standardization does not expand authority | **met** — no child authority; gates untouched; carve-out pilot-scoped |

Nine of ten clean; #4 borderline. **But** the pilot's own multi-owner analysis (F2/F3/F5) says the *readiness* conditions — a fail-closed spawn check with a red-on-omit test, a mandatory telemetry schema + real sample, a cost owner — are not yet satisfied.

## 9. Punch-list for an unconditional `STANDARDIZE BOUNDED`

1. **Fail-closed spawn check.** SKILL wording is added this PR. Add a deterministic evidence check: a `schemas/subagent_dispatch_evidence.schema.json` + `scripts/check_subagent_dispatch_evidence.py` that every row of a committed `docs/evidence/*DISPATCH*` file carries `agent_type`, `isolation: "worktree"`, and a workspace observation, cross-matched to the registry; wire into `docs-safety.yml`; test it. (Does **not** touch the AES record schema.)
2. **Mandatory per-dispatch telemetry** in the evidence-doc schema: worktree id, base HEAD, post-run tree status, `subagent_tokens`, `tool_uses`, `duration_ms`, outcome enum, retry linkage.
3. **Real sample:** ≥15 hardened dispatches across ≥3 owners incl. ≥1 deliberate failure, all with the telemetry above, before promotion — then calibrate the four `continuation.guards` thresholds.
4. **Named owner** for the dispatch cost/latency budget.

## 10. Rollback

`git revert` the 3 branch commits (`54d4d97`, `20390ed`, `fe24c04` … + this memo's commit). The `executor` block is inert data once the SKILL subsection reverts. No AES-record schema migration, no runtime store, no `.gitignore` change. Prompt-level `Invoke AI-OS`, Goal Mode, AES records, and existing routing are unaffected by a revert.

## 11. AES statuses (reported separately)

```yaml
execution_state: completed
overall_delivery: pass          # blockers closed + 3 executions observed + memo delivered
qa_status: pass                 # 6 canonical checks + provenance audit + pytest 216
judge_verdict: not_run
authority_status: owner_review_pending
merge_status: not_opened
production_status: not_applicable
```

## 12. Recommendation

# STANDARDIZE BOUNDED — conditional

The two blockers the owner named — **deterministic isolated child workspace** and **structural no-nesting on the write path** — are **genuinely closed by native runtime mechanisms**, not prompt instructions:

- isolation is a real `Agent` primitive, registry-mandated, contract-tested, 7/7 observed;
- no-nesting is enforced by the `Plan` tool set (no `Agent`), achieved by removing the write-capable child entirely.

Neither blocker was routed around with prompt text, so the outcome is **not `BLOCK` and not `KEEP PILOT-ONLY`** on blocker grounds. Nine of ten strict criteria are met.

It is **conditional** because the pilot's own `[Thinking]`/`[Analytics]`/`[AI OS]` analysis shows the readiness conditions are not yet in place: a red-on-omit spawn check, a mandatory telemetry schema with a real sample (≥15 dispatches), and a named cost owner (§9, items 1–4). The single biggest residual risk — **unverified live spawn arguments (R1)** — is irreducible for a prompt-level controller and must be carried as an accepted, reviewed risk.

**If a binary is required:** `KEEP PILOT-ONLY` until §9 items 1–4 land (one small PR), then `STANDARDIZE BOUNDED`. Standardization must be a separate owner decision and must not expand authority beyond the bounded, read-plus-patch-return, hub-and-spoke scope proven here.
