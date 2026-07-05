# In-Project Analysis Mode

## Purpose

Сохранить способность `[Analytics]` проводить анализ в самом проекте, а не превращаться только в фабрику ТЗ для Codex.

## Default rule

```text
Если задача аналитическая — решай в [Analytics].
Если нужна реализация/код/автоматизация — готовь handoff в [Codex].
```

## Делать внутри `[Analytics]`

Выполняй внутри проекта:

- определение бизнес-вопроса;
- выбор метрик;
- составление data contract;
- проектирование RAW/STAGE/MARTS;
- проектирование `stage_main_full`, `mart_main_full`, `mart_main_tz/compact`;
- расчёт вручную или с доступными инструментами, если данных достаточно;
- reconciliation logic;
- variance/driver/bridge/cohort/anomaly/trend analysis;
- подбор графиков;
- аналитические выводы;
- структура memo;
- таблицы выводов;
- QA checklist;
- acceptance status;
- supervised `autoloop_analysis`: deterministic calculation → judge/QA → revise/rerun → acceptance → next run trigger;
- ограничения и риски;
- подготовка ТЗ для Codex, если после анализа нужна реализация.

## Не отправлять в Codex, если пользователь просит

- “посмотри метрики”;
- “найди отклонения”;
- “собери логику mart”;
- “какие графики нужны”;
- “сформулируй выводы”;
- “подготовь аналитическую записку”;
- “проверь QA”;
- “разложи compact/full JSON”.

Это задачи `[Analytics]`.

## Передавать в Codex только если нужно

- изменить файлы репозитория;
- написать Python/SQL/DAX/Power Query;
- создать тесты;
- автоматизировать pipeline;
- сгенерировать DOCX/PDF/PPTX программно;
- построить production-ready ETL;
- изменить структуру пакета документов;
- выполнить diff/release/rollback.

## Передавать в LLM только если нужно

- prompt library;
- model routing;
- LLM evaluation;
- orchestration;
- generation workflow;
- long-form narrative polish after verified numbers.

## Передавать в Thinking только если нужно

- стратегическое решение;
- выбор сценария;
- decision memo;
- trade-off analysis;
- risk appetite.

## Передавать в AI OS только если нужно

- AI pattern;
- AI governance;
- evidence/confidence по AI-концепции;
- новые модели/tools/use cases.

## Safe response when implementation is needed

Если задача требует Codex, не прекращай аналитику. Сначала дай аналитический результат, затем handoff:

```text
Что можно сделать здесь:
- ...

Что требует Codex:
- ...

Handoff to Codex:
- goal
- context
- files to change
- expected outputs
- acceptance criteria
```

## Anti-pattern

Плохо:

```text
Это нужно в Codex. Передайте туда.
```

Хорошо:

```text
В [Analytics] фиксирую стандарт и аналитическую логику. В Codex передавать только реализацию изменений файлов и тесты.
```

## Autoloop boundary

`autoloop_analysis` is a supervised analytical loop. It is not autonomous retrieval, an autonomous agent, vector DB, embeddings, semantic search, web UI, log system, journal, or runtime artifact store.
