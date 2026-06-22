# Card.GetFlagEffectLabel

## Signature

```lua
Card.GetFlagEffectLabel(Card c, int code) -> int|nil,...?
```

## Description

Returns the first label value from each flag effect with the given code on c.
If c has no matching flag effect, the core returns nil. Matching flag effects with no label return 0 for that slot.

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `int|nil` - First label value, or nil if no matching flag effect exists.
- `...?` - Additional integer label values from additional matching flag effects.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3556`
