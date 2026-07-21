# Profile exports

Status: `repository-validated / ready for owner manual import; physical import and QA NOT RUN`.

`python3 StreamDeck/tools/export_profiles.py` writes 16 deterministic `.streamDeckProfile` files here: `A00_CONTROL` and the 15 `B*` action profiles. Running it twice must produce byte-identical files. Action profiles use `insertion_method: clipboard_paste`, encoded as `isTypingMode: false`, with `isSendingEnter: false`. `python3 StreamDeck/tools/validate_v3.py` checks these settings, counts, prompt bodies/hashes, embedded icons, serial neutrality, fixed ZIP timestamps, secrets and private paths.

The archive layout and action fields are based on the pinned official Elgato sample and live reference export documented in `architecture/dual_deck_architecture.md`. No owner-import observation was available. The remaining assumptions are: 15-key model `20GAA9901`; blank `Device.UUID`/`DeviceUUID` are accepted during import; deterministic profile UUIDs survive import; current Stream Deck app accepts embedded SVG icons. Therefore these repository-validated files are ready for manual import, but physical compatibility and production readiness remain unverified until owner QA.

After import, the owner must bind every controller action to the physical Deck B, confirm its target profile, verify clipboard-paste and auto-send-off behavior in a disposable chat-input, and complete `qa/physical_qa_checklist.md`. Physical multiline behavior is `NOT RUN`; archive settings alone do not prove it. Clipboard-paste overwrites the owner's current clipboard. Do not add serial numbers, raw device dumps, private paths, credentials or other sensitive content to an export.
