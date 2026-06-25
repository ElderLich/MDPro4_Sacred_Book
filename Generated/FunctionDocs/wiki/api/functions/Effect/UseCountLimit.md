# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

Manually consumes count uses of e's count limit for player p.
count defaults to 1. If oath_only is true, the count is consumed only when e's count code includes EFFECT_COUNT_CODE_OATH; otherwise the binding decrements the count limit directly.

## How To Use It

Use this to manually spend an Effect's count limit after a separate `Effect.CheckCountLimit` test.

```lua
if e:CheckCountLimit(tp) then
    e:UseCountLimit(tp,1)
end
```

The optional count defaults to 1. With `oath_only=true`, the local binding spends the count only when the effect's count code includes `EFFECT_COUNT_CODE_OATH`.

## Related Functions

- [Effect.SetCountLimit](/api/functions/Effect/SetCountLimit)
- [Effect.CheckCountLimit](/api/functions/Effect/CheckCountLimit)

## Parameters

- `e` `Effect` - Effect whose count is manually consumed.
- `p` `int` - Player whose local or shared count is consumed.
- `count` `int` optional - Number of uses to consume; default: 1.
- `oath_only` `bool` optional - If true, consume only when e's count code includes EFFECT_COUNT_CODE_OATH; default: false.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`
