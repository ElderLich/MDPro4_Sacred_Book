# Auxiliary.AddSynchroProcedure

## Signature

```lua
Auxiliary.AddSynchroProcedure(Card c, [function|nil f1], [function|nil f2], int minc, [int maxc]) -> void
```

## Description

Registers the standard Synchro Summon procedure for c.
f1 filters the Tuner material, f2 filters non-Tuner materials, and minc/maxc set the number of non-Tuner materials required.

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `minc` `int`
- `maxc` `int` optional

## Source

- `Utilities/procedure.lua:60`
