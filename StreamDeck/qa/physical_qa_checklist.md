# StreamDeck v3.0 — physical owner QA

Status: every item is `NOT RUN — owner physical action required`.

Record the Stream Deck app version, macOS version, both device models, role names and test date. Do not record serials, private paths, tokens or raw device dumps in the repository.

| Gate | Procedure | Pass evidence | Status |
|---|---|---|---|
| Minimal POC TEST_A | On Deck A bind `Switch Profile` to Deck B / TEST_A and press it | Deck B shows TEST_A; Deck A stays on controller | NOT RUN |
| Minimal POC TEST_B | Repeat for TEST_B | Deck B shows TEST_B; Deck A remains unchanged | NOT RUN |
| 15 profiles | Press every Deck A key once | Exact mapped B profile appears for all 15 | NOT RUN |
| Device target | Disconnect/reconnect and inspect bindings | All controller keys still target AIOS-ACTIONS | NOT RUN |
| Focus | Focus a disposable text field; press a safe action | Text lands only in intended field | NOT RUN |
| Text insertion | Compare inserted text with prompt registry | Exact prompt and Unicode preserved | NOT RUN |
| Auto-send | Press action without touching keyboard | Prompt is inserted but not sent | NOT RUN |
| Longest prompt | Insert the longest registry body | No truncation | NOT RUN |
| Characters | Check Cyrillic, brackets and arrows | Characters preserved | NOT RUN |
| Reconnect/sleep | Sleep/wake and reconnect both decks | Roles and profile switching remain correct | NOT RUN |
| Export | Export controller and all action profiles | Real sanitized `.streamDeckProfile` files produced | NOT RUN |
| Clean import | Import on a clean target computer/device pair | Profiles, icons and text restore correctly | NOT RUN |
| MCP visibility | List configured v3 MCP actions | Seven IDs visible or discrepancy recorded | NOT RUN |
| MCP safe smoke | Run only approved Judge/Revisor insertion actions | Prompt only; no auto-send or write | NOT RUN |
| v2.7 rollback | Disable v3 switching and restore archived baseline export | Previous working layout restored | NOT RUN |

If TEST_A or TEST_B fails, stop before building profiles in the app. Do not use UI automation, focus-driven Smart Profiles, hotkey workarounds or a plugin unless a new reviewed issue explicitly authorizes that change.
