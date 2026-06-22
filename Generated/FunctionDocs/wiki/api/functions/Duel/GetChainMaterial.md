# Duel.GetChainMaterial

## Signature

```lua
Duel.GetChainMaterial(int player) -> Effect|nil
```

## Description

Returns the first EFFECT_CHAIN_MATERIAL effect currently applying to player, or nil if none applies.
Fusion-style scripts use the returned effect's target and operation callbacks to handle Chain Material alternatives.

## Parameters

- `player` `int` - Player checked for an applying EFFECT_CHAIN_MATERIAL effect.

## Returns

- `Effect|nil` - First applying EFFECT_CHAIN_MATERIAL effect; no Lua value is pushed if player is invalid or no such effect exists, which behaves as nil in normal assignment.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4889`
