# Duel.GetFlagEffect

## Signature

```lua
Duel.GetFlagEffect(int player, int code) -> int|nil
```

## Description

Returns how many player flag effects with code are registered on player.

## Parameters

- `player` `int` - Player whose flag effects are counted.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - Number of matching player flag effects, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4854`
