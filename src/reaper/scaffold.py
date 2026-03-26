"""Build minimal scaffold bundle from arrangement plan."""

from __future__ import annotations

from mapping.contracts import ArrangementPlan
from reaper.contracts import ReaperScaffoldBundle, ReaperTrackScaffold


def arrangement_to_scaffold_bundle(plan: ArrangementPlan) -> ReaperScaffoldBundle:
    """Map arrangement plan to editable scaffold description (JSON-serializable)."""
    tracks = [
        ReaperTrackScaffold(
            track_id=lt.track_id,
            name=lt.suggested_reaper_track_name,
            role_hint=lt.role_hint,
            import_notes="Create track; import MIDI or draw items manually from canonical events.",
        )
        for lt in sorted(plan.layout_tracks, key=lambda x: x.order_index)
    ]
    hints = [
        "Draft scaffold - human review required before treating as performance-ready.",
        "REAPER is the target editing environment for this bundle.",
    ]
    hints.extend(plan.notes)
    return ReaperScaffoldBundle(
        version="0.1.0-slice1",
        project_title=plan.project_title,
        tracks=tracks,
        markers=[],
        hints=hints,
    )
