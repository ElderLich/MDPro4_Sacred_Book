# Duel.GetChainEvent

## Signature

```lua
Duel.GetChainEvent(int chainc) -> Group,int,int,Effect,int,int
```

## Description

Return the parameters related to chain chainc; if chainc=0, return parameters for the currently processed chain
Returns six parameters: eg, ep, ev, re, r, rp

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
