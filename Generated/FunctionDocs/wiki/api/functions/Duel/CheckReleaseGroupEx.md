# Duel.CheckReleaseGroupEx

## Signature

```lua
Duel.CheckReleaseGroupEx(int player, [function|nil f], int count, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> bool
```

## Description

检查玩家player场上是否存在至少count张满足过滤条件f并且不等于ex的能以原因reason解放的卡，use_hand则包括手卡
第5个参数开始为额外参数

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `count` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4978`
