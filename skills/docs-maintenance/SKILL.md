---
name: docs-maintenance
description: Maintain architectural and scope documentation for the REAPER scaffold framework. Use when changes affect MANIFEST alignment, scope boundaries, architecture documents, ADRs, risk registers, open questions, or task records.
---

# Docs Maintenance

## Use This Skill For

- manifesto alignment;
- architecture doc updates;
- ADR maintenance;
- risk and open-question tracking.

## Default Workflow

1. Identify which decision changed.
2. Update `MANIFEST.md` if project direction, principles or scope changed.
3. Update affected docs in `docs/`.
4. Update ADR if the change is decision-level.
5. Check that `Confirmed`, `Assumption`, `Risk`, `Deferred` and `Open Question` remain explicit.

## Boundary Rules

- Do not leave repository truth only in chat.
- Do not silently convert assumptions into facts.
- Keep MVP and future scope clearly separated.
