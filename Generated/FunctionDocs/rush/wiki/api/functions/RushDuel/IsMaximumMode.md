# RushDuel.IsMaximumMode

Alias: `RD.IsMaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsMaximumMode(Card card) -> bool
```

## Description

Checks that the card is in a Monster Zone, has the Maximum Summon type and still has overlay components. This Card predicate differs from RD.MaximumMode, an Effect condition that checks the Maximum marker.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the helper's Maximum-mode test passes.

## Source

`Rush/Utilities/RDCondition.lua:13`

```lua
function RushDuel.IsMaximumMode(card)
    return card:IsLocation(LOCATION_MZONE) and card:IsSummonType(SUMMON_TYPE_MAXIMUM) and card:GetOverlayCount() > 0
end
```
