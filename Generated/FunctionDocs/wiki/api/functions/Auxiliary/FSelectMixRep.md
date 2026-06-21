# Auxiliary.FSelectMixRep

## Signature

```lua
Auxiliary.FSelectMixRep(Card c, int tp, Group mg, Group sg, Card fc, bool sub, int chkfnf, ... function) -> bool
```

## Description

Candidate test for mixed-repeat Fusion selection. It temporarily adds c to sg and returns whether the selection is already valid or can still be completed.

## Parameters

- `c` `Card`
- `tp` `int`
- `mg` `Group`
- `sg` `Group`
- `fc` `Card`
- `sub` `bool`
- `chkfnf` `int`
- `...` `function`

## Returns

- `bool` - true if adding c can complete or continue the selection.

## Source

- `Utilities/procedure.lua:1188`
