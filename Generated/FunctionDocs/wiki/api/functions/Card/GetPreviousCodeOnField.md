# Card.GetPreviousCodeOnField

## Signature

```lua
Card.GetPreviousCodeOnField(Card c) -> int,int|nil
```

## Description

Returns the card code recorded for c's previous on-field state.
If the previous state had a second code, that code is returned as a second value.

## Parameters

- `c` `Card`

## Returns

- `int`
- `int|nil` - Second previous code, when present.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3449`
