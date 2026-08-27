# Failure Registry

## Purpose

Record a real observed workflow failure before considering a bounded regression
case. This is a documentation contract, not a runtime database, autonomous
failure miner, or automatic corrective loop.

## Failure record

```text
failure_id:
date:
owner_project:
workflow:
scenario:
expected_behavior:
observed_behavior:
failure_class:
evidence:
severity: low | medium | high | critical
status: candidate | confirmed | fixed | blocked | retired
related_change:
regression_test_id:
```

`candidate` means evidence is insufficient. Confirmation requires a failed
deterministic check, violated explicit contract/governance rule, reproducible
difference from expected behavior, or human confirmation. A disliked output is
not confirmation by itself.

## Failure to regression rule

Create a bounded regression case only when a confirmed failure can recur, has
material impact or violates an important contract, and has a visible expected
behavior. Not every failure needs a permanent test.

```text
test_id:
source_failure_id:
owner_project:
scenario:
input:
expected_contract:
deterministic_checks:
judge_checks:
severity:
```

Deterministic checks take priority. A Judge is permitted only for explicitly
semantic criteria. High/critical cases may use at most three controlled wording
variants; this remains bounded QA, not autonomous test generation.

## Lifecycle and boundaries

```text
observed → candidate → confirmed → regression case → fixed | blocked | retired
```

The owner decides corrective work. This registry neither changes a workflow nor
authorizes a repository change, promotion, retrieval capability, or automatic
fix. Rollback is the existing revert/manual-review path for an approved change.
