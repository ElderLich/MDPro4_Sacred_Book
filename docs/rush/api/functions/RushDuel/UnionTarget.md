# RushDuel.UnionTarget

Alias: `RD.UnionTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionTarget(any target) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:39`

```lua
function RushDuel.UnionTarget(target)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.GetLocationCount(tp,LOCATION_SZONE)>0 and Duel.IsExistingMatchingCard(target, tp, LOCATION_MZONE, 0, 1, e:GetHandler(), e)
        end
        Duel.SetOperationInfo(0, CATEGORY_EQUIP, e:GetHandler(), 1, 0, 0)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
