# Architecture

## Human-in-the-loop

- **Human-in-the-loop** is mandatory: the system produces a **draft**—editable **MIDI-oriented** scaffolds, warnings, unresolved markers, and review-oriented outputs—not final arrangements or production-ready masters.
- **REAPER** is the target **editing environment**: the scaffold is meant to be opened and refined there; the pipeline does not replace manual musical decisions.
- The Review Assistance layer is part of the trust model, not optional polish; it exists so users can verify and correct results.

## Product framing

- **Tab-first:** ingestion is organized around **tab-source adapters** (Guitar Pro ecosystem, Songsterr exports where allowed, MIDI, other notation) and **bridge formats** (e.g. MusicXML) into the canonical model.
- **Structured-core path** remains primary; screenshot/vision remains secondary and isolated.

## MVP architectural exclusions (non-goals)

The architecture does **not** target:

- audio transcription;
- audio-first workflows;
- raw audio parsing as a primary path;
- vocal workflow;
- lyric workflow;
- claims of full automatic accuracy.

Additional exclusions are listed in `MANIFEST.md` and `docs/scope.md`.

## Implementation emphasis (instruments)

For proving value and testability, the recommended **implementation order** is **drums → bass → guitar** (deterministic mapping, easier review, strong early scaffold utility). The canonical model stays source-agnostic; this ordering is about **mapping depth and defaults**, not about demoting guitar as a long-term product source.

## Recommended Direction

Рекомендация: строить систему как pipeline из шести логических слоёв с обязательной canonical model между ingestion и downstream integration.

Рационал:

- это держит REAPER-specific logic на краю системы;
- позволяет добавлять новые **tab/notation** inputs без переписывания core;
- не даёт screenshot path диктовать архитектуру всего MVP.

Trade-off:

- больше первоначальной дисциплины и документов;
- slower start по сравнению с ad-hoc скриптом;
- но заметно ниже риск архитектурного расползания.

## Logical Layers

### 1. Source Ingestion Layer

Responsibilities:

- detect source type;
- validate source;
- route to correct parser (**tab adapters** + bridge formats);
- capture source metadata;
- emit parsed representation and ingestion warnings.

Boundary:

- не владеет REAPER-specific logic;
- не обещает correctness beyond source fidelity.

### 2. Score Normalization Layer

Responsibilities:

- convert parsed source into canonical score model;
- preserve musically relevant structure;
- record missing data and uncertainty explicitly.

Boundary:

- не зависит жёстко ни от source format, ни от target DAW.

### 3. Arrangement Mapping Layer

Responsibilities:

- assign track roles (with **drums → bass → guitar** proving order in mind for MVP depth);
- define track naming;
- prepare REAPER-oriented project structure;
- produce mapping plan from canonical model to target layout.

Boundary:

- подготавливает arrangement structure, но не притворяется финальной музыкальной интерпретацией.

### 4. REAPER Integration Layer

Responsibilities:

- create editable **MIDI-oriented** scaffold;
- create tracks and importable units;
- place markers and regions where supported;
- preserve traceability back to source and canonical fragments.

Boundary:

- consumes canonical and mapped data;
- не владеет upstream business rules.

### 5. Review Assistance Layer

Responsibilities:

- expose warnings;
- surface unresolved fragments;
- create review-oriented outputs;
- point the user to manual checking areas.

Boundary:

- обязателен для trustworthiness;
- не заменяет manual refinement.

### 6. Screenshot / Vision Layer

Responsibilities:

- process screenshot-based tab inputs;
- extract semi-structured information;
- emit confidence-aware outputs with heavy warning support.

Boundary:

- isolated from structured-core path;
- не определяет архитектуру MVP в целом.

## Module Boundaries in `src/`

- `src/domain/`: canonical entities and invariants
- `src/ingest/`: source adapters and validators
- `src/normalize/`: canonical transformation rules
- `src/mapping/`: track and arrangement planning
- `src/reaper/`: scaffold generation for REAPER
- `src/review/`: warnings, unresolved markers, review reports
- `src/vision/`: screenshot-only pipeline

## Boundary Rules

- `ingest` may know source formats but not REAPER behavior;
- `normalize` may know domain semantics but not transport formats;
- `mapping` may know target layout but not target export internals;
- `reaper` may know artifact generation but not source parsing;
- `vision` must depend inward, not force changes outward.

## Связанные документы

- [STRUCTURE.md](STRUCTURE.md) — физическая структура репозитория и соответствие каталогов `src/` слоям выше.
- [DEVELOPMENT.md](DEVELOPMENT.md) — дисциплина разработки и границы модулей под `src/`.
