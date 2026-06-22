# Duel.BreakEffect

## Signature

```lua
Duel.BreakEffect() -> void
```

## Description

Separates the current resolving effect into a later timing window, then raises EVENT_BREAK_EFFECT.
Use this when card text says to do one action, then do another action afterward, so later triggers do not see both actions as simultaneous.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4927`
