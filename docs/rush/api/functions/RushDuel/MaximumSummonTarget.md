# RushDuel.MaximumSummonTarget

Alias: `RD.MaximumSummonTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumSummonTarget(any left_code, any right_code) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `left_code` `any`: Type and behavior are not yet reviewed; see the source.
- `right_code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:86`

```lua
function RushDuel.MaximumSummonTarget(left_code, right_code)
    return function(e, tp, eg, ep, ev, re, r, rp, chk, c, og, min, max)
        local mg = Duel.GetMatchingGroup(RushDuel.MaximumSummonFilter, tp, LOCATION_HAND, 0, nil, e, tp, left_code, right_code)
        local cancelable = Duel.GetCurrentChain() == 0
        local sg = RushDuel.Select(HINTMSG_MAXMATERIAL, tp, mg, RushDuel.MaximumSummonCheck, cancelable, 2, 2)
        if sg then
            sg:KeepAlive()
            e:SetLabelObject(sg)
            return true
        else
            return false
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
