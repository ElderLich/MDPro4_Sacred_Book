# RushDuel.AddFusionProcedureSP

Alias: `RD.AddFusionProcedureSP`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedureSP(any card, any sub, any insf, any matfilter, any matcheck, any min, any max) -> any
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
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `matcheck` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:49`

```lua
function RushDuel.AddFusionProcedureSP(card, sub, insf, matfilter, matcheck, min, max)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local insf = (insf ~= false)
    local sub = (sub ~= false)
    local funcs = {}
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, matfilter, min, max, matcheck)
end
```
