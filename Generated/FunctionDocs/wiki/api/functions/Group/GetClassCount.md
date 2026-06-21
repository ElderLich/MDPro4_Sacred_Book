# Group.GetClassCount

## Signature

```lua
Group.GetClassCount(Group g, function f, ... any) -> int
```

## Description

计算g中所有卡的种类数量，f为分类的依据，返回相同的值视为同一种类，从第3个参数开始为额外参数
比如 g:GetClassCount(Card.GetCode()) 就是计算g中卡名不同的卡的数量

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:927`
