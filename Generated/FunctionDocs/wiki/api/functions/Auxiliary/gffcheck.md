# Auxiliary.gffcheck

## Signature

```lua
Auxiliary.gffcheck(Group g, function f1, any a1, function f2, any a2) -> bool
```

## Description

Checks a 2-card group against two filters in either order: one card must satisfy f1(c,a1) and the other f2(c,a2).

## Parameters

- `g` `Group`
- `f1` `function`
- `a1` `any`
- `f2` `function`
- `a2` `any`

## Returns

- `bool` - true if the two cards satisfy both filters in either order.

## Source

- `Utilities/utility.lua:1160`
