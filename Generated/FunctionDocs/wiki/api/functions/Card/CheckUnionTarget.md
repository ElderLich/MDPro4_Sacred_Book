# Card.CheckUnionTarget

## Signature

```lua
Card.CheckUnionTarget(Card c, Card target) -> bool
```

## Description

Checks whether target is a valid Union equip target for c under EFFECT_UNION_LIMIT.
The core also enforces new/old Union count compatibility between c and target.

## Parameters

- `c` `Card`
- `target` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3577`
