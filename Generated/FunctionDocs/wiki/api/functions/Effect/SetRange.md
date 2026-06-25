# Effect.SetRange

## Signature

```lua
Effect.SetRange(Effect e, int range) -> void
```

## Description

Sets the location range where e applies or can be activated.
This is the handler's active location, not the affected-card range. Continuous field effects usually pair it with Effect.SetTargetRange.

## How To Use It

Use this to say where the effect itself is active or can be activated from.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_SZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
```

`SetRange` is the handler's location. `SetTargetRange` is the affected side or destination range. Continuous effects commonly need both.

## Related Functions

- [Card.RegisterEffect](/api/functions/Card/RegisterEffect)
- [Effect.SetTargetRange](/api/functions/Effect/SetTargetRange)
- [Effect.SetCode](/api/functions/Effect/SetCode)

## Parameters

- `e` `Effect`
- `range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:614`
