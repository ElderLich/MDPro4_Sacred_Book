# Group.IsExists

## Signature

```lua
Group.IsExists(Group g, function f, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

过滤函数，检查g中是否存在至少count张满足筛选条件f并且不等于ex的卡
从第5个参数开始为额外参数

## Parameters

- `g` `Group`
- `f` `function`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:919`
