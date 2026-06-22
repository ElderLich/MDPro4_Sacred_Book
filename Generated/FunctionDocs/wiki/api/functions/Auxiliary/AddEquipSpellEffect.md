# Auxiliary.AddEquipSpellEffect

## Signature

```lua
Auxiliary.AddEquipSpellEffect(Card c, bool is_self, bool is_opponent, function filter, function|nil eqlimit, [bool pause], [bool skip_target]) -> Effect
```

## Description

Creates an Equip Spell activation effect for c and registers the matching EFFECT_EQUIP_LIMIT.
The activation effect is returned; when pause is true it is created but not registered on c.

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
