# Group.SelectWithSumEqual

## Signature

```lua
Group.SelectWithSumEqual(Group g, int player, function f, int sum, int min, int max, ... any) -> Group
```

## Description

让玩家player从g中选取一个数量为min-max的子集使子集的特定函数的和等于sum，从第7个参数开始为额外参数

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `sum` `int`
- `min` `int`
- `max` `int`
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:921`
