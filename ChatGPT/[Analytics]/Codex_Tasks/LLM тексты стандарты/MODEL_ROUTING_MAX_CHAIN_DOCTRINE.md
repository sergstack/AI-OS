# MODEL ROUTING MAX CHAIN DOCTRINE

**Название:** Model Routing Max Chain Doctrine  
**Версия:** v1.0  
**Статус:** active candidate  
**Контекст:** фабрика финансово-аналитических записок  
**Основано на:** `benchmark_report.md`, `ANALYTICAL_MEMO_QUALITY_PIPELINE_STANDARD.md`  

---

## 0. Главная мысль

Модели не делают записку. Записку делает система.

```text
Код считает.
LLM пишет.
Judge режет.
Release выпускает только доказанное.
```

Это главный принцип фабрики аналитических записок.

Не надо строить “24 агента подряд”. Это не фабрика, а модельный хоровод с бюджетом и без ответственности. Каноническая архитектура — **8 quality gates**, где роли подключаются по необходимости, а не ради красивой схемы.

---

## 1. Главная формула

```text
Data truth        → Code
Business meaning  → LLM
Evidence discipline → Judge
Release decision  → Checklist + Human Review
```

Иначе говоря:

```text
Суммы не спрашивают у модели.
Формулы не обсуждают с моделью.
Периоды не угадывают моделью.
Модель получает проверенные факты и превращает их в управленческий смысл.
```

---

## 2. Канонический стек моделей

Это не “лучшие модели вообще”. Это боевой стек по ролям для финансово-аналитической фабрики.

| Слой | Primary | Fallback | Назначение |
|---|---|---|---|
| Writer / JSON / revisor | `qwen2.5-coder:32b` | `qwen3-coder:30b` | Пишет draft, собирает JSON, чинит структуру, держит формат |
| Finance checker | `mistral-small:latest` | `qwen2.5-coder:32b` | Проверяет финансовую логику, план-факт, риски интерпретации |
| Evidence / logic judge | `deepseek-r1:32b` | `mistral-small:latest` | Режет unsupported claims, слабую логику, переуверенность |
| Russian editor | `akdengi/saiga-llama3-8b:latest` | `qwen2.5-coder:32b` | Деловой русский, читабельность, убирает AI-вату |
| Executive summarizer | `phi4:latest` | `OxW/Saiga_YandexGPT_8B:q6_K` | Сжимает для руководства, делает executive summary |
| Final fallback | `qwen2.5-coder:32b` | — | Универсальная страховка, но не замена judge |

---

## 3. Главное ограничение

Benchmark — это не закон природы, а текущий замер.

Правильный статус routing:

```text
routing_status: active_candidate
production_status: allowed_after_full_validation
```

Перед production-фиксацией обязательно:

```text
make benchmark-full
make validate-benchmark
manual review high-risk runs
re-benchmark after model/runtime/hardware changes
```

---

## 4. Максимальная цепочка

Максимальная цепочка — это не максимум LLM-вызовов.

Максимальная цепочка — это профиль `high_risk`:

```text
Gates 1–8
+ все обязательные judges
+ deterministic checks
+ human review
+ release manifest
+ learning note
```

Ключевая мысль:

```text
Максимальная цепочка = максимум контроля, а не максимум моделей.
```

---

## 5. Боевой pipeline

### Gate 1. Intake & Scope

**Цель:** зафиксировать задачу, период, адресата, формат и ограничения.

```text
Primary: qwen2.5-coder:32b
Output: scope_card.json
Judge: deepseek-r1:32b только если scope сложный
```

Нельзя начинать записку, пока неизвестно:

```text
кому пишем
за какой период
по каким данным
какое решение должен принять читатель
что запрещено утверждать
```

---

### Gate 2. Data Contract

**Цель:** проверить входные данные.

```text
Primary: code / deterministic checks
LLM: только объясняет ошибки
Output: data_contract_result.json
```

Модель здесь не главный герой. Здесь главный герой — проверка колонок, типов, периодов, дубликатов, пропусков и границ данных.

---

### Gate 3. Mart / Metric Verification

**Цель:** проверить витрины, срезы, формулы, totals, план-факт.

```text
Primary: code / reconciliation
Finance review: mistral-small:latest
Output: mart_verification_result.json
```

Финансовые суммы должны пройти deterministic check. LLM может объяснить, почему отклонение важно, но не должна быть источником истины по расчётам.

---

### Gate 4. Evidence & Claim Registry

**Цель:** связать каждый вывод с evidence.

```text
Builder: qwen2.5-coder:32b
Judge: deepseek-r1:32b
Output: claim_registry.json
```

С этого момента действует правило:

```text
Нет evidence_id → нет claim.
Нет claim_registry → нет записки.
```

---

### Gate 5. Analyst Lenses

**Цель:** получить интерпретацию, но не породить новые факты.

```text
Finance lens: mistral-small:latest
Methodology lens: deepseek-r1:32b
Business lens: qwen2.5-coder:32b или phi4:latest
Output: analysis_lenses.md/json
```

Линзы дают смысл, но не имеют права менять фактуру.

---

### Gate 6. Narrative & Writing

**Цель:** собрать управленческий текст.

```text
Writer: qwen2.5-coder:32b
Output: memo_draft.md
```

Главное правило writer:

```text
Пиши только из frozen claims.
Не добавляй новые причины.
Не усиливай слабые выводы.
Не украшай цифры фантазией.
```

---

### Gate 7. Judge & Revision

**Цель:** разнести draft до того, как его разнесёт CFO.

```text
Evidence judge: deepseek-r1:32b
Finance judge: mistral-small:latest
Russian judge: akdengi/saiga-llama3-8b:latest
Management readability: phi4:latest
Revisor: qwen2.5-coder:32b
Final consensus: deepseek-r1:32b + checklist
Output: judge_report.json, revised_memo.md
```

Judge не должен переписывать текст. Judge должен находить:

```text
unsupported claims
missing evidence
weak logic
formula issues
period mismatch
overconfident recommendation
```

---

### Gate 8. Artifact / Release / Learning

**Цель:** выпустить не “текст”, а проверенный артефакт.

```text
Render QA: code / LibreOffice / automated checks
Release reviewer: deepseek-r1:32b
Learning note: phi4:latest
Output: release_manifest.json, learning_note.md
```

Записка выпускается только после проверки:

```text
scope fixed
data contract passed
mart verification passed
critical claims have evidence_id
formulas and totals passed deterministic checks
charts open correctly
DOCX/PDF opens correctly
no placeholders / TODO / fake evidence
judge_report saved
release_manifest saved
archive created
learning_note saved
```

---

## 6. Stop-rules

Pipeline обязан остановиться, если:

```text
Data Contract Gate = fail
Mart / Metric Verification Gate = fail
Critical claim has no evidence
Formula / metric check = fail
Evidence judge = fail
DOCX/render QA = fail
Release reviewer = fail
```

Это не рекомендации. Это тормоза. Без тормозов фабрика записок превращается в генератор уверенной ерунды в костюме консультанта.

---

## 7. Claim freeze rule

После `Claim Registry Gate` текст можно улучшать, но нельзя менять факты.

Разрешено:

```text
сократить
переписать
улучшить стиль
переставить блоки
повысить читаемость
```

Запрещено:

```text
добавить новый вывод
добавить новую причину отклонения
изменить сумму
изменить период
изменить формулу
усилить weak claim до strong
заменить evidence на “звучит логично”
```

Enforcement:

```text
revised_memo claims
vs
frozen claim_registry
```

Если новый claim не найден в registry → `fail`.

---

## 8. Runtime-правило

В production не должно быть “LLM-orchestrator”.

Должно быть так:

```text
orchestrator = config + pipeline state + files + checks
LLM = role executor
judge = independent critic
release = deterministic checklist
```

Модель может выполнить роль.  
Модель не должна быть всей системой.

---

## 9. Финальная конфигурация

```json
{
  "routing_profile": "high_risk_max_chain",
  "status": "active_candidate",
  "principle": "quality_gates_over_agent_chain",
  "runtime_rule": "code_first_llm_second_judge_third_release_last",
  "models": {
    "writer": {
      "primary": "qwen2.5-coder:32b",
      "fallback": "qwen3-coder:30b"
    },
    "json_schema_builder": {
      "primary": "qwen2.5-coder:32b",
      "fallback": "qwen3-coder:30b"
    },
    "revisor": {
      "primary": "qwen2.5-coder:32b",
      "fallback": "qwen3-coder:30b"
    },
    "finance_checker": {
      "primary": "mistral-small:latest",
      "fallback": "qwen2.5-coder:32b"
    },
    "evidence_judge": {
      "primary": "deepseek-r1:32b",
      "fallback": "mistral-small:latest"
    },
    "logic_judge": {
      "primary": "deepseek-r1:32b",
      "fallback": "mistral-small:latest"
    },
    "russian_editor": {
      "primary": "akdengi/saiga-llama3-8b:latest",
      "fallback": "qwen2.5-coder:32b"
    },
    "summarizer": {
      "primary": "phi4:latest",
      "fallback": "OxW/Saiga_YandexGPT_8B:q6_K"
    },
    "release_reviewer": {
      "primary": "deepseek-r1:32b",
      "fallback": "mistral-small:latest"
    }
  },
  "non_llm_layers": {
    "data_contract": "deterministic_code",
    "mart_verification": "deterministic_code",
    "formula_check": "deterministic_code",
    "docx_render_qa": "codex_libreoffice_automation",
    "release_decision": "checklist_plus_human_review_for_high_risk"
  },
  "stop_rules": [
    "data_contract_fail",
    "mart_verification_fail",
    "critical_claim_without_evidence",
    "formula_or_metric_fail",
    "evidence_judge_fail",
    "docx_render_qa_fail",
    "release_reviewer_fail"
  ],
  "claim_freeze": {
    "after_gate": "Evidence & Claim Registry Gate",
    "writer_can": [
      "rewrite_wording",
      "improve_style",
      "shorten",
      "reorder_blocks"
    ],
    "writer_cannot": [
      "add_new_claim",
      "add_new_reason",
      "change_amount",
      "change_period",
      "change_formula",
      "upgrade_weak_claim_to_strong",
      "invent_evidence"
    ]
  },
  "production_activation_requires": [
    "benchmark_full_passed",
    "validate_benchmark_passed",
    "golden_memo_run_passed",
    "failed_run_correctly_stopped",
    "routing_config_saved",
    "release_manifest_schema_saved"
  ]
}
```

---

## 10. Что передавать из уст в уста

```text
Не выбирай лучшую модель.
Строй систему, где каждая модель боится следующей проверки.

Не проси LLM посчитать.
Дай коду посчитать, а LLM заставь объяснить.

Не выпускай красивый текст.
Выпускай доказанный текст.

Не строй 24 агента.
Строй 8 gates, где каждый gate может остановить ошибку.

Writer пишет.
Checker проверяет.
Judge режет.
Release молчит, пока всё не прошло.
```

---

## 11. Одна фраза для книги

**Фабрика аналитических записок — это не цепочка генерации текста.  
Это система сдержек и противовесов, где код защищает факты, LLM собирает смысл, judge защищает от самообмана, а release выпускает только то, за что не стыдно перед CFO.**

---

## 12. Acceptance criteria

Доктрина считается принятой, когда выполнено:

```text
[ ] routing_config.json сохранён
[ ] benchmark-full пройден
[ ] validate-benchmark пройден
[ ] golden memo run passed
[ ] failed run correctly stopped
[ ] stop-rules implemented
[ ] claim freeze diff implemented
[ ] deterministic checks separated from LLM judges
[ ] release_manifest schema implemented
[ ] DOCX/render QA automated
[ ] human review включён для high_risk
```

---

## 13. Handoff

```text
From: [LLM]
To: [Codex]
Task type: implementation spec
Objective: реализовать routing и quality gates для high_risk memo factory
Inputs:
- MODEL_ROUTING_MAX_CHAIN_DOCTRINE.md
- benchmark_report.md
- ANALYTICAL_MEMO_QUALITY_PIPELINE_STANDARD.md
Expected outputs:
- routing_config.json
- stop_rules implementation
- claim freeze diff check
- judge report schema validation
- release manifest schema validation
- tests for golden memo and failed memo
Acceptance:
- deterministic checks are code-first
- LLM cannot add unfrozen claims
- pipeline stops on critical failures
- release artifact is produced only after QA pass
```
