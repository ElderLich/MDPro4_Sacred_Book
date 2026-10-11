# RushDuel.AttachAttackAnnounce

Alias: `RD.AttachAttackAnnounce`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAttackAnnounce(any e, any card, any operation, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 攻击宣言时特效
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:110`

```lua
function RushDuel.AttachAttackAnnounce(e, card, operation, desc, reset, forced)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetOperation(operation)
    if desc ~= nil then
        e1:SetDescription(desc)
        e1:SetProperty(EFFECT_FLAG_CLIENT_HINT)
    end
    e1:SetReset(reset)
    card:RegisterEffect(e1, forced)
    return e1
end
```
