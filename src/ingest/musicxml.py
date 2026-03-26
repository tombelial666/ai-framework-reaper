"""MusicXML file ingestion — minimal deterministic parse (stdlib XML)."""

from __future__ import annotations

import xml.etree.ElementTree as ET

from domain.errors import ParseError
from ingest.contracts import IngestionContext, MusicXmlIngestResult


def ingest_musicxml_path(ctx: IngestionContext) -> MusicXmlIngestResult:
    """Read path and return an ElementTree root or a structured failure."""
    warnings: list[str] = []
    try:
        tree = ET.parse(ctx.source_path)
    except ET.ParseError as e:
        raise ParseError(f"Invalid XML: {e}") from e
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if root.tag else ""
    if tag != "score-partwise" and tag != "score-timewise":
        warnings.append(
            f"Unexpected root element {tag!r}; slice 1 only validates partwise scores."
        )
    return MusicXmlIngestResult(
        success=True,
        source_path=ctx.source_path,
        root_tag=tag or None,
        warnings=warnings,
        xml_root=root,
    )
