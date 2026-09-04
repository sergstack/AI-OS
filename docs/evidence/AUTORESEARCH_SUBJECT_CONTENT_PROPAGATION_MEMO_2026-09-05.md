# AIOS AutoResearch — Subject-Content-Propagation Decision Memo — 2026-09-05

Runtime: `main`@`3b81126cb754a3b4021fa16666b418e62eda5c90`.

Status: **decision memo, not a fix.** Whether the behavior described below
is a defect or an intentional design choice is genuinely ambiguous from the
source alone — both readings are independently supported by text in the
same module. This is routed to `[AI OS]` (context-assembly governance) and
`[Analytics]` (whether the current design still supports the stochasticity
method's evidentiary needs), not resolved unilaterally by `[Codex]`.

## Exact point of loss

`scripts/autoresearch_cli.py::_case_payload(spec, case_id, ctx)`:

```python
def _case_payload(spec: ManualCandidateSpec, case_id: str, ctx: dict) -> str:
    case = next((c for c in spec.cases if c["case_id"] == case_id), {})
    task = case.get("input") or "[no case input provided]"
    return f"{cpc.render_summary(ctx)}\n\n---\nTASK:\n{task}\n"
```

`cpc.render_summary(manifest)` in `scripts/autoresearch_context_pack_compiler.py`
(~line 448) emits, per source: `` `path` (source_class, bytes) — purpose ``
— a **file inventory line**, never the file's actual text. Confirmed by
direct execution on this revision: the C1-R1 baseline and candidate
payloads (`scratchpad/arpilot/state/{baseline,candidate}_payload.txt` on
the executor's machine, referenced in
`AUTORESEARCH_C1R1_LIVE_RUN_2026-09-04.md`) list `ROUTING_RULES.md
(canonical_routing, 2596 bytes)` vs `(canonical_routing, 2593 bytes)` —
the byte-count is the *only* textual difference the subject ever receives
for the file actually being mutated. The literal changed row
("... a prompt or workflow deliverable" vs "... a prompt/workflow
deliverable") never appears in the subject's prompt.

## The ambiguity

`autoresearch_context_pack_compiler.py`'s own module docstring says, in the
same paragraph: this module "assembles the **exact ordered context that
would be sent to a model**" — implying full content is the intent — *and*
"Source selection reuses `PROJECT_CAPABILITIES.yaml`'s existing
`context_entrypoints`/`required_knowledge` governed index (issue #412's own
rule: 'Use governed indexes/manifests... **do not dump the entire
repository**.')" — an explicit anti-dump design rule. `render_summary`'s
actual behavior (manifest-only) satisfies the second reading and
contradicts the first. Nothing in the source resolves which reading is
authoritative; this needs an owner call, not a guess.

## Consequence, independent of intent

Whatever the original intent, the **effect** is that the subject model's
answer in C1-R1 could not have been causally influenced by the mutated
text, because the mutated text was never in its context. The subject's
actual answers (both conditions producing near-identical "Coding task
preparation | [Codex]; [LLM] only for a prompt or workflow deliverable" —
note: even the *candidate* condition echoed the *baseline* wording,
consistent with the subject drawing on its own prior knowledge of this
public repository's routing table rather than on anything in the injected
prompt) are consistent with this gap, not merely suggestive of it.

## Options

### 1. Full content inclusion

`render_summary` (or a new `render_full`) embeds every `ordered_sources`
file's complete text inline. Simple, unambiguous — guarantees the mutation
is visible.

- Directly contradicts issue #412's cited anti-dump rule as currently
  worded; would need that rule explicitly relaxed or reinterpreted by
  `[AI OS]`.
- Cost: the current subject prompt already lists ~10 source files, several
  multi-KB (`PROJECT_INSTRUCTIONS.md` alone is 10,261 bytes on this
  revision); full inclusion multiplies prompt size roughly an order of
  magnitude, with call-timeout and cost-cap implications for a live batch.
- Widens the "content-changed" surface entirely honestly (an accidental
  drift in any other source file becomes visible to the subject too, which
  is arguably a feature, not a bug, for detecting contamination — see
  Option 3 below and `cpc.equivalence_report`).

### 2. Bounded excerpt of just the declared mutable surface

Keep the existing manifest as-is, and additionally inline a literal excerpt
of exactly the mutable surface's anchor region — for `MUT-ROUTING-TIEBREAK`,
the `## Tie-break rules (table body only)` section — using the *already
existing* `autoresearch_shadow_runner.py::mutable_surface_line_ranges`
mechanism (same anchor-resolution logic the hard scope gate already uses to
fail closed if the anchor can't be found). Small, targeted, reuses code
instead of inventing a second content-selection mechanism.

- Directly answers "how do we prove baseline/candidate differ only on the
  declared surface": the *same* excerpted range can feed both the prompt
  and a stronger equivalence check (diff the excerpted baseline/candidate
  text itself, confirm it matches the declared patch's hunks exactly, not
  just that `ROUTING_RULES.md`'s byte count changed).
- Cost: proportional to the mutable surface's own size (a table row, a
  subsection) rather than the whole file — cheap.
- Doesn't fully resolve the anti-dump-vs-full-content tension for a future
  mutable surface that is deliberately broad (e.g. a whole document); it
  resolves the *current* four surfaces cleanly (each anchors a bounded
  subsection already).

### 3. Structured mutated-surface diff

Instead of a literal excerpt, compute and inline a structured statement
("this row changed from X to Y") derived from the patch itself.

- More explicitly "tells" the subject what changed, which is a materially
  different framing than either full content or a plain excerpt — it risks
  smuggling Researcher-style hypothesis/framing into the *subject* prompt
  (the SEMANTIC_EVALUATOR_CONTRACT's anti-leakage rules apply to the
  Judge, not explicitly to the subject, but the same epistemic concern —
  don't tell the thing being measured what answer you expect — plausibly
  applies here too and should be an explicit part of `[AI OS]`'s review).
  Not recommended as a first choice for exactly this reason.

## Recommendation

**Option 2** (bounded excerpt via the existing `mutable_surface_line_ranges`
mechanism): smallest change, reuses already-audited code, produces a
mechanically checkable equivalence proof (excerpt diff == patch hunks) that
directly answers this memo's own question, and does not require relaxing
the anti-dump governance rule for the general case — only for the narrow,
already-bounded mutable-surface anchors that exist today.

## Explicitly not done here

No change to `render_summary`, `_case_payload`, or any context-compiler
code. No test added asserting content propagation (that belongs in the
bucket-1 supporting-tests set once a direction is chosen, or as a
regression test against *current* — manifest-only — behavior in the
meantime, since asserting current behavior doesn't require a method
decision).
