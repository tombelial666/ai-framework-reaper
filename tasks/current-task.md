# Current Task

## Goal

Довести **Phase 1 slice 1** до устойчивого минимального вертикального пути: **MusicXML (bridge)** → canonical → arrangement → REAPER-oriented **MIDI-oriented** JSON scaffold → review, с тестами на фикстуру и без расширения MVP.

## Product truth (top-level)

- **Продукт:** tab-first ingestion framework для REAPER-oriented **MIDI scaffolds** и поддержки идей (Mode A/B), не «MusicXML-продукт».
- **Первый slice:** MusicXML — **технический bridge** для детерминированного кода и фикстур; продуктовые приоритеты источников — Guitar Pro, Songsterr-export, MIDI, и т.д. (см. `MANIFEST.md`).
- **Следующая практическая ценность после стабилизации slice 1:** выстраивать инкременты в логике **drums → bass → guitar** (mapping, роли, фикстуры, acceptance), не подменяя canonical model.

## Confirmed Facts

- **Slice 1** зафиксирован: **MusicXML (partwise)** как первый structured input **в реализации**; см. `docs/phase1-first-slice.md`, ADR-006.
- ADR-003 задаёт **product-приоритет** Guitar Pro и экосистемы табов; порядок **кода** (сначала MusicXML bridge) согласован в ADR-006.
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

- Audio, vocal, lyric workflow, screenshot pipeline (`src/vision/`), transcription.
- Guitar Pro, MIDI, manual tab как **следующие** срезы после стабилизации slice 1 (по продуктовым приоритетам).
- Полноценный генератор `.rpp` / ReaScript в slice 1.
- Полное покрытие MusicXML и golden для всех edge cases.

## Open Questions

- Когда подключать второй адаптер (**Guitar Pro vs MIDI**) после slice 1 — в пользу tab-first ценности.
- Формат первого «native» REAPER артефакта (`.rpp` vs ReaScript vs MIDI import pack) — после готовности canonical + mapping.
- Какие фикстуры первыми подтверждают **drums → bass → guitar** в mapping (отдельные треки vs обобщённые роли).

## Next Decision

После зелёных тестов slice 1 выбрать инкремент, согласованный с **drums-first** roadmap:

- **(A)** расширить MusicXML bridge (мультипарт / несколько тактов) с явным упором на роли **drums/bass/guitar** в mapping; **или**
- **(B)** добавить второй адаптер (например MIDI или Guitar Pro) по тем же контрактам, с сохранением tab-first позиционирования.
