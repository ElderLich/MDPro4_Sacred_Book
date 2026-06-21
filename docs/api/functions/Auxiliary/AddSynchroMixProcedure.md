# Auxiliary.AddSynchroMixProcedure

## Signature

```lua
Auxiliary.AddSynchroMixProcedure(Card c, [function|nil f1], [function|nil f2], [function|nil f3], [function|nil f4], int minc, int maxc, [function gc]) -> void
```

## Description

Add a Synchro Summon procedure for c
f1, f2, f3 are filter conditions satisfied by 1 card each, f4 is a filter condition satisfied by minc \[to maxc\] cards
At least one of f1, f2, f3, f4 must be a Tuner condition
If f2 and f3 are nil, equivalent to aux.AddSynchroProcedure(c, f1, f4, minc\[, maxc\])

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `f3` `function|nil` optional
- `f4` `function|nil` optional
- `minc` `int`
- `maxc` `int`
- `gc` `function` optional

## Source

- `Utilities/procedure.lua:135`
