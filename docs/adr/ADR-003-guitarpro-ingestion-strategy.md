# ADR-003: Guitar Pro Ingestion Strategy

## Status

Proposed

## Decision

Treat **Guitar Pro related structured sources** as the preferred **product-level** MVP ingestion path for tab-first workflows. Also explicitly recognize **Songsterr-exported / derived structured sources** where legally and technically available. Use `MIDI` and `MusicXML` as explicit **fallback/bridge** paths and manual text/tab as manual-assisted fallback.

## Rationale

- aligns with user value around part reuse, covers, and reinterpretation;
- preserves structured-first MVP direction;
- separates **product sources** (tabs/notation ecosystem) from **bridge formats** (MusicXML interchange).

## Trade-Off

- exact source fidelity may vary across concrete paths;
- direct support and converted support should not be conflated;
- Songsterr-related inputs depend on user-side export rules (**Risk** if ToS violated).

## Assumption

- At least one concrete path can provide sufficient deterministic data for MVP.

## Related

- Implementation order for the **first code slice** is recorded in [ADR-006-phase1-first-implementation-slice.md](ADR-006-phase1-first-implementation-slice.md) (**MusicXML first as bridge**; Guitar Pro remains MVP scope for a follow-on slice).
- **Implementation emphasis** for proving value: drums → bass → guitar (see `MANIFEST.md`).
