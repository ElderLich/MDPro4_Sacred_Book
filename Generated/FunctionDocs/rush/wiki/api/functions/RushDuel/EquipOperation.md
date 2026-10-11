# RushDuel.EquipOperation

Alias: `RD.EquipOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EquipOperation(any target) -> any
```

## Description

Rush Duel helper declared in `RDEquip.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDEquip.lua:40`

```lua
function RushDuel.EquipOperation(target)
    return function(e, tp, eg, ep, ev, re, r, rp)
        local c = e:GetHandler()
        Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_EQUIP)
        local g = Duel.SelectMatchingCard(tp, target, tp, LOCATION_MZONE, LOCATION_MZONE, 1, 1, nil, e, tp, true)
        local tc = g:GetFirst()
        if tc and c:IsRelateToEffect(e) then
            Duel.HintSelection(g)
            Duel.Equip(tp, c, tc)
        end
    end
end
```
