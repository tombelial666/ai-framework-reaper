# Internal Data Model

## Model Purpose

Canonical score model обязателен, чтобы:

- изолировать downstream logic от source specifics;
- не привязывать core к REAPER representation;
- одинаково обрабатывать structured и screenshot-assisted paths.

Детали транспорта (структура файлов Guitar Pro, MIDI bytes, элементы MusicXML, внутренности проекта REAPER) **не** входят в canonical model: они остаются на границах ingestion и export/adapters.

## Product vs bridge formats (canonical stays agnostic)

**Confirmed:** canonical model не различает «продуктовый Guitar Pro» и «технический MusicXML» на уровне полей — различие только в ingestion/adapters и документации. Продукт позиционируется как **tab-first**; MusicXML — типичный **bridge** к canonical representation.

**Порядок реализации downstream (mapping/review):** для MVP ориентир — **drums → bass → guitar** как приоритет глубины и проверяемости, без изменения обязательности полей модели для конкретного инструмента.

## Model Levels

### Project-Level Fields

#### Required for MVP

- `project_id`
- `project_title`
- `source_references`
- `source_metadata`
- `processing_metadata`
- `provenance`

#### Optional in MVP

- `composer`
- `arrangement_notes`
- `global_comments`

#### Deferred

- advanced editorial metadata
- collaborative annotations

### Track-Level Fields

#### Required for MVP

- `track_id`
- `track_name`
- `track_role`
- `instrument_type`

#### Optional in MVP

- `tuning`
- `capo`
- `channel_or_voice_group`
- `track_comments`

#### Deferred

- advanced performance metadata

### Timing and Form Fields

#### Required for MVP

- `tempo_map`
- `time_signatures`
- `sections`
- `measures`

#### Optional in MVP

- `beats`
- `subdivisions`

#### Deferred

- expressive tempo nuance beyond source certainty

### Event-Level Fields

#### Required for MVP

- `event_id`
- `track_id`
- `measure_ref`
- `start_position`
- `duration`
- `event_type`

For note events:

- `pitch` or `midi_pitch`

#### Optional in MVP

- `string`
- `fret`
- `rest_flag`
- `articulations`
- `techniques`
- `event_comments`
- `confidence`
- `unresolved_flags`

#### Deferred

- advanced ornament semantics not consistently available across sources

## Mandatory Fields for Structured Ingestion Success

Минимум для успешного structured ingestion:

- source must yield at least one track or logical voice;
- timing context must be reconstructable at measure level;
- note/rest events must have position and duration;
- provenance must link back to source fragment or source section.

## Warning vs Hard Failure

### Hard Failure

- source cannot be parsed deterministically;
- timing structure is unrecoverable;
- event placement cannot be established at usable scaffold level.

### Warning

- missing tuning;
- missing capo;
- partial techniques or articulations;
- uncertain track role;
- incomplete section naming;
- low-confidence screenshot extraction.

## Provenance Rule

Каждый нормализованный track, section или event по возможности должен содержать reference back to source segment, чтобы review layer могла показать происхождение спорного результата.
