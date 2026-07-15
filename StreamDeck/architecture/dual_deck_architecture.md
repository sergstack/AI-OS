# AI-OS StreamDeck v3.0 Dual Deck — архитектура

Status: `candidate / ready for repo review`; physical acceptance: `NOT RUN`.

## Роли устройств

- `AIOS-CONTROL` — один постоянный профиль `A00_CONTROL`, 15 кнопок. Каждая кнопка использует встроенное действие `Stream Deck > Switch Profile`, целевое устройство выбирается вручную как `AIOS-ACTIONS`.
- `AIOS-ACTIONS` — 15 профилей по 15 кнопок. Каждая action-кнопка вставляет canonical prompt через `System > Text`; отправка остаётся ручной.

Device serial не хранится в repository. При установке owner даёт физическим устройствам ролевые имена и выбирает target device в property inspector каждой controller-кнопки.

## Механизм переключения

Elgato официально описывает cross-device switching: для `Switch Profile` можно выбрать другое устройство и конкретный профиль. Функция появилась в Stream Deck 4.4; текущая help-статья указывает совместимость со всеми Stream Deck devices:

- <https://help.elgato.com/hc/en-us/articles/360059908112-Elgato-Stream-Deck-Switch-Profiles-On-One-Stream-Deck-using-Another-Stream-Deck>
- <https://help.elgato.com/hc/en-us/articles/5162934218637-Elgato-Stream-Deck-4-4-Release-Notes>

Это repo evidence только для design choice. Оно не доказывает, что конкретные два устройства уже прошли POC. Dedicated plugin и UI automation не используются.

## Spatial grammar

- `K1–K5`: основные действия.
- `K6–K10`: анализ, преобразование или supervised execution request.
- `K11`: `BLOCKER`.
- `K12`: `HANDOFF`.
- `K13`: `JUDGE`.
- `K14`: `REVISOR`.
- `K15`: `FINAL GATE`.

## Source of truth

1. `config/controller_map.json` и `config/action_profiles.json` — physical layout и settings.
2. `prompts/prompt_registry.json` — единственные full prompt bodies.
3. `migration/migration_manifest.json` — transfer contract и checksums.
4. `tools/generate_v3.py` — deterministic generator; `generated/button_map.md` редактировать вручную нельзя.

## Acceptance boundary

Repo checks могут проверить schema, references, hashes, assets, counts и safety metadata. Cross-device switching, focus, text insertion, truncation, reconnect, export/import, MCP visibility и rollback требуют два физических устройства и owner action. До этого status остаётся `candidate`, не `selected`, `import-ready` или `production-ready`.
