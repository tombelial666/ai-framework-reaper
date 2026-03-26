"""Normalization layer contracts."""

from __future__ import annotations

from dataclasses import dataclass, field

from domain.types import CanonicalProject


@dataclass
class NormalizationOutcome:
    """Result of normalization — canonical model plus local warnings."""

    project: CanonicalProject
    warnings: list[str] = field(default_factory=list)
