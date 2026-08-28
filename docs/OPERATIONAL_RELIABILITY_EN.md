# Operational Reliability — Candidate Contract

[English](OPERATIONAL_RELIABILITY_EN.md) | [Русский](OPERATIONAL_RELIABILITY.md)

## Status and purpose

Status: `candidate`. This paired document describes a possible operational
reliability layer for recording evidence, run intent, faults, and regressions
in a reviewable form. It is a documentation contract only. It does not create
a runtime service, persistent memory, autonomous retrieval, automatic policy
change, or production workflow.

The repository's active source-of-truth, routing, validation, and acceptance
rules remain unchanged. If this candidate is ever activated, it requires an
identifiable version, evaluation cases, observed results, owner acceptance, and
an explicit scope decision.

## The four candidate contracts

| Shared mechanic | English name | Russian name |
| --- | --- | --- |
| Evidence lifecycle | Evidence lifecycle ledger | Журнал жизненного цикла evidence |
| Run intent | Versioned run intent | Версионированное намерение запуска |
| Failure observability | Typed fault telemetry | Типизированная телеметрия сбоев |
| Turning failure into a check | Failure-to-regression harness | Контур «сбой → регрессия» |

### 1. Evidence lifecycle ledger

An `EvidenceUnit` is a bounded reference to observed evidence, its provenance,
scope, and lifecycle status. The exact status names are `ACTIVE`,
`SUPERSEDED`, and `REVOKED`.

- `ACTIVE` means the unit is the current referenced evidence for its declared
  scope; it does not mean accepted, complete, or production-ready.
- `SUPERSEDED` means a later identified unit replaces it for the same declared
  scope; the earlier evidence remains traceable.
- `REVOKED` means the evidence must not be relied on for its prior claim; the
  reason and replacement state must remain visible.

This candidate does not authorize an agent to infer lifecycle status from text
alone or to delete historical evidence.

### 2. Versioned run intent

A run records the goal, scope, constraints, expected evidence, and relevant
contract version it was authorized to use. The intent is versioned so a later
reader can distinguish a result produced under an earlier scope from one
produced under a revised scope.

The candidate rule is `fail-closed` when a required intent reference is absent,
ambiguous, or incompatible with the requested action: stop and report the
missing decision instead of silently substituting a current intent.

### 3. Typed fault telemetry

A fault record uses a named type, affected scope, observed evidence, and
disposition. It makes failures reviewable without converting every warning into
a system-wide policy change. A `digest` may summarize multiple records, but it
must not erase their identifiers, scope, or unresolved state.

`Candidate Gate` and `Human Gold` remain exact names when they occur in a
related evaluation context. They are not synonyms and this candidate does not
alter either gate, its data, its criteria, or its owner decision.

### 4. Failure-to-regression harness

When a material, evidenced failure is corrected, the correction should be
paired with a bounded replay or deterministic check that can detect the same
failure class. The harness links the observed fault, the correction scope, the
check, and the result; it does not claim general prevention beyond that scope.

It must not fabricate a regression test when the failure cannot be reproduced,
use a passing unrelated check as proof of correction, or automatically promote
a candidate change.

## Boundaries and adoption gate

This candidate layer does not change project routing, owner boundaries,
canonical governance semantics, formulas, model routing, or external ChatGPT
Project state. It cannot independently authorize merge, deployment, production
promotion, a change to `Candidate Gate`, or a `Human Gold` decision.

Before any activation, record: candidate version, target scope, evaluation
cases, Judge results, revisions applied where required, final acceptance, and
owner acceptance. Until then, existing canonical documents remain authoritative:
[Goal Mode](../GOAL_MODE.md), [Sync Contract](../SYNC_CONTRACT.md),
[AES](standards/AUTONOMOUS_EXECUTION_STANDARD.md), and
[Master Status](../MASTER_STATUS.md).
