# Benchmark Changelog

## 1.0.1

Before baseline, live UI inspection showed that `[Thinking]` preserves the repository's final newline while other Project textareas may strip it. Version 1.0.0 incorrectly normalized only the repository side and therefore misclassified `[Thinking]` as stale.

Version 1.0.1 removes at most one trailing newline from both values before exact comparison. No cases, prompts, rubric criteria, weights, floors, hard-fail rules, thresholds, holdout content or sealed holdout hash changed. Version 1.0.0 was never baselined and is not evidence.
