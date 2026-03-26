# MANIFEST

Этот файл является главным проектным манифестом. Если новая реализация, документ или архитектурное решение ему противоречат, сначала нужно обновить манифест и связанные docs, а уже потом менять код.

## 1. Project Identity

- Project name: `REAPER AI Scaffold Framework`
- Repository role: долгоживущий framework repository
- Target domain: deterministic AI-assisted preparation of editable music project scaffolds for `REAPER`
- Current phase: `Phase 0 - Discovery / Analyst Pack`

## 2. Purpose

Назначение проекта:

- принимать structured или semi-structured musical source;
- преобразовывать источник в canonical internal score model;
- строить arrangement and track plan;
- выпускать editable REAPER-oriented scaffold;
- сопровождать результат warnings, unresolved markers и review-oriented output.

**Human-in-the-loop**: ручная проверка и доработка обязательны; pipeline не заменяет review.

Проект не предназначен для создания финального идеального arrangement без участия человека.

## 3. MVP Boundaries

### In Scope

- Guitar Pro related structured sources
- `MIDI`
- `MusicXML`
- manually prepared text/tab-like structures
- controlled screenshot/tab image ingestion as secondary path
- canonical normalized score data
- track planning
- editable REAPER-ready scaffold
- warnings and unresolved markers
- review-oriented output for manual correction

### Out of Scope

- audio transcription
- audio-first workflows
- audio-first ingestion
- raw audio parsing
- note extraction from raw audio
- audio-assisted verification
- vocal workflow
- claims of full automatic accuracy
- advanced autonomous arrangement intelligence
- "press button -> final arrangement" behavior

### Deferred

- richer technique mapping beyond verified source fidelity
- broader multi-instrument sophistication
- improved screenshot extraction quality
- better review UX inside or around REAPER

## 4. Non-Negotiable Principles

- `Repository-first`: repo documents are part of the product.
- `REAPER-first output`: target artifact is an editable REAPER scaffold.
- `Deterministic MVP`: prefer explicit rules and fallbacks over vague model assumptions.
- `Human-in-the-loop`: manual review is mandatory.
- `Canonical model is mandatory`: the internal score model must be DAW-agnostic and source-agnostic.
- `Screenshot path is secondary and isolated`: vision path must not dictate the core architecture.

## 5. Decision Integrity Rules

Во всех существенных docs и tasks нужно явно разделять:

- `Confirmed`
- `Assumption`
- `Risk`
- `Deferred`
- `Open Question`

Нельзя:

- придумывать неподтверждённые capabilities;
- выдавать рискованные идеи за утверждённый design;
- смешивать MVP scope и future scope;
- обещать full automation там, где обязателен manual review.

## 6. Required Architecture

Обязательные logical layers:

1. `Source Ingestion`
2. `Score Normalization`
3. `Arrangement Mapping`
4. `REAPER Integration`
5. `Review Assistance`
6. `Screenshot / Vision`

Layer boundaries описаны в `docs/architecture.md`.

## 7. Canonical Model Requirement

Внутренняя score model должна быть независима от:

- Guitar Pro specifics
- MIDI format specifics
- MusicXML specifics
- REAPER representation specifics

Минимальный состав полей и обязательность описаны в `docs/internal-data-model.md`.

## 8. Implementation Phases

### Phase 0 - Discovery / Analyst Pack

- repository foundation
- manifesto
- scope and architecture docs
- ADR pack
- Cursor memory layers
- structured task system
- technical scaffolding plan

### Phase 1 - MVP Structured Import

- structured ingestion
- normalization into canonical model
- mapping plan
- REAPER-ready editable scaffold
- minimal review report

### Phase 2 - Better Editing Workflow

- better templates
- clearer markers and regions
- stronger source-to-result traceability
- better review helpers

### Phase 3 - Screenshot-Assisted Import

- controlled secondary screenshot pipeline
- confidence-aware extraction
- explicit manual correction flow

### Phase 4 - Advanced Non-Audio Extensions

- richer heuristics
- broader structured support
- improved normalization fidelity
- stronger review UX

## 9. Alignment Requirements

При изменении architecture, scope, boundaries или implementation direction:

- update `MANIFEST.md`;
- update affected docs in `docs/`;
- update relevant ADR if decision-level change occurred;
- update `.cursor/rules/` if permanent agent behavior must change;
- do not leave architectural truth only in chat;
- не поддерживайте параллельный второй набор правил в `.cursor/rules/` без явного решения: канонический набор — `00-project-direction.mdc` … `03-docs-first.mdc` (см. `docs/STRUCTURE.md`).

## 10. Current Status

### Confirmed

- REAPER is the target DAW.
- MVP is deterministic, structured-first and human-reviewed.
- Screenshot ingestion is secondary.

### Assumption

- A reliable deterministic path can be built for at least one Guitar Pro related structured format.

### Risk

- Source fidelity may vary across Guitar Pro conversion/export paths.

### Open Question

- Which concrete import/export mechanism will be the primary REAPER integration path in the first implementation cut.
