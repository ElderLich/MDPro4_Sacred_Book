# Duel.GetControl

## Signature

```lua
Duel.GetControl(Card|Group targets, int player, [int reset_phase], [int reset_count], [int zone]) -> bool
```

## Description

让玩家 player [直到 reset_count 次 reset_phase 时][在区域 zone]
得到 targets 的控制权，返回值表示是否成功

## Parameters

- `targets` `Card|Group`
- `player` `int`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4906`
