# RushDuel.EquipTarget

Alias: `RD.EquipTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EquipTarget(any target) -> any
```

## Description

Rush Duel helper declared in `RDEquip.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDEquip.lua:32`

```lua
function RushDuel.EquipTarget(target)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.IsExistingMatchingCard(target, tp, LOCATION_MZONE, LOCATION_MZONE, 1, nil, e, tp, true)
        end
        Duel.SetOperationInfo(0, CATEGORY_EQUIP, e:GetHandler(), 1, 0, 0)
    end
end
```
