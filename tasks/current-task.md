# Current Task

## Goal

Начать **Phase 1 — MVP Structured Import**: зафиксировать первый срез реализации (контракты canonical model, интерфейсы ingestion, минимальный путь до редактируемого REAPER scaffold и review output) без глубокой бизнес-логики сверх выбранного среза.

## Confirmed Facts

- Phase 0 foundation complete: `MANIFEST.md`, core `docs/`, ADR pack, Cursor rules/commands, skills, `tasks/_template.md`, каркас `src/` и смежных каталогов согласованы с `docs/STRUCTURE.md`.
- The repository is framework-first, not a one-off script folder.
- REAPER is the target DAW and the environment for editing scaffold output.
- MVP is structured-first, deterministic-first and human-reviewed.
- Screenshot ingestion is a secondary isolated path.
- The canonical internal score model is mandatory.

## Assumptions

- At least one Guitar Pro related source path will be suitable as the preferred structured MVP path.
- The first REAPER integration cut can be defined without finalizing every transport detail in the first commit.

## Risks

- Implementation may skip manifest/docs alignment and reintroduce drift (mitigation: docs-first, `MANIFEST.md` section 9).
- REAPER integration choices may pressure upstream architecture if boundaries are not respected.
- Screenshot path work may expand scope if not kept isolated in `src/vision/`.

## Deferred / Out of Scope

- Full parsers for all formats; audio transcription; audio-first workflows; raw audio parsing; vocal workflow; claims of full automatic accuracy.
- Choosing and implementing every REAPER artifact option before the first vertical slice works end-to-end.

## Open Questions

- Which exact Guitar Pro related format should be phase-1 primary.
- Which REAPER-compatible scaffold mechanism should be first-class for slice 1.
- How strict the manual text/tab-like mini-format should be.

## Next Decision

Choose the first vertical slice for Phase 1: primary structured input path (one format first) plus first REAPER scaffold artifact strategy, then stub contracts in `src/domain/` and adapters accordingly.
