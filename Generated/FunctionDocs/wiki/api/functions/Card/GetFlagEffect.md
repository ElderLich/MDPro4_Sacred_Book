# Card.GetFlagEffect

## Signature

```lua
Card.GetFlagEffect(Card c, int code) -> int
```

## Description

Returns how many flag effects with code are registered on c.

## Parameters

- `c` `Card` - Card whose single-card flag effects are counted.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int` - Number of matching flag effects on c.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3553`
