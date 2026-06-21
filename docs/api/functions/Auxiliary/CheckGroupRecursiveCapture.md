# Auxiliary.CheckGroupRecursiveCapture

## Signature

```lua
Auxiliary.CheckGroupRecursiveCapture(Card c, Group sg, Group g, function f, any min, any max, any ext_params) -> void
```

## Description

Internal recursive helper for Group.SelectSubGroup. It searches like Auxiliary.CheckGroupRecursive and stores one valid subgroup in Auxiliary.SubGroupCaptured.

## Parameters

- `c` `Card`
- `sg` `Group`
- `g` `Group`
- `f` `function`
- `min` `any`
- `max` `any`
- `ext_params` `any`

## Source

- `Utilities/utility.lua:1207`
