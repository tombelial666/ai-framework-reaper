"""Vertical slice 1 — MusicXML → canonical → arrangement → scaffold → review."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from domain.types import CanonicalProject
from ingest.contracts import IngestionContext
from ingest.musicxml import ingest_musicxml_path
from mapping.slice1 import map_canonical_to_arrangement
from normalize.musicxml import musicxml_to_canonical
from reaper.contracts import ReaperScaffoldBundle
from reaper.scaffold import arrangement_to_scaffold_bundle
from review.contracts import ReviewReport
from review.report import build_review_report


def _source_label_for_canonical(source_path: str, *, repo_root: Path | None) -> str:
    """Stable, portable label for provenance (repo-relative when possible)."""
    p = Path(source_path).resolve()
    base = (repo_root or Path.cwd()).resolve()
    try:
        return p.relative_to(base).as_posix()
    except ValueError:
        return p.as_posix()


def run_slice1_musicxml(
    source_path: str,
    *,
    project_id: str = "slice1-minimal",
    repo_root: Path | None = None,
) -> tuple[CanonicalProject, ReaperScaffoldBundle, ReviewReport]:
    """Run ingest → normalize → map → reaper → review for one MusicXML file."""
    ctx = IngestionContext(source_path=source_path, source_format_hint="musicxml")
    ingested = ingest_musicxml_path(ctx)
    normalized = musicxml_to_canonical(
        ingested,
        project_id=project_id,
        source_label=_source_label_for_canonical(source_path, repo_root=repo_root),
    )
    plan = map_canonical_to_arrangement(normalized.project)
    bundle = arrangement_to_scaffold_bundle(plan)
    report = build_review_report(
        ingest_messages=ingested.warnings,
        normalize_messages=normalized.warnings,
        mapping_messages=plan.notes,
        project_title=normalized.project.project_title,
    )
    return normalized.project, bundle, report


def scaffold_bundle_to_dict(bundle: ReaperScaffoldBundle) -> dict:
    """JSON-friendly dict for fixtures and tests."""
    return asdict(bundle)
