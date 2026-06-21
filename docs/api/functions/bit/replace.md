# bit.replace

## Signature

```lua
bit.replace(int r, int v, int field, [int width]) -> int
```

## Description

Returns r with width bits starting at field replaced by the low width bits of v. width defaults to 1.

## Parameters

- `r` `int`
- `v` `int`
- `field` `int`
- `width` `int` optional

## Returns

- `int` - r with the selected bit field replaced.

## Source

- `Utilities/utility.lua:45`
