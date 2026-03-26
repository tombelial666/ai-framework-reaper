# ADR-001: Target Architecture

## Status

Accepted

## Decision

Use a layered pipeline:

`ingest -> normalize -> mapping -> reaper -> review`

with isolated `vision` as a secondary path and a mandatory canonical score model in the center.

## Rationale

- keeps structured-core deterministic;
- isolates REAPER-specific behavior;
- allows future input expansion without rewriting the core.

## Trade-Off

- more upfront structure and documentation;
- less short-term speed than an ad-hoc script.
