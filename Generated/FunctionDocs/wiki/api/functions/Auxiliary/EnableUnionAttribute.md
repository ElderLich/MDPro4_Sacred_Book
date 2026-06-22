# Auxiliary.EnableUnionAttribute

## Signature

```lua
Auxiliary.EnableUnionAttribute(Card c, function filter) -> void
```

## Description

Registers the standard modern Union Monster package on c.
The helper adds equipped-card destruction substitution, an EFFECT_UNION_LIMIT using filter, an ignition effect to equip c from the Monster Zone to a valid monster, and an ignition effect to Special Summon c from the Spell & Trap Zone.

## Parameters

- `c` `Card`
- `filter` `function`

## Source

- `Utilities/utility.lua:348`
