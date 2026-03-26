# ADR-004: Score Normalization Model

## Status

Accepted

## Decision

Adopt a source-agnostic and REAPER-agnostic canonical score model as the mandatory internal representation for MVP and beyond. Product-facing sources include tabs/notation ecosystems (Guitar Pro, Songsterr exports where allowed, MIDI, etc.); interchange formats such as **MusicXML** normalize through adapters without becoming the conceptual core.

## Rationale

- prevents coupling to any single source format;
- enables deterministic mapping and review;
- keeps future extensions compatible.

## Trade-Off

- requires deliberate field design and provenance handling;
- some format-specific details may remain optional or warning-backed in MVP.
