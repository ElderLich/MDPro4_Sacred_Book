# Card.GetFlagEffect

## Signature

```lua
Card.GetFlagEffect(Card c, int code) -> int
```

## Description

Returns how many flag effects with code are registered on c.
The return value is a count, not a boolean; compare it with 0 when testing whether a card marker exists.

## How To Use It

Use this to count matching card markers.

```lua
if c:GetFlagEffect(id)==0 then
    c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
end
```

The return value is a count, not a boolean. Compare it with 0 when checking whether a marker exists.

## Related Functions

- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)
- [Card.GetFlagEffectLabel](/api/functions/Card/GetFlagEffectLabel)
- [Card.ResetFlagEffect](/api/functions/Card/ResetFlagEffect)

## Parameters

- `c` `Card` - Card whose single-card flag effects are counted.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int` - Number of matching flag effects on c.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3556`
