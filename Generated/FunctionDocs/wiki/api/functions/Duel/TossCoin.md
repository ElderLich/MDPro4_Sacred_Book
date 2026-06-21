# Duel.TossCoin

## Signature

```lua
Duel.TossCoin(int player, int count) -> ...
```

## Description

让玩家player投count(<=20)次硬币，返回值为count个结果，0或者1, 正面是 1，反面是0
若count=-1，投硬币直到出现反面，返回值为投掷次数

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5036`
