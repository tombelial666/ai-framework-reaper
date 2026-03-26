# ADR-003: Guitar Pro Ingestion Strategy

## Status

Proposed

## Decision

Treat Guitar Pro related structured sources as the preferred MVP ingestion path, with `MIDI` and `MusicXML` as explicit fallback paths and manual text/tab as manual-assisted fallback.

## Rationale

- aligns with user value around part reuse and cover preparation;
- preserves structured-first MVP direction.

## Trade-Off

- exact source fidelity may vary across concrete paths;
- direct support and converted support should not be conflated.

## Assumption

- At least one concrete path can provide sufficient deterministic data for MVP.
