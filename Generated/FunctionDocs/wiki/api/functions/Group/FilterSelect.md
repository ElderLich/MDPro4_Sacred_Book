# Group.FilterSelect

## Signature

```lua
Group.FilterSelect(Group g, int player, function f, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，让玩家player从g中选择 min-max 张满足筛选条件f并且不等于ex的卡
从第7个参数开始为额外参数

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:914`
