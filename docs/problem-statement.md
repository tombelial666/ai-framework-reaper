# Problem Statement

## Core Problem

Подготовка editable music project в `REAPER` из уже существующих музыкальных материалов слишком часто начинается с ручного ввода большого количества очевидной структуры.

Пользователю нужен способ:

- взять существующий source;
- извлечь из него usable structure;
- преобразовать её в единый внутренний вид;
- получить REAPER-ready draft;
- быстро увидеть проблемные места для ручной правки.

## What We Are Not Solving

Система не решает задачу полного автоматического понимания музыки из raw audio и не обещает финальную безошибочную аранжировку.

## Desired Resolution

Framework должен обеспечить repeatable pipeline с **human-in-the-loop**: ручная проверка обязательна на выходе.

`source -> ingestion -> normalization -> arrangement mapping -> REAPER scaffold -> review output`

## Why Existing Manual Flow Is Expensive

- ноты и структура часто переносятся вручную;
- track organization создаётся заново для каждого проекта;
- сомнительные места не маркируются системно;
- пользователь тратит время на рутинную подготовку, а не на музыкальные решения.

## Risks in Solving It Poorly

- ложная уверенность в correctness generated result;
- смешивание structured-core path и unreliable screenshot path;
- сильная привязка внутренней модели к одному формату источника или к REAPER internals.
