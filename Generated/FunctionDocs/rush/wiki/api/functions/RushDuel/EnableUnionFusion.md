# RushDuel.EnableUnionFusion

Alias: `RD.EnableUnionFusion`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableUnionFusion(any card, any desc) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可以进行同盟融合术
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:309`

```lua
function RushDuel.EnableUnionFusion(card, desc)
    local e = Effect.CreateEffect(card)
    e:SetDescription(desc)
    e:SetType(EFFECT_TYPE_FIELD)
    e:SetCode(EFFECT_SPSUMMON_PROC)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e:SetRange(LOCATION_EXTRA)
    e:SetCondition(RushDuel.UnionFusionCondition)
    e:SetTarget(RushDuel.UnionFusionTarget)
    e:SetOperation(RushDuel.UnionFusionOperation)
    e:SetValue(SUMMON_TYPE_FUSION)
    card:RegisterEffect(e)
    return e
end
```
