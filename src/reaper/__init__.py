"""REAPER integration — slice 1: JSON/text scaffold bundle, not full .rpp."""

from reaper.contracts import ReaperScaffoldBundle, ReaperTrackScaffold
from reaper.scaffold import arrangement_to_scaffold_bundle

__all__ = [
    "ReaperScaffoldBundle",
    "ReaperTrackScaffold",
    "arrangement_to_scaffold_bundle",
]
