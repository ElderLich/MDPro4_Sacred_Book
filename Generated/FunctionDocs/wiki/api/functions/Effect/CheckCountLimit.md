# Effect.CheckCountLimit

## Signature

```lua
Effect.CheckCountLimit(Effect e, int p) -> bool
```

## Description

Checks whether e's count limit is still available for player p.
Normal activation checks already use the core count-limit check; this helper is mainly for scripts that manually inspect another Effect object.
If a custom helper spends the count manually, pair this with Effect.UseCountLimit.

## How To Use It

Use this when a script helper needs to test whether an Effect still has count available for a player before manually spending it.

```lua
if e:CheckCountLimit(tp) then
    e:UseCountLimit(tp)
end
```

Ordinary activated effects usually let the engine manage the count limit. Reach for this only when the script manually controls a custom branch or helper procedure.

## Related Functions

- [Effect.SetCountLimit](/api/functions/Effect/SetCountLimit)
- [Effect.UseCountLimit](/api/functions/Effect/UseCountLimit)

## Parameters

- `e` `Effect` - Effect whose remaining count is checked.
- `p` `int` - Player whose local or shared count map is checked.

## Returns

- `bool` - True if e has no exhausted count limit for p; false when the count is already spent.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:660`
