# Analytical Memo Rubric

## Purpose

Define what a good analytical memo means for `[Analytics]`.

## Rubric

| Area | Pass condition | Fail condition |
|---|---|---|
| Executive verdict | Answers the business question | Finding catalogue without a verdict |
| Prioritization | Smallest sufficient set ranked by an explicit business criterion | Mechanical Top-3 or `ABS Delta` treated as universal importance |
| Business meaning | Each headline has supported meaning or an explicit evidence gap | Manufactured “so what” |
| Performance dimensions | Materially different dimensions remain distinct | Unsupported overall good/bad assessment |
| Effect type | Business effect and data/control artefact are separated where relevant | Data exception presented as economic effect without evidence |
| Evidence | Key conclusions trace to mart/evidence | Unsupported claims |
| Claim gate | Headline claim has complete Claim/Evidence Registry lineage (`allowed_in_executive = yes`) | Headline claim published with `allowed_in_executive = no` or no `method_execution_id`/`evidence_id` |
| Metric semantics | Flagship/ratio-like metric has an approved `METRIC_DEFINITION_CARD` | Ambiguous formula (e.g. undefined numerator/denominator) presented as a flagship result |
| Numbers | Key figures have metric, period, grain, source | Numbers without source |
| Drivers | Drivers ranked by relevant business impact | Decorative or mechanically ranked explanation |
| Risk | Risk has `risk_basis` | Risk without basis |
| Management implication | Decision/action is stated only if supported; otherwise monitoring, validation, no action, or uncertainty remains explicit | Decision manufactured from an observation |
| Thinking boundary | Analytics provides evidence and implication; strategic trade-offs remain with `[Thinking]` | Analytics chooses a strategic option without supported criteria |
| Compression | Executive layer is materially shorter than supporting evidence | Synthesis becomes a second analytical report |
| Confidence | Confidence and limitations visible | Low confidence as fact |
| Language | Russian, business-readable executive body | Technical IDs in executive body |
| Charts | Source mart, metric, period, grain visible | Caption stronger than data |

## Golden memo criteria

A memo is strong when:

- executive summary is short and evidence-backed;
- numbers are in tables and prose;
- material conclusions are ranked by an explicit business criterion;
- confirmed causes and hypotheses are separated;
- no headline claim appears without complete Claim/Evidence Registry lineage;
- limitations are visible before appendix;
- management implication does not exceed verified evidence;
- executive synthesis is materially shorter than the evidence layer;
- appendix / evidence layer supports deep claims.
