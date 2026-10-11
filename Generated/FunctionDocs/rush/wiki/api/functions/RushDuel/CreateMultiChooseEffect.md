# RushDuel.CreateMultiChooseEffect

Alias: `RD.CreateMultiChooseEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateMultiChooseEffect(any card, any condition, any cost, any hint1, any target1, any operation1, any hint2, any target2, any operation2) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 选择效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `cost` `any`: Type and behavior are not yet reviewed; see the source.
- `hint1` `any`: Type and behavior are not yet reviewed; see the source.
- `target1` `any`: Type and behavior are not yet reviewed; see the source.
- `operation1` `any`: Type and behavior are not yet reviewed; see the source.
- `hint2` `any`: Type and behavior are not yet reviewed; see the source.
- `target2` `any`: Type and behavior are not yet reviewed; see the source.
- `operation2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:182`

```lua
function RushDuel.CreateMultiChooseEffect(card, condition, cost, hint1, target1, operation1, hint2, target2, operation2)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if cost ~= nil then
        e1:SetCost(cost)
    end
    local e2 = e1:Clone()
    e1:SetDescription(hint1)
    e2:SetDescription(hint2)
    e1:SetTarget(RushDuel.MultiChooseEffectTarget(target1))
    e2:SetTarget(RushDuel.MultiChooseEffectTarget(target2))
    e1:SetOperation(operation1)
    e2:SetOperation(operation2)
    card:RegisterEffect(e1)
    card:RegisterEffect(e2)
    return e1, e2
end
```
