# RushDuel.ExecuteRitualSummon

Alias: `RD.ExecuteRitualSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ExecuteRitualSummon(any e, any tp, any type, any list, any chkf, any gc, any mat_move, any cancelable) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 进行仪式召唤
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `list` `any`: Type and behavior are not yet reviewed; see the source.
- `chkf` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `cancelable` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:262`

```lua
function RushDuel.ExecuteRitualSummon(e, tp, type, list, chkf, gc, mat_move, cancelable)
    local sg = Group.CreateGroup()
    for _, data in ipairs(list) do
        sg:Merge(data[3])
    end
    ::cancel::
    local rc = nil
    Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_SPSUMMON)
    if cancelable then
        rc = sg:SelectUnselect(nil, tp, false, true, 1, 1)
        if not rc then
            return nil
        end
    else
        rc = sg:Select(tp, 1, 1, nil):GetFirst()
    end
    local options = {}
    for _, data in ipairs(list) do
        local ce, sg = data[1], data[3]
        if sg:IsContains(rc) then
            if ce then
                table.insert(options, {true, ce:GetDescription(), data})
            else
                table.insert(options, {true, 1168, data})
            end
        end
    end
    local data = options[1][3]
    if #options > 1 then
        data = RushDuel.SelectOption(tp, table.unpack(options))
    end
    local ce, mg = data[1], data[2]
    if RushDuel.RitualExtraMaterialFilter then
        mg = mg:Filter(RushDuel.RitualExtraMaterialFilter, nil, e, tp, rc, mg)
    end
    RushDuel.CurrentRitualEffect = e
    local mat = RushDuel.SelectRitualMaterial(tp, rc, type, mg, gc)
    RushDuel.CurrentRitualEffect = nil
    if not mat then
        goto cancel
    end
    local cg = mat:Filter(RushDuel.ConfirmCardFilter, nil)
    if #cg > 0 then
        Duel.ConfirmCards(1 - tp, cg)
    end
    rc:SetMaterial(mat)
    if ce then
        local fop = ce:GetOperation()
        fop(ce, e, tp, rc, mat)
    else
        mat_move(tp, mat, e)
    end
    Duel.BreakEffect()
    Duel.SpecialSummon(rc, SUMMON_TYPE_RITUAL, tp, tp, false, false, POS_FACEUP)
    rc:CompleteProcedure()
    return rc, mat
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
