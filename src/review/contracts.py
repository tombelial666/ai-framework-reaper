"""Review layer contracts."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Warning:
    code: str
    message: str
    source_layer: str


@dataclass
class ReviewReport:
    """Human-facing review artifact for mandatory manual check."""

    summary: str
    warnings: list[Warning] = field(default_factory=list)
    unresolved_fragments: list[str] = field(default_factory=list)
