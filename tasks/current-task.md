# Current Task

## Goal

Establish the repository foundation for a deterministic AI-assisted workflow that prepares editable REAPER scaffolds from structured and semi-structured music sources.

## Confirmed Facts

- The repository is framework-first, not a one-off script folder.
- REAPER is the target DAW.
- MVP is structured-first, deterministic-first and human-reviewed.
- Screenshot ingestion is a secondary isolated path.
- The canonical internal score model is mandatory.

## Assumptions

- At least one Guitar Pro related source path will be suitable as the preferred structured MVP path.
- The first REAPER integration cut can be defined without finalizing every transport detail yet.

## Risks

- Foundation docs may drift if later implementation skips manifest alignment.
- REAPER integration choices may pressure upstream architecture if boundaries are not respected.
- Screenshot ambitions may expand scope if not tightly controlled.

## Deferred / Out of Scope

- Deep code implementation.
- Raw audio workflows.
- Final selection of every parser and REAPER artifact mechanism.

## Open Questions

- Which exact Guitar Pro related format should be phase-1 primary.
- Which REAPER-compatible scaffold mechanism should be first-class.
- How strict the manual text/tab-like mini-format should be.

## Next Decision

Choose the first implementation slice for phase 1: preferred structured input path plus first REAPER scaffold artifact strategy.
