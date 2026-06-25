# Duel.SetTargetPlayer

## Signature

```lua
Duel.SetTargetPlayer(int player) -> void
```

## Description

Stores player as the target player for the currently handled Chain.
Operations commonly read it with Duel.GetChainInfo(0, CHAININFO_TARGET_PLAYER), often together with CHAININFO_TARGET_PARAM.
This stores Chain data for a player-facing effect; it does not select a card target.

## How To Use It

Use this when the Chain Link stores a player choice or player destination rather than an official card target.

```lua
Duel.SetTargetPlayer(1-tp)
Duel.SetTargetParam(1000)
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,1000)
```

Read it during resolution with `Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)`. This is Chain data; it does not make the player a card target.

## Related Functions

- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `player` `int` - Player value stored on the current Chain.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5006`
