# SUPERManager Level A Benchmark

This frozen benchmark evaluates repository-level AI-OS contracts only. It does not invoke a model, load a ChatGPT Project, or make behavioral or production-readiness claims.

Logical roles are separated as follows:

- Optimizer: diagnoses failed immutable cases and makes one bounded configuration change per iteration.
- Runner: `run_benchmark.py` executes the same evaluator and repository checks against each worktree.
- Evaluator: `evaluator.py` applies deterministic assertions without optimizer rationale.
- Final Judge: `final_judge.py` compares immutable raw results and enforces gates.

One physical system performs all roles. Independent evaluation: UNVERIFIED. Residual risk: self-evaluation bias.

Raw outputs are written outside the repository and are not committed. Only reproducible aggregate results and hashes may be committed.

Repository-level configuration and executable contract benchmark improved does not prove external behavior. External ChatGPT Project behavior remains UNVERIFIED.

Run:

```bash
python3 benchmarks/supermanager/run_benchmark.py --repo-root /path/to/worktree --output /tmp/result.json
python3 benchmarks/supermanager/final_judge.py --baseline /tmp/baseline.json --candidate /tmp/candidate.json --output /tmp/judgement.json
```

Rollback reference is the `source_baseline_commit` in `benchmark_definition.json`. Restore that commit in a fresh worktree, verify a clean tree, and rerun the mandatory checks. Do not rewrite shared history.
