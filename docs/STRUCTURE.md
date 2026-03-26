# Структура репозитория

Этот документ фиксирует физическую структуру репозитория и границы каталогов. Он нужен, чтобы реализация не превратилась в набор случайных скриптов.

## Целевое дерево

```text
ai-framework-reaper/
├── .cursor/
│   ├── commands/
│   └── rules/
├── docs/
│   └── adr/
├── examples/
│   ├── input/
│   └── output/
├── fixtures/
│   ├── screenshot/
│   └── structured/
├── skills/
│   ├── docs-maintenance/
│   ├── music-ingestion/
│   └── reaper-scaffold/
├── src/
│   ├── domain/
│   ├── ingest/
│   ├── mapping/
│   ├── normalize/
│   ├── reaper/
│   ├── review/
│   └── vision/
├── tasks/
├── templates/
│   └── reaper/
├── tests/
│   ├── e2e/
│   ├── golden/
│   ├── integration/
│   └── unit/
├── MANIFEST.md
└── README.md
```

Пока в каталогах нет исходных файлов, структура может фиксироваться файлами `.gitkeep`, чтобы дерево в клоне репозитория совпадало с этим документом.

## Правила по областям

### `docs/`

Что относится:

- scope, requirements, architecture, risks, open questions, roadmap;
- integration notes;
- internal data model;
- ADR.

Почему существует:

- это основной слой project truth;
- решения по scope и architecture должны жить здесь, а не только в чате.

Что не класть:

- рабочий код;
- ad-hoc заметки без структуры;
- экспериментальные scratch files.

### `.cursor/rules/`

Что относится:

- постоянные правила для поведения агента;
- scope guardrails;
- decision integrity rules;
- docs-first требования.

Канонический набор (направление проекта и границы MVP): `00-project-direction.mdc`, `01-mvp-boundaries.mdc`, `02-decision-integrity.mdc`, `03-docs-first.mdc`. Дублирующие или устаревшие имена правил не должны жить параллельно этому набору без явного решения в `MANIFEST.md` / ADR.

Почему существует:

- чтобы агент стабильно читал проект одинаково и не расширял scope молча.

Что не класть:

- длинные design documents;
- команды;
- task-specific инструкции.

### `.cursor/commands/`

Что относится:

- повторяемые workflow prompts для старта задач, ingestion, scaffold generation и doc updates.

Почему существует:

- чтобы повторяющиеся процессы запускались одинаково.

Что не класть:

- постоянные правила;
- архитектурную правду вместо `docs/`.

### `skills/`

Что относится:

- специализированные workflow guides для анализа ingestion, planning REAPER scaffold и поддержания docs.

Почему существует:

- это отдельный слой domain-specific operational memory.

Что не класть:

- source code модулей;
- одноразовые task notes.

### `src/domain/`

Что относится:

- core entities, value objects, enums, invariants;
- canonical score model contracts;
- domain errors and shared boundaries.

Почему существует:

- доменная модель должна быть независима от source formats и REAPER integration details.

Что не класть:

- format parsers;
- REAPER-specific scripting;
- OCR / vision logic.

### `src/ingest/`

Что относится:

- source type detection;
- parsers and adapters for structured inputs;
- validation and metadata capture.

Почему существует:

- ingestion — отдельная ответственность до normalization.

Что не класть:

- canonical mapping policy;
- REAPER placement logic.

### `src/normalize/`

Что относится:

- преобразование parsed source в canonical score model;
- explicit missing-data and uncertainty capture.

Почему существует:

- normalization отделяет source-specific parsing от downstream logic.

Что не класть:

- raw parsing;
- final REAPER-specific structure generation.

### `src/mapping/`

Что относится:

- track roles;
- arrangement plan;
- naming conventions;
- REAPER-oriented layout preparation.

Почему существует:

- mapping связывает domain data и target project structure без смешивания с transport layer.

Что не класть:

- low-level REAPER export mechanics;
- OCR extraction.

### `src/reaper/`

Что относится:

- REAPER integration strategy implementations;
- scaffold artifact generation;
- marker and region emission;
- traceability hooks.

Почему существует:

- REAPER is the target DAW, но эта логика не должна расползаться по остальным слоям.

Что не класть:

- business rules ingestion;
- canonical model ownership.

### `src/review/`

Что относится:

- warnings;
- unresolved markers;
- review reports;
- manual-check guidance.

Почему существует:

- human review является обязательной частью trust model.

Что не класть:

- source parsing;
- DAW-specific export internals.

### `src/vision/`

Что относится:

- screenshot/tab image preprocessing;
- segmentation;
- extraction orchestration;
- confidence-aware outputs for secondary path.

Почему существует:

- screenshot path нужен, но должен оставаться изолированным.

Что не класть:

- core structured path logic;
- decisions that redefine MVP architecture.

### `templates/reaper/`

Что относится:

- reusable REAPER-oriented text templates, config skeletons, marker naming schemes.

Почему существует:

- шаблоны должны быть отделены от кода и легко ревьюиться.

Что не класть:

- generated user outputs;
- domain logic.

### `examples/input/` и `examples/output/`

Что относится:

- демонстрационные входы;
- expected scaffold examples;
- review examples.

Почему существует:

- примеры помогают объяснять поведение и ожидания без чтения кода.

Что не класть:

- regression-only fixtures;
- production secrets.

### `fixtures/structured/` и `fixtures/screenshot/`

Что относится:

- тестовые источники для regression validation;
- controlled inputs для ingestion and screenshot paths.

Почему существует:

- deterministic behavior требует стабильных fixtures.

Что не класть:

- одноразовые примеры для README;
- output artifacts без привязки к тестам.

### `tests/unit/`

Что относится:

- tests для isolated domain logic, normalization rules и mappers.

Что не класть:

- full pipeline scenarios.

### `tests/integration/`

Что относится:

- tests между слоями ingestion -> normalization -> mapping;
- REAPER export integration checks.

Что не класть:

- tiny pure-function tests;
- full dry-run workflows.

### `tests/golden/`

Что относится:

- expected canonical outputs;
- stable REAPER scaffold artifacts;
- regression baselines.

Почему существует:

- golden comparisons дают детерминированный контроль без субъективной оценки.

### `tests/e2e/`

Что относится:

- dry-run workflows от source input до scaffold and review output.

Что не класть:

- tests, зависящие от vague human interpretation.

### `tasks/`

Что относится:

- active structured tasks;
- decision-oriented work items;
- decomposition notes in approved format.

Канонический шаблон задачи — один файл: `tasks/_template.md` (дублирующие шаблоны в других каталогах не ведутся).

Почему существует:

- существенные задачи не должны существовать только в chat context.

Что не класть:

- permanent architecture docs;
- implementation source files.

## Technical Scaffolding Plan for `src/`

На phase 0 структура модулей создаётся без глубокой реализации. Следующий безопасный шаг:

1. определить contracts и typed payloads в `src/domain/`;
2. задать adapter interfaces в `src/ingest/`;
3. зафиксировать normalization boundary в `src/normalize/`;
4. описать mapping plan DTO в `src/mapping/`;
5. задать scaffold output contracts в `src/reaper/`;
6. определить warning/report model в `src/review/`;
7. держать `src/vision/` изолированным от structured-core path.
