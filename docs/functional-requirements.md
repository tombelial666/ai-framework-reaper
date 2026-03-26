# Functional Requirements

## Source Ingestion

- Система должна определять тип входного источника.
- Система должна валидировать пригодность источника для выбранного parser path.
- Система должна собирать source metadata.
- Система должна возвращать warnings, если source неполный или неоднозначный.

## Score Normalization

- Система должна преобразовывать parsed source в canonical internal score model.
- Система должна сохранять musically relevant structure, доступную в source.
- Система должна явно помечать missing data и unresolved fragments.

## Arrangement Mapping

- Система должна строить track planning на основе canonical model.
- Система должна назначать track names и track roles.
- Система должна формировать REAPER-oriented arrangement layout without claiming final interpretation.

## REAPER Integration

- Система должна выпускать editable REAPER-ready scaffold artifact или набор артефактов.
- Система должна создавать traceable mapping между source fragments и generated result.
- Система должна поддерживать markers and regions там, где это practically available.

## Review Assistance

- Система должна формировать warnings and unresolved markers.
- Система должна предоставлять review-oriented output, пригодный для ручной проверки.
- Система не должна скрывать uncertainty.

## Screenshot Path

- Система должна поддерживать screenshot/tab image ingestion как secondary path.
- Система должна возвращать confidence-aware или warning-heavy outputs.
- Система не должна представлять screenshot extraction как equally reliable with structured sources.
