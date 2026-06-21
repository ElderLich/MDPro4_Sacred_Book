# Duel.SelectReleaseGroupEx

## Signature

```lua
Duel.SelectReleaseGroupEx(int player, [function|nil f], int min, int max, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，让玩家player从场上选择min-max张满足过滤条件f并且不等于ex的能以原因reason解放的卡，use_hand则包括手卡
第6个参数开始为额外参数

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4979`
