# Current Task

## Goal

Довести **Phase 1 slice 1** до устойчивого минимального вертикального пути: MusicXML → canonical → arrangement → REAPER-oriented JSON scaffold → review, с тестами на фикстуру и без расширения MVP.

## Confirmed Facts

- **Slice 1** выбран и зафиксирован: **MusicXML (partwise)** как первый structured input; см. `docs/phase1-first-slice.md`, ADR-006.
- ADR-003 по-прежнему описывает product-приоритет Guitar Pro для MVP; порядок **реализации** (сначала MusicXML) согласован в ADR-006.
- Контракты и скелет модулей в `src/domain`, `ingest`, `normalize`, `mapping`, `reaper`, `review`; склейка — `src/slice1_pipeline.py`.
- Фикстура: `fixtures/structured/musicxml/minimal_chord.xml`; ожидаемые формы: `fixtures/expected/slice1_minimal_*.json`.
- Тесты: `tests/unit/test_slice1_contracts.py`; план: `tests/unit/test_plan_slice1.md`.
- Python 3.11+, `pyproject.toml` с editable install и optional dev (pytest).

## Assumptions

- Для slice 1 достаточно stdlib XML и подмножества MusicXML; расширение парсера не ломает границы слоёв.
- Пользователь дорабатывает черновик в REAPER; JSON bundle не заменяет ручную доработку.

## Risks

- Расширение MusicXML-парсера может раздуть `normalize/musicxml.py` — держать разбиение на функции и при необходимости вынести в подмодули без утечки в `domain`.
- Пути к файлам на Windows vs POSIX — в pipeline используется `repo_root` для стабильного `uri_or_label` в canonical.

## Deferred / Out of Scope

- Audio, vocal, screenshot pipeline (`src/vision/`), transcription.
- Guitar Pro, MIDI, manual tab как **второй** срез после стабилизации slice 1.
- Полноценный генератор `.rpp` / ReaScript в slice 1.
- Полное покрытие MusicXML и golden для всех edge cases.

## Open Questions

- Когда подключать второй формат (Guitar Pro vs MIDI) после slice 1.
- Формат первого «native» REAPER артефакта (`.rpp` vs ReaScript vs только JSON) — после готовности canonical + mapping.

## Next Decision

Выбрать следующий инкремент после зелёных тестов slice 1: **(A)** расширить MusicXML (мультипарт / несколько тактов) **или** **(B)** добавить второй адаптер (например MIDI) по тем же контрактам.
