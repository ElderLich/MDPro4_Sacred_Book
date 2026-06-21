# Group.CheckWithSumEqual

## Signature

```lua
Group.CheckWithSumEqual(Group g, function f, int sum, int min, int max, ... any) -> bool
```

## Description

子集求和判定函数，f为返回一个interger值的函数
检查g中是否存在一个数量为min-max的子集满足以f对子集的每一个元素求值的和等于sum，从第6个参数开始为额外参数
比如：g:CheckWithSumEqual(Card.GetSynchroLevel,7,2,99)
检查g中是否存在一个子集满足子集的同调用等级之和等于7

## Parameters

- `g` `Group`
- `f` `function`
- `sum` `int`
- `min` `int` - default: 0
- `max` `int`
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:920`
