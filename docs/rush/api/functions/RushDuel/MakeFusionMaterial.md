# RushDuel.MakeFusionMaterial

Alias: `RD.MakeFusionMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MakeFusionMaterial(any card, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
生成融合素材
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:60`

```lua
function RushDuel.MakeFusionMaterial(card, ...)
    local codes = {}
    local funcs = {}
    for _, val in ipairs {...} do
        local val_type = type(val)
        if val_type == "number" then
            RushDuel.AddCodeFusionMaterial(codes, funcs, val)
        elseif val_type == "function" then
            RushDuel.AddFuncFusionMaterial(codes, funcs, val)
        elseif val_type == "table" then
            RushDuel.AddMixFusionMaterial(codes, funcs, val)
        end
    end
    return codes, funcs
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
