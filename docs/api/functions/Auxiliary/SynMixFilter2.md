# Auxiliary.SynMixFilter2

## Signature

```lua
Auxiliary.SynMixFilter2(Card c, function|nil f2, function|nil f3, function|nil f4, int minc, int maxc, Card syncard, Group mg, Card|nil smat, Card c1, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

Second fixed-material candidate filter for mixed Synchro procedures, or the transition into the variable material slot when no second filter is required.

## Parameters

- `c` `Card`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `mg` `Group`
- `smat` `Card|nil`
- `c1` `Card`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if c can fill the second fixed material slot or advance selection.

## Source

- `Utilities/procedure.lua:325`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
