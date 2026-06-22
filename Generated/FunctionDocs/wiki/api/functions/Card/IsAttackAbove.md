# Card.IsAttackAbove

## Signature

```lua
Card.IsAttackAbove(Card c, int atk) -> bool
```

## Description

Checks whether c is a monster or currently treated as one, and whether its current ATK is at least atk.
Unlike Card.IsAttackBelow, this core does not add a separate guard for unknown ATK before comparing.

## Parameters

- `c` `Card`
- `atk` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3619`
