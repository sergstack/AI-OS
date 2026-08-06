"""Focused regression test for the AES Codex corrective-loop pilot fixture.

See tests/fixtures/aes_pilot/README.md and docs/pilots/AES_CODEX_PILOT.md.
This test is the primary validation signal for the pilot's seeded defect
(def-pilot-001): clamp_percentage() must clamp both bounds, not just the
upper bound.

Uses the same importlib-by-path loading convention as
tests/test_validation_scripts.py, so this fixture stays import-isolated and
does not depend on tests/ being an importable package.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent
MODULE_PATH = FIXTURE_DIR / "pilot_helper.py"

_spec = importlib.util.spec_from_file_location("aes_pilot_helper", MODULE_PATH)
assert _spec is not None
pilot_helper = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules["aes_pilot_helper"] = pilot_helper
_spec.loader.exec_module(pilot_helper)

clamp_percentage = pilot_helper.clamp_percentage


def test_clamp_percentage_clamps_upper_bound():
    assert clamp_percentage(150) == 100


def test_clamp_percentage_passes_through_in_range_values():
    assert clamp_percentage(42) == 42


def test_clamp_percentage_clamps_lower_bound():
    # This is the case that exposed def-pilot-001: negative input was
    # returned unclamped instead of being floored at 0.
    assert clamp_percentage(-10) == 0
