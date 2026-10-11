# RushDuel.CreateActivateCountLimitEffect

Alias: `RD.CreateActivateCountLimitEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateActivateCountLimitEffect(any e, any desc, any value, any count, any player, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 特定卡的效果最多发动X次 (只能针对1名玩家)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:358`

```lua
function RushDuel.CreateActivateCountLimitEffect(e, desc, value, count, player, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ACTIVATE)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(1, 0)
    e1:SetLabel(0)
    e1:SetCondition(function(e)
        return e:GetLabel() >= count
    end)
    e1:SetValue(value)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e2:SetCode(EVENT_CHAINING)
    e2:SetLabelObject(e1)
    e2:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if ep == tp and value(e, re, tp, true) then
            local te = e:GetLabelObject()
            te:SetLabel(te:GetLabel() + 1)
        end
    end)
    Duel.RegisterEffect(e2, player)
    local e3 = e2:Clone()
    e3:SetCode(EVENT_CHAIN_NEGATED)
    e3:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if ep == tp and value(e, re, tp, false) then
            local te = e:GetLabelObject()
            local ct = te:GetLabel() - 1
            if ct < 0 then
                ct = 0
            end
            te:SetLabel(ct)
        end
    end)
    return e1
end
```
