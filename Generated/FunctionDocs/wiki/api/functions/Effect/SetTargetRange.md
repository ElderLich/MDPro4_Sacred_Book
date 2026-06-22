# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

Sets e's target range fields and clears EFFECT_FLAG_ABSOLUTE_TARGET.
For most field effects, s_range is the affected locations on the handler's controller's side and o_range is the affected locations on the opponent's side. With EFFECT_FLAG_SPSUM_PARAM, they store Special Summon destination player and position.

## How To Use It

For field effects, target range decides which side and location the effect can apply to.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
```

With normal range handling, the first value is the handler controller's side and the second value is the opponent's side. `SetTargetRange` clears the absolute-target flag. Use `Effect.SetAbsoluteRange` when the ranges must mean player 0 and player 1 regardless of who controls the handler.

For Special Summon procedure effects using `EFFECT_FLAG_SPSUM_PARAM`, these fields store the Summon destination player and allowed position instead of card locations.

## Related Functions

- [Effect.SetRange](/api/functions/Effect/SetRange)
- [Effect.SetAbsoluteRange](/api/functions/Effect/SetAbsoluteRange)
- [Effect.SetProperty](/api/functions/Effect/SetProperty)

## Parameters

- `e` `Effect`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:615`
