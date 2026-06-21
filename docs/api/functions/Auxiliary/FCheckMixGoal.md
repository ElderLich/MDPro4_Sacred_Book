# Auxiliary.FCheckMixGoal

## Signature

```lua
Auxiliary.FCheckMixGoal(Group sg, int tp, Card fc, bool sub, int chkfnf, ... function) -> bool
```

## Description

Final group check for mixed Fusion Materials. It validates mandatory Fusion Materials, Tune Magician restrictions, Extra Monster Zone availability, and additional Fusion goal hooks.

## Parameters

- `sg` `Group`
- `tp` `int`
- `fc` `Card`
- `sub` `bool`
- `chkfnf` `int`
- `...` `function`

## Returns

- `bool` - true if sg is a valid mixed Fusion Material group.

## Source

- `Utilities/procedure.lua:972`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
