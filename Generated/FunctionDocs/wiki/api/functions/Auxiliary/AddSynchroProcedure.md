# Auxiliary.AddSynchroProcedure

## Signature

```lua
Auxiliary.AddSynchroProcedure(Card c, [function|nil f1], [function|nil f2], int minc, [int maxc]) -> void
```

## Description

Add a cohomology call to c
F1 to adjust the filter to meet the conditions, f2 to adjust to meet other than the filter conditions (usually aux.NonTuner)
Adjust monsters other than ct at least

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `minc` `int`
- `maxc` `int` optional

## Source

- `Utilities/procedure.lua:60`
