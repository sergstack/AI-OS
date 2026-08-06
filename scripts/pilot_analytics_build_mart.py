#!/usr/bin/env python3
"""AES Phase 4 Analytics pilot: RAW -> STAGE -> MART build + reconciliation.

SYNTHETIC PILOT SCRIPT. Operates only on the fictional fixture data under
docs/autonomous_execution/pilot_fixtures/analytics/ (see DATA_CONTRACT.md
in that directory). Not connected to any real data source, mart-building
pipeline, or business system. This script exists solely to give the AES
Phase 4 Analytics pilot (docs/pilots/AES_ANALYTICS_PILOT.md) a real,
runnable RAW -> STAGE -> MART -> reconciliation flow to execute against.

Deterministic: no randomness, no wall-clock-dependent values in the
computed data (only the JSON metadata carries a generation timestamp).

Usage:
    python3 scripts/pilot_analytics_build_mart.py

Exit code 0 on reconciliation PASS, 1 on reconciliation FAIL.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent.parent / "docs" / "autonomous_execution" / "pilot_fixtures" / "analytics"
RAW_PATH = FIXTURE_DIR / "raw_sales.csv"
STAGE_CSV_PATH = FIXTURE_DIR / "stage_sales.csv"
MART_CSV_PATH = FIXTURE_DIR / "mart_sales_by_quarter.csv"
MART_JSON_PATH = FIXTURE_DIR / "mart_sales_by_quarter.json"
RECONCILIATION_JSON_PATH = FIXTURE_DIR / "reconciliation_report.json"

REQUIRED_COLUMNS = ["order_id", "quarter", "region", "product", "units", "unit_price_usd", "status"]
ALLOWED_QUARTERS = {"Q1", "Q2"}
ALLOWED_STATUSES = {"completed", "cancelled"}
ALLOWED_REGIONS = {"North", "South"}


@dataclass
class RawRow:
    order_id: str
    quarter: str
    region: str
    product: str
    units: int
    unit_price_usd: float
    status: str


def read_raw(path: Path) -> list[RawRow]:
    """Read the RAW CSV, skipping '#' comment lines, per DATA_CONTRACT.md."""
    rows: list[RawRow] = []
    with path.open(newline="") as fh:
        lines = [line for line in fh if not line.lstrip().startswith("#")]
    reader = csv.DictReader(lines)
    for line in reader:
        for col in REQUIRED_COLUMNS:
            if not line.get(col):
                raise ValueError(f"RAW row missing required column {col!r}: {line}")
        rows.append(
            RawRow(
                order_id=line["order_id"],
                quarter=line["quarter"],
                region=line["region"],
                product=line["product"],
                units=int(line["units"]),
                unit_price_usd=float(line["unit_price_usd"]),
                status=line["status"],
            )
        )
    return rows


def build_stage(raw_rows: list[RawRow]) -> list[dict]:
    """RAW -> STAGE: validate/normalize, per DATA_CONTRACT.md metric_rules.

    metric_rules requires revenue_usd = units * unit_price_usd computed
    for every row (STAGE keeps a revenue_usd figure for all valid rows,
    completed or cancelled, so downstream consumers can see what a
    cancelled order *would have been* worth). The exclusion of cancelled
    orders from reported revenue is a MART-level rule (see build_mart),
    not a STAGE-level rule.
    """
    stage_rows: list[dict] = []
    seen_ids: set[str] = set()
    for row in raw_rows:
        if row.order_id in seen_ids:
            raise ValueError(f"duplicate order_id in RAW: {row.order_id}")
        seen_ids.add(row.order_id)
        if row.quarter not in ALLOWED_QUARTERS:
            raise ValueError(f"quarter {row.quarter!r} not in allowed set for {row.order_id}")
        if row.status not in ALLOWED_STATUSES:
            raise ValueError(f"status {row.status!r} not in allowed set for {row.order_id}")
        if row.region not in ALLOWED_REGIONS:
            raise ValueError(f"region {row.region!r} not in allowed set for {row.order_id}")

        revenue_usd = round(row.units * row.unit_price_usd, 2)

        stage_rows.append(
            {
                "order_id": row.order_id,
                "quarter": row.quarter,
                "region": row.region,
                "product": row.product,
                "units": row.units,
                "unit_price_usd": row.unit_price_usd,
                "status": row.status,
                "revenue_usd": revenue_usd,
            }
        )
    return stage_rows


def build_mart(stage_rows: list[dict]) -> list[dict]:
    """STAGE -> MART: aggregate to (quarter, region, product) grain.

    MART only aggregates completed-order revenue (per DATA_CONTRACT.md
    metric_rules: "revenue_usd = units * unit_price_usd, only for rows
    with status = completed ... cancelled orders must be excluded from
    revenue"). MART sums STAGE's per-row revenue_usd, grouped by
    (quarter, region, product).

    FIX (def-001, applied in iter-002): an earlier build of this function
    omitted the `status == "completed"` filter below, so it aggregated
    revenue_usd for every STAGE row regardless of status. Cancelled-order
    revenue silently leaked into the MART totals, so MART did not
    reconcile against the contract-defined RAW total (see PILOT_MEMO.md
    and docs/pilots/AES_ANALYTICS_PILOT_RESULTS.md for the before/after
    evidence). The filter below is the minimal fix.
    """
    grouped: dict[tuple, float] = defaultdict(float)
    grouped_units: dict[tuple, int] = defaultdict(int)
    for row in stage_rows:
        if row["status"] != "completed":
            continue
        key = (row["quarter"], row["region"], row["product"])
        grouped[key] += row["revenue_usd"]
        grouped_units[key] += row["units"]

    mart_rows = []
    for (quarter, region, product), revenue in sorted(grouped.items()):
        mart_rows.append(
            {
                "quarter": quarter,
                "region": region,
                "product": product,
                "units": grouped_units[(quarter, region, product)],
                "revenue_usd": round(revenue, 2),
            }
        )
    return mart_rows


def quarter_growth(mart_rows: list[dict]) -> dict:
    """Formula: quarter-over-quarter total revenue growth %.

    growth_pct = (Q2_total - Q1_total) / Q1_total * 100
    """
    q1_total = round(sum(r["revenue_usd"] for r in mart_rows if r["quarter"] == "Q1"), 2)
    q2_total = round(sum(r["revenue_usd"] for r in mart_rows if r["quarter"] == "Q2"), 2)
    growth_pct = None
    if q1_total:
        growth_pct = round((q2_total - q1_total) / q1_total * 100, 2)
    return {"q1_total_revenue_usd": q1_total, "q2_total_revenue_usd": q2_total, "growth_pct": growth_pct}


def reconcile(raw_rows: list[RawRow], stage_rows: list[dict], mart_rows: list[dict]) -> dict:
    """RAW == STAGE == MART reconciliation, per DATA_CONTRACT.md validation_checks.

    contract_expected_revenue_usd: computed directly from RAW, applying
    the metric_rules filter (status == "completed") independently of
    whatever STAGE/MART did. This is the ground truth the pipeline must
    reconcile against - it does NOT reuse STAGE's revenue_usd, so a bug
    in STAGE cannot silently pass reconciliation.
    """
    contract_expected_revenue_usd = round(
        sum(r.units * r.unit_price_usd for r in raw_rows if r.status == "completed"), 2
    )
    stage_completed_revenue_usd = round(
        sum(r["revenue_usd"] for r in stage_rows if r["status"] == "completed"), 2
    )
    mart_total_revenue_usd = round(sum(r["revenue_usd"] for r in mart_rows), 2)

    raw_row_count = len(raw_rows)
    stage_row_count = len(stage_rows)
    raw_completed_count = sum(1 for r in raw_rows if r.status == "completed")
    mart_row_units = sum(r["units"] for r in mart_rows)
    raw_completed_units = sum(r.units for r in raw_rows if r.status == "completed")

    checks = {
        "raw_row_count_equals_stage_row_count": raw_row_count == stage_row_count,
        "contract_expected_revenue_equals_stage_completed_revenue": (
            contract_expected_revenue_usd == stage_completed_revenue_usd
        ),
        "stage_completed_revenue_equals_mart_total_revenue": (
            stage_completed_revenue_usd == mart_total_revenue_usd
        ),
        "contract_expected_revenue_equals_mart_total_revenue": (
            contract_expected_revenue_usd == mart_total_revenue_usd
        ),
        "mart_units_equal_raw_completed_units_no_double_counting": (
            mart_row_units == raw_completed_units
        ),
    }
    overall_pass = all(checks.values())

    return {
        "raw_row_count": raw_row_count,
        "stage_row_count": stage_row_count,
        "raw_completed_order_count": raw_completed_count,
        "contract_expected_revenue_usd": contract_expected_revenue_usd,
        "stage_completed_revenue_usd": stage_completed_revenue_usd,
        "mart_total_revenue_usd": mart_total_revenue_usd,
        "raw_completed_units": raw_completed_units,
        "mart_total_units": mart_row_units,
        "checks": checks,
        "overall_pass": overall_pass,
    }


def write_stage_csv(stage_rows: list[dict], path: Path) -> None:
    fieldnames = ["order_id", "quarter", "region", "product", "units", "unit_price_usd", "status", "revenue_usd"]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in stage_rows:
            writer.writerow(row)


def write_mart_csv(mart_rows: list[dict], path: Path) -> None:
    fieldnames = ["quarter", "region", "product", "units", "revenue_usd"]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in mart_rows:
            writer.writerow(row)


def main() -> int:
    raw_rows = read_raw(RAW_PATH)
    stage_rows = build_stage(raw_rows)
    mart_rows = build_mart(stage_rows)
    growth = quarter_growth(mart_rows)
    recon = reconcile(raw_rows, stage_rows, mart_rows)

    write_stage_csv(stage_rows, STAGE_CSV_PATH)
    write_mart_csv(mart_rows, MART_CSV_PATH)

    mart_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "grain": "quarter x region x product",
        "rows": mart_rows,
        "formula": {
            "name": "quarter_over_quarter_revenue_growth_pct",
            "definition": "(Q2_total_revenue_usd - Q1_total_revenue_usd) / Q1_total_revenue_usd * 100",
            **growth,
        },
    }
    MART_JSON_PATH.write_text(json.dumps(mart_payload, indent=2) + "\n")
    RECONCILIATION_JSON_PATH.write_text(json.dumps(recon, indent=2) + "\n")

    print("=== AES Phase 4 Analytics pilot: RAW -> STAGE -> MART reconciliation ===")
    print(f"RAW rows: {recon['raw_row_count']}, STAGE rows: {recon['stage_row_count']}")
    print(f"contract_expected_revenue_usd (RAW, completed-only): {recon['contract_expected_revenue_usd']}")
    print(f"stage_completed_revenue_usd:                          {recon['stage_completed_revenue_usd']}")
    print(f"mart_total_revenue_usd:                                {recon['mart_total_revenue_usd']}")
    for name, ok in recon["checks"].items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"Q1 total revenue (mart): {growth['q1_total_revenue_usd']}")
    print(f"Q2 total revenue (mart): {growth['q2_total_revenue_usd']}")
    print(f"QoQ growth_pct: {growth['growth_pct']}")

    if recon["overall_pass"]:
        print("RECONCILIATION: PASS")
        return 0
    print("RECONCILIATION: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
