# Duel.GetChainInfo

## Signature

```lua
Duel.GetChainInfo(int chainc, ... any) -> ...
```

## Description

Returns information fields from chainc in the same order as the requested CHAININFO_* constants.
Use chainc=0 for the currently resolving Chain. Unknown requested fields return nil, and no values are returned if the Chain does not exist.
For stored LP/player data, read CHAININFO_TARGET_PLAYER and CHAININFO_TARGET_PARAM. For official targets you are about to affect, prefer relation-aware target helpers.

## How To Use It

Use `chainc=0` inside an operation to read data from the currently resolving Chain Link.

```lua
local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
```

For official card targets, prefer relation-aware helpers such as `Duel.GetFirstTarget()` or `Duel.GetTargetsRelateToChain()` when you are about to act on them.

## Related Functions

- [Duel.SetTargetPlayer](/api/functions/Duel/SetTargetPlayer)
- [Duel.SetTargetParam](/api/functions/Duel/SetTargetParam)
- [Duel.GetOperationInfo](/api/functions/Duel/GetOperationInfo)

## Parameters

- `chainc` `int` - Chain index/count to inspect; scripts commonly use 0 for the current Chain Link.
- `...` `any` - One or more CHAININFO_* constants. Each requested field produces one return value.

## Returns

- `...` - Values corresponding to the requested CHAININFO_* constants. CHAININFO_TARGET_CARDS returns the Chain's target Group.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4947`
