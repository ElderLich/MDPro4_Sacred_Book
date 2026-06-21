# Duel.DiscardHand

## Signature

```lua
Duel.DiscardHand(int player, [function|nil f], int min, int max, int reason, [Card|Group|nil ex], ... any) -> int
```

## Description

过滤函数让玩家player选择并以reason原因丢弃满足筛选条件f兵不等于ex的min-max张手卡
第7个参数开始为额外参数

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4911`
