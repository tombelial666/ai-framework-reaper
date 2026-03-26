# Test plan — Slice 1 (MusicXML)

## Goals

- Guard module boundaries (imports resolve).
- Lock deterministic output for the minimal MusicXML fixture (`fixtures/structured/musicxml/minimal_chord.xml`).
- Lock drums-first unpitched fixture (`fixtures/structured/musicxml/minimal_drums.xml`) vs expected canonical/scaffold JSON.
- Ensure review output reminds that the result is a draft.

## Current automated tests

| Location | What |
|----------|------|
| `tests/unit/test_slice1_contracts.py` | Import smoke; pipeline dict equality vs `fixtures/expected/*.json` (chord + drums); review summary contains draft wording. |

## Deferred (not in this slice)

- Full MusicXML coverage (voices, tuplets, pickups, percussion).
- Golden tests for `.rpp` or ReaScript output.
- Regression suite for Guitar Pro / MIDI / manual tab.

## How to run

```bash
pip install -e ".[dev]"
pytest tests/unit/test_slice1_contracts.py -v
```
