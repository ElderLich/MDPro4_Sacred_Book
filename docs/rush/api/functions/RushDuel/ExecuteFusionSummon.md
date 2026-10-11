# RushDuel.ExecuteFusionSummon

Alias: `RD.ExecuteFusionSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ExecuteFusionSummon(any e, any tp, any pos, any list, any chkf, any gc, any mat_move, any cancelable) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 进行融合召唤
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `list` `any`: Type and behavior are not yet reviewed; see the source.
- `chkf` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `cancelable` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:457`

```lua
function RushDuel.ExecuteFusionSummon(e, tp, pos, list, chkf, gc, mat_move, cancelable)
    local sg = Group.CreateGroup()
    for _, data in ipairs(list) do
        sg:Merge(data[3])
    end
    ::cancel::
    local fc = nil
    Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_SPSUMMON)
    if cancelable then
        fc = sg:SelectUnselect(nil, tp, false, true, 1, 1)
        if not fc then
            return nil
        end
    else
        fc = sg:Select(tp, 1, 1, nil):GetFirst()
    end
    local options = {}
    for _, data in ipairs(list) do
        local ce, sg = data[1], data[3]
        if sg:IsContains(fc) then
            if ce then
                table.insert(options, {true, ce:GetDescription(), data})
            else
                table.insert(options, {true, 1169, data})
            end
        end
    end
    local data = options[1][3]
    if #options > 1 then
        data = RushDuel.SelectOption(tp, table.unpack(options))
    end
    local ce, mg = data[1], data[2]
    RushDuel.SetFusionEffectParameter(e)
    local mat = Duel.SelectFusionMaterial(tp, fc, mg, gc, chkf)
    RushDuel.SetFusionEffectParameter()
    if #mat < 2 then
        goto cancel
    end
    local cg = mat:Filter(RushDuel.ConfirmCardFilter, nil)
    if #cg > 0 then
        Duel.ConfirmCards(1 - tp, cg)
    end
    fc:SetMaterial(mat)
    if ce then
        local fop = ce:GetOperation()
        fop(ce, e, tp, fc, mat)
    else
        mat_move(tp, mat, e)
    end
    Duel.BreakEffect()
    Duel.SpecialSummon(fc, SUMMON_TYPE_FUSION, tp, tp, false, false, pos)
    fc:CompleteProcedure()
    return fc, mat
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
