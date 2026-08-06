# `[Analytics]` Autonomous Execution Extension

Status: Phase 1-scope deliverable, authored during adoption cleanup ahead of
owner review of the Phase 1-6 PR stack.

Companion to: `AUTONOMOUS_EXECUTION_STANDARD.md` (canonical, `[AI OS]`-owned)
and `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` (the generic interface this
document implements, Section 5.2 of that contract).

This document adds `[Analytics]`-domain specifics to the canonical
Autonomous Execution Standard. It does not restate the state machine,
defect model, schema, or precedence rules defined there — it references
them by section number. Where this document and the canonical standard
disagree on a limit, the stricter one applies
(`AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 4).

Source vocabulary for everything below: `ChatGPT/[Analytics]/Knowledge/`
(`ANALYTICS_WORKFLOW.md`, `DATA_CONTRACTS.md`, `MARTS_DESIGN.md`,
`ACCEPTANCE_CRITERIA.md`, `GOVERNANCE_AND_ANTI_PATTERNS.md`) and the
compact bundle `ChatGPT/[Analytics]/Knowledge_Bundles/
ANALYTICS_02_DATA_CONTRACTS_AND_MARTS.md`. This extension does not invent
new Analytics business rules; it maps the existing, live Analytics
methodology onto the AES extension shape.

## 1. Extension declaration

```yaml
extension_id: aes-ext-analytics-v1
project: "[Analytics]"
standard_version: "1.0.0"
applies_to:
  - execution records produced by [Analytics] work (data contract, RAW,
    stage, mart, analysis, chart, memo, QA, or cross-project handoff
    deliverables)
domain_defect_subtypes:
  - data_contract_missing        # under classification: traceability
  - grain_undefined              # under classification: traceability
  - dq_fail                      # under classification: validation
  - unreconciled_totals          # under classification: validation
  - metric_formula_undefined     # under classification: implementation
  - metric_formula_changed_silently  # under classification: governance
  - mart_lineage_violation       # under classification: implementation
  - claim_without_evidence       # under classification: traceability
  - unsupported_management_conclusion  # under classification: governance
required_evidence:
  - data_contract_ref            # per ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md
  - stage_main_full_ref
  - mart_main_full_ref
  - reconciliation_result_ref
  - qa_checklist_ref             # per ChatGPT/[Analytics]/Knowledge/ACCEPTANCE_CRITERIA.md
  - claim_evidence_map_ref       # memo sentence -> metric/table/mart/period
required_validation:
  - stage_main_full: pass/fail/blocked/not_applicable
  - mart_main_full: pass/fail/blocked/not_applicable
  - mart_main_tz_or_compact: pass/fail/blocked/not_applicable
  - slices_from_mart_main_full: pass/fail/blocked/not_applicable
  - reconciliation: pass/fail/blocked/not_applicable
acceptance_scope_additions:
  - analytics_data_contract      # data contract exists or missing fields explicit
  - analytics_lineage            # RAW -> stage_main_full -> mart_main_full -> slices honored
  - analytics_reconciliation     # totals reconciled or explicitly blocked with reason
  - analytics_claim_evidence     # memo sentences traceable to metric/table/mart/period
retry_limit_overrides: {}        # none; canonical envelope (Section 9.6) applies unchanged
hard_blocker_additions:
  - unreconciled totals with no documented reason
  - grain undefined at mart_main_full
  - metric formula changed without a recorded governance defect
  - management conclusion published while a GOVERNANCE_AND_ANTI_PATTERNS.md
    "Blockers" condition is open (data contract missing, grain missing,
    DQ Fail, unreconciled totals, missing metric formula, unsupported
    cause, risk without basis, action without owner/due date, no main
    mart for a mart-based conclusion)
authority_requirements:
  - this extension grants no merge, deploy, or production authority
    (per AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md Section 3); an
    Analytics `accepted: yes` decision is a domain content-acceptance
    decision only, not an authority decision
freshness_requirements:
  - mart_main_full and stage_main_full must reflect the same data
    refresh/load timestamp cited in the data contract
  - a validation-freshness check (Section 11.2 of the canonical standard)
    is required before `accepted: yes` may be recorded
```

## 2. Domain vocabulary mapping

This extension reuses the existing, live Analytics vocabulary as-is; it
does not redefine it.

| Analytics concept | Source | AES surface |
| --- | --- | --- |
| `entity` / `grain` / `keys` / `period` / `currency` | `DATA_CONTRACTS.md` | `required_evidence.data_contract_ref`; feeds `analytics_data_contract` |
| RAW / STAGE / MART lineage | `MARTS_DESIGN.md` | `required_evidence.stage_main_full_ref`, `mart_main_full_ref`; feeds `analytics_lineage` |
| Reconciliation | `ANALYTICAL_TECHNIQUES.md`, `ACCEPTANCE_CRITERIA.md` "Blocked status" | `required_evidence.reconciliation_result_ref`; feeds `analytics_reconciliation` |
| Formulas | `MARTS_DESIGN.md` "Mart checklist" | tracked as `metric_formula_undefined` / `metric_formula_changed_silently` defect subtypes |
| Memo / claim-evidence mapping | `ANALYTICS_WORKFLOW.md` Step 11, `GOVERNANCE_AND_ANTI_PATTERNS.md` evidence labels | `required_evidence.claim_evidence_map_ref`; feeds `analytics_claim_evidence` |
| Management-conclusion blockers | `GOVERNANCE_AND_ANTI_PATTERNS.md` "Blockers" | `hard_blocker_additions` |
| `accepted: yes/no` | `ACCEPTANCE_CRITERIA.md` "Acceptance status" | domain content-acceptance signal; see Section 3 below and `docs/AUTONOMOUS_EXECUTION_STATUS_MAPPING.md` Section 4 for how (and whether) it may inform `overall_delivery` |

## 3. `accepted: yes/no` and `overall_delivery`

The normative rule for how the domain-level Analytics `accepted: yes/no`
field may or may not be reflected in the canonical `overall_delivery`
field is defined in a single place, to avoid two competing mapping
statements: `docs/AUTONOMOUS_EXECUTION_STATUS_MAPPING.md`, Section 4. That
document's rule is authoritative; this extension does not restate or
duplicate it, only points to it.

Summary for orientation only (not a substitute for the mapping doc): an
Analytics `accepted: yes` is necessary but never sufficient by itself for
`overall_delivery: pass`; it also requires the mandatory canonical
acceptance scopes (`AUTONOMOUS_EXECUTION_STANDARD.md` Section 10.1) and the
`acceptance_scope_additions` in Section 1 above to be satisfied.
`accepted: no` always blocks `overall_delivery: pass`.

## 4. What this extension does not do

Consistent with `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 3,
this document does not: expand external authority (no merge/deploy/
production permission is granted here); weaken any canonical hard blocker;
cancel or shortcut requirements traceability; or copy the canonical
standard's state machine, defect model, or schema. It also does not
introduce new Analytics business rules beyond what
`ChatGPT/[Analytics]/Knowledge/` already defines — where this document
lists a defect subtype, blocker, or evidence item, it is naming an
existing Analytics rule in AES terms, not creating a new one.
