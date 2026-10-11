# Auxiliary.CheckGroupRecursiveEach

## Signature

```lua
Auxiliary.CheckGroupRecursiveEach(Card c, Group sg, Group g, function f, any checks, any ext_params) -> void
```

## Description

Internal recursive helper for Group.CheckSubGroupEach and Group.SelectSubGroupEach. Each selected card must satisfy the filter at the matching position in checks before the final group is tested by f.

## Parameters

- `c` `Card`
- `sg` `Group`
- `g` `Group`
- `f` `function`
- `checks` `any`
- `ext_params` `any`

## Source

- `Utilities/utility.lua:1317`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
