# Card.IsCanBePlacedOnField

## Signature

```lua
Card.IsCanBePlacedOnField(Card c, [int toplayer], [int tolocation]) -> bool
```

## Description

Checks whether c can be placed onto the target player's field.
Returns false if the target player is invalid, c is forbidden, or placing c there would violate uniqueness checks.

## Parameters

- `c` `Card`
- `toplayer` `int` optional - Target player. Defaults to the current reason player.
- `tolocation` `int` optional - Target location. Defaults to LOCATION_SZONE.

## Returns

- `bool` - true if c can be placed on that player's field.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3638`
