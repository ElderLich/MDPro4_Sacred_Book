# Duel.SelectReleaseGroup

## Signature

```lua
Duel.SelectReleaseGroup(int sel_player, [function|nil f], int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，让玩家sel_player从场上选择min-max张不等于ex的满足条件f的能以原因REASON_COST解放的卡
第6个参数开始为额外参数

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4977`
