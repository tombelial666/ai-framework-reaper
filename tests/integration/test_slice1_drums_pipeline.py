"""Integration tests: full slice-1 path for drums (invariants, not golden JSON)."""

from __future__ import annotations

from pathlib import Path

from domain.serialization import canonical_project_to_dict
from slice1_pipeline import run_slice1_musicxml, scaffold_bundle_to_dict


def test_minimal_drums_pipeline_end_to_end_invariants(repo_root: Path) -> None:
    fixture = repo_root / "fixtures" / "structured" / "musicxml" / "minimal_drums.xml"
    project, bundle, report = run_slice1_musicxml(str(fixture), repo_root=repo_root)

    drum_events = [e for e in project.events if e.event_type == "note"]
    assert len(drum_events) == 2
    assert [e.midi_pitch for e in drum_events] == [36, 38]
    assert project.tracks[0].track_role == "drums"

    d = scaffold_bundle_to_dict(bundle)
    assert d["project_title"] == "Minimal Drums"
    assert len(d["tracks"]) == 1
    assert d["tracks"][0]["role_hint"] == "drums"
    assert "channel 10" in d["tracks"][0]["import_notes"].lower()

    cdict = canonical_project_to_dict(project)
    assert cdict["project_title"] == "Minimal Drums"
    assert any(r.get("format") == "musicxml" for r in cdict["source_references"])

    assert report.summary
    assert report.summary.lower().count("draft") >= 1
