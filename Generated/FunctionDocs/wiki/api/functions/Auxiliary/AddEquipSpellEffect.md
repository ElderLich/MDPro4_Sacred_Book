# Auxiliary.AddEquipSpellEffect

## Signature

```lua
Auxiliary.AddEquipSpellEffect(Card c, bool is_self, bool is_opponent, function filter, function|nil eqlimit, [bool pause], [bool skip_target]) -> Effect
```

## Description

Creates an Equip Spell activation effect for c and registers the matching EFFECT_EQUIP_LIMIT.
The activation effect is returned; when pause is true it is created but not registered on c.
Use this for ordinary Equip Spells. Write the target and operation manually when the card equips after another action or needs extra state.

## How To Use It

Use this for the normal Equip Spell activation shape: target a face-up monster, equip the handler during resolution, and register the matching `EFFECT_EQUIP_LIMIT` on the Equip Card.

```lua
aux.AddEquipSpellEffect(c,true,true,s.eqfilter,s.eqlimit)
```

Use a manual activation instead when the card Special Summons first, equips cards from another location, equips several cards at once, or needs extra state before `Duel.Equip`.

## Related Functions

- [Auxiliary.EquipSpellTarget](/api/functions/Auxiliary/EquipSpellTarget)
- [Auxiliary.EquipSpellOperation](/api/functions/Auxiliary/EquipSpellOperation)
- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.CheckEquipTarget](/api/functions/Card/CheckEquipTarget)

## Parameters

- `c` `Card`
- `is_self` `bool`
- `is_opponent` `bool`
- `filter` `function`
- `eqlimit` `function|nil`
- `pause` `bool` optional - default: false
- `skip_target` `bool` optional - default: false

## Returns

- `Effect` - Created activation effect.

## Source

- `Utilities/utility.lua:1883`
