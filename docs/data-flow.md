# Data Flow

## Primary Structured-Core Flow (tab-first)

`tab/notation structured source -> ingestion (adapters) -> parsed representation -> normalization -> canonical score model -> arrangement mapping -> REAPER integration -> MIDI-oriented scaffold artifacts + review output`

Bridge formats such as **MusicXML** participate as **adapters** into the same canonical path; they are not the product identity.

## Secondary Screenshot Flow

`image input -> vision preprocessing -> semi-structured extraction -> normalization -> canonical score model -> arrangement mapping -> REAPER integration -> warning-heavy scaffold + review output`

## Stage Outputs

### Ingestion Output

- parsed source representation
- validation results
- source metadata
- ingestion warnings

### Normalization Output

- canonical score model
- unresolved fields
- provenance links

### Mapping Output

- track plan
- role assignments (implementation emphasis: **drums → bass → guitar** where applicable)
- section and layout plan

### REAPER Output

- editable **MIDI-oriented** scaffold artifacts (bundles, importable forms; future `.rpp`/script paths per integration strategy)
- track structure
- markers and regions where supported
- traceability metadata

### Review Output

- warning list
- unresolved markers
- manual review checklist items

## Failure and Warning Philosophy

- hard failure: source is unreadable or unusable for deterministic normalization;
- warning: source is partially usable but incomplete or ambiguous;
- deferred enrichment: extra fidelity may be added later, but MVP must not fake it now.
