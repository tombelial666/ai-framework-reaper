"""JSON-oriented helpers for fixtures and golden comparisons (slice 1)."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from domain.types import (
    CanonicalProject,
    Measure,
    NoteEvent,
    ProcessingMetadata,
    SourceReference,
    TimeSignature,
    Track,
)


def canonical_project_to_dict(project: CanonicalProject) -> dict[str, Any]:
    d = asdict(project)
    d["schema"] = "canonical_project_v0"
    return d


def canonical_project_from_dict(d: dict[str, Any]) -> CanonicalProject:
    refs = [
        SourceReference(**r) if isinstance(r, dict) else r
        for r in d["source_references"]
    ]
    proc = d["processing_metadata"]
    if isinstance(proc, dict):
        proc = ProcessingMetadata(**proc)
    measures = [
        Measure(
            measure_id=m["measure_id"],
            index=m["index"],
            time_signature=TimeSignature(**m["time_signature"]) if m.get("time_signature") else None,
        )
        for m in d["measures"]
    ]
    tracks = [Track(**t) for t in d["tracks"]]
    events: list[NoteEvent] = []
    for e in d["events"]:
        events.append(
            NoteEvent(
                event_id=e["event_id"],
                track_id=e["track_id"],
                measure_ref=e["measure_ref"],
                start_position=float(e["start_position"]),
                duration=float(e["duration"]),
                event_type=e["event_type"],
                midi_pitch=e.get("midi_pitch"),
                provenance=e.get("provenance"),
            )
        )
    return CanonicalProject(
        project_id=d["project_id"],
        project_title=d["project_title"],
        source_references=refs,
        source_metadata=dict(d["source_metadata"]),
        processing_metadata=proc,
        tempo_map=list(d["tempo_map"]),
        time_signatures=list(d["time_signatures"]),
        sections=list(d["sections"]),
        measures=measures,
        tracks=tracks,
        events=events,
    )
