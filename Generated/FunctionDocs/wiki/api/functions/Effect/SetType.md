# Effect.SetType

## Signature

```lua
Effect.SetType(Effect e, int type) -> void
```

## Description

Sets e's effect type flags.
The core normalizes some type combinations: Spell/Trap activation effects become field activation effects, Flip Effects receive EVENT_FLIP handling, and ignition/Quick Effects gain field behavior.

## Parameters

- `e` `Effect`
- `type` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:619`
