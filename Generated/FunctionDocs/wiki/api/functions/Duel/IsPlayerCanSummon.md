# Duel.IsPlayerCanSummon

## Signature

```lua
Duel.IsPlayerCanSummon(int player, [int sumtype], [Card c]) -> bool
```

## Description

检查玩家player是否可以通常召唤[c，以sumtype方式]
如果需要可选参数，则必须全部使用
仅当玩家收到“不能上级召唤”等效果的影响时返回false

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5047`
