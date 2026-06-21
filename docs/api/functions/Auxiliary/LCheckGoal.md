# Auxiliary.LCheckGoal

## Signature

```lua
Auxiliary.LCheckGoal(Group sg, int tp, Card lc, function|nil gf, Card|nil lmat) -> bool
```

## Description

Final Link Material group check. It verifies Link Rating total, Extra Monster Zone availability, optional group filter, extra-material compatibility, and required lmat inclusion.

## Parameters

- `sg` `Group`
- `tp` `int`
- `lc` `Card`
- `gf` `function|nil`
- `lmat` `Card|nil`

## Returns

- `bool` - true if sg is a valid Link Material group.

## Source

- `Utilities/procedure.lua:2185`
