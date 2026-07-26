# Card.GetTurnID

## Signature

```lua
Card.GetTurnID(Card c) -> int
```

## Description

Returns c's stored turn ID.
The core updates this value when the card is added to a location, so scripts commonly compare it with Duel.GetTurnCount() for same-turn timing checks.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3479`
