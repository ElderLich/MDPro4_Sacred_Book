# RushDuel.IsSameCode

Alias: `RD.IsSameCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSameCode(any card1, any card2) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否为同名卡
```

## Parameters

- `card1` `any`: Type and behavior are not yet reviewed; see the source.
- `card2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:36`

```lua
function RushDuel.IsSameCode(card1, card2)
    return card1:IsCode(card2:GetCode())
end
```
