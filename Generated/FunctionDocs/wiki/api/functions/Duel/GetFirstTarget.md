# Duel.GetFirstTarget

## Signature

```lua
Duel.GetFirstTarget() -> Card|nil
```

## Description

Returns the first target card currently recorded for the resolving Chain.
If multiple target cards were recorded, the remaining target cards are returned as additional values in recorded order.

## How To Use It

Use this during resolution when the effect selected exactly one target card.

Always check that the returned card still exists and is still related to the resolving effect before moving, destroying, equipping, or changing it:

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.SendtoHand(tc,nil,REASON_EFFECT)
end
```

For multiple targets, use `Duel.GetTargetsRelateToChain()` when you need the group of targets that are still related to the resolving Chain.

## Returns

- `Card|nil` - First recorded target card, followed by any additional target cards as extra Lua return values. No value is returned when the current Chain has no target cards.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4949`
