# Card.IsPreviousCardTypeOnField

## Signature

```lua
Card.IsPreviousCardTypeOnField(Card c, int type) -> bool
```

## Description

Returns true if at least one requested TYPE_* bit is present in the previous on-field card-type snapshot.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3535`
