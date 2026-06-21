# Card.GetColumnZone

## Signature

```lua
Card.GetColumnZone(Card c, int location, [int left], [int right], [int player]) -> int
```

## Description

Return the zones [from player's perspective] within the location range that are in the same column as card c [including left columns and right columns], location values are LOCATION_MZONE, LOCATION_SZONE, LOCATION_ONFIELD

## Parameters

- `c` `Card`
- `location` `int`
- `left` `int` optional
- `right` `int` optional
- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3429`
