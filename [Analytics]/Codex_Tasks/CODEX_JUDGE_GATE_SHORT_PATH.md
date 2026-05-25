# Codex: короткий путь через judge gate для аналитической записки через Ollama

## Статус

KB проверен: да  
Источники: `KB__08_USE_CASES_FOR_SERGEY.md`, `KB__06_OPERATIONAL_FRAMEWORKS.md`, `KB__05_CANONICAL_CONCEPTS.md`, `KB__PROMOTION_GATES.md`  
Найдено в KB: да  
Confidence: medium  
Evidence: supported по workflow, weak по конкретным memo-файлам, потому что их содержимое не проверялось в этом чате

---

## Суть замечания

Codex нужно подсказать не «сделай записку лучше», а **сделай записку judge-friendly**: каждая управленческая мысль должна иметь проверяемую связку:

```text
claim_id → supporting_source → confidence → место в тексте
```

Короткий путь: **не чинить все варианты**, а взять `deep`-вариант как основной кандидат и добавить перед judge слой `evidence preflight`.

---

## Что отправить в Codex

```text
TASK: Make the Ollama-generated analytical memo pass judge gate by adding minimal evidence-first changes, not by weakening judge.

Context:
Both action variants were stopped by judge gate. Remaining candidates have textual supporting sources:
- memo_01: deep_conclusion_draft.md
- memo_02: management_depth_monthly_plan_fact_memo.md

Goal:
Select the shortest passing path for the analytical memo pipeline:
1. Use deep variants as primary candidates because they contain textual supporting sources.
2. Add a pre-judge evidence layer that maps every important claim to a source.
3. Regenerate or patch the memo only where claims lack evidence.
4. Run the existing judge gate and produce a deterministic pass/fail report.

Do not:
- Do not weaken judge thresholds.
- Do not bypass judge.
- Do not invent supporting sources.
- Do not turn unsupported claims into facts.
- Do not rewrite the full pipeline unless necessary.
- Do not optimize style before evidence passes.

Implementation steps:
1. Inspect existing memo generation and judge files:
   - find the judge gate implementation;
   - find expected output schema;
   - find how supporting sources are passed to the judge;
   - find where memo variants are created.

2. Create or update an evidence contract for memo candidates:
   For each generated memo, produce:
   - source_registry.json
   - claim_evidence_matrix.json
   - judge_preflight_report.json

3. claim_evidence_matrix.json must contain:
   - claim_id
   - memo_section
   - claim_text
   - claim_type: fact | interpretation | recommendation | hypothesis
   - source_file
   - source_excerpt
   - metric_ref, if claim is numeric
   - confidence: strong | medium | weak | unsupported
   - judge_ready: true | false
   - fix_action: keep | downgrade_to_hypothesis | remove | add_source

4. Preflight rule:
   - FACT requires source_file + source_excerpt.
   - RECOMMENDATION requires at least one FACT or INTERPRETATION source.
   - Numeric claim requires metric_ref or table/source reference.
   - Unsupported claim must not appear in executive summary, conclusions, or recommendations.
   - Unsupported claim may only appear in "Risks / Open questions / Hypotheses".

5. Patch memo generation:
   - Prefer memo_02 if it has clearer management structure and more source-backed plan/fact logic.
   - Prefer memo_01 only if memo_02 has more unsupported claims.
   - Insert compact evidence markers into memo text, for example: [EVID: C-001].
   - Add final appendix: "Evidence Map" with claim_id, source_file, confidence.

6. Add judge precheck before full judge:
   - If any executive-summary claim has judge_ready=false, fail fast before expensive judge.
   - Print top 10 blocking claims and exact fix_action.
   - Do not launch more variants until blockers are fixed.

7. Run validation:
   - existing tests;
   - existing judge command;
   - any memo-specific smoke/acceptance checks.
   If command names are unknown, inspect repo and use existing scripts. Do not invent a new CLI if one already exists.

Acceptance criteria:
- One selected memo candidate passes judge gate.
- judge_preflight_report.json exists.
- claim_evidence_matrix.json exists.
- Every executive summary claim has source evidence.
- Every recommendation is supported by at least one sourced fact/interpretation.
- Unsupported claims are removed or moved to hypotheses/open questions.
- Final report states selected candidate, failed candidates, judge result, residual risks.
```

---

## Почему именно так

### FACT

KB-логика для Codex-задач требует:
- собрать релевантные excerpts;
- перечислить evidence filenames до synthesis;
- разделить facts и interpretation;
- weak/missing evidence пометить явно.

### FACT

Traceability workflow требует:
- найти claim;
- найти source evidence;
- проверить source identifier;
- отметить unsupported claims;
- записать confidence.

### FACT

Judge / Reviewer в KB описан как scoring по критериям, включая:
- LLM-as-a-Judge;
- code-based scores;
- проверку качества по явным критериям.

### BLOCKER

Следующие ситуации должны останавливать прохождение judge:
- unsupported item;
- weak item as fact;
- unstable retrieval QA;
- boundary gate failure.

---

## Решение A — корректное

Дать Codex задачу на:

```text
claim_evidence_matrix + preflight + минимальный patch deep memo
```

Это короткий путь, потому что judge перестанет видеть «красивый, но бездоказательный текст» и получит проверяемую связку:

```text
claim → source
```

---

## Решение B — ошибочное

Просить Codex:

```text
улучшить стиль
сделать выводы глубже
запустить ещё варианты
```

Это только плодит новые memo-кандидаты, но не чинит причину gate fail — отсутствие доказуемой traceability.

---

## Routing

```text
Handoff to: [Codex]
Task type: implementation / QA
Goal: пройти judge gate через evidence contract, не через ослабление judge
Expected output:
- one passing memo;
- claim_evidence_matrix.json;
- judge_preflight_report.json.
```

---

## Итог

Codex нужно направить на **доказательную обвязку записки**, а не на генерацию ещё одного текста.

## Next step

Отправить Codex промпт из этого файла и попросить сначала вернуть только:

```text
Implementation plan + files to change + existing judge command
```
