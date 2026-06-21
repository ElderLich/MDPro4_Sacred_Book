# Auxiliary.SynMixHandFilter

## Signature

```lua
Auxiliary.SynMixHandFilter(Card c, int tp, Card syncard) -> bool
```

## Description

Returns true for a hand material that is being used because another card enables it, rather than by its own extra Synchro Material effect.

## Parameters

- `c` `Card`
- `tp` `int`
- `syncard` `Card`

## Returns

- `bool` - true if c is a hand material enabled by another card.

## Source

- `Utilities/procedure.lua:383`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
