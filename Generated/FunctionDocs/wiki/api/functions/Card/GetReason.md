# Card.GetReason

## Signature

```lua
Card.GetReason(Card c) -> int
```

## Description

Returns c's current reason bitmask/value.
This is the reason recorded in c's current state, such as REASON_EFFECT, REASON_COST, or REASON_BATTLE; it is not limited to position changes.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3462`
