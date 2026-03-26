# REAPER AI Scaffold Framework

Этот репозиторий является **source-of-truth framework repository** для детерминированного AI-assisted workflow, который подготавливает **редактируемые scaffolds для REAPER**.

Проект не пытается автоматически создавать финальную аранжировку. Его задача: взять структурированный или полу-структурированный музыкальный источник, нормализовать его во внутреннюю модель, подготовить план треков и выдать **редактируемый REAPER-ready черновик (draft)** с предупреждениями и маркерами для обязательной ручной доработки в **REAPER**.

## Какую задачу решает репозиторий

Система должна помогать пользователю:

- быстрее получать стартовый черновик вместо ручного ввода каждой ноты;
- копировать и переиспользовать партии из существующих источников;
- готовить cover-oriented и arrangement-oriented scaffolds;
- переносить черновик в REAPER;
- видеть спорные места и вручную уточнять результат.

Ценность проекта:

- быстрый старт;
- меньше ручной рутины;
- предсказуемый и объяснимый pipeline;
- структурированный и редактируемый результат;
- явная поддержка manual review.

## Что является MVP

MVP ограничен **structured-first** и **deterministic-first** подходом.

В MVP входят:

- ingestion для Guitar Pro related structured sources;
- ingestion для `MIDI`;
- ingestion для `MusicXML`;
- ingestion для вручную подготовленных text/tab-like structures;
- вторичный контролируемый path для screenshot/tab image ingestion;
- canonical normalized score data;
- track planning;
- REAPER-ready editable scaffold;
- warnings, unresolved markers и review-oriented output.

## Что не входит в MVP

Явно вне MVP:

- audio transcription;
- audio-first workflows;
- audio-first ingestion;
- raw audio parsing;
- извлечение нот напрямую из raw audio;
- audio-assisted verification;
- vocal workflow;
- обещания полной автоматической точности (claims of full automatic accuracy);
- advanced autonomous arrangement intelligence;
- сценарий вида "one click -> final arrangement".

## Принципы проекта

- `Repository-first`: архитектурная правда должна жить в репозитории, а не только в чате.
- `REAPER-first output`: целевой результат ориентирован на подготовку проекта в REAPER.
- `Deterministic MVP`: поведение должно быть предсказуемым, тестируемым и explainable.
- `Human-in-the-loop`: manual review обязателен.
- `Canonical model first`: внутренняя score model независима от Guitar Pro, MIDI, MusicXML и REAPER.
- `Screenshot path is secondary`: vision path изолирован и не определяет архитектуру MVP.

## Где находится основная правда проекта

- [MANIFEST.md](MANIFEST.md) — проектная идентичность, границы MVP, принципы и фазы.
- [docs/product-vision.md](docs/product-vision.md) — видение и целевой результат.
- [docs/problem-statement.md](docs/problem-statement.md) — точная формулировка решаемой проблемы.
- [docs/scope.md](docs/scope.md) — in scope / out of scope / deferred.
- [docs/architecture.md](docs/architecture.md) — логические слои и module boundaries.
- [docs/internal-data-model.md](docs/internal-data-model.md) — canonical score model.
- [docs/STRUCTURE.md](docs/STRUCTURE.md) — физическая структура репозитория и её правила.
- [docs/phase1-first-slice.md](docs/phase1-first-slice.md) — первый вертикальный срез Phase 1 (MusicXML).

## Организация репозитория

Ключевые области:

- `docs/` — product, scope, architecture, ADR и risk register;
- `.cursor/rules/` — постоянные memory layers для контроля направления и границ;
- `.cursor/commands/` — повторяемые рабочие команды;
- `skills/` — специализированные workflow instructions;
- `src/` — implementation modules по слоям (Phase 1 slice 1: см. `docs/phase1-first-slice.md`);
- `templates/reaper/` — шаблоны REAPER-oriented артефактов;
- `examples/` — примеры входов и ожидаемых результатов;
- `fixtures/` — regression fixtures для structured и screenshot pipelines;
- `tests/` — unit, integration, golden и end-to-end проверки;
- `tasks/` — структурированные рабочие задачи.

Подробности: [docs/STRUCTURE.md](docs/STRUCTURE.md).

## Разработка (Phase 1+)

- Требуется **Python 3.11+**.
- Установка в режиме разработки: `pip install -e ".[dev]"` (из корня репозитория).
- Минимальные тесты среза 1: `pytest tests/unit/test_slice1_contracts.py -v` (`PYTHONPATH` задаётся через `pyproject.toml` для pytest).

## Текущее состояние

**Phase 0** завершена. **Phase 1** в режиме kickoff: зафиксирован **slice 1** — детерминированный путь **MusicXML → canonical → arrangement → JSON scaffold bundle → review** (см. `docs/phase1-first-slice.md`, ADR-006). Реализация Guitar Pro / MIDI / manual tab и экспорт `.rpp` — следующими шагами внутри MVP, без расширения scope на audio/vocal.
