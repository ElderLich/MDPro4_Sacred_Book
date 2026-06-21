# Duel.GetChainEvent

## Signature

```lua
Duel.GetChainEvent(int chainc) -> Group,int,int,Effect,int,int
```

## Description

返回连锁 chainc 的相关参数，如果 chainc=0，则返回当前正在处理的连锁的相关参数
返回6个参数，eg,ep,ev,re,r,rp

## Parameters

- `chainc` `int`

## Returns

- `Group`
- `int`
- `int`
- `Effect`
- `int`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4948`
