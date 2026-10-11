# Card.IsDefense

## Signature

```lua
Card.IsDefense(Card c, int def1, [int def2], [... int]) -> bool
```

## Description

Checks whether c is not a Link Monster, is a monster or currently treated as one, and has current DEF equal to any supplied def value.
Nil def arguments are skipped. Unlike the old imported text, the binding does not explicitly require c to be in the Monster Zone.

## Parameters

- `c` `Card`
- `def1` `int`
- `def2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3546`
