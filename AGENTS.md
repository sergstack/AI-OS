# AGENTS.md

This is Sergey's AI-OS repository.

## Default Mode

Use Goal Mode by default.

In default Goal Mode, Sergey may give a broad goal instead of an atomic task package. Codex should inspect the repository, infer a bounded and reversible scope, create or use a non-main branch for repository changes, implement the smallest useful working version, run meaningful checks, fix in-scope failures once when safe, and report evidence, risks, rollback, and acceptance status.

Atomic task packages remain available for advanced, high-risk, strict, or ultra-long work, but they are not the default user burden. Do not turn a clear implementation goal into an epic, roadmap, child issue tree, or approval package unless Sergey asks for planning, the work cannot fit in one bounded PR, or a hard approval gate is reached.

## Autonomous Execution (AES)

Execution follows [`docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md`](docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md)
together with Goal Mode, the Codex autonomy policy, and applicable project
extensions. For normal local and reversible work, infer the smallest safe
scope, execute, validate, record assumptions, and continue without asking
unless a canonical hard blocker or materially consequential unresolved decision
is reached.

AES does not expand authority. Merge, deploy, production, destructive,
provider/API, source-mutation, business-rule, formula, metric, schema, or
output-contract gates remain governed by their canonical rules. All AES numeric
limits remain those of the canonical standard.

A bounded, reversible, in-repo corrective loop is supervised execution only
when it operates under an AES record, fixed authority and scope, validation,
stop conditions, rollback, and human acceptance. This classification does not
permit autonomous agents, generic agentic workflows, uncontrolled loops, or
any expansion of execution authority.

## Action reporting vocabulary

Use these labels only to qualify narrative claims about actions and evidence.

- `DONE` — an execution or tool result was actually observed.
- `PREPARED` — an artifact, diff, message, or package exists but has not been
  applied, sent, merged, deployed, or otherwise executed.
- `NOT RUN` — the step was not executed; state why.
- `NEEDS VERIFICATION` — a result exists, but it depends on an unverified
  source, assumption, or missing confirmation.

These labels do not replace, map to, or override AES `execution_state`,
`overall_delivery`, `qa_status`, `judge_verdict`, `authority_status`,
`merge_status`, or `production_status`. A reporting label never satisfies a
canonical hard blocker or authority gate.

## Clarification threshold

Do not ask repeat, obvious, or internal-mode questions when the user intent is
clear. Ask only when missing information materially changes the requested
outcome, authority boundary, allowed scope, acceptance criteria, risk or
irreversible action, money or privacy exposure, or creates a canonical hard
blocker.

Do not make the user choose an internal mode when it can be inferred safely.
Infer it, record it, and report it in the final report. For other ambiguity,
choose the most conservative reversible interpretation, record it as an
assumption, continue, and surface unresolved non-blocking questions in the
final report.

## Risk-mode guidance

Goal Mode is a user-facing workflow, not an AES `execution_mode`. Use only the
current AES schema values: `lightweight` for local reversible docs or
configuration work without governed semantic change; `standard` for normal
implementation, generated artifacts, or several bounded requirements; and
`full` for high-risk, explicitly hard-gated, cross-authority, governed
business/schema/formula/metric, production-adjacent work, or another canonical
full-review condition.

Risk mode affects intake and validation depth only where AES permits it. It
does not waive mandatory v2 Closure Review, hard blockers, owner authority,
merge gates, or production gates. Do not classify work as `full` solely because
its owner project is `[Analytics]`.

## Source of Truth

- Use repository files as the source of truth.
- Read relevant files before editing.
- Obey this file and any more specific local instructions.
- Keep source files and Knowledge bundle files consistent when both represent the same content.

## Local Developer Evidence

- For every substantive repository task, evaluate `$local-developer-worker` and invoke each applicable safe module. It is evidence-scoped, not a prerequisite to begin safe local work.
- Use direct bounded reading for one known file; use deterministic discovery plus `ldw context pack` for unfamiliar or multi-file work when available.
- Establish a test claim through `ldw test parse` with captured output, the observed exit code, and `command_observed=true`; establish a git/repository fact claim through `ldw git facts`; build formal evidence packages through `ldw evidence build`.
- Preserve and report `partial`, `unsupported`, `policy_blocked`, timeout, and fallback states. LDW remains read-only and never owns edits or decisions.

## Domain Capability Discovery

For an unscoped goal that needs AI-OS methodology, use `ai-os-orchestrator` as the default entrypoint. Use it for material AI-OS work:
cross-project or cross-owner work, AI-OS methodology-bearing changes, governed
semantic changes, material Analytics deliverables, canonical governance changes,
or cases where local instructions cannot safely resolve owner or scope. It must
classify the request using canonical routing rules, resolve ownership through
`PROJECT_CAPABILITIES.yaml`, and use `project-context` only after routing to
load task-relevant canonical files. The orchestrator must fail closed when
ownership or required paths cannot be verified.

Simple local, reversible repository work at `risk_mode: lightweight` may remain
local and does not require a new AI-OS orchestration pass at intake. If local
work is part of an already-active AI-OS execution, local completion does not terminate the orchestration lifecycle: return the result to the active
execution, validate it, and reassess the original acceptance criteria.

Re-enter routing or orchestration when a project or owner boundary is crossed,
AI-OS methodology becomes necessary, governed semantics are touched, or local
instructions no longer resolve the required scope safely. Risk mode is not the
sole routing mechanism. Direct already-routed and strict task packages remain
valid when the user explicitly supplies them.

## Change Rules

- Make the smallest necessary change.
- Keep changes bounded and reversible.
- Do not refactor unrelated content.
- Do not add blocked promotion items: embeddings, semantic search, vector DB, web UI, autonomous retrieval, agentic workflows, autonomous agents, production deploys, secrets, credentials, or runtime artifacts.
- Do not claim production readiness or `production_promotion=yes`.
- Do not commit directly to `main`.
- Follow the canonical merge policy in `GOAL_MODE.md`; Codex and agents must not manually merge pull requests.

## Validation

Run the smallest meaningful checks before reporting completion. For docs and project settings, prefer:

```bash
python3 scripts/check_project_instructions_length.py
python3 scripts/check_repo_public_safety.py
python3 scripts/check_codex_goal_mode_defaults.py
python3 scripts/check_manifest_paths.py
python3 scripts/check_knowledge_bundles.py
python3 scripts/check_index_coverage.py
```

If checks cannot run, report the blocker instead of inventing results.
