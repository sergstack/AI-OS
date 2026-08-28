# Coverage Matrix

Public development benchmark: 45 cases × 3 fresh-chat runs = 135 live Project runs per phase. A separately sealed holdout is not included in public counts.

| Project / route | Positive | Negative | Cross-project | Readability simple | Readability complex | Adversarial | Public cases | Runs / phase |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [Inbox Router] | 2 | 1 | 1 | 1 | 0 | 2 | 7 | 21 |
| [AI OS] | 2 | 1 | 1 | 1 | 1 | 1 | 7 | 21 |
| [Thinking] | 2 | 1 | 1 | 1 | 1 | 2 | 8 | 24 |
| [Analytics] | 2 | 1 | 0 | 0 | 1 | 1 | 5 | 15 |
| [LLM] | 2 | 1 | 1 | 1 | 1 | 1 | 7 | 21 |
| [Codex] | 2 | 1 | 1 | 1 | 0 | 1 | 6 | 18 |
| [Thinkers OS] | 2 | 1 | 0 | 0 | 1 | 1 | 5 | 15 |

Set totals: routing 21; response quality 5; readability 10 (5 simple, 5 material complex); adversarial 9. Every tested Project has three core routing cases: two positive and one negative. The nine critical hard-fail classes are each represented by at least one tagged public case.
