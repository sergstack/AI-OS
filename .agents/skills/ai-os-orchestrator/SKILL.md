---
name: ai-os-orchestrator
description: Default AI-OS entrypoint for a user goal. Route through canonical rules, resolve one owner capability, load bounded project context, and govern explicit handoffs, checks, acceptance, rollback, and reporting.
---

# AI-OS Orchestrator

Use this skill as the default front door when the user gives a goal that needs AI-OS methodology and does not manually provide a route. Simple local, reversible repository work with sufficient local instructions stays local and does not activate AI-OS.

This skill owns orchestration only. It does not own domain methodology, replace a capability, or create a second routing registry.

## Canonical sources

Before routing, verify and read:

1. the applicable `AGENTS.md` files;
2. `ChatGPT/[Inbox Router]/Knowledge/ROUTING_RULES.md` for front-door routing semantics;
3. `PROJECT_CAPABILITIES.yaml` for capability locations;
4. `.agents/skills/project-context/SKILL.md` for bounded context loading;
5. `GOAL_MODE.md` and `HANDOFF_STYLE_STANDARD.md` when execution or a cross-project handoff is required.

Treat those files as the semantic owners. Do not copy their routing tables, capability locations, project methodology, or merge policy into this skill.

## Procedure

1. **Preflight.** Confirm every required canonical source above exists. Preserve system, user, and applicable local repository constraints.
2. **Classify.** Apply the canonical front-door routing rules to the requested outcome. Require one canonical destination for the current stage. A raw or unclear intake may resolve to `[Inbox Router]` only when the canonical rules say so; it is not a fallback for conflicting owner candidates.
3. **Resolve.** Match the routed destination to registry-owned data without a hardcoded label map:
   - if routing returns a capability id, require an exact key match in `PROJECT_CAPABILITIES.yaml`;
   - if routing returns a project label, require its exact match to the final path component of exactly one registered `canonical_path`;
   - require exactly one match; zero or multiple registry matches are `blocked`;
   - then require one relative `canonical_path` and a non-empty `context_entrypoints` list whose first item is `PROJECT_INSTRUCTIONS.md`.
   The unique registered match is exactly one primary owner capability for the current stage.
   A canonical destination outside the registered AI-OS capabilities, such as Things, Calendar, Notes, or Codex APP, is an explicit terminal handoff: report it without inventing a capability and do not invoke `project-context`.
4. **Validate paths.** Resolve the canonical path inside the repository. Reject absolute paths, traversal, symlink escape, missing directories, missing entrypoints, and any entrypoint that escapes its canonical project.
5. **Load context.** Invoke or follow `project-context` only after Steps 2–4 pass. Read the owner instructions first, then only indexed or task-relevant references. Stop when context is sufficient.
6. **Execute within ownership.** Keep reasoning and methodology with the primary owner. For repository implementation, create a bounded handoff to local Codex execution with outcome, allowed scope, local constraints, checks, rollback, and acceptance criteria.
7. **Add capabilities only by handoff.** Use another capability only when the primary owner identifies a concrete cross-domain need. Record `From`, `To`, objective, inputs, constraints, expected output, acceptance, risks, evidence/confidence, and first step. Return the result to the primary owner unless the user explicitly changes the requested outcome.
8. **Validate and report.** Apply only relevant project checks plus Goal Mode acceptance, rollback, reporting, and merge gates. A passing check or Judge verdict does not authorize merge or production promotion.

## Fail-closed rules

Stop with status `blocked` and report the exact missing or conflicting evidence when:

- canonical routing does not yield exactly one destination for the current stage;
- a capability id or project label has zero or multiple registry matches;
- a required canonical source, registry entry, canonical path, or context entrypoint is absent;
- a registry or entrypoint path is absolute, escapes its canonical boundary, or cannot be verified;
- owner instructions conflict and precedence does not resolve them;
- a required handoff has no explicit owner, scope, checks, rollback, or acceptance boundary;
- safe execution or meaningful validation is impossible.

Do not guess an owner, silently substitute a nearby project, broaden scope, or load all projects to resolve uncertainty. Ask for the smallest missing decision only when canonical evidence cannot settle the blocker.

## Context boundary

Load one primary capability by default. Exclude unrelated projects, whole Knowledge trees, raw dumps, runtime artifacts, secrets, and copied methodology. Record inspected entrypoints, included files and reasons, excluded candidates and reasons, missing references, and context sufficiency.

## Output contract

Return:

- goal and routing decision;
- primary owner capability and canonical path;
- bounded context used and explicit exclusions;
- handoffs performed, or `none`;
- actions and changed scope;
- checks and observed results;
- risks and blockers;
- rollback;
- acceptance status;
- branch, PR, merge-gate, and production status when applicable.
