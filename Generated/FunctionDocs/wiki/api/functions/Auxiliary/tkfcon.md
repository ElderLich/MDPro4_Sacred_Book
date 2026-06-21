# Auxiliary.tkfcon

## Signature

```lua
Auxiliary.tkfcon([Effect|nil e], [int|nil tp]) -> bool
```

## Description

Returns true if tp controls a Token on the field. If tp is omitted and e is provided, tp defaults to e's handler player.

## Parameters

- `e` `Effect|nil` optional
- `tp` `int|nil` optional

## Returns

- `bool` - true if tp controls a Token on the field.

## Source

- `Utilities/utility.lua:874`
