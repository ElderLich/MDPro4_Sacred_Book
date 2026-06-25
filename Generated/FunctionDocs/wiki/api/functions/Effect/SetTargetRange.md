# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

Sets e's target range fields and clears EFFECT_FLAG_ABSOLUTE_TARGET.
For most field effects, s_range is the affected locations on the handler's controller's side and o_range is the affected locations on the opponent's side. With EFFECT_FLAG_SPSUM_PARAM, they store Special Summon destination player and position.
Use Effect.SetAbsoluteRange when the affected sides must be fixed to a specific player instead of relative to the handler.

## How To Use It

Use this for the cards or players affected by a field-like effect, or for special meanings required by certain properties.

```lua
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(0,LOCATION_MZONE)
```

The local binding writes `s_range` and `o_range` and clears `EFFECT_FLAG_ABSOLUTE_TARGET`. For absolute player-oriented ranges, use `Effect.SetAbsoluteRange`.

## Related Functions

- [Effect.SetRange](/api/functions/Effect/SetRange)
- [Effect.SetAbsoluteRange](/api/functions/Effect/SetAbsoluteRange)
- [Effect.SetProperty](/api/functions/Effect/SetProperty)

## Parameters

- `e` `Effect` - Effect whose target range fields are being set.
- `s_range` `int` - Usually the handler controller's affected locations. With EFFECT_FLAG_SPSUM_PARAM, this is the allowed Special Summon position.
- `o_range` `int` - Usually the opponent's affected locations. With EFFECT_FLAG_SPSUM_PARAM, this is the destination player value for the Special Summon.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:615`
