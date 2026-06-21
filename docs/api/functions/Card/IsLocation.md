# Card.IsLocation

## Signature

```lua
Card.IsLocation(Card c, int location) -> bool
```

## Description

Check if c is the current location
Note: When the monster summon, reverse call, call special summon before the success,
And location = LOCATION_MZONE, this function returns false

## Parameters

- `c` `Card`
- `location` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3610`
