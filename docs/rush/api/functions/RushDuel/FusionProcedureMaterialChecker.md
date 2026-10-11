# RushDuel.FusionProcedureMaterialChecker

Alias: `RD.FusionProcedureMaterialChecker`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionProcedureMaterialChecker(any mg, any tp, any fc, any chkfnf, any sub, any funcs, any rep, any checker) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合手续 - 素材选择
```

## Parameters

- `mg` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `chkfnf` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `rep` `any`: Type and behavior are not yet reviewed; see the source.
- `checker` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:211`

```lua
function RushDuel.FusionProcedureMaterialChecker(mg, tp, fc, chkfnf, sub, funcs, rep, checker)
    local chkf = chkfnf & 0xff
    if mg:IsExists(Auxiliary.TuneMagicianCheckX, 1, nil, mg, EFFECT_TUNE_MAGICIAN_F) then
        return false
    elseif not Auxiliary.MustMaterialCheck(mg, tp, EFFECT_MUST_BE_FMATERIAL) then
        return false
    elseif checker and not checker(mg, tp, fc, chkf) then
        return false
    elseif RushDuel.FusionExtraChecker and not RushDuel.FusionExtraChecker(mg, tp, fc, chkf) then
        return false
    elseif Auxiliary.FCheckAdditional and not Auxiliary.FCheckAdditional(mg, tp, fc, chkf) then
        return false
    elseif Auxiliary.FGoalCheckAdditional and not Auxiliary.FGoalCheckAdditional(mg, tp, fc, chkf) then
        return false
    else
        local sg = Group.CreateGroup()
        return mg:IsExists(RushDuel.FusionProcedureCheckStep, 1, nil, mg, sg, fc, sub, rep, table.unpack(funcs))
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
