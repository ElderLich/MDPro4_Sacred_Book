# RushDuel.CreateOnlySoleAttackEffect

Alias: `RD.CreateOnlySoleAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlySoleAttackEffect(any e, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用1只怪兽进行攻击
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

`Rush/Utilities/RDLimit.lua:179`

```lua
function RushDuel.CreateOnlySoleAttackEffect(e, code, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if Duel.GetFlagEffect(tp, code) == 0 then
            e:GetLabelObject():SetLabel(eg:GetFirst():GetFieldID())
            Duel.RegisterFlagEffect(tp, code, reset, 0, 1)
        end
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_CANNOT_ATTACK_ANNOUNCE)
    e2:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e2:SetTargetRange(s_range, o_range)
    e2:SetCondition(function(e)
        return Duel.GetFlagEffect(e:GetHandlerPlayer(), code) ~= 0
    end)
    e2:SetTarget(function(e, c)
        return c:GetFieldID() ~= e:GetLabel()
    end)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    e1:SetLabelObject(e2)
end
```
