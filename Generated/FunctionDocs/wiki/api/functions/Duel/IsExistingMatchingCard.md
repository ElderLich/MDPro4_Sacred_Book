# Duel.IsExistingMatchingCard

## Signature

```lua
Duel.IsExistingMatchingCard([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

过滤函数，检查以player来看的指定位置是否存在至少count张满足过滤条件f并且不等于ex的卡
s代表以player来看的自己的位置，o代表以player来看的对方的位置
第7个参数开始为额外参数

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4972`
