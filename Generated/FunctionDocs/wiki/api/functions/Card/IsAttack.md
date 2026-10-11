# Card.IsAttack

## Signature

```lua
Card.IsAttack(Card c, int atk1, [int atk2], [... int]) -> bool
```

## Description

Checks whether c is a monster or currently treated as one, and whether its current ATK equals any supplied atk value.
Nil atk arguments are skipped. Non-monsters that are not treated as monsters return false.

## Parameters

- `c` `Card`
- `atk1` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3545`
