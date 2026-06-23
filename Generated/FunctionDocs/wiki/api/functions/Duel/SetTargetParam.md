# Duel.SetTargetParam

## Signature

```lua
Duel.SetTargetParam(int param) -> void
```

## Description

Stores param as the target parameter for the currently handled Chain.
Operations commonly read it with Duel.GetChainInfo(0, CHAININFO_TARGET_PARAM), often together with CHAININFO_TARGET_PLAYER.

## Parameters

- `param` `int` - Integer target parameter stored on the current Chain.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5007`
