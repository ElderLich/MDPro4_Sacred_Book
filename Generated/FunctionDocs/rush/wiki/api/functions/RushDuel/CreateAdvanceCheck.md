# RushDuel.CreateAdvanceCheck

Alias: `RD.CreateAdvanceCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateAdvanceCheck(any card, any filter, any count, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
上级召唤时的解放怪兽检测
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:180`

```lua
function RushDuel.CreateAdvanceCheck(card, filter, count, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_MATERIAL_CHECK)
    e1:SetValue(function(e, c)
        local mg = c:GetMaterial()
        local ct = math.min(count, #mg)
        local label = 0
        if c:IsLevelBelow(6) and count == 2 then
            -- 当前等级小于解放要求
        elseif ct > 0 and mg:IsExists(filter, ct, nil, e) then
            label = flag
        end
        e:SetLabel(label)
    end)
    card:RegisterEffect(e1)
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e2:SetCode(EVENT_SUMMON_SUCCESS)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e2:SetLabelObject(e1)
    e2:SetCondition(RushDuel.AdvanceCheckCondition)
    e2:SetOperation(RushDuel.AdvanceCheckOperation)
    card:RegisterEffect(e2)
    return e1, e2
end
```
