# Supermanager Level A Benchmark

Version 1.1.0 of this benchmark compares repository configurations with immutable deterministic assertions. It does not invoke a model or a live ChatGPT Project. Version 1.0.0 was invalidated before configuration changes because its benchmark-integrity case incorrectly expected overlay infrastructure inside the source-baseline checkout; no 1.0.0 result is improvement evidence.

## Frozen scope

- Seven registered ChatGPT Projects, with at least two positive and one negative routing case each.
- Existing repository validators.
- Documented golden-eval contract preservation.
- Adversarial checks for evidence, execution truth, authority, source-of-truth, secrets, direct `main` writes, and false external-validation claims.
- No holdout: the claimed evidence level is repository-only Level A.

## Roles

- Runner loads frozen cases and evaluates baseline/candidate checkouts identically.
- Evaluator receives repository files and command results, without optimizer rationale.
- Final Judge consumes the immutable result package and gate rules.

All roles execute on one physical system. Independent evaluation is `UNVERIFIED`; residual risk is self-evaluation bias.

## Capability assessment

| Capability | Status | Evidence | Limitation |
|---|---|---|---|
| Repository validation | supported | Existing validators and benchmark commands | Repository level only |
| Python execution | supported | Python 3 standard library runner | No environment parity claim |
| Exact Instructions loading | supported | Exact tracked files loaded by path | Not loaded into ChatGPT UI |
| Exact Knowledge loading | supported | Exact tracked files available locally | Not loaded into ChatGPT UI |
| Model invocation | unsupported | No model endpoint used | Level B/C not claimed |
| Model and parameter pinning | unsupported | No model run | Behavioral comparability unavailable |
| Context preservation | UNVERIFIED | Repository snapshot is pinned | ChatGPT runtime context absent |
| Raw-output capture | supported | JSON output outside the repository | Raw output is not committed |
| Repeated runs | supported | Deterministic runner can be repeated | One run is sufficient for Level A |
| Role isolation | UNVERIFIED | Logical scripts and hashed artifacts | Same physical system |
| Independent evaluator | unsupported | Same physical system | Self-evaluation bias |
| Holdout isolation | unsupported | No holdout created | Not required for Level A-only claim |
| Branch creation | supported | Local non-main branch | Remote push checked later |
| Commit creation | supported | Local Git checkout | Remote publication checked later |
| PR creation | supported | GitHub connector | Local `gh` is unavailable |

## Run

```bash
python3 benchmarks/supermanager/runner.py \
  --repo-root <CHECKOUT> \
  --role baseline \
  --output <LOCAL_RAW_OUTPUT.json>
```

Raw output must remain untracked. The runner records benchmark/evaluator hashes and the evaluated commit.

## Coverage matrix

| Project / route | Positive | Negative | Regression | Adversarial | Deterministic | Model-evaluated |
|---|---:|---:|---:|---:|---:|---:|
| `[AI OS]` | 2 | 1 | 2 | 2 | 7 | 0 |
| `[Thinking]` | 2 | 1 | 1 | 1 | 5 | 0 |
| `[Analytics]` | 2 | 1 | 1 | 2 | 6 | 0 |
| `[LLM]` | 2 | 1 | 1 | 2 | 6 | 0 |
| `[Codex]` | 2 | 1 | 1 | 7 | 11 | 0 |
| `[Inbox Router]` | 2 | 1 | 1 | 1 | 5 | 0 |
| `[Thinkers OS]` | 2 | 1 | 0 | 1 | 4 | 0 |
| Repository / cross-project | 0 | 0 | 9 | 9 | 18 | 0 |

Counts overlap where a cross-project case covers more than one project. `cases.json` is the authoritative case inventory.
