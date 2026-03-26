# ADR-005: Screenshot to Structure Strategy

## Status

Accepted

## Decision

Support screenshot/tab image ingestion only as a secondary isolated path that produces confidence-aware or warning-heavy outputs for manual review.

## Rationale

- retains helpful fallback behavior;
- avoids letting unreliable extraction reshape the structured-core MVP.

## Trade-Off

- screenshot path will deliver rougher outputs;
- manual correction burden remains higher than for structured sources.
