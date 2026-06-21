# Group.Filter

## Signature

```lua
Group.Filter(Group g, function f, [Card|Group|nil ex], ... any) -> Group
```

## Description

过滤函数，从g中筛选满足筛选条件f并且不等于ex的卡
从第4个参数开始为额外参数

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:912`
