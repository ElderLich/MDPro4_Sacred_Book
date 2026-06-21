# Group.__bxor

## Signature

```lua
Group.__bxor(Group|Card left, Group|Card right) -> Group
```

## Description

Create a new card group, add all cards that are different between target1 and target2 (i.e., cards present in only target1 or target2) to this group, and return it; target1 and target2 remain unchanged

## Parameters

- `left` `Group|Card`
- `right` `Group|Card`

## Returns

- `Group` - A new group containing cards present in exactly one operand.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:939`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
