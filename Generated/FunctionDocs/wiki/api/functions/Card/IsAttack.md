# Card.IsAttack

## Signature

```lua
Card.IsAttack(Card c, int atk1, [int atk2], [... int]) -> bool
```

## Description

Check if card c's ATK is atk1 \[, or atk2...\], returns false if c is not a monster card or not in LOCATION_MZONE

## Parameters

- `c` `Card`
- `atk1` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3490`
