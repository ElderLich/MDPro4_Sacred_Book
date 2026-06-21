# Auxiliary.SynLimitFilter

## Signature

```lua
Auxiliary.SynLimitFilter(Card c, function|nil f, Effect e, Card syncard) -> bool
```

## Description

Returns true when limiter function f exists and rejects c for syncard.

## Parameters

- `c` `Card`
- `f` `function|nil`
- `e` `Effect`
- `syncard` `Card`

## Returns

- `bool` - true if f rejects c.

## Source

- `Utilities/procedure.lua:158`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
