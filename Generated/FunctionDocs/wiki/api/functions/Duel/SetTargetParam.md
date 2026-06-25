# Duel.SetTargetParam

## Signature

```lua
Duel.SetTargetParam(int param) -> void
```

## Description

Stores param as the target parameter for the currently handled Chain.
Operations commonly read it with Duel.GetChainInfo(0, CHAININFO_TARGET_PARAM), often together with CHAININFO_TARGET_PLAYER.
Use it for data that should be frozen at activation time; recalculate in the operation when the card text depends on the current state.

## How To Use It

Use this together with `Duel.SetTargetPlayer` to store a number needed at resolution, such as LP amount, number of cards, or a selected option.

```lua
local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
Duel.Damage(p,d,REASON_EFFECT)
```

If the amount should be recalculated at resolution, do not freeze it here; announce the expected operation with `Duel.SetOperationInfo` and calculate again in the operation.

## Related Functions

- [Duel.SetTargetPlayer](/api/functions/Duel/SetTargetPlayer)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `param` `int` - Integer target parameter stored on the current Chain.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5007`
