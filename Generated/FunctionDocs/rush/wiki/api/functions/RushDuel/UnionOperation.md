# RushDuel.UnionOperation

Alias: `RD.UnionOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionOperation(any target, any operation, any limit) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:47`

```lua
function RushDuel.UnionOperation(target, operation, limit)
    return function(e, tp, eg, ep, ev, re, r, rp)
        local c = e:GetHandler()
        Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_EQUIP)
        local g = Duel.SelectMatchingCard(tp, target, tp, LOCATION_MZONE, 0, 1, 1, c, e)
        local tc = g:GetFirst()
        if tc and c:IsRelateToEffect(e) then
            Duel.HintSelection(g)
            RushDuel.UnionEquip(tp, tc, c)
            if operation then
                operation(e, tp, eg, ep, ev, re, r, rp, tc)
            end
        end
        if limit then
            limit(e, tp, eg, ep, ev, re, r, rp)
        end
    end
end
```
