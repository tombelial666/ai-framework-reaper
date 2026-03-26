"""Mapping layer contracts — slice 1."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class LayoutTrack:
    layout_id: str
    track_id: str
    suggested_reaper_track_name: str
    order_index: int
    role_hint: str


@dataclass
class ArrangementPlan:
    """Deterministic layout intent for REAPER scaffold generation (not final mix)."""

    project_title: str
    layout_tracks: list[LayoutTrack]
    notes: list[str] = field(default_factory=list)
