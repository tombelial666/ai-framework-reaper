"""Canonical score model and shared types (DAW-agnostic, source-agnostic)."""

from domain.errors import NormalizationError, ParseError
from domain.types import (
    CanonicalProject,
    NoteEvent,
    ProcessingMetadata,
    SourceReference,
    TimeSignature,
    Track,
    Measure,
)

__all__ = [
    "CanonicalProject",
    "Measure",
    "NormalizationError",
    "NoteEvent",
    "ParseError",
    "ProcessingMetadata",
    "SourceReference",
    "TimeSignature",
    "Track",
]
