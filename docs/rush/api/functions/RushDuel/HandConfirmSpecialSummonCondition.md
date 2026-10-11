# RushDuel.HandConfirmSpecialSummonCondition

Alias: `RD.HandConfirmSpecialSummonCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HandConfirmSpecialSummonCondition(any filter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:418`

```lua
function RushDuel.HandConfirmSpecialSummonCondition(filter)
    return function(e, c)
        if c == nil then
            return true
        end
        local tp = c:GetControler()
        return Duel.GetLocationCount(tp, LOCATION_MZONE) > 0 and
                   Duel.IsExistingMatchingCard(filter, tp, LOCATION_HAND, 0, 1, nil, e, tp, c)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
