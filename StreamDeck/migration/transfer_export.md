# StreamDeck v3.0 — перенос, export и rollback

## До изменений

1. В Stream Deck app откройте Profiles и выполните `Back Up All`.
2. Запишите дату, app version, macOS version и роли двух устройств вне repository. Не коммитьте serials и private paths.
3. Сохраните v2.7/v2.9 и создавайте v3 только side-by-side.

## Сборка профилей

1. Создайте `AIOS-CONTROL` и 15 профилей `AIOS-ACTIONS / <NAME>` по ID из manifest.
2. На Deck A добавьте встроенное `Stream Deck > Switch Profile`. Для каждой кнопки выберите физический Deck B и target profile. Не задавайте Smart Profile.
3. На Deck B добавьте `System > Text`, скопируйте body по `prompt_id`, отключите Enter/Return after message и любой auto-send.
4. Иконки берите только из relative paths в `config/icon_map.json`.
5. Для MCP сверьте exact action IDs с `migration/mcp_registry.json`. `execution-verified` означает только legacy pilot evidence для двух actions, не v3 visibility.

## Export

1. После physical checklist экспортируйте `AIOS-CONTROL` и все 15 action profiles из Stream Deck app.
2. Откройте export на чистом target computer и повторите physical checklist.
3. Проверьте, что exports не содержат machine-specific paths, secrets, credentials и private content.
4. Только реальные exports можно поместить в `exports/`; не генерируйте фиктивные packages.

## Rollback

1. Отключите все 15 controller bindings или верните Deck A на backup profile.
2. Верните Deck B на профиль v2.7/v2.9 из owner backup.
3. Сохраните v3 profiles для диагностики; не удаляйте единственные evidence files.
4. Repo rollback: revert v3 change; legacy checksums и исходные файлы остаются в `StreamDeck/archive/`.
