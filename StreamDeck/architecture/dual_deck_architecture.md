# AI-OS StreamDeck v3.1.2 Dual Deck — архитектура

Status: `candidate / ready for repo review`; physical acceptance: `NOT RUN`.

## Роли устройств

- `AIOS-CONTROL` — один постоянный профиль `A00_CONTROL`, 15 кнопок. Каждая кнопка использует встроенное действие `Stream Deck > Switch Profile`, целевое устройство выбирается вручную как `AIOS-ACTIONS`.
- `AIOS-ACTIONS` — 15 профилей по 15 кнопок. Каждая action-кнопка вставляет canonical prompt через clipboard-paste режим `System > Text`; отправка остаётся ручной.

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
4. `tools/generate_v3.py` — deterministic source generator; `generated/button_map.md` редактировать вручную нельзя.
5. `tools/export_profiles.py` — deterministic archive exporter; он читает только перечисленные config/registry/icon sources и создаёт 16 candidate profiles в `exports/`.

## Profile archive format

Проверяемые источники формата:

- официальный Elgato sample profile: <https://github.com/elgatosf/streamdeck-plugin-samples/blob/8cc82bad8716c000bacc131285ffcf6805dafff9/lights-out/com.elgato.lightsout.sdPlugin/sd-mini.streamDeckProfile>;
- reference export и описание action fields, проверенные по live `.streamDeckProfile`: <https://github.com/thisis-romar/opendeck-factory/blob/9471c31258d03d792366d70fc532b336e08c4baa/builds/Reference%20-%20All%20Actions.streamDeckProfile> и <https://github.com/thisis-romar/opendeck-factory/blob/9471c31258d03d792366d70fc532b336e08c4baa/docs/obsidian-vault/File%20Format/Action%20Types.md>;
- официальная Elgato packaging documentation: <https://docs.elgato.com/stream-deck/profiles/packaging/>.

Observed structure: ZIP archive → `<UUID>.sdProfile/manifest.json` → `Profiles/<PAGE_UUID>/manifest.json` → `Controllers[].Actions`; icons находятся в соседнем `Images/`. Exporter использует `Version: 3.0`, `System > Text` с `pastedText`, `isSendingEnter: false`, `isTypingMode: false`, и `Switch Profile` с пустым `DeviceUUID`.

## Многострочная вставка

Canonical prompt bodies многоабзацные. В режиме typed text каждый перевод строки может интерпретироваться focused chat-input как Enter и отправить только первый фрагмент, даже если отдельная настройка Enter/Return after message выключена. Физически это поведение на owner devices не воспроизводилось: `NOT RUN`.

Безопасный candidate contract — `insertion_method: clipboard_paste` на каждой action-кнопке. Exporter кодирует его как `System > Text` с `isTypingMode: false`: body сначала попадает в системный clipboard, затем вставляется как единый paste event; `isSendingEnter` остаётся `false`. Repo checks подтверждают только структуру archive и настройки. Реальная вставка самого длинного многоабзацного body в disposable chat-input без отправки остаётся обязательным физическим gate.

Побочный эффект: action перезаписывает текущее содержимое clipboard. Предыдущее значение нужно сохранить заранее или восстановить из owner clipboard history; repository не может его восстановить.

Допущения до owner import: модель двух устройств — 15-key `20GAA9901`; пустые root `Device.UUID` и action `DeviceUUID` принимаются импортёром; deterministic profile UUID сохраняется после импорта; SVG icons принимаются текущей Stream Deck app. Эти допущения не являются observed import evidence.

## Acceptance boundary

Repo checks могут проверить schema, `insertion_method`, references, hashes, assets, archive determinism, counts и safety metadata. После их прохождения packages готовы к ручному импорту. Cross-device switching, clipboard-paste behavior, focus, text insertion, truncation, reconnect, import, MCP visibility и rollback требуют два физических устройства и owner action; до observed owner QA package не является `selected` или `production-ready`.
