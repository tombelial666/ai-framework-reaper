# Documentation Standard

## Purpose

Документация считается частью продукта. Архитектурная и scope truth не должна жить только в chat context.

## Mandatory Rules

Каждый существенный документ должен, где применимо:

- отделять `Confirmed` от `Assumption`;
- фиксировать `Risk`;
- перечислять `Open Question`;
- отделять `MVP` от `Deferred` или future scope;
- явно описывать architectural boundaries;
- избегать ложной уверенности.

## Writing Standard

- писать ясно и строго;
- не обещать capabilities без подтверждения;
- не смешивать решение, гипотезу и пожелание;
- обозначать recommendation, rationale и trade-off, если есть развилка.

## Update Rule

Если меняется:

- scope;
- architecture;
- module boundaries;
- integration direction;
- canonical model;

то необходимо обновить:

- relevant doc in `docs/`;
- `MANIFEST.md`;
- ADR, если это decision-level change;
- related Cursor rules, если меняется постоянное поведение агента.

## Completion Rule

Документация не считается завершённой, если:

- она скрывает uncertainty;
- не показывает out-of-scope;
- не фиксирует risks and open questions;
- конфликтует с `MANIFEST.md`.
