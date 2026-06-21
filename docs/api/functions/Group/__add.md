# Group.__add

## Signature

```lua
Group.__add(Group|Card left, Group|Card right) -> Group
```

## Description

Create a new card group, add all cards from target1 and target2 to this group, and return it; if there are duplicate cards, they are added only once; target1 and target2 remain unchanged

## Parameters

- `left` `Group|Card`
- `right` `Group|Card`

## Returns

- `Group` - A new group containing cards from both operands.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:935`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
