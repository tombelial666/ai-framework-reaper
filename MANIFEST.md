# MANIFEST

Этот файл является главным проектным манифестом. Если новая реализация, документ или архитектурное решение ему противоречат, сначала нужно обновить манифест и связанные docs, а уже потом менять код.

## 1. Project Identity

- Project name: `REAPER AI Scaffold Framework`
- Repository role: долгоживущий framework repository
- Product truth: **tab-first ingestion framework** для подготовки **REAPER-oriented MIDI scaffolds** (редактируемых черновиков структуры) и **поддержки творческих идей** на базе структурированных табов и нотации — не «универсальный импорт нотации вообще» и не проект про MusicXML как продукт.
- Target domain: deterministic AI-assisted preparation of editable **MIDI-oriented** music project scaffolds for `REAPER`, с обязательным human review
- Current phase: `Phase 1 - MVP Structured Import` (kickoff: **slice 1** — технический вертикальный путь через **MusicXML как bridge-формат**, см. `docs/phase1-first-slice.md` и ADR-006; продуктовая идентичность при этом остаётся **tab-first**)

## 2. Purpose

Назначение проекта:

- принимать **таб- и нотационно-ориентированные** structured или semi-structured источники (Guitar Pro ecosystem, экспорты Songsterr где это юридически и технически допустимо, MIDI, другие совместимые форматы);
- преобразовывать источник в canonical internal score model;
- строить arrangement and track plan;
- выпускать **editable REAPER-oriented MIDI scaffold** (draft): импортируемые/переносимые формы, структура треков, предупреждения;
- сопровождать результат warnings, unresolved markers и review-oriented output.

**Human-in-the-loop**: ручная проверка и доработка обязательны; pipeline не заменяет review и не обещает «готовую песню».

Проект не предназначен для создания финального polished arrangement без участия человека.

### Product modes (обе в рамках MVP-философии)

- **Mode A — Tab-based import / cover workflow (основной):** у пользователя уже есть качественный таб/нотация; цель — импорт → parse → canonical → MIDI-oriented scaffold в REAPER → ручная доработка.
- **Mode B — Creative assistance / style-guided scaffold:** помощь в виде **структурированных стартовых точек**, набросков грува/секции, идей аранжировки («в духе X», «намёк на Y») — **не** магическая генерация финального трека, **не** инструмент плагиата и **не** гарантия готовой композиции; выход остаётся черновиком для редактирования.

## 3. MVP Boundaries

### In Scope

- **Продуктовые источники (приоритет):** Guitar Pro related structured sources; **Songsterr-exported / derived structured sources** где это юридически и технически доступно; `MIDI`; другие совместимые structured tab/notation; вручную подготовленные text/tab-like structures
- **Технические мосты:** `MusicXML` и нормализованные промежуточные формы как **adapter/bridge**, не как суть продукта
- controlled screenshot/tab image ingestion as secondary path
- canonical normalized score data
- track planning and arrangement structure
- editable REAPER-ready **MIDI-oriented** scaffold (bundles, планы импорта, будущие пути `.rpp`/ReaScript — по roadmap)
- warnings and unresolved markers
- review-oriented output for manual correction

### Implementation proving order (инструменты)

Для первой практической ценности pipeline и валидации:

1. **Drums first** — более детерминированное событийное отображение, проще review, сильный ранний сигнал для scaffold
2. **Bass second** — часто проще полной гитарной выразительности
3. **Guitar third** — центральный продукт долгосрочно, но не обязательно первый по глубине реализации

Это порядок **реализации и proof-of-value**, не демоция гитары как источника.

### Out of Scope

- audio transcription
- audio-first workflows
- audio-first ingestion
- raw audio parsing
- note extraction from raw audio
- audio-assisted verification
- vocal workflow
- **lyric workflows** (тексты песен как отдельный продуктовый трек)
- claims of full automatic accuracy
- advanced autonomous arrangement intelligence
- **promise of final polished production-ready projects**
- "press button -> final arrangement" behavior
- представление manual review как опционального

### Deferred

- richer technique mapping beyond verified source fidelity
- broader multi-instrument sophistication
- improved screenshot extraction quality
- better review UX inside or around REAPER

## 4. Non-Negotiable Principles

- `Repository-first`: repo documents are part of the product.
- `REAPER-first output`: target artifact is an editable **MIDI-oriented** REAPER scaffold.
- `Tab-first product identity`: пользовательский смысл — табы и нотационные ресурсы → scaffold; interchange-форматы — технические мосты.
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

- structured ingestion (tab-source adapters)
- normalization into canonical model
- mapping plan
- REAPER-ready editable **MIDI-oriented** scaffold
- minimal review report
- **Slice 1 (реализуется первой):** один вертикальный путь `MusicXML (bridge) → canonical → arrangement → REAPER-oriented scaffold bundle (JSON) → review` — см. `docs/phase1-first-slice.md`, `docs/adr/ADR-006-phase1-first-implementation-slice.md`. Продуктовая подача остаётся tab-first; MusicXML — удобный детерминированный bridge для первого кода.

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

- Phase 0 foundation (manifest, core `docs/`, ADR pack, Cursor rules/commands, skills, structured tasks, repository layout) is in place.
- REAPER is the target DAW and the intended environment for editing the scaffold output.
- MVP is deterministic, **tab-first**, structured-first and human-reviewed.
- Screenshot ingestion is secondary.
- **Drums → bass → guitar** is the preferred implementation proving order after slice 1 stabilizes (Open Question: exact milestone per instrument).

### Assumption

- A reliable deterministic path can be built for at least one Guitar Pro related structured format.
- Songsterr-related structured inputs remain subject to licensing and ToS of the user’s export path (**Risk** if violated).

### Risk

- Source fidelity may vary across Guitar Pro conversion/export paths.

### Open Question

- Which concrete import/export mechanism will be the primary REAPER integration path in the first implementation cut (`.rpp`, ReaScript, MIDI files + manifest, etc.).
