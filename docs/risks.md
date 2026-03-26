# Risks

## Risk Register

| ID | Risk | Impact | Likelihood | Mitigation |
|----|------|--------|------------|------------|
| R-001 | Guitar Pro related sources lose fidelity in conversion | High | Medium | keep direct-path evaluation separate from fallback conversion paths |
| R-002 | Canonical model becomes too tied to one source format | High | Medium | enforce `domain -> normalize -> mapping` separation |
| R-003 | REAPER integration leaks target-specific rules into upstream layers | High | Medium | keep REAPER logic inside `src/reaper/` |
| R-004 | Screenshot path expands scope and destabilizes MVP | High | Medium | isolate `src/vision/` and keep warning-heavy policy |
| R-005 | Generated draft appears more trustworthy than it is | High | Medium | mandatory review output and unresolved markers |
| R-006 | Validation becomes subjective instead of deterministic | Medium | Medium | golden files, dry-run tests and explicit warning policy |
| R-007 | Repository truth drifts from implementation | High | Medium | docs-first updates and manifest alignment rules |

## Current Highest-Priority Risks

- `R-001`
- `R-003`
- `R-004`
- `R-007`

## Monitoring Rule

Если риск начинает менять scope, architecture или module boundary, update required docs and ADR immediately.
