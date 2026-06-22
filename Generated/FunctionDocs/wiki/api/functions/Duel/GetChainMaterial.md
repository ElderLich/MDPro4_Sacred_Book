# Duel.GetChainMaterial

## Signature

```lua
Duel.GetChainMaterial(int player) -> Effect|nil
```

## Description

Returns the first EFFECT_CHAIN_MATERIAL effect currently applying to player, or nil if none applies.
Fusion-style scripts use the returned effect's target and operation callbacks to handle Chain Material alternatives.

## Parameters

- `player` `int`

## Returns

- `Effect|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4889`
