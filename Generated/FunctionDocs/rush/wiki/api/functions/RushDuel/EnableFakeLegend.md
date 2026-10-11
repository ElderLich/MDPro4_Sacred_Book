# RushDuel.EnableFakeLegend

Alias: `RD.EnableFakeLegend`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableFakeLegend(any card, any location) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
当作传说卡 (赝品)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `location` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:63`

```lua
function RushDuel.EnableFakeLegend(card, location)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_LEGEND_CARD)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SET_AVAILABLE + EFFECT_FLAG_SINGLE_RANGE)
    e1:SetRange(location)
    e1:SetValue(0)
    card:RegisterEffect(e1, true)
    return e1
end
```
