# Live Benchmark Capability Matrix

Assessment date: 2026-07-31. Browser evidence was observed in the authenticated ChatGPT Project UI.

| Capability | Status | Evidence | Limitation |
|---|---|---|---|
| Actual ChatGPT Project access | supported | Authenticated Project home/chat pages opened for all seven target Projects. | Session authentication is user-owned. |
| Project selection | supported | Stable Project URLs and visible Project names were observed. | Project IDs are external runtime identifiers. |
| Exact Instructions loading | supported | Settings textarea can be read and updated; hashes can be compared with repository Instructions after UI trailing-newline normalization. | `[Thinking]` and `[Inbox Router]` were stale and `[Thinkers OS]` was empty at discovery; they must be synchronized before the valid baseline. |
| Exact Knowledge loading | supported | Required repository files can be uploaded through the Project Sources UI and filenames can be enumerated afterward. | The UI does not expose post-ingestion bytes, so server-side byte equivalence remains UNVERIFIED; source file hashes and observed filenames provide provenance. |
| Raw response capture | supported | Full visible assistant response, prompt, chat URL and hashes can be captured from each saved Project chat. | Raw captures remain local; repository copies must be anonymized. |
| Repeated identical prompts | supported | Fresh Project chats can be created repeatedly with the same prompt. | Product-side sampling is not controllable. |
| Baseline/candidate separation | supported | Configuration hashes and fresh chat URLs distinguish phases. | Same external account and product runtime are used. |
| Exact model pinning | unsupported | Project UI exposes `Medium` thinking effort but no exact model identifier in the composer. | Model comparability is UNVERIFIED if the product changes routing. |
| Context preservation | supported | Every run starts from the same Project home in a new empty chat. | Project memory is `Default` and cannot be changed in the UI. |
| Holdout isolation | supported | Holdout prompts are generated and sealed before baseline, then opened only by Runner/Evaluator after candidate selection. | Procedural isolation on one physical system; independent enforcement is UNVERIFIED. |
| Independent evaluator | UNVERIFIED | Runner, evaluator and final judge use separate artifacts and hashes. | One physical system performs all roles; residual risk is self-evaluation bias. |

No Level C improvement claim is allowed until actual baseline and candidate Project runs are captured and compared.
