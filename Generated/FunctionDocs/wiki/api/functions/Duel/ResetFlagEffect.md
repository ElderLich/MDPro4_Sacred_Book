# Duel.ResetFlagEffect

## Signature

```lua
Duel.ResetFlagEffect(int player, int code) -> void
```

## Description

Resets all player flag effects with code for player.
This clears matching player markers manually; card markers use Card.ResetFlagEffect.

## How To Use It

Use this to manually clear all matching player markers.

```lua
Duel.ResetFlagEffect(tp,id)
```

This only removes player flag effects for the requested player and code. Card markers use `Card.ResetFlagEffect`.

## Related Functions

- [Duel.RegisterFlagEffect](/api/functions/Duel/RegisterFlagEffect)
- [Duel.GetFlagEffect](/api/functions/Duel/GetFlagEffect)

## Parameters

- `player` `int` - Player whose matching flag effects are reset.
- `code` `int` - Flag-effect code to clear.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4855`
