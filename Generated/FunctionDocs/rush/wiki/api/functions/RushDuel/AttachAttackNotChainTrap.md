# RushDuel.AttachAttackNotChainTrap

Alias: `RD.AttachAttackNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAttackNotChainTrap(any e, any code, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 攻击宣言时, 对方不能把陷阱卡发动
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:124`

```lua
function RushDuel.AttachAttackNotChainTrap(e, code, card, desc, reset, forced)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    if desc ~= nil then
        e1:SetDescription(desc)
        e1:SetProperty(EFFECT_FLAG_CLIENT_HINT)
    end
    e1:SetLabel(code)
    e1:SetOperation(RushDuel.AttackNotChainTrapOperation)
    e1:SetReset(reset)
    card:RegisterEffect(e1, forced)
    local e2 = RushDuel.CreateSingleEffect(e, desc, card, EFFECT_ATTACK_NOT_CHAIN_TRAP, nil, reset, forced)
    return e1, e2
end
```
