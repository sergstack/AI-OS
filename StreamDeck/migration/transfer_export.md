# StreamDeck v3.0 — перенос, export и rollback

## До изменений

1. В Stream Deck app откройте Profiles и выполните `Back Up All`.
2. Запишите дату, app version, macOS version и роли двух устройств вне repository. Не коммитьте serials и private paths.
3. Сохраните v2.7/v2.9 и создавайте v3 только side-by-side.

## Импорт candidate-профилей

1. Запустите `python3 StreamDeck/tools/export_profiles.py`, затем `python3 StreamDeck/tools/validate_v3.py`.
2. Импортируйте 15 `B*.streamDeckProfile` на Deck B, затем `A00_CONTROL.streamDeckProfile` на Deck A.
3. На каждой controller-кнопке вручную выберите физический Deck B и target profile. Export serial-neutral: пустой `DeviceUUID` не заменяет owner binding. Не задавайте Smart Profile.
4. Проверьте на Deck B `System > Text`, exact prompt body/hash, embedded icon и отключённый Enter/Return/auto-send.
5. Для MCP сверьте exact action IDs с `migration/mcp_registry.json`. `execution-verified` означает только legacy pilot evidence для двух actions, не v3 visibility.

## Manual fallback

Если candidate import не проходит, создайте `AIOS-CONTROL` и 15 `AIOS-ACTIONS / <NAME>` вручную по config-файлам. Используйте только built-in `Switch Profile` и `System > Text`, body из `prompts/prompt_registry.json`, relative icons из `config/icon_map.json`; auto-send должен оставаться off.

## Owner acceptance

1. Импортируйте profiles на чистом target computer и повторите physical checklist.
2. Проверьте, что profiles не содержат machine-specific paths, secrets, credentials и private content.
3. Зафиксируйте app/device versions и observed result вне repository; serials не коммитьте.
4. Пока этот шаг не выполнен, status остаётся `candidate / import NOT RUN`, не `import-ready`.

## Rollback

1. Отключите все 15 controller bindings или верните Deck A на backup profile.
2. Верните Deck B на профиль v2.7/v2.9 из owner backup.
3. Сохраните v3 profiles для диагностики; не удаляйте единственные evidence files.
4. Repo rollback: revert v3 change; legacy checksums и исходные файлы остаются в `StreamDeck/archive/`.
