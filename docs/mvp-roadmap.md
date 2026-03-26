# MVP Roadmap

## Phase 0 - Discovery / Analyst Pack

Goal:

- establish repository foundation;
- define manifesto, scope and architecture;
- capture ADR and permanent memory layers;
- create technical scaffolding plan.

Done criteria:

- repository truth exists in files, not only in chat.

## Phase 1 - MVP Structured Import (tab-first)

Goal:

- **tab-first** structured and semi-structured ingestion (Guitar Pro ecosystem, Songsterr exports where allowed, MIDI, другие adapters);
- normalize into canonical model;
- generate editable **MIDI-oriented** REAPER scaffold;
- produce minimal review report;
- prove pipeline value in order **drums → bass → guitar** (implementation priority).

Done criteria:

- user can start from a supported structured input and get a non-empty editable draft;
- product positioning remains tab-first; MusicXML slice remains a **bridge** implementation path where used.

## Phase 2 - Better Editing Workflow

Goal:

- improve practical manual refinement speed in REAPER-oriented workflows.

Outputs:

- clearer track layout aligned with drums/bass/guitar scaffolding habits
- better marker and region logic
- stronger source-to-result traceability
- improved review helpers

## Phase 3 - Screenshot-Assisted Import

Goal:

- add controlled screenshot pipeline without destabilizing structured-core architecture.

## Phase 4 - Advanced Non-Audio Extensions

Goal:

- improve quality while preserving deterministic architecture and non-audio scope.
