"""MusicXML → canonical model. Slice 1 supports a minimal partwise subset only."""

from __future__ import annotations

from typing import Any

from domain.errors import NormalizationError
from domain.types import (
    CanonicalProject,
    Measure,
    NoteEvent,
    ProcessingMetadata,
    SourceReference,
    TimeSignature,
    Track,
)
from ingest.contracts import MusicXmlIngestResult
from normalize.contracts import NormalizationOutcome


def _local(tag: str) -> str:
    """Strip namespace from ElementTree tag."""
    return tag.split("}")[-1] if tag else tag


def _text(el: Any | None, path: str) -> str:
    if el is None:
        return ""
    for child in el:
        if _local(child.tag) == path:
            return (child.text or "").strip()
    return ""


def _first_measure(part: Any) -> Any | None:
    for ch in part:
        if _local(ch.tag) == "measure":
            return ch
    return None


def _pitch_to_midi(step: str, octave: int, alter: int = 0) -> int:
    base = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}.get(step.upper(), 0)
    return (octave + 1) * 12 + base + alter


def musicxml_to_canonical(
    ingest: MusicXmlIngestResult,
    *,
    project_id: str = "slice1-minimal",
    source_label: str = "musicxml",
) -> NormalizationOutcome:
    """Map ingested MusicXML root to canonical project (minimal rules)."""
    warnings: list[str] = list(ingest.warnings)
    if not ingest.success or ingest.xml_root is None:
        raise NormalizationError("Ingest result not successful")

    root = ingest.xml_root
    if _local(root.tag) != "score-partwise":
        raise NormalizationError("Slice 1 requires score-partwise MusicXML")

    title = ""
    work = next((c for c in root if _local(c.tag) == "work"), None)
    if work is not None:
        title = _text(work, "work-title")

    part_list = next((c for c in root if _local(c.tag) == "part-list"), None)
    if part_list is None:
        raise NormalizationError("Missing part-list")

    score_parts = [c for c in part_list if _local(c.tag) == "score-part"]
    if not score_parts:
        raise NormalizationError("No score-part in part-list")

    part_id = score_parts[0].get("id") or "P1"
    part_name = ""
    for sp in score_parts:
        if sp.get("id") == part_id:
            part_name = _text(sp, "part-name") or part_id
            break

    part_el = next((c for c in root if _local(c.tag) == "part" and c.get("id") == part_id), None)
    if part_el is None:
        part_el = next((c for c in root if _local(c.tag) == "part"), None)
    if part_el is None:
        raise NormalizationError("No part element")

    measure_el = _first_measure(part_el)
    if measure_el is None:
        raise NormalizationError("No measure in part")

    divisions = 1
    attrs = next((c for c in measure_el if _local(c.tag) == "attributes"), None)
    ts_el = None
    if attrs is not None:
        div_el = next((c for c in attrs if _local(c.tag) == "divisions"), None)
        if div_el is not None and div_el.text:
            divisions = max(1, int(div_el.text.strip()))
        ts_el = next((c for c in attrs if _local(c.tag) == "time"), None)

    beats, beat_type = 4, 4
    if ts_el is not None:
        b = next((c for c in ts_el if _local(c.tag) == "beats"), None)
        bt = next((c for c in ts_el if _local(c.tag) == "beat-type"), None)
        if b is not None and b.text:
            beats = int(b.text.strip())
        if bt is not None and bt.text:
            beat_type = int(bt.text.strip())

    measure_num = measure_el.get("number") or "1"
    measure_id = f"m-{measure_num}"

    events: list[NoteEvent] = []
    cursor = 0.0
    for child in measure_el:
        tag = _local(child.tag)
        if tag == "note":
            dur_el = next((c for c in child if _local(c.tag) == "duration"), None)
            duration_raw = int(dur_el.text.strip()) if dur_el is not None and dur_el.text else 0
            duration_q = float(duration_raw) / float(divisions)
            rest_el = next((c for c in child if _local(c.tag) == "rest"), None)
            if rest_el is not None:
                eid = f"evt-rest-{measure_num}-{cursor}"
                events.append(
                    NoteEvent(
                        event_id=eid,
                        track_id=part_id,
                        measure_ref=measure_id,
                        start_position=cursor,
                        duration=duration_q,
                        event_type="rest",
                        midi_pitch=None,
                        provenance={"source": "musicxml", "measure": str(measure_num)},
                    )
                )
            else:
                pitch_el = next((c for c in child if _local(c.tag) == "pitch"), None)
                step, octave, alter = "C", 4, 0
                if pitch_el is not None:
                    s = next((c for c in pitch_el if _local(c.tag) == "step"), None)
                    o = next((c for c in pitch_el if _local(c.tag) == "octave"), None)
                    a = next((c for c in pitch_el if _local(c.tag) == "alter"), None)
                    if s is not None and s.text:
                        step = s.text.strip()
                    if o is not None and o.text:
                        octave = int(o.text.strip())
                    if a is not None and a.text:
                        alter = int(a.text.strip())
                midi = _pitch_to_midi(step, octave, alter)
                eid = f"evt-note-{measure_num}-{cursor}"
                events.append(
                    NoteEvent(
                        event_id=eid,
                        track_id=part_id,
                        measure_ref=measure_id,
                        start_position=cursor,
                        duration=duration_q,
                        event_type="note",
                        midi_pitch=midi,
                        provenance={"source": "musicxml", "measure": str(measure_num)},
                    )
                )
            cursor += duration_q

    if not title:
        title = "Untitled"
        warnings.append("Missing work-title; using placeholder title.")

    ts = TimeSignature(beats_per_measure=beats, beat_unit=beat_type)
    project = CanonicalProject(
        project_id=project_id,
        project_title=title,
        source_references=[
            SourceReference(id="src-1", format="musicxml", uri_or_label=source_label)
        ],
        source_metadata={"encoding": "musicxml3-partwise"},
        processing_metadata=ProcessingMetadata(
            pipeline_version="0.1.0-slice1",
            notes=["slice1 minimal MusicXML path"],
        ),
        tempo_map=[{"beats_per_minute": 120, "at_quarter": 0.0}],
        time_signatures=[{"beats": beats, "beat_type": beat_type, "measure_ref": measure_id}],
        sections=[],
        measures=[
            Measure(measure_id=measure_id, index=int(measure_num) if measure_num.isdigit() else 1, time_signature=ts)
        ],
        tracks=[
            Track(
                track_id=part_id,
                track_name=part_name,
                track_role="unknown",
                instrument_type="unknown",
            )
        ],
        events=events,
    )
    if not events:
        warnings.append("No note or rest events extracted; empty measure?")

    return NormalizationOutcome(project=project, warnings=warnings)
