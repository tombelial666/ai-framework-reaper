"""Score normalization — slice 1: MusicXML → canonical."""

from normalize.contracts import NormalizationOutcome
from normalize.musicxml import musicxml_to_canonical

__all__ = ["NormalizationOutcome", "musicxml_to_canonical"]
