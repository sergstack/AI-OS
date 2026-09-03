#!/usr/bin/env python3
"""Cross-field validation for the AIOS AutoResearch v0.2 live-batch contract
(issue #411, parent #409). Companion to
schemas/autoresearch_v02_live_batch_config.schema.json and
docs/standards/autoresearch_v02_authority_matrix.json.

Enforces the rules the schema alone cannot express: 'authorized requires a
positive budget', 'the declared transport must be one this repository has
actually audited', and the fixed shape of the authority matrix. No live
model/provider/Judge call is made anywhere in this module.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import autoresearch_validator as av  # noqa: E402  (reuse Finding/_schema_findings, not reimplemented)

SCHEMA_PATH = av.SCHEMAS / "autoresearch_v02_live_batch_config.schema.json"

# Transport candidates actually audited in docs/evidence/
# AUTORESEARCH_V02_BASELINE_TRANSPORT_AUDIT_2026-09-03.md (issue #410).
# A batch declaring any other transport_id has not been through the
# feasibility audit this contract requires before authorization.
AUDITED_TRANSPORT_IDS = {
    "playwright_mcp",
    "claude_in_chrome",
    "browser_pane_claude_browser",
    "api_claude_code_print_mode",
    "api_openai_sdk",
}

REQUIRED_AUTHORITIES = {
    "implementation_authority",
    "live_call_authority",
    "usage_budget_authority",
    "candidate_acceptance_authority",
    "active_configuration_authority",
    "merge_authority",
    "production_authority",
}

VALID_AUTHORITY_LEVELS = {"owner_only", "bounded_delegate", "not_granted"}

# These three must never be anything but not_granted in this contract
# version -- a batch or a future contract edit that loosens them is a
# governance regression, not a routine config change.
FIXED_NOT_GRANTED = {"active_configuration_authority", "merge_authority", "production_authority"}


def validate_batch_config(doc: dict) -> list[av.Finding]:
    findings = av._schema_findings(doc, SCHEMA_PATH, "v02_live_batch_config")
    if findings:
        return findings  # structural errors first; cross-field checks assume a structurally valid doc

    if doc["transport_id"] not in AUDITED_TRANSPORT_IDS:
        findings.append(
            av.Finding(
                path="transport_id",
                rule="UNAUDITED_TRANSPORT",
                severity="high",
                evidence=f"{doc['transport_id']!r} is not one of the transports audited in issue #410: {sorted(AUDITED_TRANSPORT_IDS)}",
                consequence="reject",
            )
        )

    is_authorized = doc["authority_status"] == "authorized" or doc["transport_authority_status"] == "authorized"
    if is_authorized:
        if not (isinstance(doc["max_cost_amount"], (int, float)) and doc["max_cost_amount"] > 0):
            findings.append(
                av.Finding(
                    path="max_cost_amount",
                    rule="UNBUDGETED_AUTHORIZATION",
                    severity="critical",
                    evidence="authority_status/transport_authority_status is 'authorized' but max_cost_amount is not a positive number",
                    consequence="reject",
                )
            )
        if not doc["max_cost_currency"]:
            findings.append(
                av.Finding(
                    path="max_cost_currency",
                    rule="UNBUDGETED_AUTHORIZATION",
                    severity="critical",
                    evidence="authority_status/transport_authority_status is 'authorized' but max_cost_currency is not set",
                    consequence="reject",
                )
            )
        if doc["max_provider_calls"] is None:
            findings.append(
                av.Finding(
                    path="max_provider_calls",
                    rule="UNBOUNDED_AUTHORIZATION",
                    severity="critical",
                    evidence="authority_status/transport_authority_status is 'authorized' but max_provider_calls is unset (unbounded calls)",
                    consequence="reject",
                )
            )

    if doc["live_evidence_required"] and doc["synthetic_evidence_allowed_for"]:
        # Not itself an error -- synthetic rows may still validate the
        # deterministic machinery alongside a live batch (#396's own
        # pattern) -- but every such row must be excluded from the
        # keep/discard decision. This module cannot see individual rows
        # from the batch config alone, so it only asserts the allowed-uses
        # list stays inside the closed enum already enforced by the
        # schema; the per-row exclusion is enforced by
        # scripts/autoresearch_decision_comparator.py (#395), unchanged.
        pass

    return findings


def validate_authority_matrix(doc: dict) -> list[av.Finding]:
    findings: list[av.Finding] = []
    authorities = doc.get("authorities", {})

    missing = REQUIRED_AUTHORITIES - set(authorities)
    if missing:
        findings.append(
            av.Finding(
                path="authorities",
                rule="MISSING_AUTHORITY",
                severity="critical",
                evidence=f"authority matrix is missing required authorities: {sorted(missing)}",
                consequence="reject",
            )
        )

    for name, entry in authorities.items():
        level = entry.get("level")
        if level not in VALID_AUTHORITY_LEVELS:
            findings.append(
                av.Finding(
                    path=f"authorities.{name}.level",
                    rule="INVALID_AUTHORITY_LEVEL",
                    severity="critical",
                    evidence=f"{level!r} is not one of {sorted(VALID_AUTHORITY_LEVELS)}",
                    consequence="reject",
                )
            )
        if name in FIXED_NOT_GRANTED and level != "not_granted":
            findings.append(
                av.Finding(
                    path=f"authorities.{name}.level",
                    rule="AUTHORITY_REGRESSION",
                    severity="critical",
                    evidence=f"{name} must remain not_granted in contract_version 0.2.0; found {level!r}",
                    consequence="reject",
                )
            )

    return findings
