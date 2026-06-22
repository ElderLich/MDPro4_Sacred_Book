# Auxiliary.AddSynchroProcedure2

## Signature

```lua
Auxiliary.AddSynchroProcedure2(Card c, [function|nil f1], [function|nil f2]) -> void
```

## Description

Backward-compatible helper for a Synchro Monster that uses exactly 1 Tuner and 1 non-Tuner material.
It calls Auxiliary.AddSynchroProcedure(c, f1, f2, 1, 1).

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional

## Source

- `Utilities/procedure.lua:123`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
