# Group.SelectWithSumGreater

## Signature

```lua
Group.SelectWithSumGreater(Group g, int player, function f, int sum, ... any) -> Group
```

## Description

让玩家player从g中选取一个子集使子集的特定函数f的和大于等于sum，从第5个参数开始为额外参数

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `sum` `int`
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:923`
