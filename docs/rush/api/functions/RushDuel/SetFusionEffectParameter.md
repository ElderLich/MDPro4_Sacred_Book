# RushDuel.SetFusionEffectParameter

Alias: `RD.SetFusionEffectParameter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFusionEffectParameter(any e) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 设置融合效果的额外参数
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:378`

```lua
function RushDuel.SetFusionEffectParameter(e)
    if e then
        RushDuel.CurrentFusionEffect = e
        if e:IsHasProperty(EFFECT_FLAG_SPSUM_PARAM) then
            local min, max = e:GetLabel()
            RushDuel.MinFusionMaterialCount = min
            RushDuel.MaxFusionMaterialCount = max
        else
            RushDuel.MinFusionMaterialCount = nil
            RushDuel.MaxFusionMaterialCount = nil
        end
    else
        RushDuel.CurrentFusionEffect = nil
        RushDuel.MinFusionMaterialCount = nil
        RushDuel.MaxFusionMaterialCount = nil
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
