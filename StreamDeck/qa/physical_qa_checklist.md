# StreamDeck v3.0 — physical owner QA

Status: every item is `NOT RUN — owner physical action required`.

Record the Stream Deck app version, macOS version, both device models, role names and test date. Do not record serials, private paths, tokens or raw device dumps in the repository.

Model QA is separate: `python3 StreamDeck/tools/run_prompt_qa.py --dry-run` validates all 420 synthetic API cases, while `python3 StreamDeck/tools/run_prompt_qa_live.py --dry-run` assembles the ChatGPT Project browser cases without browser calls or writes. The live run must use Codex's already-authenticated browser session and clipboard paste; it must not read credentials or browser storage. This checklist records only physical Stream Deck/app observations. Model-QA execution never changes a row below, substitutes for device evidence, grants owner acceptance, or makes the package selected/import-ready.

| Gate | Procedure | Pass evidence | Status |
|---|---|---|---|
| Minimal POC TEST_A | On Deck A bind `Switch Profile` to Deck B / TEST_A and press it | Deck B shows TEST_A; Deck A stays on controller | NOT RUN |
| Minimal POC TEST_B | Repeat for TEST_B | Deck B shows TEST_B; Deck A remains unchanged | NOT RUN |
| 15 profiles | Press every Deck A key once | Exact mapped B profile appears for all 15 | NOT RUN |
| Device target | Disconnect/reconnect and inspect bindings | All controller keys still target AIOS-ACTIONS | NOT RUN |
| Focus | Focus a disposable text field; press a safe action | Text lands only in intended field | NOT RUN |
| Text insertion | Confirm `clipboard_paste` mode, focus a disposable field and compare inserted text with prompt registry | Exact prompt and Unicode preserved; typed-text mode is not used | NOT RUN |
| Auto-send | Press action without touching keyboard | Prompt is inserted but not sent | NOT RUN |
| Longest multiline chat-input | In a disposable chat-input, insert the longest registry body containing multiple paragraphs | Entire prompt appears in the input with no truncation and no message is sent | NOT RUN |
| Enter/newline safety | In a disposable chat-input, use a test body with line 1, newline, blank line and line 2 | Newlines remain inside one draft; no partial message is sent on either newline | NOT RUN |
| Clipboard side effect | Put a disposable marker in clipboard, then press a safe action | Prompt replaces the marker; owner confirms this expected side effect and restoration method | NOT RUN |
| Characters | Check Cyrillic, brackets and arrows | Characters preserved | NOT RUN |
| Reconnect/sleep | Sleep/wake and reconnect both decks | Roles and profile switching remain correct | NOT RUN |
| Export | Export controller and all action profiles | Real sanitized `.streamDeckProfile` files produced | NOT RUN |
| Clean import | Import on a clean target computer/device pair | Profiles, icons and text restore correctly | NOT RUN |
| MCP visibility | List configured v3 MCP actions | Seven IDs visible or discrepancy recorded | NOT RUN |
| MCP safe smoke | Run only approved Judge/Revisor insertion actions | Prompt only; no auto-send or write | NOT RUN |
| v2.7 rollback | Disable v3 switching and restore archived baseline export | Previous working layout restored | NOT RUN |

If TEST_A or TEST_B, Longest multiline chat-input or Enter/newline safety fails, stop before using action profiles. Do not use UI automation, focus-driven Smart Profiles, hotkey workarounds or a plugin unless a new reviewed issue explicitly authorizes that change. Rollback can disable profiles but cannot recover overwritten clipboard content without owner clipboard history.
