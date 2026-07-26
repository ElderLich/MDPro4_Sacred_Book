# Card.GetCounter

## Signature

```lua
Card.GetCounter(Card c, int countertype) -> int
```

## Description

Returns counters on c for countertype.
When countertype is 0, this core returns the number of different counter types currently present on c, not the total number of all counters.

## Parameters

- `c` `Card`
- `countertype` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3633`
