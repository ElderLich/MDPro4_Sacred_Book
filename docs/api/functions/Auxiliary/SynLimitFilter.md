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
