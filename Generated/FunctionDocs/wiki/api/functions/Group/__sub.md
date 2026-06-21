# Group.__sub

## Signature

```lua
Group.__sub(Group|Card left, Group|Card right) -> Group
```

## Description

Difference operator for Group/Card operands. It removes the right operand's cards from the left operand.

## Parameters

- `left` `Group|Card`
- `right` `Group|Card`

## Returns

- `Group` - A new group with cards from left that are not in right.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:937`
