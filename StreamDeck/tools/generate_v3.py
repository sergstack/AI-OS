#!/usr/bin/env python3
"""Generate the canonical AI-OS StreamDeck v3.0 source package."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT
ARCHIVE = ROOT / "archive"
VERSION = "3.0.0"
SNAPSHOT = "2026-07-15"

PROFILE_SPECS = [
    ("B00_DAILY", "DAILY", "[AI OS]", ["INBOX", "AI TREND", "DECISION", "DATA CONTRACT", "GOAL→PR", "FIN MEMO", "PROMPT", "CONTEXT", "SYNC", "KB EVIDENCE"]),
    ("B10_ROUTE", "ROUTE", "[Inbox Router]", ["RAW→ROUTE", "THINGS?", "CALENDAR?", "NOTES?", "AI OS?", "THINKING?", "ANALYTICS?", "LLM?", "CODEX?", "CODEX APP?"]),
    ("B20_AI_OS", "AI OS", "[AI OS]", ["AI TREND", "PATTERN", "USE CASE", "EVIDENCE", "GOVERNANCE", "FRESH CHECK", "SOURCE TRUTH", "LOOP DESIGN", "PROMPT QA", "STREAMDECK"]),
    ("B30_THINKING", "THINKING", "[Thinking]", ["DECISION", "OPTIONS", "RISKS", "ASSUMPTIONS", "REVERSIBLE?", "SCENARIO", "PREMORTEM", "CRITERIA", "TRADE-OFFS", "NEXT STEP"]),
    ("B40_ANALYTICS", "ANALYTICS", "[Analytics]", ["DATA CONTRACT", "DATA QUALITY", "VARIANCE", "RECONCILE", "ANOMALY", "MART SPEC", "FORMULA", "QA CHECKS", "ANALYTICS LOOP", "MEMO FACTS"]),
    ("B50_LLM", "LLM", "[LLM]", ["PROMPT BUILD", "CONTEXT PACK", "MODEL ROUTE", "WORKFLOW", "EVAL RUBRIC", "SUMMARIZE", "EXTRACT", "SYNTHESIZE", "LOCAL PROMPT", "GOAL→CODEX PACK"]),
    ("B60_CODEX", "CODEX", "[Codex]", ["GOAL→PR", "BUILD FIRST", "INSPECT", "RUN CHECKS", "FIX IN SCOPE", "SYNC", "PR JUDGE", "FIX CI", "REVIEW COMMENTS", "RELEASE NOTES"]),
    ("B70_JUDGE", "JUDGE", "[LLM] / Judge", ["UNIVERSAL", "EVIDENCE", "ROUTE", "RISK", "FRESHNESS", "ANALYTICS", "MEMO", "PROMPT", "PR", "LOCAL AI"]),
    ("B80_REVISOR", "REVISOR", "[LLM] / Revisor", ["APPLY NOTES", "SHORTEN", "CLEARER", "EXEC VERSION", "FILE-READY", "MEMO", "DECISION", "STRUCTURE", "TONE", "SOURCE-PRESERVE"]),
    ("B90_MEMO", "MEMO", "[LLM] / Memo", ["FINANCE", "MANAGEMENT", "EXEC SUMMARY", "FINDINGS", "RISKS", "RECOMMEND", "AUDIT FINDING", "CHART COMMENT", "APPENDIX", "FINAL MEMO"]),
    ("BA0_LOCAL_AI", "LOCAL AI", "[LLM] / Local AI", ["SAFETY", "SANITIZE", "DRAFT ONLY", "OLLAMA SMOKE", "OPEN WEBUI", "MODEL COMPARE", "EVAL MATRIX", "JUDGE OUTPUT", "RECORD PILOT", "CANDIDATE?"]),
    ("BB0_PILOTS", "PILOTS", "[AI OS]", ["PILOT PLAN", "TEST CASES", "RUN RECORD", "PILOT RESULT", "ACCEPTANCE", "RESIDUAL RISK", "ROLLBACK", "REGISTRY", "STATUS NOTE", "REVISIT"]),
    ("BC0_KB", "KB", "[AI OS]", ["KB SEARCH", "EVIDENCE LABEL", "REVIEW ITEM", "SUPPORT MIX", "SOURCE TRUTH", "MANIFEST", "BUNDLE SYNC", "UPLOAD CHECK", "FRESHNESS", "CONFLICT CHECK"]),
    ("BD0_MCP", "MCP", "[AI OS]", ["LIST ACTIONS", "REGISTRY", "VISIBILITY", "JUDGE", "REVISOR", "SYNC", "AI TREND", "KB SOURCE", "LOCAL SAFETY", "GOAL→PR"]),
    ("BE0_DECK_QA", "DECK QA", "[Codex]", ["SWITCH TEST", "DEVICE TARGET", "FOCUS TEST", "TEXT INSERT", "AUTO-SEND OFF", "PLACEHOLDER", "DUPLICATES", "PROMPT HASH", "EXPORT BACKUP", "IMPORT TEST"]),
]

COMMON = [
    ("K11", "BLOCKER", "blocker_review", "[Thinking]", "blocked"),
    ("K12", "HANDOFF", "handoff_prepare", "[Inbox Router]", "handoff"),
    ("K13", "JUDGE", "judge_universal", "[LLM] / Judge", "judge"),
    ("K14", "REVISOR", "revisor_apply_notes", "[LLM] / Revisor", "revise"),
    ("K15", "FINAL GATE", "final_acceptance_gate", "[LLM] / Judge", "judge"),
]

CONTROLLER_LABELS = [
    "DAILY", "ROUTE", "AI OS", "THINKING", "ANALYTICS", "LLM", "CODEX", "JUDGE",
    "REVISOR", "MEMO", "LOCAL AI", "PILOTS", "KB", "MCP", "DECK QA",
]

REUSED_IDS = {
    "AI TREND": "ai_trend", "DECISION": "thinking_decision", "DATA CONTRACT": "analytics_data_contract",
    "GOAL→PR": "codex_goal_to_pr", "SYNC": "codex_sync", "EVIDENCE": "evidence_check",
    "SOURCE TRUTH": "kb_source_truth", "RISKS": "thinking_risks", "PROMPT": "llm_prompt_review",
    "MEMO": "memo_review", "REGISTRY": "registry_review", "FRESHNESS": "freshness_check",
    "JUDGE": "judge_universal", "REVISOR": "revisor_apply_notes",
    "SAFETY": "local_ai_safety", "KB SOURCE": "kb_source_truth",
}

OWNER_BY_LABEL = {
    "AI TREND": "[AI OS]", "DECISION": "[Thinking]", "DATA CONTRACT": "[Analytics]",
    "GOAL→PR": "[Codex]", "SYNC": "[Codex]", "EVIDENCE": "[AI OS]", "SOURCE TRUTH": "[AI OS]",
    "RISKS": "[Thinking]", "PROMPT": "[LLM]", "MEMO": "[LLM] / Memo", "REGISTRY": "[AI OS]",
    "FRESHNESS": "[AI OS]", "ANALYTICS": "[Analytics]", "JUDGE": "[LLM] / Judge",
    "REVISOR": "[LLM] / Revisor", "ROUTE": "[Inbox Router]",
}

MCP_IDS = {
    "judge_universal": "AIOS_HOME_JUDGE",
    "revisor_apply_notes": "AIOS_HOME_REVISOR",
    "codex_sync": "AIOS_HOME_SYNC",
    "kb_source_truth": "AIOS_KB_SOURCE_TRUTH",
    "local_ai_safety": "AIOS_LOCAL_AI_SAFETY",
    "codex_goal_to_pr": "AIOS_CODEX_ISSUE_TO_PR",
    "ai_trend": "AIOS_AI_TREND",
}
MCP_VERIFIED = {"AIOS_HOME_JUDGE", "AIOS_HOME_REVISOR"}

ROUTE_V1_1_IDS = {
    "b10_route_raw_to_route", "b10_route_things", "b10_route_calendar", "b10_route_notes",
    "b10_route_ai_os", "b10_route_thinking", "b10_route_analytics", "b10_route_llm",
    "b10_route_codex", "b10_route_codex_app", "blocker_review", "handoff_prepare",
}

JUDGE_V1_1_IDS = {
    "judge_universal", "judge_evidence", "judge_route", "judge_risk", "judge_freshness",
    "judge_analytics", "judge_memo", "judge_prompt", "judge_pr", "judge_local_ai",
    "final_acceptance_gate",
}

ANALYTICS_V1_1_IDS = {
    "analytics_data_contract", "b40_analytics_data_quality", "b40_analytics_variance",
    "b40_analytics_reconcile", "b40_analytics_anomaly", "b40_analytics_mart_spec",
    "b40_analytics_formula", "b40_analytics_qa_checks", "b40_analytics_analytics_loop",
    "b40_analytics_memo_facts",
}

PROMPT_V1_1_IDS = ROUTE_V1_1_IDS | JUDGE_V1_1_IDS | ANALYTICS_V1_1_IDS

ROUTE_OWNER_PROJECTS = (
    "Owners: [Inbox Router] unresolved capture; [AI OS] AI concepts/evidence/governance; [Thinking] "
    "decisions/strategy/risks; [Analytics] data/metrics/calculations/marts; [LLM] prompts/models/workflows/evals; "
    "[Codex] code/tests/repo implementation. LLM roles stay under [LLM]; Codex APP is a [Codex] surface, "
    "not an owner."
)


def slug(value: str) -> str:
    value = value.lower().replace("→", "_to_").replace("?", "")
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


def prompt_version(prompt_id: str) -> str:
    return "1.1.0" if prompt_id in PROMPT_V1_1_IDS else "1.0.0"


def subject_logic(prompt_id: str) -> str:
    route_rules = {
        "b10_route_raw_to_route": (
            f"{ROUTE_OWNER_PROJECTS} First classify the input as actionable, time-bound, reference, or "
            "project work. Route concrete next actions to Things, hard date/time commitments to Calendar, "
            "and durable context without an immediate action to Notes / Obsidian. Choose exactly one owner; "
            "if two remain plausible, return clarify and name the deciding question. Example: 'compare plan "
            "versus actual revenue' -> [Analytics], not [Thinking]."
        ),
        "b10_route_things": (
            f"{ROUTE_OWNER_PROJECTS} Choose Things only when the input can be rewritten as one concrete "
            "physical or digital next action and has no mandatory time slot. Do not use Things for reference "
            "material, broad projects, decisions, calculations, or implementation without a bounded next step. "
            "Return the action as a verb-led task; if owner/project work is needed first, route there instead. "
            "Example: 'send the approved memo to Anna' -> Things; 'decide the memo position' -> [Thinking]."
        ),
        "b10_route_calendar": (
            f"{ROUTE_OWNER_PROJECTS} Choose Calendar only for a meeting, deadline, appointment, or other "
            "commitment with a hard date or time. Extract the exact date, time, timezone, duration and attendees "
            "only when supplied; missing required scheduling facts produce clarify, never invented values. A "
            "preferred day without a fixed commitment remains Things. Example: 'review at 15:00 MSK Friday' "
            "-> Calendar; 'review on Friday if possible' -> Things or clarify."
        ),
        "b10_route_notes": (
            f"{ROUTE_OWNER_PROJECTS} Choose Notes / Obsidian for durable context, ideas, source excerpts, "
            "meeting notes or reference material that has no immediate next action or hard time. Preserve a "
            "clear title, source and useful links; do not turn a decision, calculation, prompt design or code "
            "request into a passive note. If the material also implies work, separate the note from the routed "
            "action. Example: 'keep this vendor comparison for later' -> Notes / Obsidian."
        ),
        "b10_route_ai_os": (
            f"{ROUTE_OWNER_PROJECTS} Choose [AI OS] for an AI concept, use case, reusable pattern, evidence "
            "assessment, governance rule or knowledge-base question. Route prompt wording, model selection and "
            "LLM workflow design to [LLM]; strategy choices to [Thinking]; implementation to [Codex]. Require "
            "a named AI topic and the evidence or governance decision sought. Example: 'is agent memory a "
            "supported pattern for us?' -> [AI OS]."
        ),
        "b10_route_thinking": (
            f"{ROUTE_OWNER_PROJECTS} Choose [Thinking] for a decision, strategy, alternatives, scenarios, "
            "trade-offs, assumptions, risks or premortem before execution. Do not route deterministic numeric "
            "analysis to [Thinking], prompt engineering to [LLM], or code changes to [Codex]. State the decision "
            "to make and at least one constraint; otherwise clarify. Example: 'choose build versus buy under a "
            "six-month constraint' -> [Thinking]."
        ),
        "b10_route_analytics": (
            f"{ROUTE_OWNER_PROJECTS} Choose [Analytics] when the answer depends on data, metrics, formulas, "
            "periods, currencies or units, reconciliation, variance, anomaly review, mart design or deterministic "
            "calculation. Require the business question and identify missing source, grain, period or unit fields; "
            "do not calculate mentally. Example: 'why did gross margin differ from plan in June?' -> [Analytics]; "
            "'which strategic option should we prefer?' -> [Thinking]."
        ),
        "b10_route_llm": (
            f"{ROUTE_OWNER_PROJECTS} Choose [LLM] for prompt design or review, model routing, context packs, "
            "orchestration, eval rubrics, judge/revise workflows, local-model experiments or memo generation "
            "from already approved facts. Route implementation code to [Codex], deterministic calculations to "
            "[Analytics], and AI evidence/governance to [AI OS]. Example: 'design an eval rubric for this prompt' "
            "-> [LLM]."
        ),
        "b10_route_codex": (
            f"{ROUTE_OWNER_PROJECTS} Choose [Codex] for repository inspection, code or configuration changes, "
            "tests, bug fixes, refactors, generators, CI diagnosis or a bounded goal-to-PR workflow. The request "
            "must name an implementation outcome or repository artifact; raw inbox capture stays in [Inbox "
            "Router], and unresolved product strategy goes to [Thinking]. Example: 'add validation and tests for "
            "the exporter' -> [Codex]."
        ),
        "b10_route_codex_app": (
            f"{ROUTE_OWNER_PROJECTS} Use Codex APP only as the execution surface for an owner route of [Codex]: "
            "a bounded repository/workflow goal that may require local files, commands, checks and a PR. Do not "
            "treat Codex APP as a seventh owner project or send raw capture directly to it. The handoff must name "
            "goal, repository/path, constraints, expected output, checks and stop conditions. Example: 'implement "
            "issue #198 in AI-OS' -> owner [Codex], surface Codex APP."
        ),
        "blocker_review": (
            "Classify the stop reason as missing source, ambiguous owner, failed deterministic check, unsafe or "
            "unapproved action, missing permission, or unmet acceptance criterion. A blocker must cite the exact "
            "prerequisite and evidence already checked, distinguish owner action from work the current project "
            "can still do, and offer only reversible safe options. Do not label inconvenience or uncertainty as "
            "blocked. Example: a required physical device test with no device access -> blocked / owner action; "
            "a fixable local test failure -> revise, not blocked."
        ),
        "handoff_prepare": (
            f"{ROUTE_OWNER_PROJECTS} Create a handoff only when the current owner cannot complete the next "
            "bounded outcome. Name exactly one receiving owner project, the source artifact, verified facts, "
            "assumptions, constraints, forbidden actions, expected output, acceptance criteria and stop condition. "
            "Do not copy unsupported conclusions or route to Codex APP without owner [Codex]. Example: a verified "
            "analytics finding needing code automation -> [Codex] handoff with the calculation evidence attached."
        ),
    }
    judge_rules = {
        "judge_universal": (
            "Apply one rubric to the selected artifact: required schema is complete; material and owner are "
            "unambiguous; each factual claim has provided or tool-observed evidence; execution labels match "
            "observed commands; routing respects project boundaries; safety and permissions are intact; every "
            "acceptance criterion has evidence. Return pass only when all apply, revise for a fixable artifact "
            "defect, and blocked for a missing source, permission, deterministic result or owner gate. Example: "
            "passing tests with an unmet acceptance item -> revise, not pass."
        ),
        "judge_evidence": (
            "Build a claim-to-source check for the selected artifact. For each material claim, name the exact "
            "provided source or observed tool result and classify support as direct, indirect, conflicting or "
            "missing. Check whether changeable facts have dated current evidence and whether calculations cite "
            "Python/SQL output. Do not treat repetition, plausible wording or model memory as evidence. Pass only "
            "with direct support for every decision-driving claim; revise unsupported noncritical claims; block "
            "when missing evidence prevents the decision."
        ),
        "judge_route": (
            f"{ROUTE_OWNER_PROJECTS} Check the selected artifact's owner against the work: one "
            "primary destination, boundary-respecting scope, and a complete handoff when ownership changes. "
            "Things requires a concrete next action; Calendar a hard time; Notes durable reference context. "
            "Pass when owner and next action are unambiguous, revise a fixable misroute, and block when the input "
            "cannot be classified without one named clarification. Example: a repository change routed to "
            "[Thinking] -> revise to [Codex]."
        ),
        "judge_risk": (
            "Check that each material risk names the triggering condition, affected asset or decision, likely "
            "consequence, existing control, residual exposure and owner action. Do not invent numeric probability "
            "or impact scores without a supplied method and data. Verify that destructive, remote, production, "
            "security and financial-control actions have explicit gates and rollback. Pass when critical risks "
            "are controlled and residual risks are visible; revise missing mitigations; block an unsafe or "
            "unapproved action."
        ),
        "judge_freshness": (
            "Identify every claim that can change with time: versions, prices, laws, schedules, current roles, "
            "availability and external status. Require a current official source or tool observation plus its "
            "date; compare the source date with the decision period. If live verification was unavailable, the "
            "claim must say UNVERIFIED rather than present memory as current. Pass when all decision-driving "
            "changeable claims are current, revise stale noncritical claims, and block when freshness is required "
            "to decide safely."
        ),
        "judge_analytics": (
            "Require the selected analysis to state entity, grain, period, currency or unit, source layers, "
            "filters, joins, formulas and exclusions. Numeric results must come from observed Python or SQL, with "
            "reconciliation or exception evidence appropriate to the question; raw, stage, mart and report facts "
            "must not be mixed implicitly. Pass only when calculations and conclusions trace to deterministic "
            "evidence, revise a reproducible local defect, and block on missing source data, undefined metrics or "
            "unresolved reconciliation."
        ),
        "judge_memo": (
            "Check that the selected memo states audience, scope, period and currency or units; uses only "
            "Analytics-approved facts; and separates facts, interpretation, assumptions, recommendations and "
            "management confirmations. Every chart comment, variance explanation and root-cause statement must "
            "trace to evidence; unsupported causality must be softened or removed. Pass when the narrative is "
            "decision-ready and sourced, revise presentation or support gaps, and block when required facts or "
            "approvals are absent."
        ),
        "judge_prompt": (
            "Check the selected prompt for a defined role, material-selection rule, required inputs, concrete "
            "decision criteria, output contract, safety boundaries, known failure modes and a useful example where "
            "ambiguity is likely. Verify that metadata policies needed by the model also appear in the body and "
            "that execution claims are not implied by expected output. Pass only with representative test evidence "
            "or an explicit NOT RUN gate, revise a fixable instruction gap, and block when the source task cannot "
            "be identified."
        ),
        "judge_pr": (
            "Compare the selected PR with its issue or goal: intended scope, changed files, forbidden areas, every "
            "acceptance criterion, observed tests, residual risks, rollback and merge policy. Inspect the actual "
            "diff and check output; do not infer correctness from the PR description or green status alone. Pass "
            "only when evidence covers the full requested behavior and no unrelated change remains, revise an "
            "in-scope defect or missing check, and block on an unsafe change, missing authority or unavailable "
            "required evidence."
        ),
        "judge_local_ai": (
            "Check the selected local-AI artifact for data classification, sanitization, model/runtime identity, "
            "observed versus proposed execution, evaluation criteria and candidate-only labeling. Secrets, private "
            "paths, raw sensitive data and production actions must remain excluded; local execution is not proof "
            "of quality or safety. Pass when the pilot is reproducible, sanitized and bounded, revise missing "
            "evaluation or labeling, and block exposure risk, unapproved data use or a production-readiness claim "
            "without evidence."
        ),
        "final_acceptance_gate": (
            "Enumerate every acceptance criterion from the selected source and pair it with exact evidence: changed "
            "file, observed command output, test result, owner decision or explicit NOT RUN gate. A criterion is "
            "met only when evidence matches its full scope; partial implementation, proposed checks and unrelated "
            "green tests do not count. Return pass only when all required criteria are met and residual risks are "
            "accepted by the correct owner; return revise for fixable unmet criteria; return blocked for missing "
            "authority, source, deterministic evidence or mandatory owner action."
        ),
    }
    analytics_rules = {
        "analytics_data_contract": (
            "Define the decision the analysis must support, then fix entity, grain, period, currency or unit, "
            "source systems and raw/stage/mart/report layers. List required fields, keys, dimensions, measures, "
            "filters, formulas, exclusions and update cadence. Separate supplied definitions from assumptions; "
            "do not infer a business rule from column names. Specify Python/SQL checks for uniqueness, completeness "
            "and reconciliation. If grain, period, currency/unit, formula ownership or a required source is "
            "missing, return NOT RUN with the exact input needed."
        ),
        "b40_analytics_data_quality": (
            "Evaluate the selected dataset at its declared entity and grain. Use Python or SQL to profile row "
            "counts, schema/types, key uniqueness, duplicates, nulls, valid ranges, referential integrity, date "
            "coverage and category domains; compare each result with an explicit rule or source expectation. "
            "Separate blocking defects from warnings and quantify affected rows through tool output only. Do not "
            "clean or overwrite raw data implicitly. Return a reproducible check, observed result, affected layer, "
            "risk and the safe next transformation or source-owner question."
        ),
        "b40_analytics_variance": (
            "Compare fact with plan or forecast only after aligning entity, grain, period, currency/unit, metric "
            "definition, scope and filters. Calculate absolute and percentage variance in Python or SQL, including "
            "an explicit zero/null denominator rule and sign convention. Build driver contributions only from "
            "available dimensions and reconcile them to the total variance; do not state causality from correlation "
            "or magnitude alone. Return the deterministic calculation, reconciliation gap, supported drivers, "
            "unexplained remainder and required management confirmation."
        ),
        "b40_analytics_reconcile": (
            "Name the two values or layers to reconcile and state their entity, grain, period, currency/unit and "
            "metric definition. Use Python or SQL to create a bridge for source coverage, filters, joins, duplicate "
            "keys, timing/cut-off, sign, mapping and currency differences. The bridge must reproduce both endpoints "
            "and show any unresolved remainder; never plug a balancing value without labeling it. Preserve raw input "
            "and record every exclusion or transformation. Pass only at the stated tolerance; otherwise return the "
            "exact unmatched population and source-owner action."
        ),
        "b40_analytics_anomaly": (
            "Define the population, expected behavior, comparison period and anomaly rule before inspecting rows. "
            "The threshold must come from a supplied policy or a documented Python/SQL method; do not invent one. "
            "Return flagged entities with deterministic evidence, baseline, deviation, source layer and data-quality "
            "status. Separate true business anomalies, data defects and insufficient-context cases; sampling and "
            "correlation do not prove cause or fraud. Include false-positive risks, the unflagged control population "
            "and the next evidence needed for investigation."
        ),
        "b40_analytics_mart_spec": (
            "Translate the approved business question and data contract into a mart specification: target grain, "
            "facts, dimensions, keys, source-to-target mappings, period and currency/unit treatment, filters, "
            "derived fields, formulas and refresh expectations. Keep raw, stage and mart responsibilities explicit; "
            "do not introduce a new business definition or source. Define deterministic tests for uniqueness, "
            "completeness, referential integrity, reconciliation and incremental behavior. Mark unresolved ownership, "
            "history or late-arriving-data choices as blocked rather than selecting an architecture silently."
        ),
        "b40_analytics_formula": (
            "Specify the metric name, business meaning, numerator, denominator, aggregation, grain, period, "
            "currency/unit, sign convention, filters and exclusions. Define zero, null, missing-period, duplicate "
            "and restatement behavior explicitly, plus the authoritative owner/source for each rule. Implement or "
            "demonstrate the calculation only in Python or SQL and show a small tool-computed test case with expected "
            "units. Reconcile the result to source totals where applicable. If a business rule is absent or conflicting, "
            "return NOT RUN and list the exact confirmation needed."
        ),
        "b40_analytics_qa_checks": (
            "Judge the selected analytics artifact against its data contract. Require observed Python/SQL evidence "
            "for schema, key uniqueness, duplicates, nulls, ranges, join cardinality, period/currency alignment, "
            "formula edge cases and source-to-output reconciliation. Check that raw/stage/mart/report layers and "
            "fact/plan/forecast are not mixed implicitly. Return pass only when all required checks meet stated "
            "tolerances; revise a reproducible logic or mapping defect; block missing source data, undefined business "
            "rules, unresolved reconciliation or unobserved execution."
        ),
        "b40_analytics_analytics_loop": (
            "Run the supervised sequence: clarify decision -> data contract -> data-quality checks -> explicit "
            "stage/mart transformations -> Python/SQL calculation -> reconciliation -> findings -> memo-ready facts "
            "-> QA verdict. At every step record inputs, layer, period, currency/unit, filters, joins, exclusions and "
            "observed command status. Stop and return NOT RUN or blocked when a prerequisite, business definition, "
            "permission or deterministic check fails; do not skip forward or self-approve. A revise verdict may rerun "
            "only the bounded failed step and its downstream checks."
        ),
        "b40_analytics_memo_facts": (
            "Prepare a fact pack, not narrative. Include only figures and comparisons reproduced by observed "
            "Python/SQL, with entity, grain, period, currency/unit, source layer, formula, filters and reconciliation "
            "status for each item. Separate actual, plan and forecast; label assumptions, exceptions and management "
            "confirmations. Rank facts by decision relevance without inventing causality, recommendations or root "
            "causes. Each bullet must trace to a dataset/check reference and state whether it is approved, provisional "
            "or blocked for memo use."
        ),
    }
    return route_rules.get(prompt_id, judge_rules.get(prompt_id, analytics_rules.get(prompt_id, "")))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def task_type(label: str) -> str:
    upper = label.upper()
    if any(token in upper for token in ("JUDGE", "QA", "CHECK", "TEST", "EVAL", "ACCEPTANCE")):
        return "judge"
    if any(token in upper for token in ("REVIS", "FIX", "CLEARER", "SHORTEN", "TONE", "STRUCTURE")):
        return "revise"
    if any(token in upper for token in ("ROUTE", "HANDOFF", "TARGET")) or upper.endswith("?"):
        return "route"
    if upper == "MEMO FACTS":
        return "analytics"
    if "MEMO" in upper:
        return "memo"
    if any(token in upper for token in ("SUMMARY", "FINDINGS", "COMMENT", "NOTES")):
        return "narrative"
    if any(token in upper for token in ("ANALYT", "DATA", "VARIANCE", "FORMULA", "RECONCILE", "ANOMALY", "MART")):
        return "analytics"
    if any(token in upper for token in ("RUN", "IMPORT", "EXPORT", "SYNC", "OLLAMA", "WEBUI")) or re.search(r"\b(?:PR|CI|MCP)\b", upper):
        return "execution_request"
    return "draft"


def output_schema(label: str, kind: str) -> list[str]:
    exact = {
        "PROMPT BUILD": ["Recommended workflow", "Prompt / template", "Input requirements", "Output schema", "Model class", "Quality gate", "Known failure modes", "Handoff / next action"],
        "CONTEXT PACK": ["Goal", "Decision needed", "Relevant files / sources", "Facts", "Assumptions", "Constraints", "Forbidden", "Open questions", "Expected output", "Quality gate", "Owner project", "Handoff target"],
        "GOAL→PR": ["Goal", "Bounded scope", "Branch", "Files inspected", "Files changed", "Checks observed", "PR status", "Risks", "Rollback", "Merge / gate status"],
        "BUILD FIRST": ["Goal", "Repository evidence", "Smallest working change", "Checks observed", "PR status", "Risks", "Rollback", "Merge / gate status"],
        "PROMPT QA": ["Prompt ID and version", "Verdict: pass / revise / blocked", "Criteria results", "Representative test evidence", "UX score", "Required revision", "Residual risks", "Owner acceptance"],
        "DATA CONTRACT": ["Decision", "Entity", "Grain", "Period", "Currency / unit", "Sources and layers", "Fields", "Formulas", "Filters", "Deterministic checks", "Missing inputs", "Execution status"],
        "FINAL GATE": ["Verdict: pass / revise / blocked", "Acceptance criteria", "Evidence observed", "Unmet criteria", "Unsupported claims", "Residual risks", "Owner gate", "Next action"],
        "JUDGE": ["Verdict: pass / revise / blocked", "Schema fit", "Evidence", "Execution truth", "Routing", "Unsupported claims", "Required fixes", "Acceptance status"],
        "REVISOR": ["Revised source artifact", "Judge notes applied", "Facts preserved", "Claims removed or softened", "Blocked items", "Next judge action"],
        "BLOCKER": ["Blocked decision", "Missing prerequisite", "Evidence checked", "Safe options", "Stop condition", "Owner action", "Rollback"],
        "HANDOFF": ["Goal", "Source artifact", "Facts", "Constraints", "Forbidden actions", "Owner project", "Expected output", "Acceptance criteria", "Stop condition"],
    }
    if label in exact:
        return exact[label]
    if kind == "analytics":
        return [f"{label.title()} question", "Entity and grain", "Period", "Currency / unit", "Source layers", "Formula / method", "Deterministic evidence", "Result or NOT RUN", "Exceptions", "Next action"]
    if kind == "judge":
        return [f"{label.title()} verdict: pass / revise / blocked", "Criteria checked", "Evidence observed", "Unsupported claims", "Required fixes", "Residual risks", "Next action"]
    if kind == "revise":
        return [f"Revised {label.lower()} artifact", "Revision notes applied", "Source facts preserved", "Unsupported content removed", "Blocked items", "Next review"]
    if kind == "route":
        return ["Input classification", "Chosen owner project", "Reason", "Required context", "Forbidden data", "Handoff target", "Stop condition"]
    if kind == "execution_request":
        return [f"{label.title()} objective", "Commands / tool calls actually observed", "Execution status: EXECUTED / PARTIAL / NOT RUN", "Observed result", "Proposed actions not run", "Blockers", "Rollback", "Next action"]
    if kind == "memo":
        return [f"{label.title()} scope", "Period", "Currency / units", "Analytics-approved facts", "Interpretation", "Assumptions", "Recommendations", "Source traceability", "Management confirmations required"]
    if kind == "narrative":
        return [f"{label.title()} scope", "Source facts", "Interpretation", "Assumptions", "Required decisions", "Traceability", "Next action"]
    return [f"{label.title()} deliverable", "Source material used", "Decision or artifact", "Evidence and freshness", "Constraints", "Known limitations", "Stop condition", "Next action"]


def prompt_body(label: str, purpose: str, owner: str, schema: list[str], kind: str, subject: str) -> str:
    analytics = "\n\nNumeric boundary:\nAll calculations and numeric QA must be performed by Python or SQL. Require entity, grain, period, currency/unit, formulas, filters and deterministic evidence; otherwise return NOT RUN." if kind == "analytics" or owner == "[Analytics]" else ""
    freshness = "\n\nFreshness:\nCheck changeable facts through current official sources when read-only web/tool access exists. If current verification is unavailable, mark UNVERIFIED; never present model memory as fresh verification." if any(x in label for x in ("TREND", "FRESH", "MODEL", "RELEASE")) else ""
    revision = "\n\nRevision boundary:\nUse the last Judge verdict only as revision notes. Edit the source artifact the Judge reviewed, never the verdict itself. If the source is ambiguous, return blocked. Add no facts or evidence." if kind == "revise" or "REVIS" in label else ""
    goal = "\n\nGoal Mode boundary:\nUse the latest meaningful user goal; there is no paste placeholder. Keep work bounded and build-first. The Stream Deck inserts text only and never presses Send. Codex may inspect, branch, change scoped files, check and open a PR after manual send, but must not manually merge, deploy, or perform destructive/production actions." if label in {"GOAL→PR", "BUILD FIRST", "GOAL→CODEX PACK"} else ""
    judge = "\n\nJudge rule:\nReturn only pass, revise, or blocked. Check schema fit, evidence, execution truth, routing, unsupported claims and acceptance. Deterministic evidence overrides model preference." if kind == "judge" else ""
    memo = "\n\nMemo boundary:\nWrite narrative only from Analytics-approved facts. Separate facts, interpretation, assumptions, and recommendations. A root cause without evidence requires management confirmation. State period, scope, currency/units, and source traceability." if kind == "memo" else ""
    subject_block = f"\n\nSubject logic:\n{subject}\n\nSelection check:\nThe first response line must be `Selected material: \"<first about 10 words of the chosen source>\"`." if subject else ""
    return_intro = "After that first line, return exactly these sections:" if subject else "Return exactly these sections:"
    return f"""# {label} — {owner}

Purpose:
{purpose}

Material selection:
Use the latest meaningful user goal or source material. A Judge verdict is revision notes, not the editable source artifact. If the source artifact cannot be identified unambiguously, return blocked. Do not guess or substitute the source.

Execution truth:
Report Execution status as EXECUTED / PARTIAL / NOT RUN. EXECUTED is allowed only for tool calls, commands, or checks actually observed. List proposed actions separately. Expected results are not observed results.{freshness}{analytics}{revision}{goal}{judge}{memo}{subject_block}

Safety and interaction:
Text insertion only; auto-send is off and the user sends manually. Do not expose secrets or private data. Do not delete, merge, deploy, publish, mutate production, automate UI, or claim unobserved execution.

{return_intro}
""" + "\n".join(f"- {item}" for item in schema)


def prompt_key(profile_id: str, profile_name: str, label: str) -> str:
    if profile_name == "JUDGE":
        return f"judge_{slug(label)}"
    if profile_name == "REVISOR":
        return f"revisor_{slug(label)}"
    if profile_name == "MEMO":
        return f"memo_{slug(label)}"
    if label in REUSED_IDS:
        return REUSED_IDS[label]
    return f"{slug(profile_id)}_{slug(label)}"


def owner_for(label: str, default: str) -> str:
    if label.endswith("?") or label in {"RAW→ROUTE", "INBOX"}:
        return "[Inbox Router]"
    if label.startswith("LOCAL ") or label in {"SAFETY", "SANITIZE", "DRAFT ONLY", "OLLAMA SMOKE", "OPEN WEBUI", "MODEL COMPARE", "EVAL MATRIX", "JUDGE OUTPUT", "RECORD PILOT", "CANDIDATE?"}:
        return "[LLM] / Local AI"
    if label == "PROMPT QA" or "JUDGE" in label:
        return "[LLM] / Judge"
    if "MEMO" in label and label != "MEMO FACTS":
        return "[LLM] / Memo"
    if label in {"CONTEXT", "CONTEXT PACK", "PROMPT BUILD", "MODEL ROUTE", "WORKFLOW", "EVAL RUBRIC", "SUMMARIZE", "EXTRACT", "SYNTHESIZE", "LOCAL PROMPT", "GOAL→CODEX PACK"}:
        return "[LLM]"
    return OWNER_BY_LABEL.get(label, default)


def make_package() -> None:
    make_icons()
    controllers = []
    for index, ((profile_id, profile_name, _, _), label) in enumerate(zip(PROFILE_SPECS, CONTROLLER_LABELS), 1):
        controllers.append({
            "device": "AIOS-CONTROL", "profile_id": "A00_CONTROL", "button": f"K{index}", "label": label,
            "action_type": "built_in_switch_profile", "action_identifier": "Stream Deck > Switch Profile",
            "action_uuid": None,
            "target_device_role": "AIOS-ACTIONS", "target_device_binding": "manual_serial_neutral",
            "target_profile_id": profile_id, "target_profile_name": f"AIOS-ACTIONS / {profile_name}",
            "auto_send": False, "icon": f"assets/icons/controller_{slug(label)}.svg",
            "physical_status": "NOT RUN - owner physical action required",
        })

    buttons = []
    prompt_refs: dict[str, dict] = {}
    for profile_id, profile_name, default_owner, labels in PROFILE_SPECS:
        profile_buttons = []
        for index, label in enumerate(labels, 1):
            owner = owner_for(label, default_owner)
            kind = task_type(label)
            if profile_name == "JUDGE":
                owner, kind = "[LLM] / Judge", "judge"
            elif profile_name == "REVISOR":
                owner, kind = "[LLM] / Revisor", "revise"
            elif profile_name == "MEMO":
                owner, kind = "[LLM] / Memo", "memo"
            prompt_id = prompt_key(profile_id, profile_name, label)
            profile_buttons.append((f"K{index}", label, prompt_id, owner, kind))
        profile_buttons.extend(COMMON)
        for key, label, prompt_id, owner, kind in profile_buttons:
            mcp_id = MCP_IDS.get(prompt_id)
            ref = f"{profile_id}/{key}"
            version = prompt_version(prompt_id)
            row = {
                "device": "AIOS-ACTIONS", "profile_id": profile_id, "profile_name": f"AIOS-ACTIONS / {profile_name}",
                "button": key, "label": label, "action_type": "prompt", "prompt_id": prompt_id,
                "prompt_version": version, "owner_project": owner, "interaction_risk": "low",
                "workflow_risk": "medium" if kind in {"analytics", "execution_request"} else "low",
                "data_sensitivity": "none", "insertion_method": "clipboard_paste",
                "requires_confirmation": True, "auto_send": False,
                "mcp_action_id": mcp_id, "mcp_verified": (mcp_id in MCP_VERIFIED) if mcp_id else None,
                "next_on_pass": "final_acceptance_gate" if key != "K15" else "owner_acceptance",
                "next_on_revise": "revisor_apply_notes", "next_on_blocked": "blocker_review",
                "stop_condition": "Stop when required source, deterministic evidence, permission, or owner gate is missing.",
                "rollback": "Discard inserted text; no action is sent automatically. The previous clipboard value may already be overwritten.",
                "icon": f"assets/icons/action_{kind}.svg",
            }
            buttons.append(row)
            record = prompt_refs.setdefault(prompt_id, {"label": label, "owner": owner, "kind": kind, "refs": []})
            if record["owner"] != owner:
                raise ValueError(f"route mismatch for {prompt_id}: {record['owner']} != {owner}")
            record["refs"].append(ref)

    prompts = []
    qa_rows = []
    for prompt_id, record in sorted(prompt_refs.items()):
        label, owner, kind, refs = record["label"], record["owner"], record["kind"], record["refs"]
        schema = output_schema(label, kind)
        purpose = f"Produce the {label} workflow artifact for the cited source material while preserving routing, evidence, and execution truth."
        subject = subject_logic(prompt_id)
        version = prompt_version(prompt_id)
        body = prompt_body(label, purpose, owner, schema, kind, subject)
        prompt_hash = hashlib.sha256(body.encode()).hexdigest()
        prompts.append({
            "prompt_id": prompt_id, "prompt_version": version, "task_type": kind, "purpose": purpose,
            "owner_project": owner, "button_refs": refs, "input_requirements": ["latest meaningful goal or source artifact"],
            "material_selection_rule": "Latest meaningful user goal/source; Judge verdict is notes only; ambiguous source => blocked.",
            "execution_mode": "generate", "body": body, "output_schema": schema,
            "evidence_policy": "Use only provided or tool-observed evidence; unsupported claims must be marked.",
            "freshness_policy": "Verify changeable facts with current official sources when access exists; otherwise UNVERIFIED.",
            "execution_truth_policy": "EXECUTED / PARTIAL / NOT RUN; proposed is never observed.",
            "quality_gate": ["schema fit", "route fit", "source discipline", "execution truth", "no new claims"],
            "known_failure_modes": ["ambiguous source", "missing evidence", "unsafe or unapproved action"],
            "qa_status": "blocked", "ux_score_1_5": 4, "prompt_gate_10_of_10": None,
            "last_reviewed": SNAPSHOT, "owner_acceptance": "pending", "prompt_hash": prompt_hash,
        })
        criteria = [{"criterion": n, "status": "pass"} for n in range(1, 10)]
        criteria.append({"criterion": 10, "status": "blocked", "reason": "Representative model/device runs and owner acceptance are not observed."})
        static_checks = {"material_selection": "pass", "specialized_schema": "pass", "route": "pass", "execution_truth": "pass", "freshness": "pass", "no_new_claims": "pass"}
        if subject:
            static_checks["subject_logic"] = "pass"
        qa_rows.append({
            "prompt_id": prompt_id, "prompt_version": version, "button_refs": refs,
            "test_cases": [
                {"case": "normal", "status": "NOT RUN", "expected": "specialized output schema with sourced content"},
                {"case": "missing_context_or_evidence", "status": "NOT RUN", "expected": "blocked or NOT RUN without invented content"},
                {"case": "unsafe_or_ambiguous", "status": "NOT RUN", "expected": "blocked without write, send, UI automation, or source substitution"},
            ],
            "static_contract_checks": static_checks,
            "gate_criteria": criteria, "criteria_passed": 9, "ux_score_1_5": 4,
            "judge_verdict": "blocked", "required_revision": "Run the three representative cases, record observed outputs, repeat Prompt QA, and obtain owner acceptance.",
            "residual_risks": ["No live model-output evidence", "No physical insertion/focus evidence"],
            "owner_acceptance": "pending", "formal_gate_status": "blocked - not 10/10",
        })

    dump(ACTIVE / "config" / "controller_map.json", {"version": VERSION, "device": "AIOS-CONTROL", "profile_id": "A00_CONTROL", "buttons": controllers, "count": len(controllers)})
    dump(ACTIVE / "config" / "action_profiles.json", {"version": VERSION, "device": "AIOS-ACTIONS", "profile_count": len(PROFILE_SPECS), "button_count": len(buttons), "buttons": buttons})
    dump(ACTIVE / "prompts" / "prompt_registry.json", {"version": VERSION, "status": "candidate / blocked pending observed Prompt QA and owner acceptance", "prompt_count": len(prompts), "prompts": prompts})
    dump(ACTIVE / "qa" / "prompt_qa_matrix.json", {"version": VERSION, "status": "repo static QA complete; representative executions NOT RUN", "prompt_count": len(qa_rows), "rows": qa_rows})
    make_mcp_registry(buttons)
    make_icon_map(controllers, buttons)
    make_baseline_audit()
    make_human_map(controllers, buttons)
    make_manifests()


def make_icons() -> None:
    icon_dir = ACTIVE / "assets" / "icons"
    icon_dir.mkdir(parents=True, exist_ok=True)
    names = [f"controller_{slug(label)}" for label in CONTROLLER_LABELS]
    names.extend(f"action_{kind}" for kind in ("analytics", "draft", "execution_request", "judge", "memo", "narrative", "revise", "route", "blocked", "handoff"))
    colors = {
        "analytics": "#0f766e", "draft": "#2563eb", "execution_request": "#7c3aed", "judge": "#b45309",
        "memo": "#be123c", "narrative": "#be123c", "revise": "#9333ea", "route": "#0369a1", "blocked": "#b91c1c", "handoff": "#475569",
    }
    for name in sorted(set(names)):
        token = name.removeprefix("action_").removeprefix("controller_")
        color = colors.get(token, "#1f2937")
        mark = "".join(part[:1].upper() for part in token.split("_")[:3])[:3]
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">
  <rect width="144" height="144" rx="24" fill="{color}"/>
  <rect x="8" y="8" width="128" height="128" rx="19" fill="none" stroke="#ffffff" stroke-opacity=".34" stroke-width="3"/>
  <text x="72" y="84" text-anchor="middle" fill="#ffffff" font-family="Arial, sans-serif" font-size="38" font-weight="700">{mark}</text>
</svg>\n'''
        (icon_dir / f"{name}.svg").write_text(svg, encoding="utf-8")


def make_mcp_registry(buttons: list[dict]) -> None:
    actions = []
    refs = {row["prompt_id"]: row for row in buttons if row["mcp_action_id"]}
    for prompt_id, action_id in MCP_IDS.items():
        row = refs[prompt_id]
        actions.append({
            "action_id": action_id, "prompt_id": prompt_id, "owner_project": row["owner_project"],
            "action_type": "supervised_prompt_insertion", "requires_confirmation": True, "auto_send": False,
            "registry_status": "execution-verified" if action_id in MCP_VERIFIED else "registered-only",
            "evidence": "archive/v2.8/STREAMDECK_V2_8_MCP_ACTIONS_PILOT.md" if action_id in MCP_VERIFIED else None,
            "v3_visibility_status": "NOT RUN - owner MCP action required",
        })
    dump(ACTIVE / "migration" / "mcp_registry.json", {"version": VERSION, "actions": actions, "counts": {"total": len(actions), "execution_verified_legacy": sum(a["registry_status"] == "execution-verified" for a in actions), "v3_visibility_verified": 0}})


def make_icon_map(controllers: list[dict], buttons: list[dict]) -> None:
    paths = sorted({row["icon"] for row in controllers + buttons})
    dump(ACTIVE / "config" / "icon_map.json", {"version": VERSION, "icons": [{"path": path, "status": "source_svg", "relative": True} for path in paths]})


def make_baseline_audit() -> None:
    source = ARCHIVE / "v2.9" / "AIOS_StreamDeck_Button_Map_v2.9.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    rows = data["rows"]
    texts = [row["text_or_target"] for row in rows if row["action"] == "Text"]
    boilerplate = "Text insert only. Auto-send disabled. Manual execution only."
    generic = "Summary:\nFacts used:\nAssumptions:\nRisks:\nNext step:"
    counts = {
        "cells": len(rows), "screens": len({row["screen"] for row in rows}),
        "text_actions": sum(row["action"] == "Text" for row in rows),
        "empty_cells": sum(row["action"] == "Empty" for row in rows),
        "folder_actions": sum(row["action"] == "Folder" for row in rows),
        "back_actions": sum(row["label"] == "BACK" for row in rows),
        "texts_with_repeated_safety_boilerplate": sum(boilerplate in text for text in texts),
        "repeated_safety_boilerplate_chars_including_heading": len("Safety:\n" + max((re.search(r"Safety:\n(.*?)(?:\n\n(?:Required constraints|Return|Input|Freshness|Routing|Execution truth|Output contract):)", text, re.S).group(1) for text in texts if re.search(r"Safety:\n(.*?)(?:\n\n(?:Required constraints|Return|Input|Freshness|Routing|Execution truth|Output contract):)", text, re.S)), key=len)),
        "texts_with_generic_output_schema": sum(generic in text for text in texts),
        "paste_goal_placeholders": sum("[PASTE GOAL]" in text for text in texts),
    }
    dump(ACTIVE / "qa" / "baseline_audit.json", {"source": str(source.relative_to(ROOT)), "computed_at": SNAPSHOT, "counts": counts, "physical_claims": "NOT RUN"})


def make_manifests() -> None:
    legacy_files = sorted(path for path in ARCHIVE.rglob("*") if path.is_file() and path.name != "checksums.json")
    legacy = [{"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in legacy_files]
    dump(ARCHIVE / "checksums.json", {"algorithm": "sha256", "generated": SNAPSHOT, "files": legacy})
    inventory = []
    for item in legacy:
        version = item["path"].split("/")[1]
        inventory.append({"path": item["path"], "disposition": "ARCHIVE_SUPERSEDED", "rollback_role": "active baseline" if version == "v2.7" else "candidate/evidence baseline"})
    inventory.extend([
        {"path": "StreamDeck/README.md", "disposition": "REWRITE"},
        {"path": "StreamDeck/{architecture,assets,config,exports,generated,migration,prompts,qa,tools}/**", "disposition": "KEEP_ACTIVE"},
    ])
    dump(ACTIVE / "qa" / "cleanup_inventory.json", {"generated": SNAPSHOT, "items": inventory, "deletions": [], "blocked": ["Do not delete v2.7 archive before physical acceptance."]})

    active_roots = [ACTIVE / name for name in ("architecture", "assets", "config", "exports", "generated", "migration", "prompts", "qa", "tools")]
    active_files = [ACTIVE / "README.md"]
    active_files.extend(path for root in active_roots for path in root.rglob("*") if path.is_file() and path.name != "migration_manifest.json")
    active_files = sorted(active_files)
    files = [{"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in active_files]
    dump(ACTIVE / "migration" / "migration_manifest.json", {
        "version": VERSION, "status": "candidate / ready for owner review after repo checks", "generated": SNAPSHOT,
        "os": "macOS (exact owner version NOT RUN)", "stream_deck_app_version": "owner-installed version NOT RUN; built-in cross-device switch documented since 4.4",
        "devices": {"controller": {"role": "AIOS-CONTROL", "model": "15-key Stream Deck", "serial": None}, "actions": {"role": "AIOS-ACTIONS", "model": "15-key Stream Deck", "serial": None}},
        "profile_ids": [spec[0] for spec in PROFILE_SPECS], "controller_profile_id": "A00_CONTROL",
        "action_identifiers": {"profile_switch": "Stream Deck > Switch Profile (built-in; com.elgato.streamdeck.profile.rotate)", "prompt_insert": "System > Text (built-in; com.elgato.streamdeck.system.text)", "mcp": "See migration/mcp_registry.json"},
        "insertion_method": "clipboard_paste", "auto_send": False, "target_device_binding": "manual_serial_neutral", "binary_exports": "candidate generated - import NOT RUN; owner action required",
        "physical_switch": "NOT RUN - owner action required", "files": files,
        "rollback": "Import or retain the archived v2.7/v2.9 baseline, disable controller switching, and remove only the side-by-side v3 profiles. Clipboard content overwritten by an action is not recoverable unless the owner has clipboard history.",
    })


def make_human_map(controllers: list[dict], buttons: list[dict]) -> None:
    lines = ["# AI-OS StreamDeck v3.0 — generated button map", "", "> Generated from canonical JSON by `tools/generate_v3.py`; do not edit manually.", "", "## AIOS-CONTROL", "", "| Key | Label | Target profile | Device binding |", "|---|---|---|---|"]
    for row in controllers:
        lines.append(f"| {row['button']} | {row['label']} | `{row['target_profile_id']}` | `{row['target_device_binding']}` |")
    for profile_id, profile_name, _, _ in PROFILE_SPECS:
        lines.extend(["", f"## {profile_name} (`{profile_id}`)", "", "| Key | Label | Prompt ID | Version | Owner | Insertion method | Next pass |", "|---|---|---|---|---|---|---|"])
        for row in (r for r in buttons if r["profile_id"] == profile_id):
            lines.append(f"| {row['button']} | {row['label']} | `{row['prompt_id']}` | `{row['prompt_version']}` | {row['owner_project']} | `{row['insertion_method']}` | `{row['next_on_pass']}` |")
    (ACTIVE / "generated" / "button_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    make_package()
    print("generated StreamDeck v3.0 package")
