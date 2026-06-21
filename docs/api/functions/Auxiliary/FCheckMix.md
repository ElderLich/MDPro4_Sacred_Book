# Auxiliary.FCheckMix

## Signature

```lua
Auxiliary.FCheckMix(Card c, Group mg, Group sg, Card fc, bool sub, function fun1, [function|nil fun2], ... function) -> bool
```

## Description

Recursive mixed Fusion Material checker. It tests one required material function at a time, tracks selected materials in sg, and consumes the substitute-material allowance when needed.

## Parameters

- `c` `Card`
- `mg` `Group`
- `sg` `Group`
- `fc` `Card`
- `sub` `bool`
- `fun1` `function`
- `fun2` `function|nil` optional
- `...` `function`

## Returns

- `bool` - true if the remaining mixed Fusion Material functions can be satisfied.

## Source

- `Utilities/procedure.lua:956`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
