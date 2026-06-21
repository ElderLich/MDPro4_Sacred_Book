# Duel.RegisterFlagEffect

## Signature

```lua
Duel.RegisterFlagEffect(int player, int code, int reset_flag, int property, int reset_count, [int label]) -> Effect
```

## Description

For the player to register the global environment logo effect
This effect always affects the player's (EFFECT_FLAG_PLAYER_TARGET) and will not be invalidated
The rest is the same as Card.RegisterFlagEffect

## Parameters

- `player` `int`
- `code` `int`
- `reset_flag` `int`
- `property` `int`
- `reset_count` `int` - default: 1
- `label` `int` optional

## Returns

- `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4853`
