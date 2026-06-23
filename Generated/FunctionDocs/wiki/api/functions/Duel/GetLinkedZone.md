# Duel.GetLinkedZone

## Signature

```lua
Duel.GetLinkedZone(int player) -> int
```

## Description

Returns the zone bitmask currently pointed to by Link Markers from player's perspective.
Use bit operations to test individual zones. For one Link Monster's markers, use Card.GetLinkedZone.

## Parameters

- `player` `int` - Perspective player for the returned zone mask.

## Returns

- `int` - Linked-zone bitmask from player's perspective.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4942`
