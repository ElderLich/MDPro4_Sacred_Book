# Duel.IsPlayerCanSpecialSummon

## Signature

```lua
Duel.IsPlayerCanSpecialSummon(int player, [int sumtype], [int sumpos], [int target_player], [Card c]) -> bool
```

## Description

检查玩家player能否特殊召唤[c到target_player场上，以sumtype召唤方式，sumpos表示形式]
如果需要可选参数，则必须全部使用

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `sumpos` `int` optional
- `target_player` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5050`
