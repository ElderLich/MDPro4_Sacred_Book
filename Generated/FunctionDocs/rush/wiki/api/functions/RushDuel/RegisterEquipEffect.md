# RushDuel.RegisterEquipEffect

Alias: `RD.RegisterEquipEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RegisterEquipEffect(Card card, function|nil condition, function|nil cost, function target, int|nil property) -> Effect
```

## Description

Registers a Rush Equip Spell activation and its equip limit. The target argument is a card predicate; this implementation chooses the monster during resolution. Returns the activation Effect for further configuration.

## Parameters

- `card` `Card`: Equip Spell.
- `condition` `function|nil`: Activation condition, or nil.
- `cost` `function|nil`: Cost callback, or nil.
- `target` `function`: Predicate receiving card, effect, player and a legality-check flag.
- `property` `int|nil`: Optional activation property flags.

## Returns

- `Effect`: Registered activation Effect.

## Source

`Rush/Utilities/RDEquip.lua:5`

```lua
function RushDuel.RegisterEquipEffect(card, condition, cost, target, property)
    -- Activate
    local e1 = Effect.CreateEffect(card)
    e1:SetCategory(CATEGORY_EQUIP)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    if property ~= nil then
        e1:SetProperty(property)
    end
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if cost ~= nil then
        e1:SetCost(cost)
    end
    e1:SetTarget(RushDuel.EquipTarget(target))
    e1:SetOperation(RushDuel.EquipOperation(target))
    card:RegisterEffect(e1)
    -- Equip Limit
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_EQUIP_LIMIT)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e2:SetValue(RushDuel.EquipFilter(target))
    card:RegisterEffect(e2)
    return e1
end
```
