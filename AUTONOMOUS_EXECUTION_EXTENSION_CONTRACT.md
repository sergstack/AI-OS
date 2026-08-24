# Autonomous Execution Extension Contract

Status: Phase 1 — normative package and declarative contract.
Companion to: `AUTONOMOUS_EXECUTION_STANDARD.md` (canonical, `[AI OS]`-owned).

This is the one generic interface that a project-specific execution
extension must implement. It is a template/contract, not a set of already
adopted per-project extensions. Writing and adopting an actual extension for
`[Codex]`, `[Analytics]`, `[LLM]`, `[Thinking]`, or `[AI OS]` is Phase 2-5
work (see `docs/AUTONOMOUS_EXECUTION_ADOPTION_PLAN.md`) and is out of scope
for this Phase 1 package.

## 1. Extension structure

```yaml
extension_id:
project:
standard_version:
applies_to:
domain_defect_subtypes:
required_evidence:
required_validation:
acceptance_scope_additions:
retry_limit_overrides:
hard_blocker_additions:
authority_requirements:
freshness_requirements:
closure_review_requirements:
```

## 2. What an extension may do

- add domain-specific defect subtypes under the canonical `classification`
  enum (Section 9.2 of the standard);
- add domain-specific checks and required evidence;
- decrease retry/iteration limits below the canonical envelope (Section 9.6
  of the standard); it may only tighten, never loosen;
- add acceptance scopes beyond the seven mandatory ones (Section 10.1 of the
  standard);
- add project-specific hard blockers.
- add domain-specific Closure Review checks, evidence, and stricter closure
  limits; it may not omit canonical goal/scope/invariant/authority review.

## 3. What an extension must not do

- cancel or omit a canonical field;
- expand external authority (merge, deploy, production, provider/API
  execution, source mutation, destructive operations remain owner/authority
  gated regardless of what an extension says);
- weaken a hard blocker defined by the canonical standard;
- authorize merge or deploy;
- cancel or shortcut requirements traceability;
- copy the entire canonical standard into the extension document. An
  extension references the canonical standard by path; it does not restate
  the state machine, defect model, or schema.

## 4. Precedence inside an extension

An extension sits between the task package and the canonical standard in
the precedence order defined in `AUTONOMOUS_EXECUTION_STANDARD.md` Section 1:

```text
... project instructions -> project-specific execution extension
-> AUTONOMOUS_EXECUTION_STANDARD.md -> supporting playbooks/templates/examples
```

Where the extension and the canonical standard disagree on a limit, the
stricter one applies.

## 5. Per-project extension expectations (guidance for Phase 2-5 authors)

These are not new files created in Phase 1. They describe what each
project's eventual extension is expected to define, so that Phase 2-5 work
has a fixed target.

### 5.1 `[Codex]` extension

Code/config/test defect subtypes; repository scope checks; changed-file
evidence; focused-test policy; regression policy; diff review; branch/PR
fields; rollback; merge-gate separation. The existing Codex one-fix policy
(`max_corrective_fixes_per_failed_check: 1`, defined in
`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md` and restated in the standard,
Section 9.7) is preserved, not re-negotiated.

### 5.2 `[Analytics]` extension

Data contract; entity; grain; keys; period; currency/unit; RAW/STAGE/MART
lineage; formulas; reconciliation; charts; memo; claim/evidence mapping;
management-conclusion blockers; data and report freshness.

### 5.3 `[LLM]` extension

Prompt contract; context contract; routing decision; output schema;
unsupported-claim defects; eval cases; regression cases; schema compliance;
evidence limits; Judge limitations.

### 5.4 `[Thinking]` extension

Alternatives; evidence quality; assumptions; unresolved contradictions;
recommendation status; Judge findings; revision of reasoning; the
distinction between a recommendation and an owner decision.

### 5.5 `[AI OS]` extension

Canonical ownership; source/derived layers; governance defects; authority
mapping; adoption status; production authorization; status compatibility;
repository/Knowledge synchronization boundary.

## 6. Where an extension lives (future decision)

Phase 1 does not fix a canonical path convention for per-project extension
documents (e.g. whether `[Codex]`'s extension lives in
`ChatGPT/[Codex]/Knowledge/` or elsewhere). That path decision belongs to
the Phase 2 pilot task for the first project that actually adopts an
extension, so it can follow that project's live Knowledge conventions
instead of being guessed here.
