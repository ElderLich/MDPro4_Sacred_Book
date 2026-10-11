# RushDuel.AdvanceMaterialCheckValue

Alias: `RD.AdvanceMaterialCheckValue`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AdvanceMaterialCheckValue(any getter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `getter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:256`

```lua
function RushDuel.AdvanceMaterialCheckValue(getter)
    return function(e, c)
        local g = c:GetMaterial()
        local mat = RushDuel.GetTributeCount(c)
        local count = #g
        local value1, value2 = 0, 0
        if count == 1 then
            value1 = getter(g:GetFirst(), count, mat) * mat
            value2 = value1
        elseif count == 2 then
            local tc1, tc2 = g:GetFirst(), g:GetNext()
            if mat == 2 then
                value1 = getter(tc1, count, mat) + getter(tc2, count, mat)
                value2 = value1
            elseif mat == 3 then
                local ng, dg = RushDuel.SplitTribute(c)
                if #dg == 1 then
                    value1 = getter(ng:GetFirst(), count, mat) + getter(dg:GetFirst(), count, mat) * 2
                    value2 = value1
                else
                    value1 = getter(tc1, count, mat) * 2 + getter(tc2, count, mat)
                    value2 = getter(tc1, count, mat) + getter(tc2, count, mat) * 2
                end
            end
        elseif count == 3 then
            value1 = g:GetSum(getter, count, mat)
            value2 = value1
        end
        e:GetLabelObject():SetLabel(value1, value2)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
