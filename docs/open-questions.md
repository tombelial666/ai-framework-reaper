# Open Questions

## Architecture and Integration

- Which exact REAPER artifact strategy should be primary in phase 1?
- Which exact Guitar Pro related source path should be first-class in phase 1?
- Should manual text/tab-like ingestion be constrained by a mini-format specification?

## Data Model

- What minimum section metadata is required for a useful scaffold?
- Should confidence be boolean, categorical, or numeric in MVP?
- How granular should provenance be at event level in phase 1?

## Workflow

- What is the preferred user entry point: CLI, scripted workflow, or another controlled interface?
- What should the first review artifact look like for fastest manual correction?

## Validation

- Which fixture set best represents realistic cover-preparation scenarios?
- What counts as "good enough" fidelity for structured import in MVP?

## Decision Rule

Ни один open question не должен silently resolve itself in code. Если вопрос начинает влиять на architecture или implementation direction, update docs and ADR first.
