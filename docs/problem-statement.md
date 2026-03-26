# Problem Statement

## Core Problem

Подготовка editable проекта в `REAPER` из уже существующих **табов и нотационных** материалов слишком часто начинается с ручного ввода большого количества очевидной структуры — партии, секции, ритмический каркас.

Пользователю нужен способ:

- взять существующий **tab/notation-friendly** source (в т.ч. Guitar Pro, экспорты, MIDI);
- извлечь usable structure в canonical вид;
- получить **MIDI-oriented REAPER-ready draft** с ясной структурой треков;
- быстро увидеть проблемные места для ручной правки.

## What We Are Not Solving

Система не решает задачу полного автоматического понимания музыки из raw audio, не ведёт vocal/lyric-first workflow в MVP и не обещает финальную безошибочную или production-ready аранжировку без участия человека.

## Desired Resolution

Framework должен обеспечить repeatable pipeline с **human-in-the-loop**: ручная проверка обязательна на выходе.

`tab/structured source -> ingestion (adapters) -> normalization -> arrangement mapping -> REAPER MIDI scaffold -> review output`

## Why Existing Manual Flow Is Expensive

- ноты и структура часто переносятся вручную из табов;
- track organization создаётся заново для каждого cover или идеи;
- сомнительные места не маркируются системно;
- пользователь тратит время на рутинную подготовку вместо музыкальных решений.

## Risks in Solving It Poorly

- ложная уверенность в correctness generated result;
- смешивание structured-core path и unreliable screenshot path;
- сильная привязка внутренней модели к одному формату источника или к REAPER internals;
- позиционирование Mode B как «генератор клонов» или готовых произведений.
