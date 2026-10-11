# RushDuel.AttachEndPhase

Alias: `RD.AttachEndPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachEndPhase(any e, any card, any player, any code, any operation, any desc, any once) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 回合结束时特效
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `once` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:140`

```lua
function RushDuel.AttachEndPhase(e, card, player, code, operation, desc, once)
    if once then
        card:RegisterFlagEffect(0, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, code, desc)
    else
        card:RegisterFlagEffect(0, RESET_EVENT + RESETS_STANDARD, EFFECT_FLAG_CLIENT_HINT, 1, code, desc)
    end
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_PHASE + PHASE_END)
    e1:SetCountLimit(1)
    e1:SetLabelObject(card)
    e1:SetCondition(function(e, tp, eg, ep, ev, re, r, rp)
        local tc = e:GetLabelObject()
        local fids = {tc:GetFlagEffectLabel(0)}
        for i = 1, #fids do
            if fids[i] == code then
                return true
            end
        end
        e:Reset()
        return false
    end)
    e1:SetOperation(operation)
    if once then
        e1:SetReset(RESET_PHASE + PHASE_END)
    end
    Duel.RegisterEffect(e1, player)
    return e1
end
```
