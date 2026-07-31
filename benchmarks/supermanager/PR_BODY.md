## Objective

Create a frozen executable Level A repository benchmark, measure the original `main` configuration in isolation, correct only proven defects, and retain the best configuration observed within the fixed benchmark.

- Base: `main`
- Head: `supermanager/ai-os-benchmark-optimization`
- Evidence level: A — deterministic repository validation
- Source baseline: `8d45a4653012dbb5dbc0c85647d835d59886ee17`
- Benchmark definition commit: `5eabef99b4d2d86748d866ff271b4d98e0ad4fa0`
- Benchmark hash: `361db9b5b16cf2819b1bdb6978936ae24203687da35ccf1cf62e737433449ea0`
- Evaluator hash: `6517bc3391fa7c8671f66ff5ff6ccafc696579965ad928c034d0997ac7aaf73b`

## Coverage and scoring

The [coverage matrix](benchmarks/supermanager/COVERAGE.md) includes at least three core cases for each of seven ChatGPT Projects, at least two positive and one negative case for each of eleven routes, 22 individual documented passing smoke cases, and all twelve required adversarial hard-fail classes. All 99 cases are deterministic; no model cases are claimed.

Category weights are routing 25, evidence 20, authority/safety 20, execution truth 15, and regression 20. Critical floors, hard-fail rules, minimum improvement 0.5, and deterministic variance/tie-break rules were frozen before the valid baseline.

## Baseline and final results

| Result | Score | Passed | Hard failures | Mandatory checks |
|---|---:|---:|---:|---|
| Baseline | 99.038462 | 97/99 | 2 | pass |
| Final | 100.0 | 99/99 | 0 | pass |

Baseline failures were `route_thinkers_os_overview` and `adversarial_incorrect_route`. One retained iteration added the already-canonical `[Thinkers OS]` route to the repository convenience overview. No iteration was rolled back. Two final runs were byte-identical with SHA-256 `74ba407316d4bf4a346d1cfb9a628322cdba1f813cb1672fb0edce948b93eacf`.

Benchmark v1.0.0 was invalidated before any configuration change because two evaluator assertions did not match the documented repository format. Benchmark v1.0.1 was frozen, committed, and baselined again; v1.0.0 is not used as improvement evidence.

## Planned and actual changed files

Planned configuration change: `docs/PROJECT_ROUTING.md` only. Actual configuration change: the same one file and one table row. Additional changes are the benchmark definitions, tests, coverage, scope/capability record, and aggregate reproducible results under `benchmarks/supermanager/` and `tests/test_supermanager_benchmark.py`.

## Tests actually run

- `python3 -m pytest -q` — 74 passed
- `python3 scripts/sync_aios.py` — pass, including all six mandatory checks plus index coverage
- frozen benchmark v1.0.1 baseline and candidate — final 99/99, pass
- repeated final benchmark — byte-identical
- `git diff --check` — pass
- aggregate machine-path/secret-like token scan — pass

## NOT RUN

- model invocation
- simulated behavioral validation
- isolated holdout
- external ChatGPT Project validation
- production deployment
- merge

Regression: pass. Adversarial validation: pass. Holdout: NOT RUN and not required for Level A. External validation: UNVERIFIED.

Independent evaluation: UNVERIFIED. Residual risk: self-evaluation bias because one physical system performed the logically separated Optimizer, Runner, Evaluator, and Final Judge roles. Historical external smoke evidence was preserved but not rerun.

Rollback: use source baseline commit `8d45a4653012dbb5dbc0c85647d835d59886ee17` in a fresh worktree, verify clean status, and rerun mandatory checks. To undo only the bounded configuration correction, revert commit `8d9b3fa9478aa20870836bf0205259c32b56fcf0` without rewriting history.

Final verdict: `pass` at Evidence Level A. Production readiness remains UNVERIFIED; no production promotion is claimed.

Best configuration observed within the fixed benchmark, tested scope and available execution capabilities.

Merge requires owner approval.
