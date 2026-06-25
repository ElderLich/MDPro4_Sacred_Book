# Duel.RegisterFlagEffect

## Signature

```lua
Duel.RegisterFlagEffect(int player, int code, int reset_flag, int property, int reset_count, [int label]) -> Effect|nil
```

## Description

Registers a player/global flag effect on player and returns the created Effect.
The flag effect is player-targeted, field-only, cannot be disabled, and count=0 is treated as 1.
When reset_flag contains RESET_PHASE without RESET_SELF_TURN or RESET_OPPO_TURN, the core applies both turn sides. See the Reset Flags And Effect Duration learning guide for full patterns.
Use player flags for player-wide markers; use Card.RegisterFlagEffect for markers tied to one card.

## How To Use It

Use this to place a player marker, such as a once-per-turn or action-limit marker that is not attached to a specific card.

```lua
Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
```

The local binding creates a field-only player-target flag effect. Like card flags, count 0 becomes 1 and phase resets without a turn side apply to both players' turns.

## Related Functions

- [Duel.GetFlagEffect](/api/functions/Duel/GetFlagEffect)
- [Duel.GetFlagEffectLabel](/api/functions/Duel/GetFlagEffectLabel)
- [Duel.ResetFlagEffect](/api/functions/Duel/ResetFlagEffect)
- [Effect.SetReset](/api/functions/Effect/SetReset)

## Parameters

- `player` `int` - Player that receives the marker; invalid players make the core return no values.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.
- `reset_flag` `int` - RESET_* mask controlling when the marker expires; phase resets without an explicit turn side apply to both players' turns.
- `property` `int` - Effect property flags stored on the created marker; player-target, field-only, and cannot-disable flags are always added.
- `reset_count` `int` - Reset counter for the created marker; 0 is treated as 1.
- `label` `int` optional - Optional integer payload stored on the marker.

## Returns

- `Effect|nil` - The created flag effect, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4853`
