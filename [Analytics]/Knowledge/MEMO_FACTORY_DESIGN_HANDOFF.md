# Memo Factory Design Handoff

## Purpose

Define how analytical memo design moves from Analytics Project to Codex implementation and Ollama daily generation.

## Core separation

```text
[Analytics] Project = design + governance + reasoning
Codex repo = production implementation
Ollama = local daily reasoning over prepared payload
JSON layer = source facts
Templates = formatting
```

## Lifecycle

1. Prepare data for GPT / Analytics.
2. Convert XLSX / CSV / exports into:

   * `*.full.json`
   * `*.compact.json`
3. Use `[Analytics]` to design memo:

   * audience;
   * business decision;
   * period;
   * currency;
   * grain;
   * metrics;
   * dimensions;
   * limitations;
   * allowed conclusions;
   * forbidden conclusions.
4. Create design package:

   * `01_MEMO_DESIGN_BRIEF.md`
   * `02_REFERENCE_MEMO.md`
   * `03_METRICS_SPEC.md`
   * `04_SIGNAL_CATALOG.md`
   * `05_EVIDENCE_RULES.md`
   * `06_OLLAMA_ANALYST_PROMPT.md`
   * `07_OLLAMA_JUDGE_PROMPT.md`
   * `08_ACCEPTANCE_CRITERIA.md`
5. Handoff to `[Codex]`.
6. Codex implements deterministic pipeline.
7. Ollama writes daily memo only from prepared payload.
8. Judge checks evidence and unsupported claims.
9. Report is exported to markdown / docx.

## Deterministic layer

Must be code, not LLM:

* ingestion;
* normalization;
* row counts;
* metrics;
* variances;
* thresholds;
* signal detection;
* evidence IDs;
* data quality checks;
* sorting / ranking.

## LLM layer

Ollama may write:

* management summary;
* interpretation of confirmed signals;
* hypotheses;
* risks;
* recommendations;
* next step.

Ollama must not invent calculations.

## Codex handoff checklist

Every implementation task must include:

* design brief;
* reference memo;
* metrics spec;
* signal catalog;
* evidence rules;
* prompts;
* acceptance criteria;
* example full / compact JSON;
* expected output paths.

## Acceptance criteria

Pass if:

* all calculations are deterministic;
* every signal has evidence_id;
* memo facts trace to evidence;
* judge output is saved;
* markdown export exists;
* docx export exists if requested;
* tests or smoke checks exist.
