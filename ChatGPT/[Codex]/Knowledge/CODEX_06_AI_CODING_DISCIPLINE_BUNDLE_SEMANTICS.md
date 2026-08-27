# Migrated Bundle Semantics

Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_06_AI_CODING_DISCIPLINE.md`.

## Legacy section: `ChatGPT/[Codex]/Knowledge/CODEX_TDD_WORKFLOW.md`

Use test-first discipline for code, scripts, parsers, validators, bugfixes, pipeline logic, and approved output contract changes.
Loop:
Docs-only tasks do not need TDD. Use lightweight smoke checks such as affected file search, `git diff --check`, repo consistency scripts, and bundle/source consistency checks.
For numeric, financial, or analytical logic, Python or SQL performs calculations. Stop or ask before changing formulas, schemas, metrics, column names, output contracts, production behavior, or deployment.

## Legacy section: `ChatGPT/[Codex]/Knowledge/PR_JUDGE_CHECKLIST.md`

Review a PR for:
- goal match;
- changed file scope;
- scope creep;
- forbidden files or artifacts;
- unapproved formulas, schemas, metrics, output contracts, APIs, or business logic;
- tests/checks appropriate to risk;
- risks, limitations, rollback, and honest acceptance status.
Verdicts:
Output:
Codex must not decide final mergeability or manually merge PRs by itself. Follow the canonical `Merge Policy` in `GOAL_MODE.md`.

## Legacy section: `ChatGPT/[Codex]/Knowledge/WORKTREE_AND_PARALLEL_AGENT_POLICY.md`

Separate branches or worktrees are allowed for isolated, reviewable work. Each worktree needs one goal, one branch, allowed files, forbidden actions, checks, and rollback.
Parallel agents are allowed only when scopes are isolated. The main agent owns the final diff, reviews all changes before staging, stages only intended files, and reports checks actually run.
Forbidden: uncontrolled edits to the same files, hidden background automation, autonomous retrieval, production deploys, broad refactors, secrets handling, and unapproved schema/API/output contract/formula/metric/business logic changes.

## Legacy section: `ChatGPT/[Codex]/Knowledge/CODEX_TASK_EXAMPLES.md`

Good Goal Mode tasks name the goal, constraints, checks, PR expectation, and merge/gate posture while allowing Codex to infer safe scope.
Good strict tasks include objective, allowed files, forbidden changes, checks, and acceptance criteria.
Weak tasks such as "Make the pipeline better" should be improved with expected behavior, affected files, forbidden changes, checks, and acceptance criteria.

## Legacy section: `ChatGPT/[Codex]/Knowledge/EVALS_FOR_CODEX_WORKFLOW.md`

Lightweight workflow evals:
- Goal Mode intake: route, scope, files, forbidden actions, checks, rollback, acceptance.
- Test discipline: test-first for code/script/pipeline changes; smoke checks for docs-only changes.
- PR Judge: verdict plus required fixes, risks, checks reviewed, owner-review merge readiness.
- Parallel work safety: isolated files/branches and one owner for final staging.
- Forbidden feature guard: no secrets, `.env`, vector DB, embeddings, semantic search, web UI, autonomous agents, production deploys, broad refactors, or runtime artifacts.
