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

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
