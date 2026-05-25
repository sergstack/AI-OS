# Main Files Standard

## Purpose

Закрепить правило: в stage и mart создаются не только нарезки, но и главные переносимые файлы.

## Main principle

```text
Slices are secondary.
Main files are primary.
```

Правильная логика:

```text
RAW
→ stage_main_full
→ mart_main_full
→ mart_main_tz / mart_main_compact
→ slices from mart_main_full
→ charts / memo / dashboard / Excel
```

Неправильная логика:

```text
raw slice
→ mini mart
→ isolated conclusion
```

## Stage main file

### Required artifact

```text
stage_main_full
```

### Purpose

Главный stage-файл — собранный, очищенный, нормализованный и типизированный массив данных без бизнес-метрик и аналитических классификаторов.

Он должен быть пригоден для переноса в:

- database;
- dashboard;
- Excel;
- BI semantic layer;
- downstream mart build.

### Contains

- source file / source system;
- source version;
- load timestamp;
- period;
- date fields;
- entity keys;
- raw business fields after normalization;
- normalized dimensions;
- mapped IDs;
- currency / unit;
- technical lineage fields;
- row status for technical issues.

### Does not contain

- business metrics;
- classification labels;
- materiality flags;
- risk labels;
- confidence labels;
- interpretation;
- memo text;
- management conclusions.

### Stage slices

Allowed only after `stage_main_full`.

Examples:

- `stage_slice_by_source`;
- `stage_slice_by_period`;
- `stage_slice_unmatched_rows`;
- `stage_slice_for_reconciliation`.

## Mart main files

### Required artifacts

```text
mart_main_full
mart_main_tz
```

or

```text
mart_main_full
mart_main_compact
```

### `mart_main_full`

Purpose: full analysis-ready table for Sergey, Finance Team, deep conclusions and evidence.

Contains:

- all metrics required for analysis;
- all metric formulas documented;
- all business dimensions;
- grain and keys;
- classification flags;
- materiality fields;
- variance fields;
- driver fields;
- timing fields;
- risk fields;
- confidence fields;
- action fields where relevant;
- QA fields;
- evidence reference fields;
- source lineage.

### `mart_main_tz` / `mart_main_compact`

Purpose: shortened management-ready mart according to the task, audience or executive memo.

Contains:

- only decision-relevant fields;
- headline metrics;
- top deviations;
- materiality;
- risk summary;
- confidence;
- visible limitations;
- references back to `mart_main_full`.

Does not replace `mart_main_full`.

## Slice rule

All slices must be derived from `mart_main_full`.

Each slice must state:

```text
slice_name:
source_mart: mart_main_full
filter_logic:
grain:
metrics:
purpose:
used_for: chart / memo / QA / dashboard / appendix
```

## Compact/full JSON input logic

### Both compact and full provided

```text
json compact → executive requirements and short output
json full → full data/method/evidence requirements
```

Use both:

- full builds `stage_main_full` and `mart_main_full`;
- compact builds `mart_main_tz/compact` and memo focus.

### Only compact provided

Build a scoped version:

- define minimal data contract;
- define required main files;
- mark missing fields;
- avoid unsupported claims;
- create assumptions register.

## Naming convention

Recommended names:

```text
stage_main_full__<domain>__<period>__v<version>
mart_main_full__<domain>__<period>__v<version>
mart_main_compact__<domain>__<period>__v<version>
mart_slice_<purpose>__<domain>__<period>__v<version>
```

## Acceptance criteria

- [ ] `stage_main_full` exists or is explicitly designed.
- [ ] `stage_main_full` has no metrics/classifiers.
- [ ] `mart_main_full` exists or is explicitly designed.
- [ ] `mart_main_tz` or `mart_main_compact` exists or is explicitly designed.
- [ ] Mart metrics and formulas documented.
- [ ] Slices are derived from `mart_main_full`.
- [ ] Charts and memo reference mart/slice source.
- [ ] QA totals available.
- [ ] Limitations recorded.
