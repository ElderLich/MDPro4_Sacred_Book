# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

Sets how many times e can be used before its count limit is spent.
Effects that share a nonzero code share the same usage count. Special code flags such as EFFECT_COUNT_CODE_OATH, EFFECT_COUNT_CODE_DUEL, EFFECT_COUNT_CODE_SINGLE, and EFFECT_COUNT_CODE_CHAIN change how that count is scoped.

## Parameters

- `e` `Effect`
- `count` `int`
- `code` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`
