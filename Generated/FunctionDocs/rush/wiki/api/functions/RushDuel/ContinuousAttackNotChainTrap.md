# RushDuel.ContinuousAttackNotChainTrap

Alias: `RD.ContinuousAttackNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContinuousAttackNotChainTrap(any card) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续效果: 攻击宣言时, 对方不能把陷阱卡发动
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:67`

```lua
function RushDuel.ContinuousAttackNotChainTrap(card)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetLabel(card:GetOriginalCode())
    e1:SetOperation(RushDuel.AttackNotChainTrapOperation)
    card:RegisterEffect(e1)
    return e1
end
```
