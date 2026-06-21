# Effect.SetAbsoluteRange

## Signature

```lua
Effect.SetAbsoluteRange(Effect e, int playerid, int s_range, int o_range) -> void
```

## Description

设置target range属性并设置 EFFECT_FLAG_ABSOLUTE_TARGET 标志
playerid != 0 s_range和o_range反转

## Parameters

- `e` `Effect`
- `playerid` `int`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:616`
