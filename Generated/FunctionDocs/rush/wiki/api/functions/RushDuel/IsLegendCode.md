# RushDuel.IsLegendCode

Alias: `RD.IsLegendCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLegendCode(any card, ... any) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否为传说卡的卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:31`

```lua
function RushDuel.IsLegendCode(card, ...)
    return card:IsCode(table.unpack({...}))
end
```
