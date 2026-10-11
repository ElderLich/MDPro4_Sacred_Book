# RushDuel.EnableMaximumMode

Alias: `RD.EnableMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableMaximumMode(Card card, int reset) -> void
```

## Description

Registers an EFFECT_MAXIMUM_MODE marker with the supplied reset. It does not create components or perform a Maximum Summon by itself.

## Parameters

- `card` `Card`: Card receiving the marker.
- `reset` `int`: Reset flags for the marker effect.

## Returns

No return values.

## Source

`Rush/Utilities/RDMaximum.lua:123`

```lua
function RushDuel.EnableMaximumMode(card, reset)
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_MAXIMUM_MODE)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e:SetRange(LOCATION_MZONE)
    e:SetReset(reset)
    card:RegisterEffect(e, true)
end
```
