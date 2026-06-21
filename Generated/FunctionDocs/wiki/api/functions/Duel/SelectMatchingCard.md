# Duel.SelectMatchingCard

## Signature

```lua
Duel.SelectMatchingCard(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，让玩家sel_player选择以player来看的指定位置满足过滤条件f并且不等于ex的min-max张卡
s代表以player来看的自己的位置，o代表以player来看的对方的位置
第9个参数开始为额外参数

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4973`
