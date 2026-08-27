# [Codex] — Execution Autonomy Reporting

## Purpose

Compact upload artifact for [Codex] covering execution autonomy reporting.

## Source files

- `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_LONG_RUN_PLAYBOOK.md`
- `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`
- `ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`
- `AUTONOMOUS_EXECUTION_STANDARD.md`
- `ChatGPT/[Codex]/Knowledge/CODEX_02_EXECUTION_AUTONOMY_REPORTING_BUNDLE_SEMANTICS.md`

## Upload target

ChatGPT Project Sources / Knowledge for `[Codex]`.

## Status

- production_promotion: no, unless explicitly accepted elsewhere
- bundle_type: generated compact upload artifact
- source_of_truth: declared granular source files
- source_fingerprint: sha256:c562026bb97ca422690dcc95282c4bd5b7aadb8308dcca7b8659d984ca357a97
- generator: scripts/build_knowledge_bundles.py

---

# Content

## From: `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`

# Autonomy Policy
## Purpose
Define when Codex should continue autonomously and when it must stop.
For normal bounded repo work, use `Goal Mode Contract` in `GOAL_MODE.md` as the
named reusable standard for autonomy, execution order, forbidden actions,
reporting, PR/merge-gate posture, and no-deletion-without-quarantine rules.
## Continue without asking
Continue without asking when all conditions are true:
- the change is local;
- the change is reversible;
- the change is inside allowed files;
- no business logic, schema, secret, production, deploy, or runtime risk exists;
- a meaningful smoke check is possible;
- assumptions can be logged in the final report.
Safe assumptions include:
- choosing the nearest existing valid path when a requested optional doc path is missing;
- adding cross-references instead of duplicating equivalent content;
- using the smallest docs-only smoke checks when no unit tests apply;
- preserving existing wording and structure unless the task requires an addition.
## Stop conditions
Canonical hard blockers. Stop and report a blocker when work requires or may cause:
- missing required approval for real provider/API execution;
- sensitive configuration value exposure risk;
- source workbook mutation or Safe Apply without approval;
- production/runtime/deploy/migration without explicit approval and rollback;
- destructive operations;
- schema, API, output contract, file format, or column order changes without approval;
- business logic, metrics, formulas, or financial controls without approval;
- governed KB change without required evidence/acceptance;
- conflicting acceptance criteria;
- no meaningful validation path;
- governance boundary violation.
## Provider/API safeguards
Sensitive configuration values are hard blockers for real provider/API execution, not for local implementation scaffolding.
Allowed without additional approval:
- implement provider/client code;
- implement dry-run and no-network execution paths;
- implement preflight checks;
- check whether required configuration variable names are present;
- check presence/non-empty status without printing values;
- add tests with mock or fake values;
- document required configuration variable names.
Requires explicit bounded approval:
- real provider/API calls;
- source mutation;
- Safe Apply;
- production/runtime/deploy actions;
- batch expansion beyond approved sample size;
- schema, metric, formula, provider-routing, or output-contract changes.
Never print, log, expose, summarize, or commit sensitive values. Never commit local configuration or machine-local credential files. Never expose raw provider responses in repo files, PR bodies, logs, or Knowledge bundles.
Local configuration presence is not approval. Approval must be explicit and bounded.
## Retry policy
If a check fails and the issue is local, reversible, and inside allowed files, attempt one minimal fix and rerun the smallest relevant check.
If the same validation target still fails, the one-fix budget is exhausted
for that target and the independently evidenced defect it represents. Stop
further correction attempts for that target and report:
- failing command;
- observed failure;
- attempted fix;
- residual risk;
- acceptance status.
This does not terminate all execution: a different in-scope defect may be
handled only when it is independently evidenced against a different affected
requirement or independently failing validation target and remains eligible
under AES Section 9.6 and all applicable limits. Renaming or changing only a
`defect_id`, subtype, classification, label, wording, or representation never
creates a new correction budget for the same failed validation target.
## Final report requirement
Use the canonical final report schema in `EXECUTION_REPORTING_RULES.md`. Assumptions must be marked as assumptions, not facts.

## From: `ChatGPT/[Codex]/Knowledge/CODEX_LONG_RUN_PLAYBOOK.md`

# Codex Long-Run Playbook
## Purpose
Help Codex keep working on scoped local tasks without unnecessary questions.
## Cycle
Use this cycle for long-running implementation:
```text
Inspect -> Plan -> Implement -> Test -> Retry once if safe -> Review -> Report
```
## Working rules
- Do not ask on reversible docs or configuration decisions inside allowed files.
- Use safe defaults from the task package and existing repository structure.
- Keep the diff small and trace every changed line to the task.
- Prefer updating existing files and cross-references over creating duplicate guidance.
- Do not widen scope to unrelated cleanup.
- Treat missing optional docs links as recoverable when a nearest valid path exists.
## Test and retry
Run the smallest meaningful checks for the task.
If a check fails:
1. decide whether the failure is local, reversible, and inside allowed files;
2. attempt one minimal fix only when safe;
3. rerun the smallest relevant check;
4. if it still fails, stop and report diagnostics.
Do not retry when the issue involves secrets, production systems, migrations, destructive commands, governed KB content outside scope, or output contracts.
## Reporting
Report:
- changed files;
- commands and checks run;
- assumptions;
- risks or limitations;
- rollback path;
- acceptance status.
Use `pass`, `partial`, `fail`, or `blocked` honestly. Do not claim checks passed unless they were run and observed.

## From: `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`

# Codex Execution And Reporting Rules
## Execution modes
- inspect-only: изучи repo, верни files/entrypoints/risks/plan, не редактируй.
- implement: минимально измени allowed files, запусти checks.
- bugfix: reproduce/define failure -> root cause -> minimal patch -> regression check.
- refactor: зафиксируй текущее behavior -> minimal refactor -> regression/golden check.
- test/QA: выбери smallest useful test, запусти/добавь checks, верни pass/fail.
- data pipeline: проверь contracts, grain, raw/stage/marts, reconciliation, artifacts.
- release: acceptance, tests, release notes, rollback, residual risks.
## Planning
Перед edit дай короткий action-oriented plan:
- scope;
- files to inspect/modify;
- assumptions;
- risks;
- tests to run.
Не раскрывай лишнюю internal reasoning.
## Parent / Child Issue Gate
If an issue references `Parent / Child Issue Gate Standard`, respect `Depends on` / child issue order, do not start a downstream child until its dependency is accepted or merged, normally use one PR per child issue, report blocked dependencies as gates, do not close the parent until final QA passes, and do not silently replace old contracts without a migration note or blocker.
## Existing Script Controlled Refactor
When using `Existing Script Controlled Refactor Standard`, report baseline, output contract, safety tests, before/after comparison, behavior changes, and acceptance status explicitly.
```text
Summary:
Branch:
Files inspected:
Files changed:
Baseline captured:
Output contract:
Safety tests:
Before/after comparison:
Behavior changes:
Checks run:
Risks:
Rollback:
PR:
Acceptance status:
```
## Testing
После изменений запусти доступные проверки:
- unit / integration / contract / smoke / golden / data quality / artifact validation;
- build / type check / lint, если они есть и релевантны;
- repo-specific commands из README, package files или task package.
Если тесты не запускались, явно напиши почему и какой минимальный check нужен.
## Review
Перед финальным ответом проверь:
- diff соответствует scope;
- forbidden actions не выполнены;
- output contracts сохранены;
- tests/checks понятны;
- risks и assumptions названы;
- rollback/next step есть.
## Blocker format
```text
blocked_reason:
missing_input:
risk_if_continue:
safe_next_step:
files_inspected:
```
## Final response format
Canonical final report schema:
```text
Summary:
Branch:
Files inspected:
Files changed:
Commands run:
Test results:
Evidence / artifacts:
Assumptions:
Blockers:
Risks:
Rollback:
PR:
Acceptance status:
Merge / gate status:
```
Mode-specific reports may be shorter, but they must not conflict with this schema.
Пиши как инженер: конкретно, проверяемо, без воды.

## From: `ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`

# Failure Modes
## Severity levels
Use one of these severity levels before deciding whether to stop.
### recoverable
Continue when the issue is local, reversible, and can be logged.
Examples:
- missing optional docs link;
- ambiguous wording in README;
- missing non-critical checklist item;
- no dedicated docs test command.
### needs_check
Continue only after checking the affected text and validating the diff.
Examples:
- changed instructions affect Codex behavior;
- changed file references;
- changed task contract wording;
- changed checklist acceptance language.
### hard_blocker
Stop when the issue creates governance, safety, or validation risk. Use the canonical hard-blocker list in `AUTONOMY_POLICY.md`; do not maintain a competing list here.
## Common failures
- Scope creep.
- Broad refactor instead of task.
- No tests.
- Business logic changed silently.
- Output schema changed silently.
- Secrets exposed.
- Sensitive values or raw provider responses exposed in repo files, PR bodies, logs, or Knowledge bundles.
- Real provider/API execution treated as approved only because local configuration exists.
- LLM narrative mixed with deterministic calculations.
- Validation deleted.
- Acceptance criteria missing.
- Rollback missing.
- Premature automation added.
## Response
If a failure mode appears:
1. classify it as `recoverable`, `needs_check`, or `hard_blocker`;
2. continue for `recoverable` issues and log the assumption;
3. inspect and validate before continuing for `needs_check` issues;
4. stop for `hard_blocker` issues and report blocker plus safe minimal next step.

## From: `AUTONOMOUS_EXECUTION_STANDARD.md`

# Autonomous Execution Standard (AES) v2.0.0
Status: normative package with scoped advisory semantic validation.
Canonical owner: `[AI OS]`.
Canonical source path: `AUTONOMOUS_EXECUTION_STANDARD.md` (this file, repo root).
Companion contract: `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`.
Current schema: `schemas/autonomous_execution_record.schema.json`.
Historical v1 schema: `schemas/autonomous_execution_record.v1.schema.json`.
This document is the single canonical source for the Autonomous Execution
Standard. Knowledge Bundles, upload packages, and any future generated
indexes that mention AES are derived artifacts: they may summarize or link
to this file, but they must not restate the state machine, defect model, or
schema and must not become an independent semantic owner. If a derived
summary and this file ever disagree, this file wins.
## 0. What this is, and what it is not
AES does not replace or weaken any existing AI-OS component:
- Goal Mode (`GOAL_MODE.md`);
- routing;
- Codex autonomy policy (`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`);
- testing workflows;
- execution reporting (`ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`);
- Judge/Revisor;
- project handoffs (`ChatGPT/[AI OS]/Knowledge/HANDOFF_PROTOCOL.md`);
- Analytics methodology;
- the GitHub merge policy in `GOAL_MODE.md`;
- owner, deploy, and production gates.
AES is a shared execution layer that connects these existing components into
one closed loop:
```text
requirements
-> execution
-> validation
-> defect registration
-> corrective action
-> affected-scope rerun
-> revalidation
-> requirements traceability
-> Closure Review
-> terminal acceptance / stopped
```
Where AES and an existing project rule set different limits for the same
situation, the stricter rule wins (see Section 3).
### 0.1 Phase 1 boundary
Phase 1 (this package) delivers only:
- this canonical standard;
- the state model and status namespaces;
- the declarative execution-record JSON Schema;
- requirement, defect, iteration, and artifact structures;
- the project-extension contract;
- the status migration map;
- the acceptance-case specification;
- example execution records;
- pilot specifications;
- the adoption plan;
- thin references from existing canonical entry documents.
The original Phase 1 package explicitly did **not** include: a semantic execution validator,
blocking CI enforcement, an automatic stale-artifact gate, automatic
handoff-ID enforcement, an automatic scope-creep detector, an automatic
authority evaluator, a runtime execution service, an orchestration platform,
or any production enforcement. Only advisory structural validation of the
declarative JSON Schema is in scope: JSON syntax, required fields, field
types, enum values, nested object structure, and ID format patterns.
The scoped advisory semantic validator now checks its documented subset of
cross-field invariants. It remains read-only and is not a blocking CI service.
Closure Review is mandatory for every new v2 record; historical v1 records
remain historical evidence and are not rewritten.
## 1. Precedence model
```text
1. system, safety and non-overridable governance constraints
2. explicit user instruction
3. approved task package
4. project instructions
5. applicable project-specific execution extension
6. this document (AUTONOMOUS_EXECUTION_STANDARD.md)
7. supporting playbooks, templates and examples
```
General rule: when two applicable rules conflict, the stricter constraint on
authority, safety, scope, validation, retry, or external side effect wins.
Consequences:
- user instruction does not override safety;
- an extension does not expand authority;
- an extension may only shrink an iteration limit, never grow it;
- a task package may narrow allowed scope, never widen it;
- this standard does not lift the stricter Codex one-fix policy (Section 9.5);
- `overall_delivery: pass` does not imply owner approval;
- Judge `pass` does not imply merge approval;
- `merged` does not imply production authorization.
## 2. Canonical ownership
```yaml
canonical_owner: "[AI OS]"
canonical_source_path: "AUTONOMOUS_EXECUTION_STANDARD.md"
derived_artifacts: []   # none registered in Phase 1
supersedes: []
superseded_by: []
```
`[AI OS]` owns: execution-state semantics, authority separation, status
namespaces, the canonical governance mapping, adoption status, and the
source-versus-derived distinction. Project extensions (Section 10) own only
domain-specific detail and never become an alternate semantic owner.
### 2.1 Resolved owner boundary
Once canonical routing resolves the primary owner for a material decision or
deliverable, that ownership remains authoritative for the current stage. An
upstream project may prepare evidence, contradictions, context, bounded
options, risks, constraints, and a compact handoff, but it must not silently
make, approve, or operationalize the owner-only outcome.
The handoff must preserve the material evidence and contradictions, the
decision boundary they affect, relevant requirements and constraints, risks,
acceptance criteria, and the first safe step. It must carry enough bounded
context for the receiving owner to continue without re-decomposing the goal.
If the receiving owner cannot act, report the handoff or blocker; do not
substitute a nearby project's judgment. Section 15 defines the execution-state
fields that must persist across that handoff.
## 3. Target architecture
### 3.1 User entry layer
`GOAL_MODE.md` remains the user-facing entry contract:
```text
user outcome -> route -> bounded scope -> applicable Autonomous Execution Standard
```
Goal Mode carries only a thin reference to this document; it does not
duplicate the state machine, defect model, or schema.
### 3.2 Canonical execution layer (this document)
Owns only universal mechanics: execution identity, requirements, states,
validation records, defects, iterations, corrective actions, reruns,
acceptance scopes, freshness, handoff persistence, rollback readiness,
external authority separation, and terminal reporting.
### 3.3 Project-extension layer
Owns only domain-specific detail: defect subtypes, domain checks, domain
evidence, risk overrides, stricter retry limits, acceptance scopes,
project-specific blockers, and project-specific authority gates. An
extension must not copy the canonical standard wholesale (Section 10).
## 4. Canonical status namespaces
All machine-readable values use lowercase `snake_case`. Uppercase aliases in
canonical records are not permitted.
### 4.1 `execution_state`
`initialized`, `scoped`, `executing`, `validating`, `correcting`,
`revalidating`, `completed`, `stopped`.
### 4.2 `requirement.status`
`not_started`, `implemented`, `validation_pending`, `passed`, `failed`,
`blocked`, `not_applicable`.
### 4.3 Acceptance-scope `status`
`not_evaluated`, `pass`, `partial`, `fail`, `blocked`, `not_applicable`.
### 4.4 `overall_delivery`
`not_evaluated`, `pass`, `partial`, `fail`, `blocked`.
### 4.5 `qa_status`
`not_run`, `pass`, `fail`, `blocked`, `not_applicable`.
### 4.6 `judge_verdict`
`not_run`, `pass`, `revise`, `blocked`.
### 4.7 `authority_status`
`not_required`, `owner_review_pending`, `approved`, `rejected`.
### 4.8 `merge_status`
`not_applicable`, `not_opened`, `open`, `checks_pending`,
`owner_review_pending`, `merge_ready`, `merged`, `closed_without_merge`.
### 4.9 `production_status`
`not_applicable`, `not_authorized`, `authorized`, `deployed`, `rolled_back`.
### 4.10 `artifact_freshness_status` / `validation_freshness_status`
`current`, `stale`, `unverifiable`, `not_applicable`.
### 4.11 `closure_review.status`
`not_run`, `pass`, `revise`, `blocked`. This applies the existing review
verdict namespace to terminal evidence; it is not a delivery status and never
authorizes merge, deploy, or another external action.
There is no combined `judge_or_qa_status` field. `judge_verdict` and
`qa_status` are always separate fields (Section 8).
## 5. Execution-record identity and versioning
Minimal top-level structure (full contract: `schemas/autonomous_execution_record.schema.json`):
```yaml
schema_version: "2.0.0"  # current, closure-required record
standard_version: "2.0.0"
execution_id:
parent_execution_id:
project:
project_extension:
execution_mode:
risk_mode:
source_revision:
created_at:
updated_at:
execution_state:
requirements:
defects:
iterations:
validation_runs:
artifacts:
acceptance_scopes:
overall_delivery:
qa_status:
judge_verdict:
authority_status:
merge_status:
production_status:
rollback:
external_actions:
handoffs:
continuation:
closure_review:
final_report:
```
### 5.1 Required identity fields
`schema_version`, `standard_version`, `execution_id`, `project`,
`execution_mode`, `risk_mode`, `execution_state`, `created_at`, `updated_at`.
### 5.2 Parent execution
Root execution: `parent_execution_id: null`.
Child or continued execution: `parent_execution_id: "exec-..."`.
### 5.3 ID format
Recommended prefixes: `exec-`, `req-`, `def-`, `iter-`, `val-`, `art-`,
`ev-`, `handoff-`, `action-`.
Minimum requirements: lowercase; stable within the execution; unique within
its namespace; never reused after a record is deleted. A global UUID
infrastructure is not required for v1.
Example: `execution_id: "exec-aios-aes-v1-001"`, `requirement_id: "req-001"`,
`defect_id: "def-001"`, `iteration_id: "iter-001"`, `artifact_id: "art-001"`,
`evidence_id: "ev-001"`.
### 5.4 Compatibility and migration
New records must validate against the current v2 schema. It requires
`schema_version` and `standard_version` to be `2.0.0`, plus a
`closure_review` object. A successful v2 terminal record must carry a passed
Closure Review; the advisory semantic validator enforces the cross-field
conditions. Existing v1 evidence validates only against the explicitly named
historical schema and is read-only: do not rewrite accepted evidence solely to
add closure data. A v1 path is never a new-record intake path.
### 5.5 Continuation envelope for Invoke AI-OS
`continuation` is optional for ordinary AES records. Once `Invoke AI-OS`
orchestration begins, it is required and is the canonical durable continuation
state for that execution. It contains the original goal and acceptance
criteria, resolved owner, resume stage, stable `record_ref`, scope and routing
references, source revision, and state hashes. It does not create a second
state machine or override the record's requirements, defects, authority, or
terminal fields.
The record referenced by `record_ref` is the source of truth. Session context,
handoffs, and any ignored local pointer are derived views only. A local pointer
may contain only an execution ID and record reference, may be introduced only
after a behavioral test establishes a need, and is never required for a cold
entry.
Warm resume is permitted only after checking that the continuation envelope is
present and valid and that the original goal boundary, acceptance criteria,
resolved owner, relevant scope, authority, canonical routing state, and source
revision remain compatible. An unchanged source revision alone is insufficient.
### 5.6 Bounded multi-owner continuation control plane
The optional continuation control plane is defined in
`AUTONOMOUS_EXECUTION_CONTINUATION_CONTROL_PLANE_CONTRACT.md`.  It adds an
auditable route trace, acceptance progress, and independent continuation
guards without creating a parallel state machine or changing the existing
status namespaces.  Its guard thresholds are named parameters, not canonical
numeric defaults; the stricter applicable corrective-loop limit still wins.
### 5.7 Authority provenance for transformed context
`authority_status` reports the execution's owner-approval state; it is not a
claim-level provenance label. When an active `Invoke AI-OS` execution carries
a decision-relevant claim through a context pack, handoff, or resume, its
`continuation.authority_provenance` and every new AES handoff preserve:
```yaml
claim_text:
authority_class:       # source_fact | owner_instruction | accepted_policy |
                        # observed_execution_evidence | candidate_research |
                        # hypothesis_recommendation
source_refs: []
action_eligibility:    # eligible | not_eligible | owner_decision_required
```
The same text may legitimately have different action eligibility because its
authority class differs. `candidate_research` and `hypothesis_recommendation`
must be `not_eligible`; they can inform review or evidence collection but
never authorize acceptance, policy change, or execution. `source_fact` and
`observed_execution_evidence` are evidence, not authority. `eligible` is
permitted only for an in-scope `owner_instruction` or `accepted_policy` and
never replaces an external authority gate. Source references are retained; a
summary, confidence label, or generic evidence reference is not a substitute.
## 6. Source-revision contract
```yaml
source_revision:
  revision_type:        # git_commit | git_tree | content_manifest | iteration_reference
  baseline_revision:
  final_revision:
  content_manifest:
  final_iteration_id:
```
For uncommitted working state, prefer a git tree reference, a content hash
manifest, or a deterministic iteration reference over a bare timestamp. A
timestamp alone is never sufficient freshness evidence.
## 7. State machine
```text
initialized -> scoped -> executing -> validating
```
If mandatory checks pass: `validating -> requirements traceability -> Closure
Review -> completed`.
If a correctable defect is found: `validating -> correcting -> revalidating`.
After a successful re-check: `revalidating -> requirements traceability ->
Closure Review -> completed`.
On a hard blocker or inability to continue, from any non-terminal state:
`any non-terminal state -> stopped`.
Terminal reasons (when `execution_state: stopped`): `hard_blocker`,
`iteration_limit_reached`, `repeated_defect_limit_reached`,
`conflicting_acceptance`, `validation_unavailable`,
`scope_boundary_violation`, `required_external_action_not_authorized`,
`closure_iteration_limit_reached`.
`required_external_action_not_authorized` applies only when a specific
external action is part of the mandatory objective and the objective cannot
be completed without it. Waiting for owner review after a successfully
completed local implementation does **not** move execution to `stopped`.
The correct terminal shape for that case is:
```yaml
execution_state: completed
overall_delivery: pass
authority_status: owner_review_pending
merge_status: owner_review_pending
production_status: not_authorized
```
## 8. Requirements traceability
Each mandatory requirement is a record:
```yaml
requirement_id:
requirement:
source:
mandatory:
implementation_locations:
evidence_refs:
validation_refs:
status:            # current status only, see 8.1
status_history:
gap:
corrective_action_refs:
```
### 8.1 Status model
One current field, `status`. History is kept separately:
```yaml
status_history:
  - status:
    iteration_id:
    recorded_at:
    evidence_refs:
```
There is no separate duplicating `final_status` field. At terminal
execution, the current `status` value is the final one.
### 8.2 Rules
1. `requirement_id` is unique within the execution.
2. Every mandatory requirement must end in `passed`, `blocked`, or
   `not_applicable` with a stated reason.
3. `not_applicable` requires a reason.
4. `passed` requires evidence, or an explanation of why no change was
   required.
5. A mandatory requirement with `status: failed` forbids
   `overall_delivery: pass`.
6. A requirement that went through correction must reference the iteration
   and the repeated validation.
7. A handoff must not drop requirement IDs.
8. Requirement scope may not be widened inside a corrective loop without a
   new, explicit scope decision.
## 9. Defects and the corrective loop
### 9.1 Defect record
```yaml
defect_id:
requirement_id:
detected_in_iteration:
detected_by:
classification:
subtype:
severity:
description:
evidence_refs:
correction_eligible:
required_authority:
remediation_owner:
corrective_action_refs:
affected_scope:
required_validation_refs:
status:
status_history:
resolved_in_iteration:
resolution_evidence_refs:
```
### 9.2 Classification
`implementation`, `validation`, `test`, `artifact`, `traceability`,
`contract`, `governance`, `authority`, `external_dependency`. An extension
may add a `subtype`, but must not change the classification semantics.
### 9.3 Severity
`recoverable`, `needs_check`, `hard_blocker` — compatible with the existing
Codex failure-classification model in
`ChatGPT/[Codex]/Knowledge/FAILURE_MODES.md`.
### 9.4 Defect status
`open`, `correcting`, `resolved`, `accepted_risk`, `blocked`.
`accepted_risk` requires `accepted_by`, `authority_evidence_ref`,
`acceptance_reason`, `accepted_at`. An executor may not self-accept as
`accepted_risk`: a security defect, a business-rule defect, a formula or
metric defect, a schema incompatibility, a public-API incompatibility, a
failed mandatory check, a production risk, or a source-mutation risk.
### 9.5 Corrective-loop contract
Mandatory sequence:
```text
validate -> register defect -> classify defect
-> determine correction eligibility and authority
-> apply minimal correction -> rerun affected checks
-> run required regression scope -> update defect evidence
-> update requirement evidence -> re-evaluate affected acceptance scopes
```
The executor must not: fix a defect without registering it; close a defect
without resolution evidence; reuse a stale test result after changing the
affected scope; widen scope for convenience of the fix; delete or weaken
validation; change business logic to obtain a `pass`; or use `blocked`
instead of an available, permitted local correction.
### 9.5.1 Trace-grounded repair eligibility
A failed execution is evidence of an observed defect, not by itself evidence
that the harness, prompt, skill, or workflow caused that defect. Before a
repair candidate changes one of those control surfaces, record a bounded
attribution statement that names the proposed target, the failed trace or
reproducible trajectory, the evidence that connects the target to the
failure, and the plausible alternatives considered.
`harness/workflow repair eligible: true` requires at least one of: a
reproducible failed step localized to the target; a paired or counterfactual
replay that distinguishes the target; a deterministic contract violation in
the target; or an isolated target change that removes the failure without
widening scope. The statement must also name the affected scope, reversible
minimal repair, and required revalidation/regression checks.
An invalid input, unavailable external dependency, missing authority, or
unidentified competing cause makes a harness/workflow repair `ineligible` or
`revise`, as applicable. Keep attribution status `uncertain` when the trace
cannot identify a cause; do not select a convenient repair. A candidate repair
that introduces a hard regression is rejected by the existing regression gate.
This gate is evidence discipline before a human-authorized, bounded repair;
it creates no autonomous diagnosis, self-modification, acceptance, or
unattended change authority.
### 9.6 Iteration model
```yaml
iteration_id:
iteration_number:
iteration_type:      # full_iteration | operation_retry
started_at:
completed_at:
trigger:
requirements_affected:
defects_addressed:
changes:
validation_refs:
result:
```
A **full iteration** starts when a substantive change to source,
configuration, contract, generated-source input, an analytical source
layer, or a prompt/workflow contract has been made after validation and a
new acceptance evaluation is required.
An **operation retry** repeats a single operation without changing
requirement scope or source state — e.g. a transient file lock, a transient
local command failure, a repeated parsing operation, or a repeated check
after a recoverable environment issue.
Default canonical envelope (a ceiling, not a standing permission):
```yaml
max_full_iterations: 5
max_retries_per_operation: 3
max_same_defect_recurrence: 2
```
Effective limit = `minimum(canonical limit, project-extension limit,
task-package limit, applicable safety limit)`.
### 9.7 Codex compatibility (hard constraint)
Until a separate owner decision changes it, `[Codex]` keeps its stricter
existing policy:
```yaml
max_corrective_fixes_per_failed_check: 1
```
If the same validation target fails again after one minimal correction
attempt: stop further file-changing corrections for that target, record the
evidence, report the residual risk, and set an honest acceptance status. This
standard's canonical envelope (Section 9.6) never widens this policy. A
distinct defect is eligible for separate handling only when independently
evidenced against a different affected requirement or independently failing
validation target; changing only `defect_id`, subtype, classification, label,
wording, or representation never resets the one-fix budget.
For the prohibition on agentic workflows, a bounded, reversible, in-repo
corrective loop operating under an AES record, fixed authority and scope,
validation, stop conditions, rollback, and human acceptance is supervised
execution. This narrow classification neither permits autonomous agents or
generic agentic workflows nor expands execution authority.
## 10. Acceptance model
```yaml
acceptance_scopes: {}   # object, keyed by scope name
overall_delivery: pass  # scalar
```
Example:
```yaml
acceptance_scopes:
  requirements_traceability:
    status: pass
    required_checks: []
    checks_run: []
    evidence_refs: []
    open_defect_ids: []
    limitations: []
  implementation:
    status: pass
    required_checks: []
    checks_run: []
    evidence_refs: []
    open_defect_ids: []
    limitations: []
overall_delivery: pass
```
### 10.1 Mandatory acceptance scopes
`requirements_traceability`, `implementation`, `tests`, `validation`,
`output_artifacts`, `corrective_loop`, `rollback_readiness`. Each scope
carries `status`, `required_checks`, `checks_run`, `evidence_refs`,
`open_defect_ids`, `limitations`.
### 10.2 Overall-delivery rule
`overall_delivery: pass` is permitted only when: all mandatory requirements
are resolved; mandatory scopes are `pass` or a justified `not_applicable`;
no open `recoverable` or `needs_check` defects remain; no hard blockers
remain; validation evidence matches the final source state; mandatory
artifacts are current; rollback readiness has been evaluated; and external
authority statuses are reported separately. Waiting for owner review does
not pull `overall_delivery` down to `fail`.
### 10.3 Closure Review (v1.1)
Before a closure-aware record can successfully terminate, build a compact
`closure_context` from the original goal/task, agreed scope, constraints,
acceptance criteria, material invariants, final revision/state references,
requirements traceability, latest test/validation/artifact evidence,
limitations, residual risks, rollback and external-authority status, and
input/state hashes. The full transcript is not required.
Review the original goal rather than the last fix list. State the general
invariant behind known defects and inspect applicable decision-bearing inputs,
transformations, aggregation points, outputs, and material trust boundaries.
Preserve uncertainty: `UNKNOWN != NOT_REPORTED`, `PARSE_FAILED != NOT_REPORTED`,
`PROBABLE != CONFIRMED`, `NOT_RUN != PASS`, and `HYPOTHESIS != OBSERVED`.
Mutation evidence is observed only when the mutation was applied, validation
ran, and its result was recorded.
For `material`, `complex`, or high-risk work, use existing execution/risk modes
for a bounded adversarial attempt to reject acceptance: boundary and
contradictory states, missing evidence, invalid transitions, aggregation loss,
unsupported defaults, routing/requirement omissions, status inflation, forged
intermediate state, and stale downstream artifacts are applicable classes.
Lightweight reversible work may use a proportionate review.
If an observable in-scope gap affects acceptance, is technically correctable,
needs no new owner/business/policy decision, and can be fixed with available
authority/tools, register it and return to `correcting`. Do not relabel it a
limitation, residual risk, or future improvement merely to terminate. Scope or
owner-policy changes follow existing blocked/stopped authority mapping.
`max_closure_corrective_iterations: 2` is a ceiling separate from normal full
iterations. Effective limit is the minimum of canonical, extension,
task-package, and stricter applicable policy. A counted closure iteration
changes state for a newly found correctable acceptance defect and completes
rerun/revalidation. It never widens `[Codex]`
`max_corrective_fixes_per_failed_check: 1`. After a closure correction,
affected validations and artifacts are stale until refreshed under Section 11.
## 11. Validation runs and freshness
### 11.1 Validation-run record
```yaml
validation_id:
validation_type:   # unit | integration | contract | smoke | golden | data_quality | artifact | schema | docs_consistency | judge | manual_review
command_or_method:
validated_revision:
covered_paths:
covered_requirement_ids:
started_at:
completed_at:
result:
evidence_refs:
freshness_status:
limitations:
```
### 11.2 Validation freshness
`freshness_status: current` is permitted when
`validation.validated_revision == source_revision.final_revision`, or when a
documented affected-scope analysis proves that changes made after the
validation run did not touch the covered paths and requirements. In the
latter case the record must also carry `freshness_justification` and
`unaffected_paths_evidence`. A check run before the last relevant change is
`stale`.
### 11.3 Artifact-freshness record
```yaml
artifact_id:
path:
artifact_type:
mandatory:
source_inputs:
  - path:
    content_hash:
    last_changed_iteration:
generation_method:
generated_from_revision:
generated_in_iteration:
generated_at:
validation_refs:
freshness_status:
freshness_evidence_refs:
```
A mandatory artifact is `current` when `generated_from_revision` matches the
final relevant source state, the hashes of all mandatory source inputs
match, artifact validation ran on the final version, and no relevant source
change occurred after generation. Timestamp is auxiliary evidence only. An
artifact is `stale` when a source input changed after generation, a content
hash mismatches, the artifact predates the last corrective iteration, or its
final validation belongs to a previous version. `overall_delivery: pass` is
forbidden while a mandatory artifact is stale — this matters most for XLSX,
DOCX, PDF, PPTX, marts, charts, memos, and other generated bundles.
## 12. Validation responsibility matrix
The original Phase 1 matrix separated deterministic structural checks from
future semantic enforcement. The repository now has a scoped, read-only
advisory semantic validator (`scripts/validate_autonomous_execution_record.py`)
for its documented subset; it is not CI or runtime enforcement.
| Property checked | Structural mechanism | Current semantic coverage |
| --- | --- | --- |
| JSON syntax | JSON parser | unchanged |
| Required fields | JSON Schema | unchanged |
| Field types | JSON Schema | unchanged |
| Enum values | JSON Schema | unchanged |
| ID string format | JSON Schema pattern | unchanged |
| Nested record shape | JSON Schema | unchanged |
| Duplicate IDs by property | acceptance-case specification | SEM-002 |
| Mandatory failed requirement with overall pass | normative rule and case specification | SEM-001 |
| Open defect with overall pass | normative rule and case specification | SEM-003 |
| Artifact revision mismatch | normative rule and pilot | SEM-004 |
| Test revision mismatch | normative rule and pilot | SEM-005 |
| Iteration-limit enforcement | normative rule and pilot | SEM-006/010 |
| Allowed-file scope | exact scope manifest and git diff review | repository validator |
| Extension authority expansion | contract and Judge review | deterministic policy validator where feasible |
| Canonical-content duplication | docs consistency and Judge review | optional repository consistency check |
| Business-rule preservation | project-specific checks | project-specific enforcement |
| Merge/deploy authority | explicit fields and owner review | external platform gates |
The advisory validator covers only SEM-001…014 and is not evidence of CI,
runtime enforcement, owner approval, merge, deploy, or production
authorization. See
`docs/autonomous_execution/AUTONOMOUS_EXECUTION_ACCEPTANCE_CASES.md` for the
full structural and semantic case list.
## 13. External authority separation
An execution record always reports these fields separately, and never
collapses one into another:
```yaml
overall_delivery:
qa_status:
judge_verdict:
authority_status:
merge_status:
production_status:
```
Forbidden implicit conversions: judge `pass` -> owner approved;
implementation `pass` -> merge ready; merge ready -> merged; merged ->
production authorized; not merged -> failed; owner review pending ->
blocked.
### 13.1 External-action record
```yaml
action_id:
action_type:   # provider_api_call | source_mutation | merge | deploy | production_promotion | migration | destructive_operation
required_for_objective:
requested:
required_authority:
authority_evidence_ref:
status:
executed_at:
result_evidence_ref:
```
An external action without explicit authority is not executed, is not
retried automatically, is not treated as authorized just because local
configuration exists, and does not turn a successful local implementation
into `fail` when the action was not part of the mandatory objective.
### 13.2 Effect-boundary invariant
Every side-effecting `external_action` follows this bounded sequence:
```text
PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY
```
The required `effect_boundary.preview` records the target resource, intended
mutation, affected scope, required authority, reversibility/rollback note,
expected verification, and an intent fingerprint. A preview is information,
not authorization. Commit is forbidden without an authority evidence reference
and recorded authority check. A material change between the preview fingerprint
and commit intent requires an authority recheck before commit. After commit,
verification must pass with evidence before successful completion can be
reported; a failed or blocked verification is not a successful external action.
This contract applies only to declared side-effect types in Section 13.1. It
does not add a runtime approval service, auto-approval, or a preview burden to
read-only actions.
## 14. Rollback readiness
```yaml
rollback:
  strategy:
  scope:
  command_or_procedure:
  prerequisites:
  data_loss_risk:
  validation_after_rollback:
  status:   # ready | partial | unavailable | not_applicable
```
For docs/schema Phase 1 work, acceptable strategies are a scoped
`git restore`, closing the PR without merging, or reverting a single commit
after merge. `git reset --hard` is never a default rollback strategy.
## 15. Cross-project handoff persistence
```yaml
handoff_id:
execution_id:
parent_execution_id:
from:
to:
requirement_ids:
open_defect_ids:
current_iteration_id:
evidence_refs:
acceptance_snapshot:
qa_status:
judge_verdict:
authority_status:
authority_provenance:
next_owner:
```
A new execution ID is permitted only with an explicit parent/child link.
### 15.1 Reverse handoff (Judge/QA back to executor)
```yaml
handoff_id:
execution_id:
from:
to:
judge_verdict:
qa_status:
defects_added:
requirements_affected:
required_corrections:
evidence_refs:
next_owner:
```
A handoff must never drop: execution ID, requirement IDs, defect IDs,
iteration ID, evidence references, authority status, or authority provenance
for a decision-relevant claim. A new AES handoff carries an
`authority_provenance` object even when its `claims` list is empty.
### 15.2 Continuation handoff rule
For an active `Invoke AI-OS` execution, a local or cross-project handoff is an
intermediate stage, never a lifecycle terminator. Return its evidence to the
same AES execution, update `continuation.resume_stage`, validate the affected
requirements or defects, and compare the result with the original acceptance
criteria before selecting `completed`, `stopped`, or the next authorized stage.
## 16. Risk-scaled modes
One standard; only evidence depth changes.
### 16.1 Lightweight
For simple docs-only changes, local reversible config changes, a single
scope, low risk. Minimum: execution ID, requirements, relevant checks, a
minimal defect record, acceptance scopes, rollback, authority statuses.
### 16.2 Standard
For ordinary repository tasks, code/config changes, generated artifacts,
multiple requirements. Minimum: full execution record, requirements,
defects, iterations, validation runs, artifact manifest, acceptance scopes,
rollback.
This Phase 1 package itself was executed at Standard risk mode (docs and
schema, several requirements, no runtime execution record required as a
bookkeeping artifact — see `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md`).
### 16.3 Full
For Analytics, high-risk tasks, production-adjacent work, cross-project
workflows, multiple artifact layers. Minimum: full traceability, several QA
layers, detailed defects, partial scope acceptance, cross-project handoff
preservation, an explicit authority map, full artifact lineage.
## 17. Non-goals and enforcement boundary
Forbidden in this task: a runtime service; an execution database; a
blocking CI gate; changes to `.github/workflows/*`; a
web UI; a vector DB; embeddings; an agent orchestration platform; automatic
project invocation; automatic issue creation or closing; automatic PR
creation as a runtime behavior of the standard; automatic PR approval or
merge; automatic deploy; routing-architecture changes; merging projects;
rewriting all Project Instructions; moving project methodology into the
canonical standard; a separate file per runtime defect; changes to business
formulas, metrics, financial controls, or provider/API routing; real
external API calls; source-data mutation; or changes to existing product
schemas or public APIs.
## 18. PR semantics
The implementation PR for adopting AES (or any AES-tracked change) is only a
delivery mechanism for a repository change.
```text
The implementation PR is a delivery mechanism.
The Autonomous Execution Standard does not automatically create,
approve, merge or deploy pull requests.
```
## 19. Adoption phases
See `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md` for the full phase list.
Summary: Phase 1 (historical normative package) -> Phase 2 (Codex pilot,
separate issue/PR) -> Phase 3 (artifact pilot) -> Phase 4 (Analytics pilot)
-> Phase 5 (cross-project pilot) -> scoped advisory semantic validation
(delivered) -> any blocking enforcement (requires a separate owner decision).
## 20. Next owner
```text
[Codex] Phase 1 implementation
-> [Thinking]/Judge architecture review
-> owner acceptance
-> separate Codex pilot task
```
Completion of this Phase 1 package does not authorize: pilot execution,
semantic enforcement, CI blocking, merge, deploy, or production adoption.

## From: `ChatGPT/[Codex]/Knowledge/CODEX_02_EXECUTION_AUTONOMY_REPORTING_BUNDLE_SEMANTICS.md`

# Migrated Bundle Semantics
Canonical source created during Issue #285 provenance migration.
Legacy bundle provenance: `ChatGPT/[Codex]/Knowledge_Bundles/CODEX_02_EXECUTION_AUTONOMY_REPORTING.md`.
## Legacy section: `ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md`
For normal bounded repo work, use `Goal Mode Contract` in `GOAL_MODE.md` as the named reusable standard for autonomy, execution order, forbidden actions, reporting, PR/merge-gate posture, and no-deletion-without-quarantine rules.
If the same validation target still fails, the one-fix budget is exhausted for
that target and the independently evidenced defect it represents. Stop further
file-changing corrections for that target and report:
## Legacy section: `ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`
## Autonomous Execution Standard
Execution in `[Codex]` now also follows the canonical Autonomous Execution
Standard defined in `AUTONOMOUS_EXECUTION_STANDARD.md` at the repo root
(canonical owner: `[AI OS]`). It sits above `AUTONOMY_POLICY.md`,
`CODEX_LONG_RUN_PLAYBOOK.md`, and `EXECUTION_REPORTING_RULES.md` as a shared
loop — requirements, execution, validation, defect registration, corrective
action, revalidation, and scope acceptance — without replacing any of them or
the merge policy in `GOAL_MODE.md`. The `[Codex]` AES extension at
`docs/autonomous_execution/extensions/CODEX_EXTENSION.md` adds only
Codex-specific evidence, validation, acceptance, freshness, and authority
detail; it does not expand authority or numeric limits. New v2 Closure Review
rechecks repository trust boundaries, regression coverage, diff/freshness, and
rollback; its ceiling never widens `max_corrective_fixes_per_failed_check: 1`.
For an `Invoke AI-OS` continuation, the canonical AES envelope preserves the
original goal, acceptance criteria, resolved owner, stage, and freshness state;
it does not turn a local completed step into terminal acceptance.
Once routing resolves a material decision or deliverable owner, `[Codex]`
keeps that boundary: it may execute a bounded handoff and preserve its
evidence, contradictions, constraints, acceptance, and first safe step, but it
must not silently replace the resolved owner's judgment.
