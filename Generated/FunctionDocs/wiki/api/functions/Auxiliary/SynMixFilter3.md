# Auxiliary.SynMixFilter3

## Signature

```lua
Auxiliary.SynMixFilter3(Card c, function|nil f3, function|nil f4, int minc, int maxc, Card syncard, Group mg, Card|nil smat, Card c1, Card c2, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

Third fixed-material candidate filter for mixed Synchro procedures, or the transition into the variable material slot when no third filter is required.

## Parameters

- `c` `Card`
- `f3` `function|nil`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `mg` `Group`
- `smat` `Card|nil`
- `c1` `Card`
- `c2` `Card`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if c can fill the third fixed material slot or advance selection.

## Source

- `Utilities/procedure.lua:334`
