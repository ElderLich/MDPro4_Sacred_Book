# Auxiliary.AddEquipSpellEffect

## Signature

```lua
Auxiliary.AddEquipSpellEffect(Card c, bool is_self, bool is_opponent, function filter, [function|nil eqlimit], [bool pause], [bool skip_target]) -> void
```

## Description

Add EFFECT_TYPE_ACTIVATE effect to Equip Spell Cards

## Parameters

- `c` `Card`
- `is_self` `bool`
- `is_opponent` `bool`
- `filter` `function`
- `eqlimit` `function|nil` optional
- `pause` `bool` optional
- `skip_target` `bool` optional

## Source

- `Utilities/utility.lua:1883`
