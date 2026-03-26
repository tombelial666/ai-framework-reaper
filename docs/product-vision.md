# Product Vision

## Vision

Создать **tab-first ingestion framework**: детерминированная AI-assisted подготовка **editable MIDI-oriented REAPER scaffolds** из табов, нотации и совместимых structured источников — для cover, reinterpretation и **ускорения музыкальных идей**, с обязательным human review.

## Product Outcome

Пользователь получает не «финальную аранжировку» и не «готовый трек», а:

- переносимую структуру и план треков;
- **MIDI-oriented** черновик для REAPER (bundles, импортируемые формы, дальнейшие пути интеграции);
- warnings и unresolved markers;
- быстрый вход в ручную доработку.

## User Value

- меньше ручного ввода с нуля;
- быстрее старт для **tab-based cover** и arrangement drafting;
- для Mode B — **идейные и ритмические наброски** и структурные подсказки, которые остаются редактируемыми черновиками;
- прозрачные ограничения системы;
- сохранение редактируемости результата.

## Product Positioning

Это **не** generative «сделай песню до мастеринга» и **не** raw-audio transcription engine.

Это deterministic preparation workflow для случаев, когда у пользователя есть или появляется:

- **Guitar Pro related** structured source;
- **Songsterr-exported** structured material (где допустимо);
- `MIDI`;
- другие совместимые tab/notation;
- вручную подготовленный text/tab-like source;
- или, во вторичном path, screenshot/tab image.

**MusicXML** — полезный **технический bridge** между инструментами и canonical model; продукт позиционируется как **tab-first**, не как «фреймворк про MusicXML».

## Modes

- **Mode A (primary):** импорт таба → scaffold в REAPER → ручная доработка.
- **Mode B:** стилистические и структурные **наброски** (идеи секций, грув, каркас партий) — без обещания финальной композиции, без обхода авторских прав и без сценария «одна кнопка — готовый хит».

## Confirmed

- Target DAW: `REAPER`.
- **Human-in-the-loop**: manual review is mandatory.
- Structured-core path is primary; screenshot is secondary.
- **Implementation proving order:** drums → bass → guitar (см. `MANIFEST.md`).

## Deferred

- Полноценная интеллектуальная orchestration как замена музыканту.
- Audio-first workflows.
- Lyric-centric product track.
