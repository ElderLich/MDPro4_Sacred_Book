# Auxiliary.gfcheck

## Signature

```lua
Auxiliary.gfcheck(Group g, function f, any a1, any a2) -> bool
```

## Description

Checks a 2-card group against one filter in either order: one card must satisfy f(c,a1) and the other f(c,a2).

## Parameters

- `g` `Group`
- `f` `function`
- `a1` `any`
- `a2` `any`

## Returns

- `bool` - true if the two cards satisfy the filter in either order.

## Source

- `Utilities/utility.lua:1150`
