# Card.CheckUniqueOnField

## Signature

```lua
Card.CheckUniqueOnField(Card c, int check_player, [int check_location], [Card|nil icard]) -> bool
```

## Description

Checks whether c can coexist on check_player's field under the current unique-on-field rules.
check_location defaults to LOCATION_ONFIELD and is masked to on-field locations. icard can be supplied as an ignored card when testing a pending move.

## Parameters

- `c` `Card`
- `check_player` `int`
- `check_location` `int` optional - default: LOCATION_ONFIELD
- `icard` `Card|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3658`
