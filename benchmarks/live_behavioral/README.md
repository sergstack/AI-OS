# SUPERManager Live Behavioral Benchmark

This benchmark evaluates actual responses from the seven AI-OS ChatGPT Projects. Static repository checks do not substitute for live runs.

Workflow:

1. freeze benchmark, rubric, public cases, coverage and sealed holdout hashes;
2. synchronize the source-baseline Instructions and Knowledge into the actual Projects;
3. run every public case three times in a fresh Project chat;
4. capture prompt, full raw response, Project URL, configuration hash, model condition and response hash;
5. evaluate raw responses without Optimizer rationale;
6. make at most five bounded configuration iterations;
7. repeat the same full run procedure for the selected candidate;
8. open the sealed holdout only after candidate selection;
9. apply the frozen final gate and create a separate PR without merging.

Raw responses and the sealed holdout stay outside the repository. The PR contains anonymized cases, response samples, aggregate results and hashes without private data.

Independent evaluation: UNVERIFIED. Residual risk: self-evaluation bias.
