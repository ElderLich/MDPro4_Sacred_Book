# Effect.SetAbsoluteRange

## Signature

```lua
Effect.SetAbsoluteRange(Effect e, int playerid, int s_range, int o_range) -> void
```

## Description

Sets e's target range from an absolute player viewpoint and marks the effect with EFFECT_FLAG_ABSOLUTE_TARGET.
If playerid is 1, the supplied ranges are swapped internally so the stored ranges still line up with player 0/player 1 absolute handling.

## How To Use It

Use this for field effects whose affected side must be fixed to player 0/player 1 instead of relative to the handler's controller.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetAbsoluteRange(tp,0,LOCATION_MZONE)
```

The core stores the ranges with `EFFECT_FLAG_ABSOLUTE_TARGET` set. If `playerid` is 1, it swaps `s_range` and `o_range` internally so the final effect still points at the intended absolute player.

## Related Functions

- [Effect.SetTargetRange](/api/functions/Effect/SetTargetRange)
- [Effect.SetProperty](/api/functions/Effect/SetProperty)

## Parameters

- `e` `Effect`
- `playerid` `int`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:616`
