# Auxiliary.CheckGroupRecursive

## Signature

```lua
Auxiliary.CheckGroupRecursive(Card c, Group sg, Group g, function f, any min, any max, any ext_params) -> void
```

## Description

Internal recursive helper for Group.CheckSubGroup. It tries adding c to sg, respects Auxiliary.GCheckAdditional, and searches for a subgroup between min and max that satisfies f.

## Parameters

- `c` `Card`
- `sg` `Group`
- `g` `Group`
- `f` `function`
- `min` `any`
- `max` `any`
- `ext_params` `any`

## Source

- `Utilities/utility.lua:1196`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
