# Group.__sub

## Signature

```lua
Group.__sub(Group|Card left, Group|Card right) -> Group
```

## Description

Create a new card group, add all cards from target1 to this group, then remove all cards from target2, and return the resulting group; target1 and target2 remain unchanged

## Parameters

- `left` `Group|Card`
- `right` `Group|Card`

## Returns

- `Group` - A new group with cards from left that are not in right.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:937`
