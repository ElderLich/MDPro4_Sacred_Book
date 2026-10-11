# RushDuel.CreateOnlySoleDirectAttackEffect

Alias: `RD.CreateOnlySoleDirectAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlySoleDirectAttackEffect(any e, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用1只怪兽进行直接攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:208`

```lua
function RushDuel.CreateOnlySoleDirectAttackEffect(e, code, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if Duel.GetAttackTarget() == nil and Duel.GetFlagEffect(tp, code) == 0 then
            e:GetLabelObject():SetLabel(eg:GetFirst():GetFieldID())
            Duel.RegisterFlagEffect(tp, code, reset, 0, 1)
        end
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e2:SetCode(EVENT_ATTACK_DISABLED)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e2:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if Duel.GetAttackTarget() == nil and Duel.GetFlagEffect(tp, code) ~= 0 then
            Duel.ResetFlagEffect(tp, code)
        end
    end)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    local e3 = Effect.CreateEffect(e:GetHandler())
    e3:SetType(EFFECT_TYPE_FIELD)
    e3:SetCode(EFFECT_CANNOT_DIRECT_ATTACK)
    e3:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e3:SetTargetRange(s_range, o_range)
    e3:SetCondition(function(e)
        return Duel.GetFlagEffect(e:GetHandlerPlayer(), code) ~= 0
    end)
    e3:SetTarget(function(e, c)
        return c:GetFieldID() ~= e:GetLabel()
    end)
    e3:SetReset(reset)
    Duel.RegisterEffect(e3, player)
    e1:SetLabelObject(e3)
end
```
