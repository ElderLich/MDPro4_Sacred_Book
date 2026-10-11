# Auxiliary.damcon1

## Signature

```lua
Auxiliary.damcon1(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

Condition helper for effects that would make player tp take effect damage.
It checks the operation info for damage to tp, or recovery to tp that is reversed into damage, and respects EFFECT_REVERSE_DAMAGE, EFFECT_REVERSE_RECOVER, and EFFECT_NO_EFFECT_DAMAGE.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:882`
