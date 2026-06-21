# Card.RemoveCounter

## Signature

```lua
Card.RemoveCounter(Card c, int player, int countertype, int count, int reason) -> void
```

## Description

让玩家player以原因reason移除c上的count个countertype类型的指示物， countertype=0 则清除c的所有指示物

## Parameters

- `c` `Card`
- `player` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3629`
