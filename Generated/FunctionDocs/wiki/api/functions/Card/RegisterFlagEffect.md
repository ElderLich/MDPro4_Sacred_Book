# Card.RegisterFlagEffect

## Signature

```lua
Card.RegisterFlagEffect(Card c, int code, int reset_flag, int property, int reset_count, [int label], [int desc]) -> Effect
```

## Description

Registers a special single-card flag effect on c and returns the created Effect.
Flag effects are script markers: their code is kept separate from regular effect codes, they cannot be disabled, and count=0 is treated as 1.

## Parameters

- `c` `Card` - Card that receives the marker.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.
- `reset_flag` `int` - RESET_* mask controlling when the marker expires.
- `property` `int` - Effect property flags stored on the created marker; EFFECT_FLAG_CANNOT_DISABLE is always added.
- `reset_count` `int` - Reset counter for the created marker; 0 is treated as 1.
- `label` `int` optional - Optional integer payload stored on the marker.
- `desc` `int` optional - Optional client description id for marker hints.

## Returns

- `Effect` - The created flag effect.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3552`
