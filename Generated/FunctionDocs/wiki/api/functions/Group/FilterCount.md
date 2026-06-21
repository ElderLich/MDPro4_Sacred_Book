# Group.FilterCount

## Signature

```lua
Group.FilterCount(Group g, function f, [Card|Group|nil ex], ... any) -> int
```

## Description

过滤函数，和Group.Filter基本相同，不同之处在于此函数只返回满足条件的卡的数量

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:913`
