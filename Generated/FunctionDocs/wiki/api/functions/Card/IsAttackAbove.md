# Card.IsAttackAbove

## Signature

```lua
Card.IsAttackAbove(Card c, int atk) -> bool
```

## Description

Checks whether c is a monster or currently treated as one, and whether its current ATK is at least atk.
Unlike Card.IsAttackBelow, this core does not add a separate guard for unknown ATK before comparing.

## Parameters

- `c` `Card` - Card whose current ATK is checked.
- `atk` `int` - Minimum ATK value accepted by the check.

## Returns

- `bool` - True if c is a monster or treated as one and its current ATK is at least atk.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3674`
