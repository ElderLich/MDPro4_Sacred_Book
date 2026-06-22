# Effect.SetRange

## Signature

```lua
Effect.SetRange(Effect e, int range) -> void
```

## Description

Sets the location range where e applies or can be activated.

## How To Use It

`SetRange` tells the engine where the handler must be for this effect to apply or be activated.

For an ignition effect that can be activated while the monster is face-up on the field:

```lua
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
```

For a Graveyard trigger or ignition effect, use `LOCATION_GRAVE`. For a continuous field effect, `SetRange` is the handler's location, while `SetTargetRange` describes which cards or players are affected.

## Related Functions

- [Card.RegisterEffect](/api/functions/Card/RegisterEffect)
- [Effect.SetTargetRange](/api/functions/Effect/SetTargetRange)
- [Duel.GetLocationCount](/api/functions/Duel/GetLocationCount)

## Parameters

- `e` `Effect`
- `range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:614`
