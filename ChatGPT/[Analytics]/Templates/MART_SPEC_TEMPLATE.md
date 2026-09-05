# Mart Spec Template

mart_name:
business purpose:
audience:
grain:
period:
keys:
mode:
field_budget:
visible_columns:
hidden_evidence_columns:
excluded_fields:
reason_for_each_extra_metric:
compact_front_view: yes/no
source stage files:
source stage main file:
metrics:
formulas:
metric_definition_cards (material/flagship/ratio-like): see Templates/METRIC_DEFINITION_CARD_TEMPLATE.md
dimensions:
classifiers:
filters:
QA totals:
evidence fields:
value_state_preserved: yes/no (VALUE_STATE not collapsed to generic null where material)
limitations:

## Required main mart files

mart_main_full:
mart_main_tz / compact:

## Slices

| slice_name | source_mart | filter_logic | grain | metrics | purpose |
|---|---|---|---|---|---|
| | mart_main_full | | | | |
