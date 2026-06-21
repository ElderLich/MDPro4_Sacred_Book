# Card.RegisterFlagEffect

## Signature

```lua
Card.RegisterFlagEffect(Card c, int code, int reset_flag, int property, int reset_count, [int label], [int desc]) -> Effect
```

## Description

For the registration of a logo with the results
Note: The effect of the registration to the card is not used for the system,
Even if the code and the built-in effect code coincidence will not affect,
And the type is always EFFECT_TYPE_SINGLE, reset method, property, and the general effect of the same,
And will not be invalidated, immune effect from the card

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
