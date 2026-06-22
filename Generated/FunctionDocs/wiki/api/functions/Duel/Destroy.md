# Duel.Destroy

## Signature

```lua
Duel.Destroy(Card|Group targets, int reason, [int dest], [int reason_player]) -> int
```

## Description

Destroys targets for reason and returns the number of cards actually destroyed.
dest defaults to LOCATION_GRAVE. reason_player defaults to the current Chain's reason player. Use REASON_EFFECT for normal card effects and reserve REASON_RULE for rule/procedure cleanup.

## How To Use It

Use this during resolution after checking that the target is still related to the effect.

The return value is important. It is 0 when no card was actually destroyed, for example because the card left the expected place or could not be destroyed.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) and Duel.Destroy(tc,REASON_EFFECT)>0 then
    -- follow-up that requires successful destruction
end
```

Use `Duel.SetOperationInfo(0,CATEGORY_DESTROY,...)` in the Target callback when the destruction is known before resolution.

## Related Functions

- [Card.IsDestructable](/api/functions/Card/IsDestructable)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Duel.SendtoGrave](/api/functions/Duel/SendtoGrave)

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `dest` `int` optional
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4858`
