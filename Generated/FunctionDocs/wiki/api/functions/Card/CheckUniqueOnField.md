# Card.CheckUniqueOnField

## Signature

```lua
Card.CheckUniqueOnField(Card c, int check_player, [int check_location], [Card|nil icard]) -> bool
```

## Description

Checks whether c can coexist on check_player's field under the current unique-on-field rules.
check_location defaults to LOCATION_ONFIELD and is masked to on-field locations. icard can be supplied as an ignored card when testing a pending move.

## Parameters

- `c` `Card` - Card being tested against unique-on-field restrictions.
- `check_player` `int` - Player whose field is checked for a uniqueness conflict.
- `check_location` `int` optional - On-field location mask to check; default: LOCATION_ONFIELD. The core masks this value to LOCATION_ONFIELD.
- `icard` `Card|nil` optional - Optional card ignored during the check, useful when testing a pending replacement or move.

## Returns

- `bool` - True if c can coexist under the unique-on-field rules for the requested player and location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3658`
