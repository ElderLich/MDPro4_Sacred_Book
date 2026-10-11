# Card.IsCardType

## Signature

```lua
Card.IsCardType(Card c, int type) -> bool
```

## Description

Returns true if at least one bit in type is present in c:GetCardType(). Use IsAllCardTypes when every requested bit must match.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3533`
