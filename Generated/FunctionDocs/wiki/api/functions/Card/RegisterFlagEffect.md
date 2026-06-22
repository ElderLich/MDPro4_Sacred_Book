# Card.RegisterFlagEffect

## Signature

```lua
Card.RegisterFlagEffect(Card c, int code, int reset_flag, int property, int reset_count, [int label], [int desc]) -> Effect
```

## Description

Registers a special single-card flag effect on c and returns the created Effect.
Flag effects are script markers: their code is kept separate from regular effect codes, they cannot be disabled, and count=0 is treated as 1.

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `property` `int`
- `reset_count` `int`
- `label` `int` optional
- `desc` `int` optional

## Returns

- `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3552`
