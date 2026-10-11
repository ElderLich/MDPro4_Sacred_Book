# Duel.CheckSynchroMaterial

## Signature

```lua
Duel.CheckSynchroMaterial(Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> bool
```

## Description

Checks whether scard has a legal Synchro Material selection with optional tuner/non-tuner filters, count limits, required Synchro Material, and material group.

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `smat` `Card|nil` optional
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4994`

## Guided Examples

Learn how to use this function in context:

- [Synchro Procedure Guide](/learn/synchro-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
