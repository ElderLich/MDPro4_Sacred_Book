# Duel.RemoveCounter

## Signature

```lua
Duel.RemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

让玩家player以reason为原因移除场上存在的countertype类型的count个指示物，返回值表示是否成功
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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4877`
