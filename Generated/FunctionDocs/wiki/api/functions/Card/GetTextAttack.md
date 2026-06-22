# Card.GetTextAttack

## Signature

```lua
Card.GetTextAttack(Card c) -> int
```

## Description

Returns the ATK value recorded in c's card data.
This is the printed/database value, not the current ATK. Unlike Card.GetAttack, the binding does not clamp unknown ATK to 0, except cards marked STATUS_NO_LEVEL return 0.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3442`
