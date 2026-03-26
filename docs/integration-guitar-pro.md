# Guitar Pro Integration

## Recommendation

Рекомендация: считать Guitar Pro related structured sources **приоритетным продуктовым structured path** MVP (tab-first identity), но не обещать поддержку деталей, которые не подтверждены конкретным import/export route.

## Priority of Paths

### 1. Preferred Structured Path

Guitar Pro related source в формате, который:

- можно читать детерминированно;
- даёт track structure, timing и note data;
- позволяет сохранять provenance and warnings.

### 2. Songsterr-Related Structured Path

**Assumption:** пользователь использует **легально доступные** экспорты/derived structured sources с Songsterr или совместимых сервисов.

**Risk:** ToS, лицензирование и доступность экспорта меняются; нарушение правил сервиса недопустимо.

### 3. Acceptable Fallback Path

Conversion/export from Guitar Pro into `MIDI` or `MusicXML` (**bridge**), если fidelity loss явно принимается и помечается warnings.

### 4. Manual-Assisted Fallback Path

Ручная подготовка text/tab-like structure, если structured file unavailable или conversion unreliable.

## Expected Information

Желаемые данные из Guitar Pro related sources:

- track names
- measure and timing structure
- note events
- string/fret where available
- tuning
- capo
- articulations and techniques where available
- section-like structure if exposed

## Possible Data Loss Areas

- techniques and articulations may be partially lost in conversion;
- tuning and capo may not survive some export paths;
- naming may degrade or become inconsistent;
- voice/channel distinctions may flatten.

## Deterministic Handling Rule

- Подтверждённые поля заполняются.
- Частично доступные поля заполняются с warnings.
- Неподтверждённые details не выдумываются.

## Confirmed

- Guitar Pro related sources are in MVP as **primary product sources** (tab-first).
- `MusicXML` may be used as a **technical bridge** from Guitar Pro tools without becoming the product headline.

## Assumption

- At least one concrete import path will expose enough data for useful normalization.

## Risk

- Fidelity differences between native and converted representations may be significant.

## Open Questions

- Which exact Guitar Pro related format should be first-class in the next slice after the MusicXML bridge.
- Whether a direct parser or conversion-based route is the best deterministic-first choice.
- How Songsterr-exported structured inputs will be validated and labeled in ingestion (format detection).
