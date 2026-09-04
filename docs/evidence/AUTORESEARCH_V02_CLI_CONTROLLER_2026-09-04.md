# AIOS AutoResearch v0.2 — Live Controller & CLI — 2026-09-04

Parent: [#409](https://github.com/sergstack/AI-OS/issues/409).
Child: [#416](https://github.com/sergstack/AI-OS/issues/416) (Integrate matched live runs, hard
gates, ledger, and stable CLI).

Status: **implementation + automated checks complete.** #416 builds the working instrument; it
does **not** run the Phase 0 calibration (#417) or the Phase 1 batch (#418). No live model /
provider / Judge call was made in producing this document.

---

## Final response format (per #416)

```text
Parent:                #409. Child #416.
Dependencies:          #412 (PR #422, merged), #413 (PR #423), #414 (PR #425), #415 (PR #426); #411 controlling.
CLI path/version:      scripts/autoresearch_cli.py, autoresearch_cli 0.2.0. Guide: docs/guides/AUTORESEARCH_CLI.md.
Commands implemented:  doctor, context, baseline, reproduce, propose, experiment, batch, report, cleanup (9).
Integrated components: autoresearch_validator (verify_ledger), autoresearch_shadow_runner (worktree / parent-fingerprint / remove), autoresearch_decision_comparator (aggregate_decision), autoresearch_context_pack_compiler #412 (compile_subject_baseline / render_summary), autoresearch_live_browser_adapter #413 (invoke / BudgetState), autoresearch_live_judge #414 (run_blind_ab / EvaluatorConfig), autoresearch_failure_intake #415 (assess_reproduction / run_researcher). All invoked through real import points; none reimplemented.
Dry-run/preview:       every external-calling verb (baseline/experiment/batch, reproduce, propose) supports --dry-run: it prints the preview (subject/researcher/judge calls counted SEPARATELY, budget before/after, worktrees, outputs) and makes ZERO external calls (exit 0). Example below.
Matched-run controls:  preview counts baseline+candidate x run_count x cases for subject, plus 2 x cases for the blind A/B Judge (both orders); config precedence explicit-flag > --batch-config > default; a real run runs doctor first, then reports blocked (exit 4) with the preview because no authorized PlaywrightMcpBrowserTransport binding is wired into a bare CLI invocation (live-contract §5/§10).
Budget/resume/cleanup: RoleBudget accounts subject/researcher/judge/retries separately, exposes remaining in doctor/experiment/report, and is authorized only with a numeric call ceiling + cost cap + currency ($0 + USD valid). RunManifest (schemas/autoresearch_run_manifest.schema.json) is the durable per-run state for bounded resume — plain done/pending/failed step vocabulary, not a second lifecycle. cleanup removes ONLY worktrees registered in the run manifest.
Tests/checks run:      20 focused #416 tests; full suite 592 passed (572 + 20); check_manifest_paths 189/189; check_repo_public_safety PASS; check_index_coverage 9/9; run-manifest schema valid draft-07. No network call in any test; active repo fingerprint asserted unchanged.
Acceptance status:     Artifact/content acceptance met. Business acceptance: the whole supported flow is operable through one documented CLI; a real end-to-end live decision is exercised only under the coordinated live session (#417).
Live Phase 0 readiness: READY for #417 to construct a Controller(transport=<real PlaywrightMcpBrowserTransport>, judge_model=<BrowserJudgeModel>, researcher_model=<BrowserResearcherModel>) once the owner signs in to the dedicated Playwright profile and a live mcp_call binding exists.
Residual limitations:  a bare CLI invocation cannot make live calls by design (blocked, exit 4); the full experiment_record -> ledger_append path is exercised by #417/#418 with real matched observations; a browser UI exposes no token/cost usage (marked not_captured).
Rollback:              remove scripts/autoresearch_cli.py, schemas/autoresearch_run_manifest.schema.json, docs/guides/AUTORESEARCH_CLI.md, tests/test_autoresearch_cli.py, this doc, and the README line. v0.1 modules and all earlier v0.2 evidence remain intact. Remove only registered ephemeral worktrees.
```

---

## Example `--dry-run` (zero external calls)

```console
$ python3 scripts/autoresearch_cli.py experiment \
    --batch-config batch.json --cases routing-01,handoff-01 --run-count 3 \
    --max-calls 40 --max-cost 0 --cost-currency USD --dry-run
{
  "verb": "experiment",
  "dry_run": true,
  "preview": {
    "action_class": "matched_live_experiment",
    "external_calls": { "subject": 12, "researcher": 0, "judge": 4, "total": 16 },
    "budget_before":      { "total_calls": 0,  "remaining_calls": 40, "authorized": true },
    "budget_after_if_run":{ "total_calls": 16, "remaining_calls": 24, "authorized": true },
    "transport_id": "playwright_mcp",
    "worktrees": ["<ephemeral candidate worktree at baseline_revision>"],
    "outputs": ["run_manifest.json", "run_report.json"],
    "note": "preview only; not authorization (AES §13.2 / live-contract §5). Zero external calls made."
  }
}
```

`doctor` on the same authorized batch prints `=> READY` and exits `0`; with no `--batch-config`
it prints the failing gate and exits `3`. `experiment` without `--dry-run` and without a wired
transport binding prints `"status": "blocked"` with the preview and exits `4`.

---

## Rollback

Remove the five child-owned files listed above plus the one `docs/evidence/README.md` index
line. No v0.1 module, earlier v0.2 evidence, Project configuration, or active AI-OS behaviour is
touched.

---

## Checks run

```bash
python3 -m pytest tests/test_autoresearch_cli.py -q         # 20 passed
python3 -m pytest tests/ -q                                 # 592 passed
python3 scripts/autoresearch_cli.py --help                  # documents verbs, exit codes, precedence, examples
python3 -m json.tool schemas/autoresearch_run_manifest.schema.json   # parses
python3 scripts/check_manifest_paths.py                     # 189/189
python3 scripts/check_repo_public_safety.py                 # PASS
python3 scripts/check_index_coverage.py                     # 9/9
```

This document was scanned for secrets, raw credentials, personal data, and unsupported live-run
claims before commit: none found. No live call has occurred.
