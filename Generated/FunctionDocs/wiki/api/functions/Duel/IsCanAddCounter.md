# Duel.IsCanAddCounter

## Signature

```lua
Duel.IsCanAddCounter(int player, [int countertype], [int count], [Card c]) -> bool
```

## Description

检查玩家player能否向卡片c添加count个countertype类型的指示物，如果 player 不是 0或者1，则返回false

## Parameters

- `player` `int`
- `countertype` `int` optional
- `count` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4876`
