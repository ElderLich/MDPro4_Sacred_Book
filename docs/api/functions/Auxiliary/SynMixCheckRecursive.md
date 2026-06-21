# Auxiliary.SynMixCheckRecursive

## Signature

```lua
Auxiliary.SynMixCheckRecursive(Card c, int tp, Group sg, Group mg, int ct, int minc, int maxc, Card syncard, Group sg1, Card|nil smat, function|nil gc, bool mgchk, bool goalchk, bool fulltraversal) -> bool
```

## Description

Recursive mixed Synchro Material search helper. It temporarily adds c, checks the goal, and continues through mg while the branch remains possible.

## Parameters

- `c` `Card`
- `tp` `int`
- `sg` `Group`
- `mg` `Group`
- `ct` `int`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `sg1` `Group`
- `smat` `Card|nil`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`
- `fulltraversal` `bool`

## Returns

- `bool` - true if the recursive search can reach a valid group.

## Source

- `Utilities/procedure.lua:364`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
