# ANALYTICAL_MEMO_JUDGE_GATE_STANDARD

## Назначение

Этот стандарт нужен для аналитических записок, которые генерируются через Ollama / LLM и должны проходить judge gate.

Главная идея: judge gate проходится не красотой текста, а доказуемостью каждого управленческого утверждения.

```text
claim → source → confidence → section → judge verdict
```

Если у записки нет слоя evidence contract, judge будет регулярно останавливать даже хорошие по стилю варианты.

---

## 1. Главный принцип

Codex должен реализовывать не просто генератор записки, а фабрику доказуемой записки.

Правильный pipeline:

```text
data / marts
→ analytical facts
→ source registry
→ claim evidence matrix
→ memo draft
→ judge preflight
→ judge gate
→ final memo
```

Неправильный pipeline:

```text
Ollama draft
→ красивый markdown
→ docx
→ judge fail
→ ручная боль
```

---

## 2. Почему action-варианты падают на judge

Action-варианты часто формулируют рекомендации быстрее, чем успевают доказать их источниками.

| Что пишет memo | Что видит judge | Риск |
|---|---|---|
| Необходимо пересмотреть лимиты | Нет источника / метрики | unsupported recommendation |
| Основной драйвер отклонения — рост расходов | Нет ссылки на mart / source | unsupported causal claim |
| Рекомендуется усилить контроль | Нет факта, на котором стоит вывод | generic management advice |
| Ситуация ухудшается | Нет периода сравнения | temporal claim без evidence |

Action-вариант хорош как стиль финальной записки, но плох как первый кандидат для judge.

---

## 3. Почему deep-варианты лучше

Deep-вариант обычно содержит больше рассуждений, промежуточных оснований и supporting sources.

Использовать так:

```text
deep draft
→ claim extraction
→ evidence matrix
→ unsupported cleanup
→ final management memo
```

Deep-вариант — это не финал, а сырьё для evidence extraction.

---

## 4. Evidence contract

Перед judge gate каждый memo candidate должен иметь минимум три файла:

```text
source_registry.json
claim_evidence_matrix.json
judge_preflight_report.json
```

### 4.1 source_registry.json

Назначение: список всех источников, которыми можно подтверждать memo.

Минимальная структура:

```json
{
  "source_id": "S-001",
  "source_file": "mart_budget_fact_monthly.csv",
  "source_type": "mart",
  "period": "2026-04",
  "description": "Monthly plan-fact mart by article and responsibility center",
  "allowed_for_claims": true
}
```

### 4.2 claim_evidence_matrix.json

Назначение: связать каждое важное утверждение записки с источником.

Минимальная структура:

```json
{
  "claim_id": "C-001",
  "memo_section": "Executive summary",
  "claim_text": "Расходы по статье X превысили план на 12%",
  "claim_type": "fact",
  "source_file": "mart_budget_fact_monthly.csv",
  "source_excerpt": "article=X, plan=1000000, fact=1120000, variance_pct=12.0",
  "metric_ref": "variance_pct",
  "confidence": "strong",
  "judge_ready": true,
  "fix_action": "keep"
}
```

### 4.3 judge_preflight_report.json

Назначение: остановить плохой memo до дорогого/финального judge.

Минимальная структура:

```json
{
  "candidate": "memo_02",
  "preflight_status": "fail",
  "blocking_claims_count": 3,
  "unsupported_in_executive_summary": 1,
  "numeric_claims_without_metric_ref": 2,
  "recommended_action": "patch_claims_before_full_judge"
}
```

---

## 5. Claim types и правила допуска

| Claim type | Разрешено где | Что нужно для прохода |
|---|---|---|
| fact | везде | source_file + source_excerpt + metric_ref для чисел |
| interpretation | summary / body / conclusion | минимум один подтверждающий fact |
| recommendation | recommendations / conclusion | факт + логика, почему рекомендация следует из факта |
| hypothesis | risks / open questions / hypotheses | явная маркировка как гипотеза |
| unsupported | нигде как факт | удалить, понизить до hypothesis или добавить источник |

Жёсткое правило:

```text
Unsupported claim must not appear in executive summary, conclusions, or recommendations.
```

---

## 6. Preflight gate

Preflight запускается до full judge.

Порядок:

```text
Ollama draft
→ extract claims
→ attach sources
→ preflight fail/pass
→ patch memo
→ final judge
```

Preflight должен проверять:

- 100% executive summary claims have evidence;
- 100% numeric claims have metric_ref;
- 100% recommendations link to sourced facts or interpretations;
- 0 unsupported claims in conclusions / recommendations;
- all weak claims are marked as hypothesis, risk, or open question;
- evidence appendix exists.

---

## 7. Что запретить Codex

Codex не должен чинить judge gate через обход контроля.

```text
Do not weaken judge.
Do not bypass judge.
Do not invent sources.
Do not use unsupported claims in executive summary.
Do not create more memo variants until current blockers are classified.
Do not optimize wording before evidence passes.
Do not rewrite the whole pipeline unless evidence contract cannot be added locally.
```

---

## 8. Как обрабатывать unsupported, но полезные мысли

| Тип мысли | Правильная обработка |
|---|---|
| Без источника, но полезно | Перенести в Hypotheses / Open questions |
| Слабая логика | Перенести в Risks / Requires validation |
| Управленческий совет без факта | Удалить или привязать к факту |
| Число без источника | Удалить до подтверждения |
| Причинно-следственный вывод без анализа драйверов | Downgrade до hypothesis |

---

## 9. Роль Ollama

Ollama лучше использовать как слой narrative generation, а не как источник истины.

Ollama может:

- черновать формулировки;
- превращать таблицы в текст;
- делать первичный narrative;
- переписывать текст в управленческий русский;
- помогать с claim extraction.

Ollama не должна:

- сама решать, что является фактом;
- придумывать причины;
- усиливать вывод без источника;
- подменять deterministic расчёты;
- проходить judge за счёт уверенного тона.

---

## 10. Acceptance criteria

Задача считается выполненной, если:

```text
- One selected memo candidate passes judge gate.
- source_registry.json exists.
- claim_evidence_matrix.json exists.
- judge_preflight_report.json exists.
- Every executive summary claim has source evidence.
- Every numeric claim has metric_ref.
- Every recommendation is supported by at least one sourced fact or interpretation.
- Unsupported claims are removed or moved to hypotheses / open questions.
- Final report states selected candidate, failed candidates, judge result, residual risks.
```

---

## 11. Minimal Codex task

Use this task when the current analytical memo fails judge gate.

```text
TASK: Add evidence-first judge preflight for analytical memo generation.

Context:
Current memo variants are stopped by judge gate. Deep variants contain textual supporting sources and should be used as the primary candidates for evidence extraction.

Goal:
Make one memo candidate pass judge by adding a minimal evidence contract and preflight layer.

Steps:
1. Inspect existing memo generation and judge implementation.
2. Identify current memo candidates and supporting source files.
3. Create source_registry.json.
4. Extract important claims into claim_evidence_matrix.json.
5. Mark each claim as fact, interpretation, recommendation, hypothesis, or unsupported.
6. Add source_file, source_excerpt, metric_ref, confidence, judge_ready, and fix_action.
7. Add judge_preflight_report.json.
8. Patch memo text only where claims lack evidence.
9. Move unsupported useful ideas to Hypotheses / Open questions.
10. Run existing judge gate.

Do not:
- weaken judge;
- bypass judge;
- invent sources;
- create new variants before blockers are classified;
- rewrite the whole pipeline unless necessary.

Acceptance:
- selected memo passes judge;
- preflight report exists;
- claim evidence matrix exists;
- no unsupported claims remain in executive summary, conclusions, or recommendations.
```

---

## 12. Short reminder

```text
Judge gate is not a style gate.
Judge gate is an evidence gate.

First prove claims.
Then polish text.
```
