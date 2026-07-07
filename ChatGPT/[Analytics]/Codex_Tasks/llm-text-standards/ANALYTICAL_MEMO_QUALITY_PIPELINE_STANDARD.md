KB проверен: да
Источники: `KB__USE_CASE_ROUTING.md`, `KB__05_CANONICAL_CONCEPTS.md`, `PROJECT_DESCRIPTION_REPORT.md`
Найдено в KB: частично
Confidence: medium
Evidence: supported для принципов evidence / QA / judge / routing, weak для утверждения “именно 24 роли всегда обязательны”

# STANDARD: Analytical Memo Quality Pipeline

Версия: `v0.1`
Статус: `draft standard`
Назначение: стандарт подготовки аналитических записок с проверяемыми данными, доказательными выводами, LLM-слоем и release QA.

## 1. Принцип стандарта

Аналитическая записка строится не как “24 LLM-агента подряд”, а как **8 обязательных quality gates**.

```text
Intake → Data → Mart → Evidence → Claims → Narrative → Judges → Release → Learning
```

Для production-use workflow должен быть привязан к operational use case, иметь required confidence, sources, risks и routing; KB прямо требует маппинг сильных workflow/pattern/use case перед production-применением. 

## 2. Базовое правило

**Данные и формулы проверяются кодом.
Смысл, логика, читаемость и unsupported claims проверяются LLM-judges.**

LLM-as-a-Judge в KB подтверждён как подход для оценки качества по критериям, но не заменяет deterministic checks для формул, метрик и totals. 

## 3. Обязательные gates

|  № | Gate                               | Цель                                                         | Output                                      |
| -: | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
|  1 | Intake & Scope Gate                | Зафиксировать задачу, период, адресата, формат               | `scope_card.json`                           |
|  2 | Data Contract Gate                 | Проверить входные данные, обязательные поля, периоды         | `data_contract_result.json`                 |
|  3 | Mart / Metric Verification Gate    | Проверить marts, slices, formulas, totals                    | `mart_verification_result.json`             |
|  4 | Evidence & Claim Registry Gate     | Связать каждый вывод с evidence                              | `claim_registry.json`                       |
|  5 | Analyst Lenses Gate                | Получить финансовую, методологическую и бизнес-интерпретацию | `analysis_lenses.md/json`                   |
|  6 | Narrative & Writing Gate           | Собрать управленческий текст без новых фактов                | `memo_draft.md`                             |
|  7 | Judge & Revision Gate              | Проверить evidence, формулы, читаемость, язык, actionability | `judge_report.json`, `revised_memo.md`      |
|  8 | Artifact / Release / Learning Gate | Проверить DOCX/PDF/графики, release checklist, уроки         | `release_manifest.json`, `learning_note.md` |

## 4. Запрещённая трактовка

Нельзя утверждать:

```text
24 шага = 24 обязательных отдельных LLM-вызова для каждой записки.
```

Правильная трактовка:

```text
24 роли = каталог ролей и проверок внутри 8 gates.
```

Иначе будет дорогой “LLM-комитет”: много умных голосов, а ответственность за итог растворилась в тумане.

## 5. Профили запуска

| Профиль     | Когда использовать                        | Состав                                |
| ----------- | ----------------------------------------- | ------------------------------------- |
| `fast`      | быстрый черновик                          | Gates 1, 3, 4, 6, 7-lite              |
| `daily`     | ежедневная записка                        | Gates 1–4, 6–8                        |
| `monthly`   | управленческая записка за месяц           | Gates 1–8, analyst lenses full        |
| `high_risk` | аудит, совет директоров, внешний документ | Gates 1–8 + все judges + human review |

## 6. Role catalog

Исходные 24 пункта фиксируются так:

| Роль / проверка              | Gate  | Статус                          |
| ---------------------------- | ----- | ------------------------------- |
| Intake / постановщик задачи  | 1     | mandatory                       |
| Scope controller             | 1     | mandatory                       |
| Data contract checker        | 2     | mandatory                       |
| Mart / slice verifier        | 3     | mandatory                       |
| Evidence builder             | 4     | mandatory                       |
| Claim registry builder       | 4     | mandatory                       |
| Chart planner                | 5 / 8 | conditional                     |
| LLM financial analyst        | 5     | conditional                     |
| LLM methodology analyst      | 5     | conditional                     |
| LLM business analyst         | 5     | conditional                     |
| LLM narrative architect      | 6     | conditional                     |
| LLM business writer          | 6     | mandatory for memo              |
| Evidence judge               | 7     | mandatory                       |
| Formula / metric judge       | 3 / 7 | mandatory, code-first           |
| Management readability judge | 7     | mandatory for management memo   |
| Russian language judge       | 7     | mandatory                       |
| Style / tone editor          | 7     | conditional                     |
| Actionability judge          | 7     | mandatory for management memo   |
| LLM revisor                  | 7     | mandatory                       |
| Final consensus judge        | 7     | mandatory for monthly/high-risk |
| DOCX/render QA               | 8     | mandatory                       |
| Visual QA judge              | 8     | conditional                     |
| Release reviewer             | 8     | mandatory                       |
| Post-fix learning reviewer   | 8     | mandatory after release         |

## 7. Stop-rules

Pipeline обязан останавливаться, если:

```text
Data Contract Gate = fail
Mart / Metric Verification Gate = fail
Critical claim has no evidence
Formula / metric check = fail
Evidence judge = fail
DOCX/render QA = fail
Release reviewer = fail
```

`warn` допускает выпуск только если:

1. нет critical issues;
2. issue внесён в release manifest;
3. есть owner и срок исправления.

## 8. Claim freeze rule

После `Claim Registry Gate` запрещено добавлять новые факты в текст.

Разрешено:

* переписать формулировку;
* улучшить стиль;
* сократить;
* повысить читаемость;
* переставить блоки.

Запрещено:

* добавить новую причину отклонения;
* добавить новый вывод;
* изменить сумму, период, формулу;
* усилить weak claim до уверенного факта;
* заменить evidence на “звучит логично”.

## 9. Claim registry schema

Минимальная структура:

```json
{
  "claim_id": "CLM-001",
  "claim_text": "",
  "claim_type": "fact | interpretation | recommendation | risk | action",
  "period": "YYYY-MM-DD/YYYY-MM-DD",
  "metric_ids": [],
  "evidence_ids": [],
  "source_table": "",
  "chart_id": "",
  "confidence": "strong | medium | weak",
  "owner_gate": "",
  "status": "draft | frozen | revised | rejected"
}
```

## 10. Judge result schema

Минимальная структура:

```json
{
  "judge_name": "",
  "verdict": "pass | warn | fail",
  "severity": "critical | major | minor | style",
  "critical_issues": [],
  "unsupported_claims": [],
  "missing_evidence": [],
  "weak_logic": [],
  "formula_or_metric_issues": [],
  "required_fixes": [],
  "optional_fixes": [],
  "human_review_required": true
}
```

В проектном описании уже есть похожая логика: judge schema требует `pass|warn|fail`, critical issues, unsupported claims, missing evidence, weak logic, required/optional fixes и human review flag. 

## 11. Severity model

| Severity   | Значение                                              | Действие                              |
| ---------- | ----------------------------------------------------- | ------------------------------------- |
| `critical` | ошибка факта, формулы, evidence, периода              | stop                                  |
| `major`    | слабый вывод, неполная логика, риск неверного решения | fix before release                    |
| `minor`    | локальная неточность, улучшение структуры             | fix if time                           |
| `style`    | язык, тон, гладкость                                  | не блокирует, если факты не затронуты |

## 12. Release checklist

Записка может быть выпущена только если:

```text
[ ] scope зафиксирован
[ ] data contract passed
[ ] mart / metric verification passed
[ ] все critical claims имеют evidence_id
[ ] все суммы и формулы прошли deterministic check
[ ] charts построены и открываются
[ ] DOCX/PDF открывается
[ ] нет placeholder / TODO / fake evidence
[ ] unsupported claims отсутствуют или удалены
[ ] judge_report сохранён
[ ] release_manifest сохранён
[ ] archive создан
[ ] post-fix learning note создан после исправлений
```

## 13. Routing

| Блок                                    | Owner project |
| --------------------------------------- | ------------- |
| Data contract, mart, formulas           | `[Analytics]` |
| Prompt / model / judge orchestration    | `[LLM]`       |
| Код, тесты, render QA automation        | `[Codex]`     |
| Стратегический выбор и спорные решения  | `[Thinking]`  |
| Evidence policy и AI-pattern governance | `[AI OS]`     |

## 14. Acceptance criteria for standard

Стандарт считается принятым, когда есть:

```text
[ ] markdown standard file
[ ] JSON schemas: scope_card, claim_registry, judge_report, release_manifest
[ ] 4 run profiles: fast, daily, monthly, high_risk
[ ] stop-rules implemented
[ ] deterministic formula/mart checks separated from LLM judges
[ ] LLM writer cannot add unfrozen claims
[ ] at least 1 golden memo run passed
[ ] at least 1 failed run correctly stopped
```

## 15. Короткое название

Рекомендуемое имя файла:

```text
ANALYTICAL_MEMO_QUALITY_PIPELINE_STANDARD.md
```

Рекомендуемое внутреннее название:

```text
Analytical Memo Quality Pipeline
```

## Итог

Стандарт утверждать в формате **8 gates + role catalog + profiles + stop-rules**, а не как обязательную линейку из 24 LLM-агентов. Это даст качество, traceability и управляемость без превращения записки в бюрократический квест.

Next step:
Передать этот стандарт в `[LLM]` для упаковки prompt/model/judge orchestration и затем в `[Codex]` для реализации JSON-схем и acceptance tests.
