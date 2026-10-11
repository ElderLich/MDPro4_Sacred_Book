# RushDuel.RegisterUnionEffect

Alias: `RD.RegisterUnionEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RegisterUnionEffect(any card, any target, any condition, any cost, any operation, any limit) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
注册效果: 同盟怪兽的同盟效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `cost` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:5`

```lua
function RushDuel.RegisterUnionEffect(card, target, condition, cost, operation, limit)
    local filter = function(c, e, re)
        return c:IsFaceup() and target(c, e, re)
    end
    -- Union
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(1060)
    e1:SetCategory(CATEGORY_EQUIP)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    if condition then
        e1:SetCondition(condition)
    end
    if cost then
        e1:SetCost(cost)
    end
    e1:SetTarget(RushDuel.UnionTarget(filter))
    e1:SetOperation(RushDuel.UnionOperation(filter, operation, limit))
    card:RegisterEffect(e1)
    -- Equip Limit
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_EQUIP_LIMIT)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e2:SetValue(RushDuel.UnionFilter(filter))
    card:RegisterEffect(e2)
    local e3 = Effect.CreateEffect(card)
    e3:SetType(EFFECT_TYPE_SINGLE)
    e3:SetCode(EFFECT_UNION_TARGET)
    e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e3:SetValue(filter)
    card:RegisterEffect(e3)
    return e1
end
```
