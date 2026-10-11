# RushDuel.HandToGraveSpecialSummonTarget

Alias: `RD.HandToGraveSpecialSummonTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HandToGraveSpecialSummonTarget(any filter, any count) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:465`

```lua
function RushDuel.HandToGraveSpecialSummonTarget(filter, count)
    return function(e, tp, eg, ep, ev, re, r, rp, chk, c)
        local mg = Duel.GetMatchingGroup(filter, tp, LOCATION_HAND, 0, c, e, tp)
        local sg = RushDuel.Select(HINTMSG_TOGRAVE, tp, mg, nil, true, count, count)
        if sg and sg:GetCount() == count then
            sg:KeepAlive()
            e:SetLabelObject(sg)
            return true
        else
            return false
        end
    end
end
```
