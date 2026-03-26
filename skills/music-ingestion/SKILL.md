---
name: music-ingestion
description: Analyze structured and semi-structured music ingestion workflows for the REAPER scaffold framework. Use when defining source detection, parser boundaries, validation rules, normalization inputs, or warning behavior for Guitar Pro related sources, MIDI, MusicXML, text/tab-like inputs, or screenshot paths.
---

# Music Ingestion

## Use This Skill For

- source ingestion analysis;
- parser boundary definition;
- validation and warning strategy;
- normalization handoff planning.

## Default Workflow

1. Classify the source path: structured-core or screenshot-secondary.
2. State `Confirmed`, `Assumption`, `Risk`, `Deferred`, `Open Question`.
3. Define what metadata the ingestion layer must capture.
4. Define what parsed representation must hand off to normalization.
5. Mark missing or unreliable fields as warnings instead of fabricating data.

## Boundary Rules

- Do not put REAPER-specific logic into ingestion.
- Do not claim correctness beyond source fidelity.
- Do not let screenshot handling redefine the structured-core architecture.
