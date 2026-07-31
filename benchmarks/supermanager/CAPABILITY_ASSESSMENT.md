# Capability Assessment

Evidence level: Level A repository validation only.

| Capability | Status | Evidence | Limitation |
|---|---|---|---|
| Repository validation | supported | Repository scripts and tests execute locally. | Does not validate external ChatGPT behavior. |
| Python execution | supported | Python 3 executes the standard-library evaluator. | Local environment only. |
| Exact Instructions loading | supported | Evaluator reads repository bytes directly. | ChatGPT UI copy is not compared. |
| Exact Knowledge loading | supported | Evaluator and repository checks read repository files. | External Project Knowledge is not loaded. |
| Model invocation | unsupported | No approved model runtime is part of this benchmark. | No Level B or C claims. |
| Model and parameter pinning | unsupported | No model is invoked. | Behavioral comparability is unavailable. |
| Context preservation | UNVERIFIED | No external Project session is run. | External context may differ. |
| Raw-output capture | supported | Runner writes deterministic JSON to a caller-selected local path. | Raw results remain untracked. |
| Repeated runs | supported | Runner can be repeated against the same commit. | Determinism applies only to Level A assertions. |
| Role isolation | supported | Optimizer, runner, evaluator, and final judge are separate logical stages. | One physical system performs all stages. |
| Independent evaluator | UNVERIFIED | Evaluation logic is deterministic and frozen. | Residual risk: self-evaluation bias. |
| Holdout isolation | unsupported | No isolated execution context is available. | Holdout is NOT RUN and not required for Level A. |
| Branch creation | supported | Git branch is created from `main`. | Local repository capability only. |
| Commit creation | supported | Git repository is writable. | Commit success is verified when performed. |
| PR creation | supported | Authenticated GitHub CLI is available. | Remote success is verified when performed. |

Repository-level configuration and executable contract benchmark may be evaluated. External ChatGPT Project behavior remains UNVERIFIED.
