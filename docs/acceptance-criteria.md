# Acceptance Criteria

## Phase 0 Acceptance

- `README.md` explains purpose, problem, MVP, out-of-scope and repository organization.
- `MANIFEST.md` defines identity, principles, boundaries, phases and alignment rules.
- Core scope, architecture, canonical model, risks and open questions are captured under `docs/`.
- ADR set exists for target architecture, REAPER strategy, Guitar Pro strategy, normalization model and screenshot strategy.
- Cursor memory layers exist as rules, commands and skills.
- Structured task template exists and current task is captured in `tasks/current-task.md`.

## Validation Thinking for the Framework

### Ingestion Validation Tests

- verify source type detection;
- verify parser routing;
- verify validation outcomes for valid and invalid structured inputs.

### Normalization Tests

- verify canonical field population;
- verify warning creation for partial data;
- verify hard failure rules for unusable timing or event placement.

### Mapping Verification Tests

- verify stable track role assignment;
- verify naming policy;
- verify deterministic layout planning.

### REAPER Scaffold Validation Tests

- verify scaffold contains expected editable structure;
- verify markers/regions policy where supported;
- verify source-to-result traceability hooks.

### Golden File Tests

- compare canonical model snapshots;
- compare scaffold artifacts or normalized intermediates.

### Dry-Run End-to-End Tests

- start from representative fixtures and verify non-empty scaffold plus review output.

### Screenshot Path Validation Strategy

- accept warning-heavy outputs;
- verify ambiguity is surfaced rather than hidden;
- avoid treating screenshot extraction as low-risk by default.

### Manual Review Checklist

- unresolved fragments are visible;
- warning summary is readable;
- user can identify where to refine manually.

### Regression Fixtures

- maintain stable structured fixtures and screenshot fixtures for repeatability.
