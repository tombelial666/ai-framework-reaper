"""Slice 1 — smoke tests and fixture comparison (minimal suite)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

from domain.serialization import canonical_project_to_dict  # noqa: E402
from slice1_pipeline import (  # noqa: E402
    run_slice1_musicxml,
    scaffold_bundle_to_dict,
)


def test_imports_smoke() -> None:
    import domain  # noqa: F401
    import ingest  # noqa: F401
    import mapping  # noqa: F401
    import normalize  # noqa: F401
    import reaper  # noqa: F401
    import review  # noqa: F401


def test_slice1_pipeline_matches_expected_canonical_and_scaffold() -> None:
    fixture = ROOT / "fixtures" / "structured" / "musicxml" / "minimal_chord.xml"
    exp_c = json.loads((ROOT / "fixtures" / "expected" / "slice1_minimal_canonical.json").read_text(encoding="utf-8"))
    exp_s = json.loads((ROOT / "fixtures" / "expected" / "slice1_minimal_scaffold.json").read_text(encoding="utf-8"))

    project, bundle, report = run_slice1_musicxml(str(fixture), repo_root=ROOT)

    assert canonical_project_to_dict(project) == exp_c
    assert scaffold_bundle_to_dict(bundle) == exp_s
    assert report.summary
    assert "draft scaffold" in report.summary.lower()
