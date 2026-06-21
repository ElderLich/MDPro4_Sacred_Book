# Auxiliary.EquipSpellTarget

## Signature

```lua
Auxiliary.EquipSpellTarget(bool is_self, bool is_opponent, function filter, any eqlimit) -> void
```

## Description

Returns the shared Equip Spell target function. is_self and is_opponent choose which Monster Zones can be targeted, filter selects a valid target, and eqlimit is rechecked for chained target changes and resolution.

## Parameters

- `is_self` `bool`
- `is_opponent` `bool`
- `filter` `function`
- `eqlimit` `any`

## Source

- `Utilities/utility.lua:1909`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
