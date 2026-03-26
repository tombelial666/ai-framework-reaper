"""Domain-level errors for ingestion and normalization."""


class ParseError(Exception):
    """Deterministic parse failure (hard failure for unusable input)."""


class NormalizationError(Exception):
    """Cannot map parsed source to a usable canonical score at scaffold level."""
