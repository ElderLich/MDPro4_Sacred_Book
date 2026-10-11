# RushDuel.EnableContactFusion

Alias: `RD.EnableContactFusion`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableContactFusion(any card, any desc) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可以进行接触融合术
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:253`

```lua
function RushDuel.EnableContactFusion(card, desc)
    local e = Effect.CreateEffect(card)
    e:SetDescription(desc)
    e:SetType(EFFECT_TYPE_FIELD)
    e:SetCode(EFFECT_SPSUMMON_PROC)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e:SetRange(LOCATION_EXTRA)
    e:SetCondition(RushDuel.ContactFusionCondition)
    e:SetTarget(RushDuel.ContactFusionTarget)
    e:SetOperation(RushDuel.ContactFusionOperation)
    e:SetValue(SUMMON_TYPE_FUSION)
    card:RegisterEffect(e)
    return e
end
```
