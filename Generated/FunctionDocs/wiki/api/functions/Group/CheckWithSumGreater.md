# Group.CheckWithSumGreater

## Signature

```lua
Group.CheckWithSumGreater(Group g, function f, int sum, ... any) -> bool
```

## Description

子集求和判定函数之二，f为返回一个interger值的函数
检查g中是否存在一个子集满足以f对子集的每一个元素求值的和刚好大于或者等于sum，从第4个参数开始为额外参数
比如：g:CheckWithSumGreater(Card.GetRitualLevel,8)
检查g中是否存在一个子集满足子集的仪式用等级之和大于等于8
注：判定必须是“刚好”大于或者等于
以等级为例，要使等级合计大于等于8，可以选择LV1+LV7而不可以选择LV1+LV4+LV4

## Parameters

- `g` `Group`
- `f` `function`
- `sum` `int`
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:922`
