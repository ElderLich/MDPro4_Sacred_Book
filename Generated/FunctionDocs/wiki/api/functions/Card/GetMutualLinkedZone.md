# Card.GetMutualLinkedZone

## Signature

```lua
Card.GetMutualLinkedZone(Card c, [int player]) -> int
```

## Description

Returns the zone mask of c's mutually linked zones, swapped to player viewpoint when a player argument opposite c's controller is supplied.

## Parameters

- `c` `Card`
- `player` `int` optional - default: c:GetControler()

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3427`
