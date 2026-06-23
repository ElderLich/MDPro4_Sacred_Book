# Effect.CheckCountLimit

## Signature

```lua
Effect.CheckCountLimit(Effect e, int p) -> bool
```

## Description

Checks whether e's count limit is still available for player p.
Normal activation checks already use the core count-limit check; this helper is mainly for scripts that manually inspect another Effect object.

## Parameters

- `e` `Effect` - Effect whose remaining count is checked.
- `p` `int` - Player whose local or shared count map is checked.

## Returns

- `bool` - True if e has no exhausted count limit for p; false when the count is already spent.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:660`
