# RushDuel.HandToGraveSpecialSummonCondition

Alias: `RD.HandToGraveSpecialSummonCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HandToGraveSpecialSummonCondition(any filter, any count) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:455`

```lua
function RushDuel.HandToGraveSpecialSummonCondition(filter, count)
    return function(e, c)
        if c == nil then
            return true
        end
        local tp = c:GetControler()
        return Duel.GetLocationCount(tp, LOCATION_MZONE) > 0 and
                   Duel.IsExistingMatchingCard(filter, tp, LOCATION_HAND, 0, count, c, e, tp)
    end
end
```
