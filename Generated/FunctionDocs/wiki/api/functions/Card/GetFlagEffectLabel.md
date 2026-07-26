# Card.GetFlagEffectLabel

## Signature

```lua
Card.GetFlagEffectLabel(Card c, int code) -> int|nil,...?
```

## Description

Returns the first label value from each flag effect with the given code on c.
If c has no matching flag effect, the core returns nil. Matching flag effects with no label return 0 for that slot.
If several matching markers exist, the binding returns several Lua values.

## How To Use It

Use this when a card marker stored an integer payload.

```lua
local label=c:GetFlagEffectLabel(id)
if label then
    e:SetLabel(label)
end
```

If no marker exists, this returns nil. If several matching markers exist, the local binding returns one label value per marker.

## Related Functions

- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)
- [Card.GetFlagEffect](/api/functions/Card/GetFlagEffect)
- [Card.ResetFlagEffect](/api/functions/Card/ResetFlagEffect)

## Parameters

- `c` `Card` - Card whose single-card flag effects are inspected.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - First label value, or nil if no matching flag effect exists.
- `...?` - Additional integer label values from additional matching flag effects.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3559`
