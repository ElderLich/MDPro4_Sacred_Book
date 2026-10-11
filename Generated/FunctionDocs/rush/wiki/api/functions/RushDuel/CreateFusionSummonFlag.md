# RushDuel.CreateFusionSummonFlag

Alias: `RD.CreateFusionSummonFlag`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFusionSummonFlag(any card, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
记录融合术召唤的状态
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:308`

```lua
function RushDuel.CreateFusionSummonFlag(card, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_SPSUMMON_SUCCESS)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetLabel(flag)
    e1:SetCondition(RushDuel.FusionSummonFlagCondition)
    e1:SetOperation(RushDuel.FusionSummonFlagOperation)
    card:RegisterEffect(e1)
    return e1
end
```
