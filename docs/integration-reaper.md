# REAPER Integration

## Target Behavior

Система должна производить **editable MIDI-oriented scaffold**, а не финальный polished project. Выход — черновик структуры: треки, план импорта, маркеры review; пользователь доводит звук и аранжировку в REAPER.

## Recommended Separation

### Preprocessing Outside REAPER

- source ingestion
- canonical normalization
- track planning
- warning generation
- traceability metadata preparation

### REAPER-Oriented Logic

- track creation strategy
- project organization strategy
- marker and region emission
- **MIDI-oriented** items or importable units (files, bundles, future `.rpp`/script emission)
- scaffold artifact generation

### Generic Logic That Must Stay REAPER-Independent

- core domain model
- source parsing
- normalization rules
- uncertainty handling policy

## Track Creation Strategy

Рекомендация:

- создавать tracks from mapping plan, not directly from raw source structure;
- придерживаться stable naming rules;
- группировать tracks по role where useful for editing;
- для MVP-глубины: **drums → bass → guitar** как порядок приоритета реализации и проверки (не как ограничение canonical model).

Trade-off:

- требует extra mapping layer;
- зато предотвращает смешивание source quirks и REAPER layout.

## Marker and Region Strategy

- sections should map to regions where available;
- warnings and unresolved fragments should map to visible review markers where feasible;
- marker naming must support quick manual navigation.

## Importable Artifact Strategy

На phase 0 точный artifact format не фиксируется окончательно.

Confirmed:

- output must be editable in REAPER;
- output must be **MIDI-scaffold-oriented** (importable MIDI, structured bundles, or generated project stubs as chosen);
- output must preserve traceability;
- output must not hide uncertainty.

Open Question:

- What first artifact strategy gives the best deterministic-first balance: script-driven project creation, intermediate importable MIDI + manifest, JSON bundle only, or hybrid.

## Manual Refinement Entry

REAPER integration должна помогать пользователю быстро начать ручную доработку через:

- ясные track names;
- predictable track ordering (aligned with drums/bass/guitar emphasis where applicable);
- visible unresolved markers;
- source-linked review hints.
