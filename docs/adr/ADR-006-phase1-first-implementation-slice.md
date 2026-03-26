# ADR-006: Phase 1 First Implementation Slice (MusicXML as Bridge)

## Status

Accepted

## Context

- ADR-003 positions Guitar Pro related sources and the broader **tab-first** ecosystem as the preferred **MVP ingestion story** at the product level.
- Phase 1 still requires a **first vertical slice** that is easy to validate deterministically without binary parsers or license-dependent tooling.
- **MusicXML must not be mistaken for the product identity:** it is an interchange **bridge** toward the canonical model.

## Decision

The **first code slice** implements end-to-end contracts using **MusicXML** as the sole primary **structured input in code**:

1. `ingest` — MusicXML file → parsed handle / validated tree (implementation may use stdlib XML first).
2. `normalize` — parsed MusicXML → canonical `domain` score model.
3. `mapping` — canonical model → minimal arrangement plan (track layout intent); subsequent increments should align with **drums → bass → guitar** proving order.
4. `reaper` — arrangement plan → minimal REAPER-oriented **MIDI-scaffold** bundle (JSON/text artifacts, not a full `.rpp` generator in slice 1).
5. `review` — cross-cutting warnings + review report from pipeline stages.

Guitar Pro related ingestion remains **in MVP scope** per `MANIFEST.md` but is **deferred to a follow-up slice** after the MusicXML path proves the pipeline.

## Rationale

- Text-based fixtures diff cleanly in git.
- XML parsing is deterministic with fixed inputs.
- Avoids coupling slice 1 to a specific Guitar Pro library or conversion path.
- Establishes canonical and mapping contracts before deeper tab adapters.

## Trade-Off

- Product story (**tab-first**, Guitar Pro / Songsterr / MIDI) and implementation order (**MusicXML bridge first**) diverge briefly; this ADR makes that explicit.

## Confirmed

- Slice 1 does not include screenshot/vision, audio, or vocals.

## Deferred

- Guitar Pro adapter, MIDI, manual text/tab parsers, full `.rpp` export, rich arrangement heuristics.
