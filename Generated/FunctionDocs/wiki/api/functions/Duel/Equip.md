# Duel.Equip

## Signature

```lua
Duel.Equip(int player, Card c1, Card c2, [bool up], [bool is_step]) -> bool
```

## Description

Equips c1 to c2 for player and returns true if the equip succeeds.
up defaults to true and makes the Equip Card face-up. When is_step is true, call Duel.EquipComplete after all step equips have been created.

## How To Use It

Use this after both the Equip Card and the monster it will equip to are still valid.

A self-equip effect usually creates an Equip Limit after the equip succeeds so the card stays attached only to the intended monster:

```lua
local tc=Duel.GetFirstTarget()
local c=e:GetHandler()
if tc and tc:IsRelateToEffect(e) and c:IsRelateToEffect(e) and Duel.Equip(tp,c,tc) then
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_EQUIP_LIMIT)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetValue(function(e,ec) return ec==tc end)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD)
    c:RegisterEffect(e1)
end
```

When several cards are equipped as one procedure with `is_step=true`, call `Duel.EquipComplete()` after the final successful step.

## Related Functions

- [Card.CheckEquipTarget](/api/functions/Card/CheckEquipTarget)
- [Duel.EquipComplete](/api/functions/Duel/EquipComplete)
- [Auxiliary.AddEquipSpellEffect](/api/functions/Auxiliary/AddEquipSpellEffect)

## Parameters

- `player` `int`
- `c1` `Card`
- `c2` `Card`
- `up` `bool` optional - default: true
- `is_step` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4904`
