# Effect.SetProperty

## Signature

```lua
Effect.SetProperty(Effect e, int prop1, [int prop2]) -> void
```

## Description

Sets e's property flags. prop1 holds the normal effect property flags; prop2 is used for the second property word when needed.
Internal flags are preserved when prop1 is replaced.

## How To Use It

Use `SetProperty` for flags that change targeting, timing, visibility, and activation rules.

For targeting effects, `EFFECT_FLAG_CARD_TARGET` should be paired with `Duel.SelectTarget` in the Target callback:

```lua
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetTarget(s.target)
```

Other common flags include `EFFECT_FLAG_DELAY` for missed-timing-sensitive triggers, `EFFECT_FLAG_DAMAGE_STEP` for effects that can activate in the Damage Step, and `EFFECT_FLAG_CANNOT_DISABLE` for rules or equip limits that should not be negated normally.

## Related Functions

- [Effect.IsHasProperty](/api/functions/Effect/IsHasProperty)
- [Effect.SetTargetRange](/api/functions/Effect/SetTargetRange)

## Parameters

- `e` `Effect`
- `prop1` `int`
- `prop2` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:620`
