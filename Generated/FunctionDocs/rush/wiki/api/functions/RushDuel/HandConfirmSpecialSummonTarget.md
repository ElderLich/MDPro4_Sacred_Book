# RushDuel.HandConfirmSpecialSummonTarget

Alias: `RD.HandConfirmSpecialSummonTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HandConfirmSpecialSummonTarget(any filter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:428`

```lua
function RushDuel.HandConfirmSpecialSummonTarget(filter)
    return function(e, tp, eg, ep, ev, re, r, rp, chk, c)
        local mg = Duel.GetMatchingGroup(filter, tp, LOCATION_HAND, 0, nil, e, tp, c)
        Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_CONFIRM)
        local tc = mg:SelectUnselect(nil, tp, false, true, 1, 1)
        if tc then
            e:SetLabelObject(tc)
            return true
        else
            return false
        end
    end
end
```
