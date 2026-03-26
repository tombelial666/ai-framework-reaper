# ADR-001: Target Architecture

## Status

Accepted

## Decision

Use a layered pipeline:

`ingest -> normalize -> mapping -> reaper -> review`

with isolated `vision` as a secondary path and a mandatory canonical score model in the center. Ingestion is organized around **tab/notation source adapters** plus **bridge formats** (e.g. MusicXML) into the same canonical path.

## Rationale

- keeps structured-core deterministic;
- isolates REAPER-specific behavior;
- allows future tab-source expansion without rewriting the core;
- preserves tab-first product framing while keeping interchange formats as adapters.

## Trade-Off

- more upfront structure and documentation;
- less short-term speed than an ad-hoc script.
