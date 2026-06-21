# Duel.IsEnvironment

## Signature

```lua
Duel.IsEnvironment(int code, [int player], [int loc]) -> bool
```

## Description

检查场地卡号是否是code [，来源玩家是否是 player][，生效区域是否在 loc 内]
场地卡号指当前生效的场地卡的卡号，或者海神的巫女把场地变化效果的值
来源玩家指当前生效的场地卡的控制者，或者海神的巫女等卡的控制者

## Parameters

- `code` `int`
- `player` `int` optional - default: PLAYER_ALL
- `loc` `int` optional - default: LOCATION_ONFIELD

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4898`
