# `[Codex]` Autonomous Execution Extension

Companion to `AUTONOMOUS_EXECUTION_STANDARD.md` and
`AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md`. This extension adds only
Codex-specific execution detail; it inherits all canonical limits and does
not duplicate the AES state machine, defect model, or schema.

## 1. Extension declaration

```yaml
extension_id: aes-ext-codex-v2
project: "[Codex]"
standard_version: "2.0.0"
applies_to:
  - bounded repository implementation, docs/workflow, configuration, test,
    and corrective-loop work performed by [Codex]
domain_defect_subtypes:
  - allowed_scope_violation          # classification: governance
  - missing_change_evidence          # classification: traceability
  - validation_target_failure        # classification: validation
  - stale_validation_after_change    # classification: validation
  - regression_check_failure         # classification: test
  - rollback_not_ready               # classification: governance
  - intake_assumption_not_recorded   # classification: traceability
required_evidence:
  - allowed_file_scope_ref
  - changed_file_diff_ref
  - validation_target_ref
  - rerun_result_ref_after_correction
  - rollback_ref
required_validation:
  - smallest relevant check: pass/fail/blocked/not_applicable
  - affected-scope rerun after a correction: pass/fail/blocked/not_applicable
  - diff review against allowed scope: pass/fail/blocked
acceptance_scope_additions:
  - codex_scope_control
  - codex_validation_freshness
  - codex_change_evidence
retry_limit_overrides: {}            # canonical limits, including the stricter Codex one-fix rule, apply unchanged
hard_blocker_additions:
  - a requested correction would cross allowed-file scope without an explicit scope decision
  - a required validation target cannot be meaningfully identified
authority_requirements:
  - this extension grants no authority for merge, deploy, production, provider/API execution, source mutation, or destructive operations
```

## 2. Corrective-loop boundary

The Codex one-fix rule in AES Section 9.7 is per failed validation target and
independently evidenced defect. Once its correction has been attempted, no
renaming or reclassification may obtain another file-changing attempt for the
same target. An independently failing in-scope target may continue only under
the canonical iteration, recurrence, authority, scope, and hard-blocker
limits.

## 3. Acceptance and authority

`codex_scope_control` confirms changed files remain inside the recorded scope;
`codex_validation_freshness` confirms final validation matches the affected
revision; and `codex_change_evidence` links changes and reruns to requirements
and defects. This extension does not make a PR mergeable, authorize external
actions, or treat human acceptance as automatic.
