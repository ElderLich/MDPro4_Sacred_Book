# Duel.IsPlayerCanMSet

## Signature

```lua
Duel.IsPlayerCanMSet(int player, [int sumtype], [Card scard]) -> bool
```

## Description

检查玩家player是否可以[以sumtype的召唤方式将scard]盖放。
如果要加入后面的可选参数，则所有两个可选参数都必须加上。

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `scard` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5048`
