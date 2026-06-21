# Group.__band

## Signature

```lua
Group.__band(Group|Card left, Group|Card right) -> Group
```

## Description

Create a new card group, add all cards that are identical in target1 and target2 (i.e., cards present in both) to this group, and return it; target1 and target2 remain unchanged

## Parameters

- `left` `Group|Card`
- `right` `Group|Card`

## Returns

- `Group` - A new group containing cards present in both operands.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:938`
