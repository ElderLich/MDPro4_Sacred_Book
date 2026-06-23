# Card.GetSequence

## Signature

```lua
Card.GetSequence(Card c) -> int
```

## Description

Returns c's sequence within its current location.
For field zones, Main Monster Zones and Spell & Trap Zones use 0-4 from left to right, the Field Zone uses 5, and Pendulum Zones use 6-7.
For other locations, sequence is the card's position in that location, starting from 0.

## Parameters

- `c` `Card` - Card whose current sequence is returned.

## Returns

- `int` - Sequence in c's current location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3468`
