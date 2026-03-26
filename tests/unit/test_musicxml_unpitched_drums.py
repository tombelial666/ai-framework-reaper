"""Unit tests: MusicXML unpitched drum positions → canonical (GM) — slice 1."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from domain.errors import NormalizationError
from ingest.contracts import MusicXmlIngestResult
from normalize.musicxml import musicxml_to_canonical


def _ingest_from_string(xml: str) -> MusicXmlIngestResult:
    root = ET.fromstring(xml)
    return MusicXmlIngestResult(
        success=True,
        source_path="<string>",
        root_tag="score-partwise",
        warnings=[],
        xml_root=root,
    )


def _minimal_score(
    *,
    work_title: str = "T",
    part_name: str = "Drums",
    measure_inner: str,
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<score-partwise version="3.1">
  <work><work-title>{work_title}</work-title></work>
  <part-list>
    <score-part id="P1"><part-name>{part_name}</part-name></score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <time><beats>4</beats><beat-type>4</beat-type></time>
      </attributes>
      {measure_inner}
    </measure>
  </part>
</score-partwise>
"""


def test_unpitched_f4_and_c5_map_to_gm_36_and_38() -> None:
    inner = """
      <note>
        <unpitched><display-step>F</display-step><display-octave>4</display-octave></unpitched>
        <duration>1</duration>
      </note>
      <note>
        <unpitched><display-step>C</display-step><display-octave>5</display-octave></unpitched>
        <duration>1</duration>
      </note>
    """
    out = musicxml_to_canonical(_ingest_from_string(_minimal_score(measure_inner=inner)))
    notes = [e for e in out.project.events if e.event_type == "note"]
    assert [e.midi_pitch for e in notes] == [36, 38]
    assert all((e.provenance or {}).get("kind") == "drum_hit" for e in notes)
    assert out.project.tracks[0].track_role == "drums"


def test_unsupported_unpitched_position_warns_and_omits_note_event() -> None:
    inner = """
      <note>
        <unpitched><display-step>G</display-step><display-octave>5</display-octave></unpitched>
        <duration>1</duration>
      </note>
    """
    out = musicxml_to_canonical(_ingest_from_string(_minimal_score(measure_inner=inner)))
    assert not any(e.event_type == "note" for e in out.project.events)
    assert any("Unsupported unpitched drum position G/5" in w for w in out.warnings)


def test_display_step_lowercase_first_letter_still_maps() -> None:
    inner = """
      <note>
        <unpitched><display-step>f</display-step><display-octave>4</display-octave></unpitched>
        <duration>1</duration>
      </note>
    """
    out = musicxml_to_canonical(_ingest_from_string(_minimal_score(measure_inner=inner)))
    notes = [e for e in out.project.events if e.event_type == "note"]
    assert len(notes) == 1
    assert notes[0].midi_pitch == 36


def test_track_role_drums_from_part_name_even_without_unpitched() -> None:
    inner = """
      <note>
        <pitch><step>C</step><octave>4</octave></pitch>
        <duration>1</duration>
      </note>
    """
    out = musicxml_to_canonical(_ingest_from_string(_minimal_score(part_name="Drums", measure_inner=inner)))
    assert out.project.tracks[0].track_role == "drums"
    assert out.project.events[0].midi_pitch is not None


def test_ingest_not_success_raises() -> None:
    bad = MusicXmlIngestResult(
        success=False,
        source_path="x",
        root_tag=None,
        warnings=[],
        xml_root=None,
    )
    with pytest.raises(NormalizationError, match="not successful"):
        musicxml_to_canonical(bad)


def test_fixture_minimal_drums_xml_parses_same_gm_hits(repo_root: Path) -> None:
    """Sanity: on-disk minimal fixture stays aligned with string-built case."""
    path = repo_root / "fixtures" / "structured" / "musicxml" / "minimal_drums.xml"
    root = ET.parse(path).getroot()
    out = musicxml_to_canonical(
        MusicXmlIngestResult(
            success=True,
            source_path=str(path),
            root_tag="score-partwise",
            warnings=[],
            xml_root=root,
        )
    )
    notes = [e for e in out.project.events if e.event_type == "note"]
    assert [e.midi_pitch for e in notes] == [36, 38]
