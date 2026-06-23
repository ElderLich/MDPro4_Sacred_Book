# Duel.SetTargetPlayer

## Signature

```lua
Duel.SetTargetPlayer(int player) -> void
```

## Description

Stores player as the target player for the currently handled Chain.
Operations commonly read it with Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER), often together with CHAININFO_TARGET_PARAM.

## Parameters

- `player` `int` - Player value stored on the current Chain.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5006`
