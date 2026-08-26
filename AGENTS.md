# AGENTS.md

This is Sergey's AI-OS repository.

## Default Mode

Use Goal Mode by default.

In default Goal Mode, Sergey may give a broad goal instead of an atomic task package. Codex should inspect the repository, infer a bounded and reversible scope, create or use a non-main branch for repository changes, implement the smallest useful working version, run meaningful checks, fix in-scope failures once when safe, and report evidence, risks, rollback, and acceptance status.

Atomic task packages remain available for advanced, high-risk, strict, or ultra-long work, but they are not the default user burden. Do not turn a clear implementation goal into an epic, roadmap, child issue tree, or approval package unless Sergey asks for planning, the work cannot fit in one bounded PR, or a hard approval gate is reached.

## Autonomous Execution (AES)

[`AUTONOMOUS_EXECUTION_STANDARD.md`](AUTONOMOUS_EXECUTION_STANDARD.md) is the
direct execution contract for AES.
For local, reversible docs or workflow changes whose safe scope can be
inferred, Goal Mode/AES proceeds with the smallest bounded scope, validation,
and a recorded execution mode and risk mode; it does not require an intake
round-trip. Assume and log non-blocking ambiguity rather than asking: use the
conservative branch, keep scope fixed, and record `DEFERRED:` in
`Assumptions:` when it remains unresolved. Canonical hard blockers remain the
only immediate stop conditions; see `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`.
All AES numeric limits remain those of the canonical standard.

A bounded, reversible, in-repo corrective loop is supervised execution only
when it operates under an AES record, fixed authority and scope, validation,
stop conditions, rollback, and human acceptance. This classification does not
permit autonomous agents, generic agentic workflows, uncontrolled loops, or
any expansion of execution authority.

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

For an unscoped goal that needs AI-OS methodology and whose canonical owner is
genuinely unresolved, use `ai-os-orchestrator` as the default entrypoint. It must
classify the request using canonical routing rules, resolve exactly one owner
through `PROJECT_CAPABILITIES.yaml`, and use `project-context` only after routing
to load task-relevant canonical files. When canonical ownership is
already resolved locally, execute under that owner's instructions; preserve
ownership boundaries, add capabilities only through explicit handoffs, and
fail closed when ownership or paths cannot be verified.

Simple local, reversible repository work with sufficient local instructions remains local Codex execution and does not require AI-OS orchestration. Direct already-routed and strict task packages remain valid when the user explicitly supplies them.

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
