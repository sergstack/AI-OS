# AES Artifact-Freshness Pilot — Results (Phase 3, executed)

Status: this pilot was actually run, on a purpose-built pilot fixture pair.
It is Phase 3 evidence per `AUTONOMOUS_EXECUTION_STANDARD.md` Section 20 and
`docs/pilots/AES_ARTIFACT_PILOT.md`; it does not authorize enforcement or CI
gating of the Autonomous Execution Standard.

## Scoping decision and the discovered limitation

`docs/pilots/AES_ARTIFACT_PILOT.md` scoped the pilot to "a real generation
pipeline that already exists in the repository" — candidates listed were
DOCX/XLSX/PDF/PPTX outputs or an existing Analytics memo / StreamDeck export
bundle. On inspection, this repository has **no DOCX/XLSX/PDF/PPTX
generation tooling** and no committed Analytics-memo or StreamDeck-export
generation pipeline to pilot against.

The repository's actual, real "derived artifact" concept is the **Knowledge
Bundle** system: compact markdown files under
`ChatGPT/<project>/Knowledge_Bundles/`, generated/kept in sync from granular
Knowledge source files, and checked by `scripts/check_knowledge_bundles.py`
(which already implements a `source_fingerprint: sha256:...` freshness
check against concatenated source file contents — see
`declared_source_fingerprint()` / `source_fingerprint()` in that script).

Per the pilot spec's own §45.2-style allowance in the Phase 3 task ("another
deterministic artifact"), and to avoid touching real, governed
`ChatGPT/*/Knowledge_Bundles/*` content (explicitly out of scope for a
pilot), this pilot built a small, clearly-labeled **pilot fixture pair**
that mirrors the Knowledge Bundle freshness pattern (a granular source doc,
a derived doc carrying a manifest with a `generated_from_revision` content
hash) without touching any real bundle.

## Artifact pair

- Source (granular): `docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_source.md`
- Derived (generated): `docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_derived.md`
- Generation/validation tool: `scripts/pilot_generate_artifact_fixture.py`
  (`generate` mode renders a markdown table from the source's `## Facts`
  key/value lines and stamps a manifest with `generated_from_revision =
  sha256(source file bytes)`; `check` mode recomputes the source hash and
  compares it against the recorded `generated_from_revision`, printing
  `CURRENT` and exiting 0 on match, or `STALE` and exiting 1 on mismatch)

Both fixture files are explicitly labeled as pilot fixtures ("not real
product content") in their own text, and live under `pilot_fixtures/` so
they are not mistaken for real Knowledge Bundle or product artifacts.

## Steps performed (real commands, real output)

### 1. Generate derived artifact from source revision A

```
$ python3 scripts/pilot_generate_artifact_fixture.py generate
GENERATED docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_derived.md
generated_from_revision: sha256:351f3761f47f66aa0000196e56712bd95dcdd1f7733b9984539ffb444534986a
```

Committed as revision A:

```
$ git commit -m "Add AES artifact-freshness pilot fixtures (revision A, current)"
6fb1780
```

### 2. Validate (expect CURRENT)

```
$ python3 scripts/pilot_generate_artifact_fixture.py check
source current content_hash:      sha256:351f3761f47f66aa0000196e56712bd95dcdd1f7733b9984539ffb444534986a
derived generated_from_revision:  sha256:351f3761f47f66aa0000196e56712bd95dcdd1f7733b9984539ffb444534986a
CURRENT: derived fixture matches current source content
exit=0
```

### 3. Introduce a real defect — edit source, do not regenerate

Source edited: `retry_limit: 3 -> 5`, `timeout_seconds: 30 -> 45`,
`status: draft -> reviewed`. Committed without touching the derived file:

```
$ git commit -m "Introduce pilot defect: change source facts without regenerating derived fixture"
3384d23
```

Validation correctly flags staleness:

```
$ python3 scripts/pilot_generate_artifact_fixture.py check
source current content_hash:      sha256:ad18e0ad969c59a8a4631bbb2cad384f60e24abef66c98a9d4be3905e40ed7ee
derived generated_from_revision:  sha256:351f3761f47f66aa0000196e56712bd95dcdd1f7733b9984539ffb444534986a
STALE: source content has changed since the derived fixture was generated
exit=1
```

This is a genuine, reproducible mismatch (not a fabricated flag): the
derived file's recorded `generated_from_revision` hash literally does not
match the current source content hash.

### 4. Fix — regenerate derived artifact from source revision B

```
$ python3 scripts/pilot_generate_artifact_fixture.py generate
GENERATED docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_derived.md
generated_from_revision: sha256:ad18e0ad969c59a8a4631bbb2cad384f60e24abef66c98a9d4be3905e40ed7ee
```

Committed as revision B (fix):

```
$ git commit -m "Fix pilot defect: regenerate derived fixture from current source revision"
03793fc
```

### 5. Validate final artifact (expect CURRENT)

```
$ python3 scripts/pilot_generate_artifact_fixture.py check
source current content_hash:      sha256:ad18e0ad969c59a8a4631bbb2cad384f60e24abef66c98a9d4be3905e40ed7ee
derived generated_from_revision:  sha256:ad18e0ad969c59a8a4631bbb2cad384f60e24abef66c98a9d4be3905e40ed7ee
CURRENT: derived fixture matches current source content
exit=0
```

### 6. Compare source revisions

```
$ git log --oneline -3
03793fc Fix pilot defect: regenerate derived fixture from current source revision
3384d23 Introduce pilot defect: change source facts without regenerating derived fixture
6fb1780 Add AES artifact-freshness pilot fixtures (revision A, current)
```

The prior (stale) derived-fixture version remains retrievable via git
history at commit `3384d23` (rollback readiness), satisfying the pilot
spec's rollback constraint.

## Before/after content hashes

| State | Source content_hash | Derived `generated_from_revision` | check result |
| --- | --- | --- | --- |
| Revision A (6fb1780) | `sha256:351f3761f4...534986a` | `sha256:351f3761f4...534986a` | CURRENT (exit 0) |
| Defect (3384d23) | `sha256:ad18e0ad96...5e40ed7ee` | `sha256:351f3761f4...534986a` (stale) | STALE (exit 1) |
| Regenerated (03793fc) | `sha256:ad18e0ad96...5e40ed7ee` | `sha256:ad18e0ad96...5e40ed7ee` | CURRENT (exit 0) |

Full hashes are recorded in
`docs/autonomous_execution/examples/pilot_evidence/artifact_freshness_pilot.json`.

## Execution record

A structurally valid execution record demonstrating the full
`AUTONOMOUS_EXECUTION_STANDARD.md` Section 11.3 artifact-freshness contract
(`generated_from_revision`, `source_inputs[].content_hash`,
`freshness_status` transitioning `stale` -> `current`) is saved at
`docs/autonomous_execution/examples/pilot_evidence/artifact_freshness_pilot.json`.
It validates against `schemas/autonomous_execution_record.schema.json`:

```
$ python3 -c "
import json, jsonschema
schema = json.load(open('schemas/autonomous_execution_record.schema.json'))
record = json.load(open('docs/autonomous_execution/examples/pilot_evidence/artifact_freshness_pilot.json'))
jsonschema.validate(record, schema)
print('SCHEMA VALID')
"
SCHEMA VALID
```

It records `art-001` (`freshness_status: current`, matching the final
source content hash after regeneration) and `art-000-stale-snapshot`
(`freshness_status: stale`, the honestly-recorded first, stale generation)
— per the pilot spec's acceptance criterion, the first artifact is recorded
as `stale`, not silently skipped, and `overall_delivery: pass` is only
asserted after the final artifact reached `current`.

## Gap analysis: canonical contract vs. what was actually observable

- **Content-hash freshness works cleanly for text artifacts.** The
  sha256-over-file-bytes approach mirrors what
  `scripts/check_knowledge_bundles.py` already does for real Knowledge
  Bundles (`source_fingerprint`), and it detected the seeded defect
  correctly and deterministically.
- **No pipeline exists yet for binary generated artifacts** (DOCX, XLSX,
  PDF, PPTX) in this repository, so this pilot could not exercise
  freshness detection against a binary-artifact generation step (e.g. a
  template render with embedded formulas). That remains an open gap for a
  future pilot if/when such tooling is added.
- **`last_changed_iteration` and `generated_in_iteration` are
  self-reported**, not derived automatically from git history by tooling;
  this pilot populated them by hand from the iteration record, matching
  Phase 1's documented scope (structural schema validation only, no
  semantic/automatic iteration tracking — see schema description and
  `AUTONOMOUS_EXECUTION_STANDARD.md` Section 12).
- **The pilot's "generation method" is intentionally trivial** (a ~100-line
  script parsing `- key: value` lines into a markdown table). This is
  sufficient to prove the freshness contract's mechanics but is not
  representative of the complexity of a real report/memo generation
  pipeline; a real pipeline would need to also validate semantic
  correctness of the transform, not just source/artifact hash agreement.

## Scope-acceptance verdict

- First artifact honestly recorded as `stale`, not silently skipped: **yes**
  (`art-000-stale-snapshot`, `def-001`).
- Regenerated artifact's `generated_from_revision` matches the final source
  revision: **yes** (`art-001.generated_from_revision` ==
  `sha256:ad18e0ad969c59a8a4631bbb2cad384f60e24abef66c98a9d4be3905e40ed7ee`,
  the final source content hash at commit `03793fc`).
- `overall_delivery: pass` asserted only once the final artifact is
  `current`: **yes**.

**Pilot verdict: PASS.** The artifact-freshness contract's mechanics
(generate -> validate -> detect defect -> fix source -> regenerate ->
validate final artifact -> compare source revision) were demonstrated end
to end with genuine, reproducible commands and hashes, on a clearly-labeled
pilot fixture pair. This is pilot evidence only; it does not authorize
enforcement or CI blocking of the Autonomous Execution Standard, and it
does not modify or govern real Knowledge Bundle content.

## Baseline checks

Existing repository checks were re-run after the pilot changes; all passed:

```
$ python3 -m pytest tests/ -q
74 passed in 1.40s

$ python3 scripts/check_project_instructions_length.py   # exit=0
$ python3 scripts/check_repo_public_safety.py             # exit=0, "Public safety check passed."
$ python3 scripts/check_codex_goal_mode_defaults.py        # exit=0, Failed: 0
$ python3 scripts/check_manifest_paths.py                  # exit=0, checked: 122, passed: 122, failed: 0
$ python3 scripts/check_knowledge_bundles.py                # exit=0, projects checked: 7, bundles checked: 33, failed: 0
$ python3 scripts/check_index_coverage.py                   # exit=0, Index coverage pairs checked: 9, Failed: 0
```

`check_knowledge_bundles.py` reporting `failed: 0` across all 33 real
bundles confirms this pilot did not touch or destabilize any real Knowledge
Bundle content. The pilot's diff against
`origin/codex/autonomous-execution-standard-v1` touches only three files:
`docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_source.md`,
`docs/autonomous_execution/pilot_fixtures/aes_artifact_pilot_derived.md`,
and `scripts/pilot_generate_artifact_fixture.py`, plus this results doc and
the evidence JSON — no `.github/workflows/*`, `MANIFEST.json`, or
`ChatGPT/*/Knowledge_Bundles/*` files were modified.
