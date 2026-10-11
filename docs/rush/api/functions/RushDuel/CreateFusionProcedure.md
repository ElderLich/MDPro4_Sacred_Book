# RushDuel.CreateFusionProcedure

Alias: `RD.CreateFusionProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFusionProcedure(any card, any sub, any insf, any funcs, any rep, any min, any max, any checker) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建融合手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `insf` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.
- `rep` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `checker` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:136`

```lua
function RushDuel.CreateFusionProcedure(card, sub, insf, funcs, rep, min, max, checker)
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_FUSION_MATERIAL)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e:SetCondition(RushDuel.FusionProcedureCondition(sub, insf, funcs, rep, min, max, checker))
    e:SetOperation(RushDuel.FusionProcedureOperation(sub, insf, funcs, rep, min, max, checker))
    card:RegisterEffect(e)
    return e
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
