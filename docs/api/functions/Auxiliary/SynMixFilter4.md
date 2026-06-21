# Auxiliary.SynMixFilter4

## Signature

```lua
Auxiliary.SynMixFilter4(Card c, function|nil f4, int minc, int maxc, Card syncard, Group mg1, Card|nil smat, Card c1, Card|nil c2, Card|nil c3, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

Variable-slot candidate filter for mixed Synchro procedures; after adding c it checks whether the remaining material pool can complete the summon.

## Parameters

- `c` `Card`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `mg1` `Group`
- `smat` `Card|nil`
- `c1` `Card`
- `c2` `Card|nil`
- `c3` `Card|nil`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if c can fill the variable material slot.

## Source

- `Utilities/procedure.lua:343`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
