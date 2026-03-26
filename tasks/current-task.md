# Current Task

## Goal

Закрепить **drums-first** инкремент поверх стабильного slice 1: **MusicXML (bridge)** → canonical (в т.ч. unpitched/GM) → arrangement → REAPER-oriented JSON scaffold → review — без расширения MVP и без смены продуктовой рамки.

## Current implementation reality

- Вертикаль `run_slice1_musicxml` в `src/slice1_pipeline.py`: ingest → `musicxml_to_canonical` → `map_canonical_to_arrangement` → `arrangement_to_scaffold_bundle` → `build_review_report`.
- **Реализовано:** partwise MusicXML, один `score-part` / одна `part`, первый `measure`, `pitch` + `rest`, divisions/time, трек с `track_role`/`instrument_type` (ранее только `unknown`).
- **Drums-first (этот инкремент):** парсинг `<unpitched>` (`display-step` / `display-octave`), детерминированная мини-таблица **F4→36 (kick), C5→38 (snare)**; неизвестные позиции → **warning**, событие не создаётся; трек с `part-name`/unpitched → `track_role`/`instrument_type` = `drums`; provenance `kind: drum_hit`, `gm_midi`.
- Scaffold: для `role_hint == drums` — отдельные `import_notes` (GM, channel 10) и hint в arrangement notes.

## Selected drums-first increment (confirmed scope)

| Элемент | Содержание |
|--------|------------|
| Фикстура | `fixtures/structured/musicxml/minimal_drums.xml` — один такт 4/4, две четверти unpitched kick + snare |
| События | Два `note` с `midi_pitch` 36 и 38, `start_position` 0.0 и 1.0 (в кварталях от divisions=1) |
| Timing | Один measure, последовательные длительности без полифонии/сложных голосов |
| Warnings | Неподдерживаемая пара step/octave → строка в `normalize` warnings, hit не попадает в canonical |
| Scaffold | `role_hint: drums`, hints с mapping note + import_notes про GM drums |

## Expected value of this increment

- Доказывает, что pipeline переносит **осмысленную ударную структуру** (GM note numbers + позиции) в canonical и в **редактируемый** REAPER-oriented bundle (импорт MIDI / ручная расстановка по canonical).
- Сохраняет MusicXML как **bridge**, tab-first narrative — через реалистичный unpitched percussion path.

## Confirmed Facts

- Тесты: `tests/unit/test_slice1_contracts.py` — существующий golden для `minimal_chord.xml` + новый focused test для `minimal_drums.xml`.
- Ожидаемые JSON: `fixtures/expected/slice1_minimal_drums_*.json`.
- Python 3.11+, `pyproject.toml` задаёт `pythonpath = ["src"]` для pytest.

## Assumptions

- Для MVP-доказательства достаточно двух фиксированных позиций нотации; расширение таблицы — отдельные инкременты.
- Пользователь сопоставляет canonical `midi_pitch` с GM drum map в REAPER вручную при необходимости.

## Risks

- Разные экспортёры (MuseScore vs др.) могут давать другие `display-step`/`display-octave` для тех же звуков → потребуются новые пары в таблице + regression fixtures (**Open Question**).

- Дублирование `_infer_track_role` логики при появлении bass/guitar — позже вынести в общий helper (**Deferred**).

## Deferred / Out of Scope

- Bass/guitar приоритеты после расширения drums coverage.
- Полифония/несколько voices, chord на ударных, полный GM map.
- Экспорт нативного `.mid` / `.rpp`, ReaScript.
- Audio, vocal, screenshot implementation, plugin automation.

## Open Questions

- Нужен ли отдельный explicit `drum` event type в domain vs текущий `note` + provenance (**Deferred** до обсуждения модели).
- Когда добавлять второй адаптер (MIDI/Guitar Pro) относительно расширения drum map.

## Next Decision

Выбрать следующий малый шаг: **(A)** расширить `_UNPITCHED_GM_DRUM` + фикстуру (hi-hat, tom) с теми же правилами warnings; **или** **(B)** вынести drum mapping в отдельный модуль `normalize/musicxml_drums.py` при первом признаке раздувания `musicxml.py`.
