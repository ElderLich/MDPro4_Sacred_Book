# Card.IsCanAddCounter

## Signature

```lua
Card.IsCanAddCounter(Card c, int countertype, int count, [int singly], [int location]) -> bool
```

## Description

检查c是否可以[逐个(singly=true)在 location 区域]放置count个countertype类型的指示物

## Parameters

- `c` `Card`
- `countertype` `int`
- `count` `int`
- `singly` `int` optional - default: false
- `location` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3635`
