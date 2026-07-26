# Card.AddCounter

## Signature

```lua
Card.AddCounter(Card c, int countertype, int count, [bool singly]) -> bool
```

## Description

Attempts to add count counters of countertype to c and returns whether the core accepted the addition.
The card must be affected by the resolving reason effect. The current reason player is used as the player adding the counters. When singly is true, counter-limit checks allow a partial addition up to the remaining limit.

## Parameters

- `c` `Card`
- `countertype` `int`
- `count` `int`
- `singly` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3631`
