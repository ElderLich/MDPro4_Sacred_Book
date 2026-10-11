# RushDuel.AddFusionProcedure

Alias: `RD.AddFusionProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedure(Card card, bool|any sub, bool|any insf, ... int|function|table) -> Effect|nil
```

## Description

Registers a Rush Fusion material procedure using fixed material slots. Each slot may be a card code, a predicate, or a table of alternatives. sub controls substitutes and insf permits non-Fusion special-summon handling; use explicit booleans to make the call unambiguous.

## Parameters

- `card` `Card`: Fusion monster.
- `sub` `bool|any`: Substitute permission; non-booleans are interpreted as the first material slot.
- `insf` `bool|any`: Non-Fusion summon allowance; non-booleans are interpreted as a material slot.
- `...` `int|function|table`: Material slots.

## Returns

- `Effect|nil`: Fusion procedure effect; nil while copying effects.

## Source

`Rush/Utilities/RDFusion.lua:15`

```lua
function RushDuel.AddFusionProcedure(card, sub, insf, ...)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local vals = {...}
    -- 简易融合
    if type(insf) ~= "boolean" then
        table.insert(vals, 1, insf)
        insf = true
    end
    -- 融合素材替代
    if type(sub) ~= "boolean" then
        table.insert(vals, 1, sub)
        sub = true
    end
    -- 融合素材
    local codes, funcs = RushDuel.MakeFusionMaterial(card, table.unpack(vals))
    RushDuel.SetFusionMaterialData(card, codes, #funcs, #funcs)
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, nil, 0, 0, nil)
end
```
