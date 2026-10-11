# RushDuel.CreateAdvanceSummonFlag

Alias: `RD.CreateAdvanceSummonFlag`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateAdvanceSummonFlag(any card, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
记录攻击表示上级召唤的状态
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:289`

```lua
function RushDuel.CreateAdvanceSummonFlag(card, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_SUMMON_SUCCESS)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetLabel(flag)
    e1:SetCondition(RushDuel.AdvanceSummonFlagCondition)
    e1:SetOperation(RushDuel.AdvanceSummonFlagOperation)
    card:RegisterEffect(e1)
    return e1
end
```
