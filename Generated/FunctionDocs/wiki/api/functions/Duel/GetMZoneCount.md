# Duel.GetMZoneCount

## Signature

```lua
Duel.GetMZoneCount(int player, [Group|Card targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

返回玩家player场上[targets 离开后]可用的[区域 zone 里的]怪兽区数量
##第三个第四个额外参数与凯撒斗技场等限制格子的效果有关

## Parameters

- `player` `int`
- `targets` `Group|Card` optional
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`
- `int` - zone

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4936`
