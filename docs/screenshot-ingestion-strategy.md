# Screenshot Ingestion Strategy

## Role in MVP

Screenshot/tab image ingestion — это **контролируемый вторичный path**, который нужен, когда structured source отсутствует, но rough structured draft всё ещё полезен.

Он не должен переопределять архитектуру MVP.

## Where It Is Useful

- есть только screenshot/tab image;
- пользователь готов к явной ручной коррекции;
- rough extraction лучше, чем старт с пустого проекта.

## Where It Is Unreliable

- сложная или нечёткая графика;
- неоднозначная табулатурная нотация;
- неполные изображения;
- случаи, где нужна высокая точность без manual review.

## Expected Pipeline

`image input -> segmentation/structure identification -> symbol extraction/tab interpretation -> canonical normalization -> warnings/confidence output -> manual correction`

## Expected Output

- semi-structured extracted representation;
- canonical model population where feasible;
- confidence-aware flags or warning-heavy output;
- review artifacts for manual correction.

## Boundary Rules

- screenshot path must remain isolated from structured-core path;
- low-confidence extraction must not be silently promoted to confirmed fact;
- ambiguity must surface as warnings or unresolved flags.

## Confirmed

- screenshot path is in MVP only as a secondary controlled path.

## Risk

- extraction quality may vary significantly by image quality and notation style.

## Deferred

- high-automation screenshot intelligence;
- low-warning extraction claims across broad notation styles.
