# RushDuel.AddFusionProcedureRep

Alias: `RD.AddFusionProcedureRep`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedureRep(any card, any sub, any insf, any func, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加融合手续: 指定条件, 不固定数量
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `insf` `any`: Type and behavior are not yet reviewed; see the source.
- `func` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:37`

```lua
function RushDuel.AddFusionProcedureRep(card, sub, insf, func, min, max, ...)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local vals = {...}
    -- 融合素材
    local codes, funcs = RushDuel.MakeFusionMaterial(card, table.unpack(vals))
    RushDuel.SetFusionMaterialData(card, codes, #funcs + min, #funcs + max)
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, func, min, max, nil)
end
```
