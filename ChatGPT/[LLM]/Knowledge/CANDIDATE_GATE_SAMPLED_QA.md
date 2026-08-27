# Candidate Gate Sampled QA

Status: `candidate / ready for owner review`.

## Purpose and boundary

This is a reusable QA procedure for Candidate Gate. It evaluates a bounded
sample of results actually selected in one current run. It does not create a
permanent dataset, corpus registry, or manifest layer; it does not require
historical frozen artifacts; and it does not change Candidate Gate
automatically.

The sample record is run-scoped evidence: retain its selection timestamp or
run identifier, the stable identifiers of selected results, and the current
Candidate Gate revision in that run's issue or PR evidence. It exists only to
make the before/after replay for that QA run reproducible.

## Procedure

1. Select a bounded sample from results that Candidate Gate actually selected
   in the current run. Freeze the sample membership before review.
2. An owner or designated reviewer assigns exactly one label to each sampled
   result: `relevant`, `adjacent`, `irrelevant`, or `uncertain`.
3. Calculate observed precision for this reviewed sample only:

   ```text
   observed_precision = relevant / (relevant + adjacent + irrelevant)
   ```

   Exclude `uncertain` from the denominator and report its count separately.
   Do not report recall: no labelled denominator of all relevant results is
   available from this procedure.
4. List every sampled `irrelevant` result as a false positive. Include its
   query-family and Candidate Gate rule attribution when that attribution is
   available; otherwise record `attribution: unavailable`.
5. Propose at most one minimal candidate-rule change, with the exact intended
   effect and a rollback statement. This is a proposal, not an applied change.
6. Replay the proposed change against the identical frozen sample. Do not add,
   remove, or relabel sample members between the before and after comparison.
7. Compare before and after: selected membership, reviewed-label counts,
   observed precision, `uncertain` count, and false positives with available
   attribution.
8. The owner explicitly accepts or rejects the proposal. Only an accepted,
   separately scoped implementation may change Candidate Gate.

## Required run evidence

Record only the following bounded fields for each QA run:

- current-run identifier or timestamp and Candidate Gate revision;
- sample size, membership identifiers, and evidence that members were
  actually selected by the current run;
- reviewer identity or owner-review reference, each of the four permitted
  labels, and the `uncertain` count;
- observed-precision numerator and denominator, explicitly scoped to the
  reviewed sample;
- false-positive list and query-family/rule attribution where available;
- proposed change, replay result on the same sample, before/after comparison,
  owner decision, and rollback path.

## Stop conditions

- No reviewer labels: stop before calculating observed precision.
- Sample membership cannot be tied to results selected by the current run:
  stop; do not substitute a historical or synthetic corpus.
- No labelled denominator beyond the sample: report no recall.
- Attribution is unavailable: retain the false positive and mark attribution
  unavailable; do not infer a query family or rule.
- Owner decision is absent or rejects the proposal: retain evidence only; do
  not change Candidate Gate.

## Acceptance examples

| Scenario | Expected result |
| --- | --- |
| Reviewed sample includes `uncertain` labels | Precision excludes only those entries and reports their count. |
| All labels are reviewed but no denominator of all relevant results exists | Observed sample precision may be reported; recall is not reported. |
| Replay improves observed precision but owner has not accepted the change | `candidate / ready for owner review`; Candidate Gate remains unchanged. |
| A false positive has no stored rule attribution | Include it with `attribution: unavailable`; do not manufacture an explanation. |

## Rollback

This procedure is documentation only. Revert its PR to remove the procedure;
it does not alter Candidate Gate behavior or any runtime state.
