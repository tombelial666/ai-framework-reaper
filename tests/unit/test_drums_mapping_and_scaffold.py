"""Unit tests: canonical drums → arrangement → REAPER scaffold (slice 1)."""

from __future__ import annotations

from domain.types import (
    CanonicalProject,
    NoteEvent,
    ProcessingMetadata,
    SourceReference,
    Track,
)
from mapping.slice1 import map_canonical_to_arrangement
from reaper.scaffold import arrangement_to_scaffold_bundle


def _minimal_drums_project(*, events: list[NoteEvent] | None = None) -> CanonicalProject:
    ev = events or [
        NoteEvent(
            event_id="e1",
            track_id="P1",
            measure_ref="m-1",
            start_position=0.0,
            duration=1.0,
            event_type="note",
            midi_pitch=36,
            provenance={"kind": "drum_hit"},
        )
    ]
    return CanonicalProject(
        project_id="u",
        project_title="Drum Test",
        source_references=[SourceReference(id="s", format="musicxml", uri_or_label="x")],
        source_metadata={},
        processing_metadata=ProcessingMetadata(),
        tempo_map=[{"beats_per_minute": 120, "at_quarter": 0.0}],
        time_signatures=[{"beats": 4, "beat_type": 4, "measure_ref": "m-1"}],
        sections=[],
        measures=[],
        tracks=[
            Track(
                track_id="P1",
                track_name="Drums",
                track_role="drums",
                instrument_type="drums",
            )
        ],
        events=ev,
    )


def test_map_canonical_drums_adds_review_note_and_layout() -> None:
    plan = map_canonical_to_arrangement(_minimal_drums_project())
    assert len(plan.layout_tracks) == 1
    lt = plan.layout_tracks[0]
    assert lt.role_hint == "drums"
    assert lt.track_id == "P1"
    assert any("GM-style MIDI" in n for n in plan.notes)


def test_scaffold_bundle_drums_import_notes_mention_gm_channel() -> None:
    plan = map_canonical_to_arrangement(_minimal_drums_project())
    bundle = arrangement_to_scaffold_bundle(plan)
    assert len(bundle.tracks) == 1
    t = bundle.tracks[0]
    assert t.role_hint == "drums"
    assert "channel 10" in t.import_notes.lower()
    assert "36" in t.import_notes and "38" in t.import_notes
    assert any("GM-style MIDI" in h for h in bundle.hints)


def test_non_drums_track_generic_import_notes() -> None:
    proj = _minimal_drums_project()
    proj.tracks = [
        Track(
            track_id="P1",
            track_name="Guitar",
            track_role="unknown",
            instrument_type="unknown",
        )
    ]
    plan = map_canonical_to_arrangement(proj)
    bundle = arrangement_to_scaffold_bundle(plan)
    assert "channel 10" not in bundle.tracks[0].import_notes.lower()
