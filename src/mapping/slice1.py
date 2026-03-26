"""Minimal mapping: one layout row per canonical track."""

from __future__ import annotations

from domain.types import CanonicalProject
from mapping.contracts import ArrangementPlan, LayoutTrack


def map_canonical_to_arrangement(project: CanonicalProject) -> ArrangementPlan:
    """Default slice-1 mapping — stable ordering, no advanced musical roles."""
    notes: list[str] = []
    layout: list[LayoutTrack] = []
    for i, t in enumerate(project.tracks):
        layout.append(
            LayoutTrack(
                layout_id=f"lay-{t.track_id}",
                track_id=t.track_id,
                suggested_reaper_track_name=t.track_name or t.track_id,
                order_index=i,
                role_hint=t.track_role,
            )
        )
        if t.track_role == "drums":
            notes.append(
                "Drums track: canonical events use GM-style MIDI note numbers per hit; human review required."
            )
    if not layout:
        notes.append("No tracks in canonical project; empty arrangement plan.")
    return ArrangementPlan(project_title=project.project_title, layout_tracks=layout, notes=notes)
