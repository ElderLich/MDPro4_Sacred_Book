# Duel.CheckEvent

## Signature

```lua
Duel.CheckEvent(int event, [bool get_info]) -> bool,Group,int,int,Effect,int,int
```

## Description

检查当前是否是event时点
若get_info=true并且是正确的时点，则还返回触发时点的信息 eg,ep,ev,re,r,rp

## Parameters

- `event` `int`
- `get_info` `bool` optional

## Returns

- `bool`
- `Group` - 可能为空
- `int` - 可能为空
- `int` - 可能为空
- `Effect` - 可能为空
- `int` - 可能为空
- `int` - 可能为空

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4894`
