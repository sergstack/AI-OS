# `[Codex]` Autonomous Execution Extension

Companion to `docs/standards/AUTONOMOUS_EXECUTION_STANDARD.md` (canonical `[AI OS]` owner)
and `docs/standards/AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`. This extension maps existing
Codex repository-execution rules onto the AES extension shape. It does not
duplicate the canonical state machine, record schema, numeric limits, or
authority model.

## 1. Extension declaration

```yaml
extension_id: aes-ext-codex-v1
project: "[Codex]"
standard_version: "2.0.0"
applies_to:
  - bounded in-repository implementation, documentation, configuration, test,
    bugfix, refactor, and release-preparation work performed by [Codex]
domain_defect_subtypes:
  - changed_file_outside_allowed_scope       # traceability
  - focused_validation_failed                # validation
  - regression_validation_failed             # test
  - validation_evidence_stale                # validation
  - rollback_readiness_missing               # traceability
  - unauthorized_external_action_requested   # authority
required_evidence:
  - bounded_scope_ref
  - changed_file_diff_ref
  - focused_validation_output_ref
  - final_revision_ref
  - rollback_ref
required_validation:
  - changed_file_scope_review: pass/fail/blocked/not_applicable
  - focused_affected_check: pass/fail/blocked/not_applicable
  - relevant_regression_check: pass/fail/blocked/not_applicable
  - final_diff_review: pass/fail/blocked/not_applicable
acceptance_scope_additions:
  - codex_changed_file_scope
  - codex_validation_evidence
  - codex_external_authority_separation
retry_limit_overrides: {}                    # canonical limits apply unchanged
hard_blocker_additions: []                   # existing Codex policy remains authoritative
authority_requirements:
  - this extension grants no merge, deploy, production, provider/API,
    source-mutation, destructive-operation, schema, output-contract, business,
    formula, metric, or financial-control authority
freshness_requirements:
  - focused and regression validation evidence must cover the final affected
    revision, or be marked stale and rerun where required
  - final diff review must cover the same revision reported for acceptance
```

## 2. Codex corrective-loop constraint

`ChatGPT/[Codex]/Knowledge/AUTONOMY_POLICY.md` and AES Section 9.7 set the
stricter Codex rule: one eligible minimal file-changing correction per failed
validation target. If that target still fails, its budget is exhausted. A
separate correction is permitted only for an independently evidenced,
in-scope eligible defect with a different affected requirement or validation
target; a renamed or reclassified representation never creates a new budget.

All canonical AES iteration, recurrence, Closure Review, stop-condition, and
rollback requirements remain unchanged.

## 3. Evidence, validation, and acceptance

The required evidence above is drawn from existing Codex rules in
`ChatGPT/[Codex]/Knowledge/EXECUTION_REPORTING_RULES.md`,
`ACCEPTANCE_CRITERIA.md`, and `AUTONOMY_POLICY.md`. It records bounded scope,
the actual diff, focused and relevant regression validation, final revision,
and rollback readiness. Narrative labels such as `DONE`, `PREPARED`, `NOT RUN`,
and `NEEDS VERIFICATION` qualify evidence claims only; they do not replace any
AES status or satisfy a hard blocker.

## 4. Authority boundary

This extension adds no hard-blocker exceptions and no authority. Canonical
Codex hard blockers remain in `AUTONOMY_POLICY.md`; merge, deploy, production,
and other external actions remain subject to their existing owner and GitHub
gates. A bounded reversible in-repository corrective loop is supervised
execution only under the conditions in AES Section 9.7; this is not permission
for autonomous agents, generic agentic workflows, autonomous retrieval,
daemon/background execution, self-approval, or self-expanding authority.
