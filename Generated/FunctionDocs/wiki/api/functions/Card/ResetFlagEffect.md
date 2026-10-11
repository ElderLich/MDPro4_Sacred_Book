# Card.ResetFlagEffect

## Signature

```lua
Card.ResetFlagEffect(Card c, int code) -> void
```

## Description

Resets all flag effects on c with code.
This clears matching card markers manually; it does not affect player markers registered with Duel.RegisterFlagEffect.

## How To Use It

Use this to clear all card markers with the matching code before their natural reset would remove them.

```lua
c:ResetFlagEffect(id)
```

This is a manual clear for flag effects, not a replacement for choosing the right reset mask when the marker is registered.

## Related Functions

- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)
- [Card.GetFlagEffect](/api/functions/Card/GetFlagEffect)

## Parameters

- `c` `Card` - Card whose matching flag effects are reset.
- `code` `int` - Flag-effect code to clear.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3609`
