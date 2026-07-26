# Card.RegisterFlagEffect

## Signature

```lua
Card.RegisterFlagEffect(Card c, int code, int reset_flag, int property, int reset_count, [int label], [int desc]) -> Effect
```

## Description

Registers a special single-card flag effect on c and returns the created Effect.
Flag effects are script markers: their code is kept separate from regular effect codes, they cannot be disabled, and count=0 is treated as 1.
When reset_flag contains RESET_PHASE without RESET_SELF_TURN or RESET_OPPO_TURN, the core applies both turn sides. See the Reset Flags And Effect Duration learning guide for full patterns.
Use card flags for markers tied to one card's lifecycle; use Duel.RegisterFlagEffect for player markers.

## How To Use It

Use this to place a marker on one card, usually to remember that the card used an effect or entered a temporary state.

```lua
c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
```

The local binding masks the code as a flag-effect code, adds `EFFECT_FLAG_CANNOT_DISABLE`, treats count 0 as 1, and adds both turn sides to phase resets when no turn side is specified.

## Related Functions

- [Card.GetFlagEffect](/api/functions/Card/GetFlagEffect)
- [Card.GetFlagEffectLabel](/api/functions/Card/GetFlagEffectLabel)
- [Card.ResetFlagEffect](/api/functions/Card/ResetFlagEffect)
- [Effect.SetReset](/api/functions/Effect/SetReset)

## Parameters

- `c` `Card` - Card that receives the marker.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.
- `reset_flag` `int` - RESET_* mask controlling when the marker expires; phase resets without an explicit turn side apply to both players' turns.
- `property` `int` - Effect property flags stored on the created marker; EFFECT_FLAG_CANNOT_DISABLE is always added.
- `reset_count` `int` - Reset counter for the created marker; 0 is treated as 1.
- `label` `int` optional - Optional integer payload stored on the marker.
- `desc` `int` optional - Optional client description id for marker hints.

## Returns

- `Effect` - The created flag effect.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3555`
