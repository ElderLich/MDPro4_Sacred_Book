# Card.IsCanRemoveCounter

## Signature

```lua
Card.IsCanRemoveCounter(Card c, int player, int countertype, int count, int reason) -> bool|nil
```

## Description

Checks whether player can remove count counters of countertype from c for reason.

## Parameters

- `c` `Card`
- `player` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool|nil` - nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3691`
