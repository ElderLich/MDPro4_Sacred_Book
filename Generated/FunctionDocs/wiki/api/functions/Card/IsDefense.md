# Card.IsDefense

## Signature

```lua
Card.IsDefense(Card c, int def, [int atk2], [... int]) -> bool
```

## Description

Check if c's DEF is def1 [, or def2...]; returns false if c is not a monster card or not in LOCATION_MZONE

## Parameters

- `c` `Card`
- `def` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3491`
