# RushDuel.IsLegendCard

Alias: `RD.IsLegendCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLegendCard(Card card) -> bool
```

## Description

Checks TYPE_LEGEND or an EFFECT_LEGEND_CARD marker. This supports both the printed Rush Legend bit and effect-based Legend treatment.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card is treated as Legend.

## Source

`Rush/Utilities/RDLegend.lua:26`

```lua
function RushDuel.IsLegendCard(card)
    return card:IsType(TYPE_LEGEND) or card:IsHasEffect(EFFECT_LEGEND_CARD) ~= nil
end
```
