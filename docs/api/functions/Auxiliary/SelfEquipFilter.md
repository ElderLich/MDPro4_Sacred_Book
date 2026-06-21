# Auxiliary.SelfEquipFilter

## Signature

```lua
Auxiliary.SelfEquipFilter(Card c, int id) -> bool
```

## Description

Returns true if c has a flag with id, used by Auxiliary.IsSelfEquip to identify cards equipped by their own effect.

## Parameters

- `c` `Card`
- `id` `int`

## Returns

- `bool` - true if c has the flag id.

## Source

- `Utilities/utility.lua:1956`
