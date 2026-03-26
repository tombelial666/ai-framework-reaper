"""Minimal canonical types for Phase 1 slice 1 — extend per docs/internal-data-model.md."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

EventType = Literal["note", "rest"]


@dataclass(frozen=True)
class SourceReference:
    id: str
    format: str
    uri_or_label: str = ""


@dataclass
class ProcessingMetadata:
    pipeline_version: str = "0.1.0-slice1"
    notes: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class TimeSignature:
    beats_per_measure: int
    beat_unit: int


@dataclass(frozen=True)
class Measure:
    measure_id: str
    index: int
    time_signature: TimeSignature | None = None


@dataclass(frozen=True)
class Track:
    track_id: str
    track_name: str
    track_role: str
    instrument_type: str


@dataclass
class NoteEvent:
    event_id: str
    track_id: str
    measure_ref: str
    start_position: float
    duration: float
    event_type: EventType
    midi_pitch: int | None = None
    provenance: dict[str, Any] | None = None


@dataclass
class CanonicalProject:
    """Canonical score snapshot — transport-agnostic."""

    project_id: str
    project_title: str
    source_references: list[SourceReference]
    source_metadata: dict[str, str]
    processing_metadata: ProcessingMetadata
    tempo_map: list[dict[str, Any]]
    time_signatures: list[dict[str, Any]]
    sections: list[dict[str, Any]]
    measures: list[Measure]
    tracks: list[Track]
    events: list[NoteEvent]
