# RushDuel.IsAbleToHandOrExtraAsCost

Alias: `RD.IsAbleToHandOrExtraAsCost`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAbleToHandOrExtraAsCost(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以作为Cost回到手卡或者额外卡组
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:122`

```lua
function RushDuel.IsAbleToHandOrExtraAsCost(card)
    return card:IsAbleToHandAsCost() or card:IsAbleToExtraAsCost()
end
```
