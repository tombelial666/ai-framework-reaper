# Scope

MVP предполагает **human-in-the-loop**: выход — **черновик (draft)**: редактируемые scaffolds и review-oriented артефакты; финальная аранжировка не является целью pipeline. Ручная проверка и доработка обязательны. **REAPER** — целевая среда, в которой пользователь доводит этот черновик (см. `MANIFEST.md`).

## In Scope for MVP

- Guitar Pro related structured sources
- `MIDI`
- `MusicXML`
- manually prepared text/tab-like structures
- screenshot/tab image ingestion as a controlled secondary path
- source validation and metadata capture
- canonical normalized score data
- arrangement and track planning
- REAPER-ready editable scaffold
- warnings, unresolved markers and review-oriented outputs

## Out of Scope for MVP

- audio transcription
- audio-first workflows
- audio-first ingestion
- raw audio parsing
- raw audio note extraction
- audio-assisted verification
- vocal workflow
- claims of full automatic accuracy
- advanced autonomous arrangement intelligence
- final polished arrangement generation (automation of a finished arrangement)

## Deferred Beyond MVP

- richer technique interpretation where source fidelity is inconsistent
- broader support for multi-instrument edge cases
- advanced review UX around generated scaffold
- more capable screenshot extraction

## Scope Boundary Rule

Если новое предложение:

- требует raw audio как primary source;
- скрывает uncertainty;
- ломает deterministic reviewability;
- или превращает scaffold generation в black-box automation,

то оно не должно входить в MVP без явного обновления `MANIFEST.md` и связанных docs.
