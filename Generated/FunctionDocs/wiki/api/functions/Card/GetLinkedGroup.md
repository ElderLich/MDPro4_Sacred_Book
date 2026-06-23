# Card.GetLinkedGroup

## Signature

```lua
Card.GetLinkedGroup(Card c) -> Group
```

## Description

Returns the cards currently occupying zones linked by c.
Use this when an effect cares about the actual cards in zones pointed to by c's Link Markers.

## Parameters

- `c` `Card`

## Returns

- `Group` - Cards currently in c's linked zones.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3419`
