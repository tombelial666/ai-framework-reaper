"""REAPER integration contracts — slice 1."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ReaperTrackScaffold:
    """Human-editable scaffold row for a REAPER track."""

    track_id: str
    name: str
    role_hint: str
    import_notes: str


@dataclass
class ReaperScaffoldBundle:
    """Artifact bundle for manual import / future ReaScript — not a raw .rpp binary."""

    version: str
    project_title: str
    tracks: list[ReaperTrackScaffold]
    markers: list[dict[str, str]] = field(default_factory=list)
    hints: list[str] = field(default_factory=list)
