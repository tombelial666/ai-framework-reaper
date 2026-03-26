# Data Flow

## Primary Structured-Core Flow

`structured source -> ingestion -> parsed representation -> normalization -> canonical score model -> arrangement mapping -> REAPER integration -> scaffold artifacts + review output`

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
- role assignments
- section and layout plan

### REAPER Output

- editable scaffold artifacts
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
