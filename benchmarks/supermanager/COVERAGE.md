# Coverage Matrix

All listed cases are deterministic Level A assertions. Model-evaluated and isolated holdout cases are not available and are NOT RUN.

| Project / route | Positive | Negative | Regression | Adversarial | Deterministic | Model-evaluated |
|---|---:|---:|---:|---:|---:|---:|
| `[AI OS]` core | 3 | 0 | 7 | 0 | 10 | 0 |
| `[Thinking]` core | 3 | 0 | 3 | 0 | 6 | 0 |
| `[Analytics]` core | 3 | 0 | 3 | 0 | 6 | 0 |
| `[LLM]` core | 3 | 0 | 3 | 0 | 6 | 0 |
| `[Codex]` core | 3 | 0 | 3 | 0 | 6 | 0 |
| `[Inbox Router]` core | 3 | 0 | 3 | 0 | 6 | 0 |
| `[Thinkers OS]` core | 3 | 0 | 0 | 0 | 3 | 0 |
| Route: `[Inbox Router]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: Things | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: Calendar | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: Notes / Obsidian | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[AI OS]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[Thinkers OS]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[Thinking]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[Analytics]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[LLM]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: `[Codex]` | 3 | 1 | 0 | 0 | 4 | 0 |
| Route: Codex APP | 3 | 1 | 0 | 0 | 4 | 0 |
| Repository-wide hard-fail classes | 0 | 0 | 0 | 12 | 12 | 0 |

The 22 regression cases preserve every individual `pass` row documented in `SMOKE_QA_RESULTS.md` and `CROSS_PROJECT_SMOKE_QA_RESULTS.md`; the cross-project aggregate `[AI OS]` row is represented by its seven underlying cases rather than counted twice.
