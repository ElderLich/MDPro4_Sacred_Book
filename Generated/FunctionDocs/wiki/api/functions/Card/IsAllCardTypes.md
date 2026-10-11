# Card.IsAllCardTypes

## Signature

```lua
Card.IsAllCardTypes(Card c, int type) -> bool
```

## Description

Returns true if every bit in type is present in c:GetCardType(). A zero mask matches.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3534`
