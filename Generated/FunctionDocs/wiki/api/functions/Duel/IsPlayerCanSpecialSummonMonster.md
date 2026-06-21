# Duel.IsPlayerCanSpecialSummonMonster

## Signature

```lua
Duel.IsPlayerCanSpecialSummonMonster(int player, int code, [int|nil setcode], [int|nil type], [int|nil atk], [int|nil def], [int|nil level], [int|nil race], [int|nil attribute], [int pos], [int target_player], [int sumtype], [int zone]) -> bool
```

## Description

检查玩家player是否可以[以sumtype 方式][以 pos 表示形式]特殊召唤 给定参数的怪兽到target_player场上
此函数通常用于判定是否可以特招token和陷阱怪兽

## Parameters

- `player` `int`
- `code` `int`
- `setcode` `int|nil` optional
- `type` `int|nil` optional
- `atk` `int|nil` optional
- `def` `int|nil` optional
- `level` `int|nil` optional
- `race` `int|nil` optional
- `attribute` `int|nil` optional
- `pos` `int` optional - default: POS_FACEUP
- `target_player` `int` optional - default: player
- `sumtype` `int` optional - default: 0
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5052`
