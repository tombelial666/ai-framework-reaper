# Non-Functional Requirements

## Determinism

- Для одинакового validated input pipeline должен стремиться выдавать одинаковый результат.
- Ambiguity должна приводить к warnings, а не к скрытой вариативности.

## Explainability

- Каждый слой должен иметь понятную boundary.
- Output decisions должны быть traceable назад к source или mapping policy.

## Reviewability

- Пользователь должен быстро видеть unresolved or low-confidence fragments.
- Generated result не должен маскироваться под final truth.

## Modularity

- Core model не должен зависеть от конкретного source format или REAPER-specific representation.
- Screenshot path должен быть изолирован от structured-core path.

## Testability

- Deterministic core behavior должен проверяться unit, integration, golden и e2e tests.
- Regression fixtures должны быть стабильными и версионируемыми.

## Maintainability

- Архитектурные решения фиксируются в `docs/` и `docs/adr/`.
- Существенные задачи ведутся через structured task files.
