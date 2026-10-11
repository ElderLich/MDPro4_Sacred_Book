# RushDuel.MaximumSummonCondition

Alias: `RD.MaximumSummonCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumSummonCondition(any left_code, any right_code) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `left_code` `any`: Type and behavior are not yet reviewed; see the source.
- `right_code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:75`

```lua
function RushDuel.MaximumSummonCondition(left_code, right_code)
    return function(e, c, og, min, max)
        if c == nil then
            return true
        end
        local tp = c:GetControler()
        local mg = Duel.GetMatchingGroup(RushDuel.MaximumSummonFilter, tp, LOCATION_HAND, 0, nil, e, tp, left_code, right_code)
        local fg = Duel.GetFieldGroup(tp, LOCATION_MZONE, 0)
        return Duel.GetMZoneCount(tp, fg) > 0 and mg:CheckSubGroup(RushDuel.MaximumSummonCheck, 2, 2)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
