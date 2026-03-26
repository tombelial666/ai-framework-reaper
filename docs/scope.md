# Scope

MVP предполагает **human-in-the-loop**: выход — **черновик (draft)**: редактируемые **MIDI-oriented** scaffolds и review-oriented артефакты; финальная polished продукция не является целью pipeline. Ручная проверка и доработка обязательны. **REAPER** — целевая среда редактирования (см. `MANIFEST.md`).

## Product vs technical sources

**Продуктовая идентичность:** табы и нотационные ресурсы → canonical model → REAPER scaffold.

**Продуктовые источники (in scope):**

- Guitar Pro related structured sources
- Songsterr-exported / derived structured sources (где юридически и технически допустимо)
- `MIDI`
- другие совместимые structured tab/notation
- manually prepared text/tab-like structures

**Технические мосты (in scope как adapters, не как «суть продукта»):**

- `MusicXML` — interchange / bridge
- нормализованные промежуточные представления
- internal canonical model

## In Scope for MVP

- source validation and metadata capture
- canonical normalized score data
- arrangement and track planning
- REAPER-ready editable **MIDI-oriented** scaffold (importable/draft bundles и связанные артефакты)
- warnings, unresolved markers and review-oriented outputs
- screenshot/tab image ingestion as a controlled **secondary** path

## Implementation emphasis (proof order)

Для первой практической ценности: **drums → bass → guitar** (детерминизм, review, ранняя польза). Гитара остаётся ключевым источником долгосрочно.

## Out of Scope for MVP

- audio transcription
- audio-first workflows
- audio-first ingestion
- raw audio parsing
- raw audio note extraction
- audio-assisted verification
- vocal workflow
- lyric workflows
- claims of full automatic accuracy
- advanced autonomous arrangement intelligence
- final polished production-ready project generation as an automated promise
- any implication that manual review is optional

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
- превращает scaffold generation в black-box «final song» automation;
- или нарушает границы Mode B (плагиат, обещание готовой композиции),

то оно не должно входить в MVP без явного обновления `MANIFEST.md` и связанных docs.
