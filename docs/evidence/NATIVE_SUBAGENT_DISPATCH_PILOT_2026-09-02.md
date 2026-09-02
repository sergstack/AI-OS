# Native Subagent Dispatch MVP — Pilot Evidence — 2026-09-02

- Follow-up to issue #350 (`BLOCKED_FOR_NATIVE_DISPATCH` on the ChatGPT/Codex surface).
- Surface under test: **Claude Code** (`Agent` tool + built-in agent types).
- Baseline: `origin/main` @ `5ea37b6`. Branch: `codex/native-subagent-dispatch-mvp`.
- Governance: bounded owner-approved carve-out "Supervised AI-OS subagent dispatch (pilot)", 2026-09-02 (`owner_instruction`). Pilot-only; not a standard workflow; does not generalize.
- Evidence status: observed dispatches recorded below; no owner acceptance, no merge, no production authorization.

## Summary

The `Invoke AI-OS` orchestrator was bound to the native Claude Code subagent
primitive and driven through three multi-owner executions. Each pilot ran as
one AES `execution_id` with the root as the only router; every hop returned to
the root; loop guards were exercised (Pilot C refused a bare repeat route and
allowed it only after a material `evidence_delta`). No new router, state
machine, schema field, or database was added. Two runtime defects were
registered, not hidden.

## FACT — native runtime capability (observed this task)

| Primitive | Result | How observed |
|---|---|---|
| Child creation | works | 10 `Agent` dispatches across a probe + 3 pilots |
| Separate context | confirmed | children reported "I can see only this prompt … no earlier conversation" |
| Bounded task transfer | confirmed | each child received only the crafted prompt |
| Result return to parent | confirmed | every child report returned to the root, not the user |
| Typed identity + tool limits | confirmed | `Plan` children had no Edit/Write/Agent; `general-purpose` child was instructed read-only and made no writes |
| Nested delegation control | confirmed | `Plan` cannot spawn children (no Agent tool) → hub-and-spoke structurally enforced for read slices |
| Sequential execution | confirmed | `run_in_background:false` blocked to completion each time |
| Warm continuation of a child | available (not exercised) | the `general-purpose` child returned an `agentId` for `SendMessage` |
| Parallel execution | not exercised | pilots were deliberately sequential |
| Timeout | **not available** | no `Agent` timeout param; recorded as a runtime limitation |
| Filesystem isolation | **shared by default** | children ran in the parent cwd on the parent's checked-out branch (see DEF-001) |

## Governance classification

`A. policy-compatible supervised AES execution` **for this bounded pilot only**,
under the carve-out in `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md`
("Supervised AI-OS Subagent Dispatch (Pilot)"). Standing prohibition on
"agentic workflows / autonomous agents" is unchanged for everything else;
`AGENTS.md` and `CURRENT_STATUS.md` annotate the single exception.

## Architecture selected and why

Option 1 (minimal): root holds the only `Agent` tool; per resolved capability
it spawns one built-in agent type (`Plan` for read-only reasoning slices,
`general-purpose` only for a write-capable implementation slice) with a bounded
prompt that names the capability, `canonical_path`, `context_entrypoints`, the
slice objective and acceptance, and forbids next-owner selection and
sub-subagent spawning. Capability→executor binding is a **semantic** `executor`
block in `PROJECT_CAPABILITIES.yaml`; no `.claude/agents/*` files, `.gitignore`
unchanged, no AES-record schema change. Rejected: declared `.claude/agents`
specialists (touches repo hygiene) and SDK `agents` config (not repo
source-of-truth).

## Files changed

| File | Change |
|---|---|
| `ChatGPT/[AI OS]/Knowledge/AGENT_LOOP_PLAYBOOK.md` | + allowed loop type + "Supervised AI-OS Subagent Dispatch (Pilot)" section (all mandatory bounds) |
| `ChatGPT/[AI OS]/Knowledge_Bundles/AIOS_05_SUPERVISED_AGENT_LOOPS.md` | regenerated (deterministic) |
| `docs/knowledge_bundle_provenance_audit.{json,md}` | regenerated (byte counts + fingerprint) |
| `AGENTS.md` | "agentic workflows" blocked item annotated with the single bounded exception |
| `CURRENT_STATUS.md` | `native_subagent_dispatch_status` line + `blocked_items` annotation |
| `PROJECT_CAPABILITIES.yaml` | additive `executor` block per capability (`backend`, `agent_type`, `context_loader`, `write_capable`, `child_dispatch: forbidden`) |
| `.agents/skills/ai-os-orchestrator/SKILL.md` | "Native subagent dispatch (pilot)" subsection incl. the mechanical-root constraint from DEF-002 |
| `.agents/skills/project-context/SKILL.md` | one line binding it as the child context loader |
| `tests/test_project_capabilities_executor.py` | new — 8 deterministic invariants |
| `tests/test_aios_dual_surface.py` | key-set assertion updated for `executor` |
| `docs/evidence/NATIVE_SUBAGENT_DISPATCH_PILOT_2026-09-02.md` | this file |
| `docs/evidence/README.md`, `MASTER_STATUS.md` | pointers |

Not touched: `schemas/autonomous_execution_record.schema.json`, `ROUTING_RULES.md`, `GOAL_MODE.md`, `HANDOFF_STYLE_STANDARD.md`, AES standard, `.github/`, any merge/production gate, `.gitignore`.

## Commands / checks run

`check_project_instructions_length` · `check_repo_public_safety` ·
`check_codex_goal_mode_defaults` · `check_manifest_paths` ·
`check_knowledge_bundles` · `check_index_coverage` — PASS.
`audit_bundle_provenance.py --check` — PASS.
`python3 -m pytest tests/ -q` — 215 passed (207 baseline + 8 new).

## Pilot traces

All three: one user prompt, no manual project selection, canonical routing
(`ROUTING_RULES.md`) chose every owner, each child got bounded `project-context`
only, one `execution_id`, root-only re-routing, Closure Review against the
original goal, one final result.

### Pilot A — `Thinking → root → Analytics → root → Thinking`

- `execution_id`: `exec-pilotA-2026-09-02`
- Goal: "Should AI-OS adopt a nightly automated knowledge-bundle drift check as a blocking CI gate? One recommendation + decision status + revisit triggers."
- Route trace:
  | # | from → to | agent_type | outcome | evidence_delta | criteria addressed |
  |---|---|---|---|---|---|
  | A1 | root → thinking | Plan | completed | — | frame options + quantitative need |
  | A2 | root → analytics | Plan | completed | — | quantify drift-halt frequency from repo evidence |
  | A3 | root → thinking | Plan | completed | `new_evidence` (A2 result) | final recommendation |
- Context boundary: each child declared `included/excluded/context_sufficiency`; A1/A3 excluded all non-`[Thinking]` projects; A2 excluded non-`[Analytics]` methodology.
- Evidence produced: A1 → 4 reversible options + one quantitative question; A2 → "a blocking per-PR bundle gate already exists (`docs-safety.yml` + `source_fingerprint` since 2026-07-09); ~0 merged-history drift halts / 90d; true-positive fraction and lead time `unknown`"; A3 → recommendation = **advisory nightly check, not blocking**; `decision_status: recommended` (advisory) / `blocked` (blocking gate, pending data); 5 revisit triggers.
- Closure Review vs original goal: **satisfied** — one recommendation, decision status, ≥2 revisit triggers.

### Pilot B — `AI OS → root → LLM → root → implementation ([Codex])`

- `execution_id`: `exec-pilotB-2026-09-02`
- Goal: "Design a minimal prompt-level check that a dispatched subagent loaded only bounded project-context; say where it lives in the repo."
- Route trace:
  | # | from → to | agent_type | outcome | criteria addressed |
  |---|---|---|---|---|
  | B1 | root → ai_os | Plan | completed | checkable "bounded context" signals |
  | B2 | root → llm | Plan | completed | turn checklist into a CHECK spec (prompt, schema, aggregation, per-item method, fixtures) |
  | B3 | root → codex | general-purpose (read-only) | completed | verify repo placement + gating checks, no writes |
- Context boundary: B1 excluded sibling projects; B2 excluded `[AI OS]` Judge doctrine + repo-root `CONTEXT_PACK_STANDARD.md` with reasons; B3 loaded only `[Codex]` + the specific files it verified.
- Evidence produced: B1 → 10 pass/fail signals grounded in `project-context/SKILL.md`; B2 → `bounded_context_check` spec (10 items classified deterministic vs llm-judge, 2 calibration fixtures); B3 → verified minimal change set with `path:line` citations, caught that `check_index_coverage.py` also needs `LLM_PROJECT_STATUS.md` and that `UPLOAD_LIST.md` is bundles-only. **No file was modified.**
- Closure Review: **satisfied** — check designed + exact repo home identified.

### Pilot C — multi-hop, ≥3 owner transitions + loop-guard demonstration

- `execution_id`: `exec-pilotC-2026-09-02`
- Goal: "One-paragraph governance note: is the native-subagent-dispatch pilot consistent with AES §2.1 resolved-owner boundary + the continuation control-plane contract?"
- Route trace:
  | # | from → to | agent_type | outcome | evidence_delta | note |
  |---|---|---|---|---|---|
  | C1 | root → ai_os | Plan | completed | — | structural consistency (5 points) + decision-level cross_domain_need |
  | C2 | root → thinking | Plan | completed | — | verdict (b): consistent only if a mechanical-root constraint is added; exact wording supplied |
  | C-r | root → ai_os | — | **refused** | **none** | `repeat_route_refused_missing_evidence_delta` — bare repeat route, not dispatched |
  | C3 | root → ai_os | Plan | completed | `new_evidence` (C2 verdict) | final one-paragraph note |
- **Loop-guard result (mandatory check):**
  - repeat route to `ai_os` **without** `evidence_delta` → `refused`, recorded, not dispatched. ✔
  - repeat route to `ai_os` **with** material `evidence_delta` (`new_evidence` = C2 verdict) → **allowed**, dispatched as C3. ✔
- Owner transitions: root→ai_os→root→thinking→root→(refused)→root→ai_os→root = 3 completed transitions + 1 refused.
- Corrective loop: C2's verdict (b) is `implementation_feedback` → registered as **DEF-002** and the mechanical-root constraint was added to `ai-os-orchestrator/SKILL.md` (one fix).
- Closure Review vs original goal: **satisfied** — 168-word paragraph, conditional-consistency conclusion, cites AES §2.1 + continuation contract + hub-and-spoke / one-`execution_id` / route-trace-guard reuse, names the risk, states where the constraint belongs.

## Defects / failures registered

| id | classification | severity | description | status |
|---|---|---|---|---|
| DEF-001 | `external_dependency` | `needs_check` | Dispatched children inherit the parent cwd, which was on a stale local branch (`codex/chatgpt-project-live-optimization-source`), so several children reported repo-state facts that are wrong on `origin/main` (e.g. "build/audit bundle scripts absent", "root manifest absent", "PR #298 not found"). Their domain reasoning against files that *do* exist in the tree was sound; decision outputs were not affected because later slices re-verified key facts. | mitigated (pilot); open as a design risk |
| DEF-002 | `contract` | `needs_check` | The orchestrator "Native subagent dispatch (pilot)" subsection did not state that the root's after-child step is mechanical, leaving room for a discretionary root that would breach the AES §2.1 resolved-owner boundary. | resolved — constraint text added, one fix |

No failure was hidden by retry. No child selected a next owner. No child spawned a sub-subagent. No unauthorized write occurred.

## Route trace result

Reconstructable end-to-end from the tables above: every dispatch, its owner,
outcome, `evidence_delta`, and the one refused repeat route. All three
executions kept a single `execution_id`; no new `execution_id` was created at
any hop.

## Residual risks

1. **Shared filesystem + branch inheritance (DEF-001).** Children see the
   parent's working tree/branch. Mitigations for any future use: run dispatch
   from a checkout on the intended ref, pass absolute paths into the intended
   worktree, or use `Agent` `isolation: "worktree"`. Not fixed in this pilot.
2. **No timeout primitive.** Only manual cancel + guard limits.
3. **`general-purpose` can nest.** The write-capable `codex` executor has the
   `Agent` tool; hub-and-spoke there relies on the prompt instruction, not a
   structural block. `Plan` executors are structurally safe.
4. **Agent-type fit is approximate.** `Plan` is a planning/read role reused for
   `[Thinking]`/`[Analytics]` reasoning; behavior is shaped by the bounded
   prompt + `project-context`, not the type label.
5. **Cost.** Each spawn starts cold and re-derives context.

## Rollback

Single PR → `git revert <sha>`. The `executor` block is inert data once the
orchestrator subsection is reverted; the carve-out, bundle regen, tests, and
this evidence file revert with it. No schema migration, no runtime store, no
`.gitignore` change. Prompt-level `Invoke AI-OS`, Goal Mode, AES records, and
existing routing are unaffected by a revert.

## AES statuses (reported separately)

```yaml
execution_state: completed        # MVP build + 3 pilots complete
overall_delivery: pass            # all 14 acceptance items observed (see verdict)
qa_status: pass                   # 6 canonical checks + provenance audit + pytest 215
judge_verdict: not_run            # no independent Judge review
authority_status: owner_review_pending
merge_status: not_opened          # → open on PR
production_status: not_applicable
```

## Acceptance check (owner's 14 criteria)

| # | criterion | result |
|---|---|---|
| 1 | one user prompt | pass (one goal per pilot) |
| 2 | ≥3 real native subagent dispatches | pass (9 completed across A/B/C; 3 per pilot) |
| 3 | no manual project selection by user | pass |
| 4 | owner chosen by canonical routing | pass (`ROUTING_RULES.md` each hop) |
| 5 | each child bounded context | pass (declared included/excluded/sufficiency; other projects excluded with reasons) |
| 6 | one `execution_id` | pass (`exec-pilot{A,B,C}-2026-09-02`, unchanged across hops) |
| 7 | requirements / evidence / authority provenance preserved | pass (carried in every dispatch prompt + route_trace) |
| 8 | control returns to root after each child | pass (hub-and-spoke; no child→child) |
| 9 | original acceptance re-evaluated after each stage | pass (root reassessed before each next route; Closure Review per pilot) |
| 10 | next owner chosen only by root | pass (children returned `cross_domain_need` only) |
| 11 | repeat / no-progress route detected by existing AES guards | pass (Pilot C: `repeat_route_refused_missing_evidence_delta`) |
| 12 | runtime failure registered as evidence/defect | pass (DEF-001, DEF-002) |
| 13 | Closure Review checks the original user goal | pass (per pilot) |
| 14 | one final result to the user | pass (one recommendation / one check design / one governance note) |
| C-extra | repeat route without `evidence_delta` → refused; with material `evidence_delta` → allowed | pass (both branches observed in Pilot C) |

## Verdict

# PASS

Executable multi-capability dispatch was actually run and observed end-to-end
(`goal → route → real child execution → central return → AES update → reroute →
Closure Review → one result`) across three multi-owner executions, with the
loop guard exercised in both directions. All 14 owner acceptance criteria and
the Pilot C extra check are met. Two defects were registered and handled, not
hidden. `qa_status` pass; `judge_verdict` not run; owner review pending; merge
and production unauthorized.

## Recommendation — pilot-only vs standardization

**Keep pilot-only for now; do not standardize yet.** Open a separate owner
decision for standardization, gated on:

1. **DEF-001 fixed** — a deterministic rule for the child's checkout/worktree
   (or mandatory `isolation: "worktree"`), so dispatched children cannot read a
   stale tree.
2. **Structural hub-and-spoke for the write path** — either restrict the
   `codex` executor to a non-nesting agent type or add an enforced block, so
   `child_dispatch: forbidden` is not prompt-only.
3. **2–3 more real executions** across `[AI OS] / [LLM] / Judge` and a
   deliberate runtime-failure case, to calibrate the four guard thresholds
   (currently unset) per the continuation contract.
4. A named owner for the dispatch cost/latency budget.

Until then this remains a bounded, reversible pilot under the 2026-09-02
carve-out and is not a standard workflow.
