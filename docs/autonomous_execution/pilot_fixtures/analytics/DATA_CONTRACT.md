# Data Contract — Analytics Pilot Fixture (SYNTHETIC)

> **This dataset is 100% fictional pilot/test data.** It was invented for
> Phase 4 of the Autonomous Execution Standard (AES) rollout, to exercise
> the `[Analytics]` methodology (data contract -> mapping -> RAW/STAGE/MART
> reconciliation -> formulas -> findings -> memo -> Judge -> correction ->
> rebuild -> final acceptance) end to end. It is **not** derived from, and
> does not resemble, any real company's sales, revenue, or business data.
> No conclusion drawn from it is a real business claim. See
> `docs/pilots/AES_ANALYTICS_PILOT_RESULTS.md` for the scope note on why a
> synthetic fixture was used instead of a real governed dataset (this
> repository has no real Analytics data infrastructure to run the pilot
> against — see that document's "Scope deviation" section).

Follows the minimum contract shape in
`ChatGPT/[Analytics]/Knowledge/DATA_CONTRACTS.md`.

```text
Dataset:            pilot_synthetic_sales
Owner:               AES Phase 4 pilot (Analytics extension)
Business owner:      n/a (synthetic pilot, no real business owner)
Technical owner:      AES Phase 4 executor
Source:               fabricated for this pilot; not sourced from any system
Source file / system:  docs/autonomous_execution/pilot_fixtures/analytics/raw_sales.csv
Refresh frequency:    one-time, static pilot fixture (no refresh)
Load timestamp:       2026-08-06T00:00:00Z (fixture creation)
Period:               2026-Q1 vs 2026-Q2 (two synthetic quarters, fictional)
Grain:                one row per (order_id) = one synthetic sales order line
Primary keys:         order_id
Foreign keys:         none (single-table fixture)
Required columns:     order_id, quarter, region, product, units, unit_price_usd,
                       status
Optional columns:     none
Column types:         order_id: string; quarter: string (Q1/Q2);
                       region: string; product: string; units: integer;
                       unit_price_usd: decimal(2); status: string
                       (enum: completed, cancelled)
Allowed values:       quarter in {Q1, Q2}; status in {completed, cancelled};
                       region in {North, South}; product in
                       {Widget A, Widget B, Widget C}
Date logic:           quarter is a coarse period label, not a calendar date;
                       no timezone handling needed at this grain
Currency / units:     unit_price_usd is in whole US dollars (synthetic,
                       fictional currency values); units is a raw count
Null policy:          no nulls allowed in any required column; a row with a
                       null in a required column is dropped at STAGE and
                       logged, not silently kept
Duplicate policy:     order_id must be unique; duplicate order_id is a data
                       defect, not summed
Freshness rule:       not applicable (static fixture, freshness pinned to
                       fixture creation date above)
Mapping rules:        none beyond the enum allow-lists above
Join rules:            none (single table)
Metric rules:         revenue_usd = units * unit_price_usd, only for rows
                       with status = "completed" (cancelled orders must be
                       excluded from revenue — this is the rule the
                       injected defect violates, see PILOT_MEMO.md)
Classification rules:  region and product are dimensions for the MART
                       aggregation; no further classification
Validation checks:    RAW total units/revenue-eligible-row-count must equal
                       STAGE total; STAGE sum(revenue_usd) must equal MART
                       sum(revenue_usd) (reconciliation, no double counting)
Known limitations:    tiny fixture (16 rows), two-quarter comparison only,
                       no seasonality/outlier handling, synthetic numbers
                       chosen for illustrative round percentages
Expected outputs:     mart_sales_by_quarter.csv/json (grain: quarter x
                       region x product), with revenue_usd and a
                       quarter-over-quarter revenue growth % formula
```

## Entity / grain / period / currency summary (Analytics extension
## expectations, `AUTONOMOUS_EXECUTION_EXTENSION_CONTRACT.md` Section 5.2)

- **Entity**: a synthetic sales order line (`raw_sales.csv`, one row per
  `order_id`).
- **Grain (RAW/STAGE)**: one row per order line. **Grain (MART)**: one row
  per `(quarter, region, product)`.
- **Keys**: `order_id` (RAW/STAGE primary key); `(quarter, region,
  product)` (MART grouping key).
- **Period**: two fictional quarters, `Q1` and `Q2` of a synthetic year
  ("2026", used only as a label, not a real fiscal period).
- **Currency / unit**: `unit_price_usd` — synthetic USD-denominated unit
  price; `units` — raw unit count; `revenue_usd` — derived metric
  (`units * unit_price_usd`), synthetic USD.
