# AI-OS StreamDeck v3.0 Dual Deck

Status: `candidate / repo package`; physical acceptance: `NOT RUN — owner action required`.

## Назначение

v3.0 разделяет навигацию и действия между двумя 15-кнопочными Stream Deck:

- `AIOS-CONTROL` всегда остаётся контроллером. Его 15 кнопок переключают профиль только на втором устройстве.
- `AIOS-ACTIONS` показывает 15 действий выбранного project/workflow. Кнопка вставляет prompt, но не нажимает Send.

В repository есть переносимые source settings, prompts, icons, mapping, checksums и 16 детерминированных candidate `.streamDeckProfile`. Физический import не выполнялся: Codex не имел доступа к Stream Deck app и двум устройствам, поэтому package не считается `import-ready`.

## Совместимость

- Два Stream Deck с раскладкой 5×3. Device serials не хранятся; модели привязываются к ролям вручную.
- Stream Deck app 4.4 или новее: Elgato добавила cross-device `Switch Profile` в 4.4. Используйте актуальную поддерживаемую версию; точная owner-версия ещё `NOT RUN`.
- Controller switching и prompt insertion используют встроенные `Stream Deck > Switch Profile` и `System > Text`; dedicated switching plugin не нужен.
- MCP plugin/server нужен только для MCP profile. Точная версия и v3 visibility ещё не проверены.

Официальная инструкция cross-device switching: <https://help.elgato.com/hc/en-us/articles/360059908112-Elgato-Stream-Deck-Switch-Profiles-On-One-Stream-Deck-using-Another-Stream-Deck>.

## Backup и установка

1. В Stream Deck app откройте Profiles и выполните `Back Up All`. Не перезаписывайте v2.7/v2.9.
2. Переименуйте физические устройства в `AIOS-CONTROL` и `AIOS-ACTIONS` или запишите это ролевое соответствие.
3. Выполните `python3 StreamDeck/tools/export_profiles.py`; команда создаёт 16 candidate-профилей в `StreamDeck/exports/`.
4. Импортируйте 15 `B*.streamDeckProfile` на Deck B, затем `A00_CONTROL.streamDeckProfile` на Deck A.
5. В property inspector каждой controller-кнопки выберите именно физический Deck B и target profile: архивы намеренно не содержат device serial. На Deck A не создавайте prompt, send, GitHub или terminal actions.
6. Выполните минимальный POC и полный checklist из `qa/physical_qa_checklist.md`; до наблюдаемого результата import status остаётся `NOT RUN`.
7. Если импорт не поддерживается или не проходит, используйте manual fallback: создайте профили по таблице ниже, добавьте `Switch Profile`/`System > Text`, вставьте exact `body`, выключите Enter/Return и назначьте relative icon из `config/icon_map.json`.

## Все профили и кнопки

| Deck A ID | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | K11 | K12 | K13 | K14 | K15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A00_CONTROL | DAILY | ROUTE | AI OS | THINKING | ANALYTICS | LLM | CODEX | JUDGE | REVISOR | MEMO | LOCAL AI | PILOTS | KB | MCP | DECK QA |

| ID | Profile | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 | K11 | K12 | K13 | K14 | K15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B00_DAILY | DAILY | INBOX | AI TREND | DECISION | DATA CONTRACT | GOAL→PR | FIN MEMO | PROMPT | CONTEXT | SYNC | KB EVIDENCE | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B10_ROUTE | ROUTE | RAW→ROUTE | THINGS? | CALENDAR? | NOTES? | AI OS? | THINKING? | ANALYTICS? | LLM? | CODEX? | CODEX APP? | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B20_AI_OS | AI OS | AI TREND | PATTERN | USE CASE | EVIDENCE | GOVERNANCE | FRESH CHECK | SOURCE TRUTH | LOOP DESIGN | PROMPT QA | STREAMDECK | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B30_THINKING | THINKING | DECISION | OPTIONS | RISKS | ASSUMPTIONS | REVERSIBLE? | SCENARIO | PREMORTEM | CRITERIA | TRADE-OFFS | NEXT STEP | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B40_ANALYTICS | ANALYTICS | DATA CONTRACT | DATA QUALITY | VARIANCE | RECONCILE | ANOMALY | MART SPEC | FORMULA | QA CHECKS | ANALYTICS LOOP | MEMO FACTS | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B50_LLM | LLM | PROMPT BUILD | CONTEXT PACK | MODEL ROUTE | WORKFLOW | EVAL RUBRIC | SUMMARIZE | EXTRACT | SYNTHESIZE | LOCAL PROMPT | GOAL→CODEX PACK | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B60_CODEX | CODEX | GOAL→PR | BUILD FIRST | INSPECT | RUN CHECKS | FIX IN SCOPE | SYNC | PR JUDGE | FIX CI | REVIEW COMMENTS | RELEASE NOTES | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B70_JUDGE | JUDGE | UNIVERSAL | EVIDENCE | ROUTE | RISK | FRESHNESS | ANALYTICS | MEMO | PROMPT | PR | LOCAL AI | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B80_REVISOR | REVISOR | APPLY NOTES | SHORTEN | CLEARER | EXEC VERSION | FILE-READY | MEMO | DECISION | STRUCTURE | TONE | SOURCE-PRESERVE | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| B90_MEMO | MEMO | FINANCE | MANAGEMENT | EXEC SUMMARY | FINDINGS | RISKS | RECOMMEND | AUDIT FINDING | CHART COMMENT | APPENDIX | FINAL MEMO | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| BA0_LOCAL_AI | LOCAL AI | SAFETY | SANITIZE | DRAFT ONLY | OLLAMA SMOKE | OPEN WEBUI | MODEL COMPARE | EVAL MATRIX | JUDGE OUTPUT | RECORD PILOT | CANDIDATE? | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| BB0_PILOTS | PILOTS | PILOT PLAN | TEST CASES | RUN RECORD | PILOT RESULT | ACCEPTANCE | RESIDUAL RISK | ROLLBACK | REGISTRY | STATUS NOTE | REVISIT | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| BC0_KB | KB | KB SEARCH | EVIDENCE LABEL | REVIEW ITEM | SUPPORT MIX | SOURCE TRUTH | MANIFEST | BUNDLE SYNC | UPLOAD CHECK | FRESHNESS | CONFLICT CHECK | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| BD0_MCP | MCP | LIST ACTIONS | REGISTRY | VISIBILITY | JUDGE | REVISOR | SYNC | AI TREND | KB SOURCE | LOCAL SAFETY | GOAL→PR | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |
| BE0_DECK_QA | DECK QA | SWITCH TEST | DEVICE TARGET | FOCUS TEST | TEXT INSERT | AUTO-SEND OFF | PLACEHOLDER | DUPLICATES | PROMPT HASH | EXPORT BACKUP | IMPORT TEST | BLOCKER | HANDOFF | JUDGE | REVISOR | FINAL GATE |

Точные prompt IDs, risks, owner route, next action, stop condition и rollback на каждой кнопке находятся в `config/action_profiles.json`; readable derived map — в `generated/button_map.md`.

## Prompt registry и Prompt QA

Full bodies хранятся только в `prompts/prompt_registry.json`. Button maps хранят `prompt_id`, version и hash, а не дубли body. После ручной настройки сверьте inserted text с `prompt_hash` через `DECK QA / PROMPT HASH`.

QA matrix содержит отдельную строку для каждого unique prompt. Static contract checks выполнены, но normal, missing-context/evidence и unsafe/ambiguous model runs не выполнены. Поэтому каждый prompt имеет verdict `blocked`, UX `4/5`, owner acceptance `pending` и ни один не назван `10/10`. `PROMPT QA` только судит; rewrite выполняет отдельный `REVISOR`.

## MCP

`migration/mcp_registry.json` сохраняет семь action IDs. `AIOS_HOME_JUDGE` и `AIOS_HOME_REVISOR` имеют legacy execution evidence в v2.8 pilot; остальные пять — `registered-only`. Это не равно v3 visibility и не доказывает настройку на текущих devices. После manual setup нужно получить visible action list, сверить exact IDs и выполнить только supervised safe smoke.

## Перенос на другой компьютер

1. На исходном компьютере повторно создайте candidate exports командой `python3 StreamDeck/tools/export_profiles.py` и завершите physical checklist.
2. На target computer установите ту же или новее поддерживаемую Stream Deck app и нужные MCP components.
3. Импортируйте action profiles, затем controller. Заново привяжите все controller keys к физическому Deck B: device IDs не переносятся как universal settings.
4. Повторите весь physical checklist, включая clean import, focus, longest prompt, reconnect и rollback.

Подробный checklist: `migration/transfer_export.md`.

## Примеры

1. Raw input → `ROUTE`: на Deck A нажать ROUTE; на Deck B — RAW→ROUTE; проверить owner route; отправить вручную.
2. Broad goal → `CODEX`: нажать GOAL→PR или BUILD FIRST. Prompt берёт последнюю цель без placeholder, ограничивает scope, требует checks и PR, но не manual merge/deploy.
3. AI release → `AI OS`: AI TREND проверяет изменяемые факты по current official sources; затем K13 JUDGE проверяет evidence и unsupported claims.
4. Decision → `THINKING`: DECISION → OPTIONS/RISKS/PREMORTEM → K15 FINAL GATE. Недостающие assumptions должны остаться явными.
5. Data question → `ANALYTICS`: DATA CONTRACT фиксирует entity, grain, period, currency/unit, sources, formulas и filters; QA CHECKS принимает numeric result только из Python/SQL evidence.
6. Draft → JUDGE → REVISOR → FINAL GATE: Judge verdict используется только как notes; Revisor редактирует исходный artifact и не добавляет факты.
7. Finance facts → `MEMO`: FINANCE или FINAL MEMO используют только Analytics-approved facts, отделяют interpretation/assumptions/recommendations и указывают period, scope, units и traceability.
8. Local AI safe pilot: `LOCAL AI` → SANITIZE → OLLAMA SMOKE → JUDGE OUTPUT → RECORD PILOT. Только sanitized non-sensitive input; все results candidate.
9. KB source conflict: `KB` → SOURCE TRUTH → CONFLICT CHECK → JUDGE. Исходный source и bundle не смешиваются без explicit sync rule.
10. MCP visibility/action check: `MCP` → LIST ACTIONS → VISIBILITY. Если ID не виден, status `NOT RUN/blocked`; expected output не выдаётся за observed result.

## Полный сценарий двух устройств

1. На Deck A нажмите LLM; Deck A должен остаться на `AIOS-CONTROL`, Deck B — перейти на `B50_LLM`.
2. На Deck B нажмите PROMPT BUILD.
3. В focused text field проверьте вставленный prompt и убедитесь, что он не отправился.
4. Нажмите Send вручную.
5. После output нажмите K13 JUDGE; при `revise` нажмите K14 REVISOR; затем повторите JUDGE и завершите K15 FINAL GATE.

## Troubleshooting

- Deck A тоже сменил профиль: откройте controller key property inspector и повторно выберите физический Deck B.
- Профиль не виден: сначала создайте/импортируйте target profile на Deck B, затем настраивайте controller.
- Text вставился не туда: немедленно отмените, перейдите в disposable field и повторите focus test.
- Prompt сразу отправился: в `System > Text` выключите Enter/Return after message. До исправления не используйте profile.
- Prompt обрезан или искажён: сверьте exact body/hash, проверьте longest prompt и Unicode test; не исправляйте generated map вручную.
- MCP action не виден: сверьте exact ID и local MCP setup; оставьте `NOT RUN`, если tool list его не возвращает.
- Import потерял icons/bindings: восстановите relative icons и повторите manual target-device binding; serial-neutral package не может автоматически угадать target device.

## Rollback и source of truth

При failure отключите controller switching, верните Deck B на owner backup v2.7/v2.9 и сохраните v3 для диагностики. Legacy не удалён: он перенесён в `archive/` и защищён SHA-256 manifest.

Canonical sources:

- architecture: `architecture/dual_deck_architecture.md`;
- controller/action settings: `config/*.json`;
- prompt bodies: `prompts/prompt_registry.json`;
- QA: `qa/`;
- deterministic exporter: `tools/export_profiles.py`; generated profiles и format notes: `exports/`;
- migration, MCP и checksums: `migration/`;
- legacy rollback: `archive/legacy_manifest.md` и `archive/checksums.json`.

Repo checks проверяют JSON, counts, routing, references, hashes, embedded icons, deterministic exports, secrets/private paths и derived map. Physical switching, focus, text insertion, reconnect, import, MCP visibility и v2.7 rollback остаются `NOT RUN` до заполнения owner checklist. До этого v3.0 не является `selected`, `import-ready` или `production-ready`.
