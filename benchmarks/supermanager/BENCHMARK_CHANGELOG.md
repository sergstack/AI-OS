# Benchmark Changelog

## 1.0.1

The 1.0.0 baseline attempt was invalidated before any tested-configuration change. It exposed two evaluator defects:

- project registry cases expected a full instructions-file path, while the registry contract intentionally stores the canonical project directory plus a separate instructions rule;
- the unauthorized-mutation adversarial case searched for the word `production` instead of the repository's explicit `deploy without explicit approval` boundary.

Version 1.0.1 corrects only those assertions. The invalid 1.0.0 result is not used as improvement evidence. A new baseline is required and all later comparisons must use the 1.0.1 hashes.
