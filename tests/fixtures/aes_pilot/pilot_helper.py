"""AES Codex corrective-loop pilot fixture module.

Isolated fixture for docs/pilots/AES_CODEX_PILOT.md. Not used by any
production code path. See tests/fixtures/aes_pilot/README.md.
"""

from __future__ import annotations


def clamp_percentage(value: float) -> float:
    """Clamp a numeric value into the inclusive percentage range [0, 100].

    This mirrors a realistic small utility (e.g. clamping a progress or
    confidence score before display) so the pilot's corrective loop has a
    real, minimal defect to demonstrate.
    """
    return max(0, min(value, 100))
