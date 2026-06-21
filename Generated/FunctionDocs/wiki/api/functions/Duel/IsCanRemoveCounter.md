# Duel.IsCanRemoveCounter

## Signature

```lua
Duel.IsCanRemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

检查玩家player以reason为原因是否能移除场上的countertype类型的count个指示物
s表示对player来说的己方的可移除指示物的位置，o表示对player来说的对方的可移除指示物的位置

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4878`
