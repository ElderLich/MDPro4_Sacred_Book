# Auxiliary.SynMixFilter1

## Signature

```lua
Auxiliary.SynMixFilter1(Card c, function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minc, int maxc, Card syncard, Group mg, Card|nil smat, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

First fixed-material candidate filter for mixed Synchro procedures.

## Parameters

- `c` `Card`
- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `mg` `Group`
- `smat` `Card|nil`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if c can fill the first fixed material slot.

## Source

- `Utilities/procedure.lua:322`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
