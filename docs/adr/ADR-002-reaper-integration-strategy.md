# ADR-002: REAPER Integration Strategy

## Status

Proposed

## Decision

REAPER integration must consume mapped canonical data and generate an **editable scaffold**, not own parsing or musical interpretation logic.

## Rationale

- protects architecture boundaries;
- supports traceability;
- keeps target-specific concerns at the edge.

## Trade-Off

- requires explicit intermediate mapping artifacts;
- exact first scaffold mechanism remains open.

## Open Question

- Which concrete REAPER-compatible artifact should be first in implementation.
