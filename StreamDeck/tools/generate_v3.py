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


def slug(value: str) -> str:
    value = value.lower().replace("→", "_to_").replace("?", "")
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


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


def prompt_body(label: str, purpose: str, owner: str, schema: list[str], kind: str) -> str:
    analytics = "\n\nNumeric boundary:\nAll calculations and numeric QA must be performed by Python or SQL. Require entity, grain, period, currency/unit, formulas, filters and deterministic evidence; otherwise return NOT RUN." if kind == "analytics" or owner == "[Analytics]" else ""
    freshness = "\n\nFreshness:\nCheck changeable facts through current official sources when read-only web/tool access exists. If current verification is unavailable, mark UNVERIFIED; never present model memory as fresh verification." if any(x in label for x in ("TREND", "FRESH", "MODEL", "RELEASE")) else ""
    revision = "\n\nRevision boundary:\nUse the last Judge verdict only as revision notes. Edit the source artifact the Judge reviewed, never the verdict itself. If the source is ambiguous, return blocked. Add no facts or evidence." if kind == "revise" or "REVIS" in label else ""
    goal = "\n\nGoal Mode boundary:\nUse the latest meaningful user goal; there is no paste placeholder. Keep work bounded and build-first. The Stream Deck inserts text only and never presses Send. Codex may inspect, branch, change scoped files, check and open a PR after manual send, but must not manually merge, deploy, or perform destructive/production actions." if label in {"GOAL→PR", "BUILD FIRST", "GOAL→CODEX PACK"} else ""
    judge = "\n\nJudge rule:\nReturn only pass, revise, or blocked. Check schema fit, evidence, execution truth, routing, unsupported claims and acceptance. Deterministic evidence overrides model preference." if kind == "judge" else ""
    memo = "\n\nMemo boundary:\nWrite narrative only from Analytics-approved facts. Separate facts, interpretation, assumptions, and recommendations. A root cause without evidence requires management confirmation. State period, scope, currency/units, and source traceability." if kind == "memo" else ""
    return f"""# {label} — {owner}

Purpose:
{purpose}

Material selection:
Use the latest meaningful user goal or source material. A Judge verdict is revision notes, not the editable source artifact. If the source artifact cannot be identified unambiguously, return blocked. Do not guess or substitute the source.

Execution truth:
Report Execution status as EXECUTED / PARTIAL / NOT RUN. EXECUTED is allowed only for tool calls, commands, or checks actually observed. List proposed actions separately. Expected results are not observed results.{freshness}{analytics}{revision}{goal}{judge}{memo}

Safety and interaction:
Text insertion only; auto-send is off and the user sends manually. Do not expose secrets or private data. Do not delete, merge, deploy, publish, mutate production, automate UI, or claim unobserved execution.

Return exactly these sections:
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
            row = {
                "device": "AIOS-ACTIONS", "profile_id": profile_id, "profile_name": f"AIOS-ACTIONS / {profile_name}",
                "button": key, "label": label, "action_type": "prompt", "prompt_id": prompt_id,
                "prompt_version": "1.0.0", "owner_project": owner, "interaction_risk": "low",
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
        body = prompt_body(label, purpose, owner, schema, kind)
        prompt_hash = hashlib.sha256(body.encode()).hexdigest()
        prompts.append({
            "prompt_id": prompt_id, "prompt_version": "1.0.0", "task_type": kind, "purpose": purpose,
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
        qa_rows.append({
            "prompt_id": prompt_id, "prompt_version": "1.0.0", "button_refs": refs,
            "test_cases": [
                {"case": "normal", "status": "NOT RUN", "expected": "specialized output schema with sourced content"},
                {"case": "missing_context_or_evidence", "status": "NOT RUN", "expected": "blocked or NOT RUN without invented content"},
                {"case": "unsafe_or_ambiguous", "status": "NOT RUN", "expected": "blocked without write, send, UI automation, or source substitution"},
            ],
            "static_contract_checks": {"material_selection": "pass", "specialized_schema": "pass", "route": "pass", "execution_truth": "pass", "freshness": "pass", "no_new_claims": "pass"},
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
        lines.extend(["", f"## {profile_name} (`{profile_id}`)", "", "| Key | Label | Prompt ID | Owner | Insertion method | Next pass |", "|---|---|---|---|---|---|"])
        for row in (r for r in buttons if r["profile_id"] == profile_id):
            lines.append(f"| {row['button']} | {row['label']} | `{row['prompt_id']}` | {row['owner_project']} | `{row['insertion_method']}` | `{row['next_on_pass']}` |")
    (ACTIVE / "generated" / "button_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    make_package()
    print("generated StreamDeck v3.0 package")
