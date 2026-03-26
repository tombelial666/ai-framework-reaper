# Constraints and Assumptions

Авторитетные границы MVP и фаз: [`MANIFEST.md`](../MANIFEST.md) и [`scope.md`](scope.md). Этот документ — краткая сводка ограничений и рабочих допущений; при расхождении приоритет у `MANIFEST.md`.

## Constraints

### Confirmed

- Target DAW is `REAPER`.
- MVP must stay deterministic, reviewable and structured-first.
- **Human-in-the-loop**: human review is mandatory.
- Screenshot path is secondary and isolated.
- Canonical score model is required.

### Technical Constraints

- Repository is foundation-first; deep implementation should follow documented boundaries.
- Integration strategy must respect source fidelity instead of inventing missing musical information.
- REAPER integration should consume mapped canonical data, not own upstream business logic.

## Assumptions

- At least one Guitar Pro related structured path can supply enough information for useful MVP ingestion.
- `MIDI` and `MusicXML` can serve as structured inputs with known fidelity limitations.
- Manual text/tab-like inputs can be constrained enough to normalize deterministically.

## Risks

- Guitar Pro conversion path may lose techniques or metadata.
- Screenshot extraction quality may vary too much for low-warning output.
- REAPER integration path may require trade-offs between portability and richness of scaffold artifacts.

## Deferred

- Exact first implementation language and build tooling.
- Exact primary REAPER artifact format.

## Open Questions

- Which Guitar Pro related format should be the primary structured path in phase 1.
- Which REAPER import mechanism offers the best deterministic-first trade-off.
