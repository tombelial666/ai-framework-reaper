# Development

Последовательность фаз и целей см. [`mvp-roadmap.md`](mvp-roadmap.md); этот файл описывает дисциплину разработки, а не дублирует roadmap.

## Foundation-First Rule

До глубокой реализации сначала фиксируются:

- scope;
- architecture;
- module boundaries;
- risks and open questions;
- manifest alignment.

## Task Discipline

- Все существенные задачи ведутся в `tasks/`.
- Основной шаблон задачи: [../tasks/_template.md](../tasks/_template.md).
- `tasks/current-task.md` должен отражать активную работу, если задача влияет на architecture, scope или implementation direction.

## Documentation Discipline

- Если меняется архитектура или scope, сначала обновляйте `MANIFEST.md` и нужные документы в `docs/`.
- Следуйте [documentation-standard.md](documentation-standard.md).
- Decision-level changes фиксируйте в `docs/adr/`.

## Implementation Discipline

- Когда код появится, он должен следовать границам `src/domain`, `src/ingest`, `src/normalize`, `src/mapping`, `src/reaper`, `src/review`, `src/vision`.
- Не смешивайте REAPER-specific integration с ingestion и normalization.
- Screenshot path не должен диктовать архитектуру structured-core MVP.

## Validation Discipline

- Deterministic behavior проверяется через unit, integration, golden и e2e layers.
- Ambiguous outcomes должны давать warnings, а не фальшивый success.
