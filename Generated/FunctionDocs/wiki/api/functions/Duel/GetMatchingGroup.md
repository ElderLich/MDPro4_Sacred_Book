# Duel.GetMatchingGroup

## Signature

```lua
Duel.GetMatchingGroup([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，返回以player来看的指定位置满足过滤条件f并且不等于ex的卡
s代表以player来看的自己的位置，o代表以player来看的对方的位置
第6个参数开始为额外参数

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4969`
