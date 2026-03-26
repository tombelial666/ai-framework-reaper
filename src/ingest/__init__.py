"""Source adapters — slice 1: MusicXML only."""

from ingest.contracts import IngestionContext, MusicXmlIngestResult
from ingest.musicxml import ingest_musicxml_path

__all__ = [
    "IngestionContext",
    "MusicXmlIngestResult",
    "ingest_musicxml_path",
]
