# Card.IsLocation

## Signature

```lua
Card.IsLocation(Card c, int location) -> bool
```

## Description

Checks whether c is currently in location.
Cards treated as not being on the field return false for field locations, including during a Summon before it successfully reaches the Monster Zone.

## Parameters

- `c` `Card`
- `location` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3665`
