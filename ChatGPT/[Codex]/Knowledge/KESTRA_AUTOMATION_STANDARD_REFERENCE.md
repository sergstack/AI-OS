# Kestra Automation Standard Reference

## Purpose

Use Kestra for orchestration and run control of stable workflows.

Kestra is not a substitute for validation.
A successful Kestra execution does not automatically mean valid business output.

## Core model

```text
scripts / Python / Ollama / services → executors
Kestra → orchestration and run control
artifacts → evidence of execution
run_summary → audit trail
validation → quality gate
```

## Required production-like flow structure

```text
preflight
→ prepare_inputs
→ main_run
→ validation
→ save_artifacts
→ run_summary
→ error_handling
```

## Required metadata

Each production-like flow should define:

* owner;
* purpose;
* environment;
* flow_type;
* input contract;
* output contract;
* validation rule;
* artifact policy;
* timeout policy;
* retry policy or no-retry decision;
* failure behavior.

## Flow types

* business;
* service;
* healthcheck;
* smoke_test;
* maintenance.

## Artifact policy

Every meaningful run should leave evidence:

* output;
* metrics / status;
* run_summary;
* execution logs available.

Recommended logical path:

```text
artifacts/runs/<flow_id>/<execution_id>/
```

## Run summary minimum fields

* Flow;
* Namespace;
* Execution ID;
* Status;
* Validation result;
* Artifacts / evidence;
* Errors;
* Next action.

## Production checklist

Flow is not production-ready unless:

* validation exists;
* run_summary exists;
* artifacts / evidence exist;
* execution logs are available;
* timeout policy exists;
* retry or no-retry decision exists;
* failure behavior exists;
* no temporary names like `_final`, `_new`, `_test2`.

## Open decisions

Do not create final YAML templates until these are known:

* artifact backend;
* actual task types;
* current flow YAML;
* storage layout;
* alerting policy;
* isolation strategy.
