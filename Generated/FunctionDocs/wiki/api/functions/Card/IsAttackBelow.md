# Card.IsAttackBelow

## Signature

```lua
Card.IsAttackBelow(Card c, int atk) -> bool
```

## Description

Checks whether c is a monster, or treated as one, whose current ATK is known and less than or equal to atk.
Cards with unknown ATK return false because the core requires the current ATK to be at least 0.

## Parameters

- `c` `Card` - Card whose current ATK is checked.
- `atk` `int` - Maximum ATK value accepted by the check.

## Returns

- `bool` - True if c is a monster or treated as one, has known ATK, and that ATK is at most atk.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3621`
