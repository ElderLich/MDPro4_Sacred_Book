# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

Manually reduce player p's available activation count for effect e by count [oath_only indicates whether the effect is EFFECT_FLAG_OATH]

## Parameters

- `e` `Effect`
- `p` `int`
- `count` `int` optional - default: 1
- `oath_only` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`
