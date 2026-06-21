# Group.Remove

## Signature

```lua
Group.Remove(Group g, function f, [Card|nil ex], ... any) -> void
```

## Description

从g中移除满足筛选条件f并且不等于ex的所有卡，第4个参数开始是额外参数

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|nil` optional
- `...` `any`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:928`
