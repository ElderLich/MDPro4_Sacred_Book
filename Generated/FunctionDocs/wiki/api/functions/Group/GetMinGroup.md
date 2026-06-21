# Group.GetMinGroup

## Signature

```lua
Group.GetMinGroup(Group g, function f, ... any) -> Group,int
```

## Description

f为返回一个interger值的函数，从g中筛选出具有最小的f的值的卡
第2个返回值为这个最小值，从第3个参数开始为额外参数
要使用第2个返回值注意检查g非空

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `Group`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:924`
