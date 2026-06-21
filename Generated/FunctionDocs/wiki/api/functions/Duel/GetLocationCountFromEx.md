# Duel.GetLocationCountFromEx

## Signature

```lua
Duel.GetLocationCountFromEx(int player, [int reason_player], [Group|Card|nil targets], [Card|int sc], [int zone]) -> int
```

## Description

返回玩家player场上[假如因玩家 reason_player 的原因让 targets 离场后，把卡片 sc 在 zone 区域特殊召唤]可用的 能让额外卡组的怪兽 出场的空格数

## Parameters

- `player` `int`
- `reason_player` `int` optional - default: player
- `targets` `Group|Card|nil` optional
- `sc` `Card|int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4938`
