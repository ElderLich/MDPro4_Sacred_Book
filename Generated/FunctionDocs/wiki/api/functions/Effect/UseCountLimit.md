# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

Manually consumes count uses of e's count limit for player p.
count defaults to 1. If oath_only is true, the count is consumed only when e's count code includes EFFECT_COUNT_CODE_OATH; otherwise the binding decrements the count limit directly.

## Parameters

- `e` `Effect`
- `p` `int`
- `count` `int` optional - default: 1
- `oath_only` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`
