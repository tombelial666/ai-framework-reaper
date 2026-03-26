"""Aggregate warnings from pipeline stages."""

from __future__ import annotations

from review.contracts import ReviewReport, Warning


def build_review_report(
    *,
    ingest_messages: list[str],
    normalize_messages: list[str],
    mapping_messages: list[str],
    project_title: str,
) -> ReviewReport:
    """Collect warnings into a single review report (slice 1)."""
    warnings: list[Warning] = []
    for i, m in enumerate(ingest_messages):
        warnings.append(Warning(code=f"INGEST-{i}", message=m, source_layer="ingest"))
    for i, m in enumerate(normalize_messages):
        warnings.append(Warning(code=f"NORM-{i}", message=m, source_layer="normalize"))
    for i, m in enumerate(mapping_messages):
        warnings.append(Warning(code=f"MAP-{i}", message=m, source_layer="mapping"))

    summary = (
        f'Review required for "{project_title}". '
        "This output is a draft scaffold; verify tracks, timing, and pitches in REAPER."
    )
    unresolved: list[str] = []
    if warnings:
        unresolved.append("See warning list — resolve or accept before relying on the scaffold.")
    return ReviewReport(
        summary=summary,
        warnings=warnings,
        unresolved_fragments=unresolved,
    )
