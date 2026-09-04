# AutoResearch v0.2 CLI — Operating Guide

`scripts/autoresearch_cli.py` (issue #416, parent
[#409](https://github.com/sergstack/AI-OS/issues/409)) is the **one** command
surface for the AutoResearch v0.2 live loop. It integrates the v0.1 foundation
(`autoresearch_validator`, `autoresearch_shadow_runner`,
`autoresearch_decision_comparator`, v0.1 schemas / manifest / ledger) with the
v0.2 live components (`autoresearch_context_pack_compiler` #412,
`autoresearch_live_browser_adapter` #413, `autoresearch_live_judge` #414,
`autoresearch_failure_intake` #415).

It **does not** run the Phase 0 calibration (#417) or the Phase 1 autotuning
batch (#418), mutate any active Project configuration, or commit / push / merge
/ deploy.

## Invocation

```bash
python3 scripts/autoresearch_cli.py <verb> [options]
python3 scripts/autoresearch_cli.py --version      # -> autoresearch_cli 0.2.0
python3 scripts/autoresearch_cli.py <verb> --help
```

## Exit codes

| code | meaning |
|---|---|
| `0` | success |
| `2` | usage error (bad flags / missing file) |
| `3` | `doctor` / preflight failure — a required gate is missing or failed |
| `4` | **blocked** — a live call is required but no authorized live transport binding is wired in. Not an error: this is live-contract §5/§10's "no authorized transport/budget ⇒ blocked". |
| `5` | integrity failure — ledger / worktree / drift |

## Configuration precedence

`explicit CLI flag` > `--batch-config <file>` value > built-in default.

The batch-config file is the machine-readable per-batch contract
(`schemas/autoresearch_v02_live_batch_config.schema.json`, #411). The CLI reads
`transport_id`, `context_manifest_hash`, `authority_status` /
`transport_authority_status` from it during `doctor` and previews.

## Verbs

### `doctor`

```bash
python3 scripts/autoresearch_cli.py doctor \
  --batch-config batch.json --max-calls 40 --max-cost 0 --cost-currency USD
```

Validates, **before any external call**: v0.1 manifest present, v0.2 live
contract present, budget authorized (numeric call ceiling + cost cap +
currency; `$0` + `USD` is a valid plan-included cap), batch `authority_status`
== `authorized`, `context_manifest_hash` present, `transport_id` ==
`playwright_mcp`, evaluator config loads with no drift, and whether a live
transport binding is present. A missing live-transport binding is reported but
does **not** fail `doctor` (dry-run is a legitimate state); any other missing
gate makes `doctor` exit `3`.

### `context`

```bash
python3 scripts/autoresearch_cli.py context \
  --role subject_baseline --project ai_os --source-revision HEAD [--summary]
```

Compiles a `repo_replay` context pack via the #412 compiler and prints the
manifest JSON (or the human summary with `--summary`). **No model call.**

### `baseline` · `experiment` · `batch`

```bash
python3 scripts/autoresearch_cli.py experiment \
  --batch-config batch.json --cases c1,c2 --run-count 3 \
  --max-calls 40 --max-cost 0 --cost-currency USD --dry-run
```

`--dry-run` prints the external-action preview — planned **subject / researcher
/ judge** calls counted separately, budget before/after, ephemeral worktrees,
output files — and makes **zero external calls** (exit `0`).

Without `--dry-run`: the CLI runs `doctor` first (exit `3` on failure), then —
because no authorized `PlaywrightMcpBrowserTransport` binding is wired into a
bare CLI invocation — reports `status: "blocked"` with the preview and exits
`4`. A real live run happens only under the coordinated live session (#417),
which constructs a `Controller` with a real transport / judge / researcher
binding.

`--run-manifest <path>` writes/reads the durable run manifest
(`schemas/autoresearch_run_manifest.schema.json`) for bounded resume: resume
re-validates source revision, context / evaluator hashes, authority, remaining
budget, and worktree state; completed live calls are never repeated without a
newly recorded authorized rerun; duplicate experiment decisions are rejected
unless they are append-only ledger corrections.

### `reproduce`

```bash
python3 scripts/autoresearch_cli.py reproduce \
  --failure-record f.json --runs runs.json [--dry-run]
```

Runs `autoresearch_failure_intake.assess_reproduction` over the supplied
repo-replay run records. A field observation with no qualifying runs (each
needs a real `context_hash` + `model_hash` + failure signal) is
`not_reproduced`, never `reproduced`.

### `propose`

```bash
python3 scripts/autoresearch_cli.py propose --failure-record f.json [--dry-run]
```

`--dry-run` states the planned single Researcher call (+ one bounded retry).
Without a live Researcher binding it exits `4` (blocked).

### `report`

```bash
python3 scripts/autoresearch_cli.py report \
  --run-manifest run.json --ledger ledger.jsonl [--decision keep_candidate]
```

Renders a run report reconciling steps, live invocation ids, budget, decision,
and — if `--ledger` is given — the result of `autoresearch_validator.verify_ledger`
(exit `5` on integrity failure). A `keep_candidate` decision is rendered with
`authority_status: owner_review_pending`, `merge_status: not_applicable`,
`production_status: not_applicable` — research evidence only; it never advances
a baseline or opens a PR.

### `cleanup`

```bash
python3 scripts/autoresearch_cli.py cleanup --run-manifest run.json
```

Removes **only** the ephemeral worktrees registered in that run manifest
(`autoresearch_shadow_runner.remove_shadow_worktree`), preserves all evidence,
and never touches `main`, the parent working tree, or any unregistered path.

## Coordinated-session seam (`experiment`, non-dry-run — issue #433)

A bare shell `autoresearch_cli.py experiment` has **no live transport** and
cannot get one (a shell process has no MCP access), so it still exits `4`
(`blocked`) with a reason pointing here. A live run happens only through the
**coordinated-session** entrypoint, driven by an operator/agent that holds the
`mcp__playwright__browser_*` tools:

```python
import autoresearch_coordinated_session as acs

def mcp_call(tool_name, arguments):
    # forward to the real mcp__playwright__browser_* tool and return its dict
    ...

result = acs.run_manual_candidate_evaluation(
    mcp_call=mcp_call,
    batch_config=json.load(open("batch.json")),      # #411 schema; authority_status == "authorized",
                                                     # authority_evidence_ref set, call_timeout_seconds set
    spec=acs.load_spec("spec.json"),                 # ManualCandidateSpec: one frozen human-authored candidate
    budget=cli.RoleBudget(max_provider_calls=40, max_cost_amount=0.0, max_cost_currency="USD"),
    evidence_dir=Path("docs/evidence/…"),
)
```

`mcp_call` is the **only** new privilege. Everything downstream is the frozen
pipeline: `PlaywrightMcpBrowserTransport` (#413) → `run_shadow_experiment`
(#393, isolated worktree + scope gate) → deterministic hard gates (#392) →
blind A/B `run_blind_ab` in both orders (#414) → `aggregate_decision` (#395) →
sanitized evidence package. `Controller.run_experiment` is a **sequencer with
no decision logic of its own**.

Outcome is exactly one of `reject | inconclusive | candidate_for_owner_review`
— never `keep_candidate`. `candidate_for_owner_review` is research evidence
only: it is not owner acceptance, merge, or promotion authority.

Fail-closed is unchanged: missing transport binding, missing/`!= "authorized"`
batch authority, unauthorized budget, missing `authority_evidence_ref`, patch
scope violation, or context drift outside the one declared mutation all stop
the run before or at the first gate.

Method-sensitive glue — rerun orchestration (**MD-1**), the
`CaseSemanticEvidence → CaseObservation` mapping (**MD-2**), and the decision
label (**MD-4**) — is isolated in `autoresearch_cli` and **requires
[AI OS] / [Analytics] sign-off** against `AUTORESEARCH_STOCHASTICITY_NONINFERIORITY_METHOD.md`
and `AUTORESEARCH_SEMANTIC_EVALUATOR_CONTRACT.md` before it drives a paid/live
call. It does not modify either document or the comparator method.

## What the CLI never does

Phase 0/1 batches; hard-coded observations in a live path; active Project
Instructions / routing edits; automatic baseline advancement, candidate
promotion, commit / push / PR / merge / deploy / Project sync; holdout access;
open-ended loops or a daemon; multi-provider fallback; credential logging;
bypassing the v0.1 validator, worktree isolation, hard gates, Judge blindness,
comparator, or ledger.
