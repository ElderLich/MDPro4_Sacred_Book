# RushDuel.InitLegendCard

Alias: `RD.InitLegendCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.InitLegendCard(any c) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:15`

```lua
function RushDuel.InitLegendCard(c)
    local e1 = Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_LEGEND_CARD)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SET_AVAILABLE)
    e1:SetRange(0xff)
    e1:SetValue(c:GetOriginalCodeRule())
    c:RegisterEffect(e1, true)
end
```
