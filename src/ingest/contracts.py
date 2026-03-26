"""Ingestion layer contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class IngestionContext:
    """What the adapter knows before parsing."""

    source_path: str
    source_format_hint: str | None = "musicxml"


@dataclass
class MusicXmlIngestResult:
    """Output of MusicXML ingestion — slice 1."""

    success: bool
    source_path: str
    root_tag: str | None
    warnings: list[str]
    xml_root: Any | None  # xml.etree.ElementTree.Element when success
