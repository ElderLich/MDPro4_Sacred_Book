# Auxiliary.SynMixCheck

## Signature

```lua
Auxiliary.SynMixCheck(Group mg, Group sg1, int minc, int maxc, Card syncard, Group mg1, Card|nil smat, function|nil gc, bool mgchk, bool goalchk) -> bool
```

## Description

Checks whether the remaining mixed Synchro Material pool can complete the selected fixed-material group within the variable material count range.

## Parameters

- `mg` `Group`
- `sg1` `Group`
- `minc` `int`
- `maxc` `int`
- `syncard` `Card`
- `mg1` `Group`
- `smat` `Card|nil`
- `gc` `function|nil`
- `mgchk` `bool`
- `goalchk` `bool`

## Returns

- `bool` - true if the mixed Synchro Material selection can be completed.

## Source

- `Utilities/procedure.lua:356`
