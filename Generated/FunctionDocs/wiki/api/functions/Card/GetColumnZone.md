# Card.GetColumnZone

## Signature

```lua
Card.GetColumnZone(Card c, int loc, [int player]) -> int
```

## Description

Returns the zone bitmask for columns overlapping c within loc.
When player is supplied as the opposing perspective, the core swaps the player/opponent halves of the mask.

## Parameters

- `c` `Card`
- `loc` `int`
- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3480`
