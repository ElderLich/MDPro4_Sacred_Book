# Duel.RegisterFlagEffect

## Signature

```lua
Duel.RegisterFlagEffect(int player, int code, int reset_flag, int property, int reset_count, [int label]) -> Effect
```

## Description

Registers a player/global flag effect on player and returns the created Effect.
The flag effect is player-targeted, field-only, cannot be disabled, and count=0 is treated as 1.

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
