# Phase 1 — First Implementation Slice (MusicXML as Technical Bridge)

## Selected slice

**End-to-end deterministic path:** `MusicXML file → canonical score → arrangement plan → REAPER-oriented MIDI-scaffold bundle (JSON) → review report.**

**Primary structured input in code:** **MusicXML 3.x** (partwise), starting with minimal single-part scores.

**Product positioning:** the repository is **tab-first**; MusicXML is the **first implementation bridge**, not the headline product.

## Why this slice

- **Determinism:** same fixture XML yields the same canonical JSON shape (modulo explicit versioning later).
- **Validation:** human-readable fixtures and expected JSON snapshots.
- **Dependencies:** stdlib `xml.etree` or `lxml` optional later; no proprietary formats in slice 1.
- **Architecture proof:** exercises all six logical layers used in structured-core path (vision excluded).

## What it proves

- Boundaries between `domain`, `ingest`, `normalize`, `mapping`, `reaper`, `review` are usable.
- Canonical model can be populated from at least one real interchange format (**bridge**).
- Scaffold + review outputs exist as explicit artifacts for human-in-the-loop workflow.

## What it intentionally does not solve yet

- Guitar Pro / MIDI / manual tab ingestion (next slices per product priorities).
- Full REAPER `.rpp` project generation (may come later; slice 1 uses a manifest + track list as editable scaffold).
- Musical interpretation beyond mapping defaults (e.g. sophisticated roles).
- Screenshot pipeline (`src/vision/`).

## Next proving order (after slice 1 stabilizes)

**Drums → bass → guitar** in mapping depth, fixtures, and tests: deterministic event mapping, easier review, strong early scaffold value (see `MANIFEST.md`).

## Dependencies avoided (for now)

- Guitar Pro SDKs and binary readers.
- Audio DSP, ML, or transcription stacks.
- Heavy DAW-specific binary writers.

## Module boundaries (slice 1)

| Module | Responsibility | Inputs | Outputs | In slice 1 | Deferred |
|--------|----------------|--------|---------|------------|----------|
| `src/domain/` | Canonical types, errors, JSON helpers | — | `CanonicalProject`, domain errors | Dataclasses + `serialization.py` | Rich editorial metadata; full provenance granularity |
| `src/ingest/` | Read MusicXML, validate root | File path (`IngestionContext`) | `MusicXmlIngestResult` (ElementTree root) | `musicxml.py` stdlib XML | Guitar Pro, MIDI, manual tab, timewise scores |
| `src/normalize/` | Parsed XML → canonical | `MusicXmlIngestResult` | `NormalizationOutcome` | `musicxml.py` minimal partwise subset | Full MusicXML spec, multiple parts/voices |
| `src/mapping/` | Canonical → layout plan | `CanonicalProject` | `ArrangementPlan` | One `LayoutTrack` per canonical track | Smart roles, sections, stems; drums→bass→guitar depth |
| `src/reaper/` | Plan → editable scaffold bundle | `ArrangementPlan` | `ReaperScaffoldBundle` (JSON-serializable) | Text hints + track rows | Native `.rpp` writer, ReaScript |
| `src/review/` | Aggregate warnings → report | Stage messages + title | `ReviewReport` | `build_review_report` | Rich UX, IDE integration |
| `src/slice1_pipeline.py` | Glue for slice 1 | MusicXML path | project, bundle, report | `run_slice1_musicxml` | Other pipelines |

Python package layout: пакеты `domain`, `ingest`, `normalize`, `mapping`, `reaper`, `review` под `src/`; модуль верхнего уровня `slice1_pipeline` для склейки среза.

## Validation (slice 1)

- Fixture: `fixtures/structured/musicxml/minimal_chord.xml`
- Expected shapes: `fixtures/expected/slice1_minimal_canonical.json`, `fixtures/expected/slice1_minimal_scaffold.json`
- Tests: `tests/unit/test_slice1_contracts.py` (imports + JSON shape smoke checks)
- Full parsing/normalization tests are added when logic is implemented.
