# Duel.SelectTunerMaterial

## Signature

```lua
Duel.SelectTunerMaterial(int player, Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> Group|nil
```

## Description

Lets player select Synchro Materials for scard using the fixed tuner, optional filters, count limits, and optional material group.

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `Group|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4995`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
