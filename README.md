# REAPER AI Scaffold Framework

Этот репозиторий — **source-of-truth framework** для **tab-first ingestion**: превращение качественных табов и нотационных ресурсов в **редактируемые MIDI-oriented scaffolds для REAPER**, плюс обзорные черновики и маркеры для обязательной ручной доработки.

Проект **не** про транскрипцию аудио, **не** про вокал и **не** про автоматическую «готовую песню». Он про **быстрый старт editable структуры** в REAPER: cover, переосмысление, наброски партий и идей — с человеком в контуре.

## Какую задачу решает репозиторий

**Mode A (основной) — импорт таба / cover:** пользователь уже имеет или находит Guitar Pro / Songsterr-export / MIDI / другой structured tab — импорт → canonical model → план треков → **MIDI-oriented scaffold** → доработка вручную.

**Mode B — творческая помощь:** «намёк на стиль», набросок секции, быстрый каркас ударных/баса/гитары — только как **структурированные стартовые точки и черновики**, не как гарантия финальной композиции и не как инструмент копирования чужих произведений.

Ценность:

- меньше ручного ввода с нуля;
- быстрее вход в arrangement и идеи для cover / reinterpretation;
- предсказуемый pipeline;
- редактируемый результат и явные ограничения системы;
- обязательный manual review.

## Что является MVP

MVP — **tab-first, structured-source-first** workflow для **editable MIDI-oriented REAPER scaffolds**.

**Продуктовые источники (приоритет):**

1. Guitar Pro related structured sources  
2. Songsterr-exported / derived structured sources (где юридически и технически допустимо)  
3. `MIDI`  
4. другие совместимые tab/notation  
5. `MusicXML` — **технический мост/adapter**, не лицо продукта  

Также: вручную подготовленные text/tab-like structures; вторичный контролируемый path для screenshot/tab image.

**Порядок доказательства ценности по инструментам:** drums → bass → guitar (детерминизм, review, ранняя польза для scaffold; гитара остаётся ключевым источником долгосрочно).

## Что не входит в MVP

Явно вне MVP:

- audio transcription;
- audio-first workflows;
- audio-first ingestion;
- raw audio parsing;
- извлечение нот напрямую из raw audio;
- audio-assisted verification;
- vocal workflow;
- lyric workflows;
- обещания полной автоматической точности;
- обещание **финального production-ready** проекта без ручной доработки;
- advanced autonomous arrangement intelligence;
- сценарий вида "one click -> final arrangement";
- представление ручной проверки как необязательной.

## Принципы проекта

- `Repository-first`: архитектурная правда в репозитории.
- `REAPER-first output`: целевой артефакт — редактируемый **MIDI-oriented** scaffold в экосистеме REAPER.
- `Tab-first product`: смысл для пользователя — табы и нотация; MusicXML — мост там, где удобно.
- `Deterministic MVP`: предсказуемое, тестируемое поведение.
- `Human-in-the-loop`: manual review обязателен.
- `Canonical model first`: внутренняя score model независима от формата источника и REAPER.
- `Screenshot path is secondary`: vision path изолирован.

## Где находится основная правда проекта

- [MANIFEST.md](MANIFEST.md) — идентичность, режимы A/B, границы MVP, принципы и фазы.
- [docs/product-vision.md](docs/product-vision.md) — видение и целевой результат.
- [docs/problem-statement.md](docs/problem-statement.md) — формулировка проблемы.
- [docs/scope.md](docs/scope.md) — in scope / out of scope / deferred.
- [docs/architecture.md](docs/architecture.md) — слои и границы модулей.
- [docs/internal-data-model.md](docs/internal-data-model.md) — canonical score model.
- [docs/STRUCTURE.md](docs/STRUCTURE.md) — структура репозитория.
- [docs/phase1-first-slice.md](docs/phase1-first-slice.md) — slice 1: **MusicXML как bridge** для первого кода (не продуктовая идентичность).

## Организация репозитория

Ключевые области:

- `docs/` — product, scope, architecture, ADR;
- `.cursor/rules/` — постоянные правила направления;
- `src/` — модули по слоям (slice 1: см. `docs/phase1-first-slice.md`);
- `templates/reaper/` — шаблоны REAPER-oriented артефактов;
- `fixtures/`, `tests/`, `tasks/` — фикстуры, тесты, задачи.

Подробности: [docs/STRUCTURE.md](docs/STRUCTURE.md).

## Разработка (Phase 1+)

- Требуется **Python 3.11+**.
- Установка в режиме разработки: `pip install -e ".[dev]"` (из корня репозитория).
- Минимальные тесты среза 1: `pytest tests/unit/test_slice1_contracts.py -v` (`PYTHONPATH` через `pyproject.toml`).

## Текущее состояние

**Phase 0** завершена. **Phase 1** в kickoff: **slice 1** — детерминированный путь **MusicXML (bridge) → canonical → arrangement → JSON scaffold bundle → review**; следующие инкременты должны выстраивать ценность в логике **drums → bass → guitar** и tab-first источников, без расширения scope на audio/vocal.
