# Duel.GetFlagEffectLabel

## Signature

```lua
Duel.GetFlagEffectLabel(int player, int code) -> int|nil,int...
```

## Description

Returns the label values stored on player flag effects with code.
If no matching flag effect exists, the core returns nil; if multiple matching flag effects exist, it returns one label value for each. A matching flag effect with no label returns 0 for that slot.

## Parameters

- `player` `int` - Player whose player flag effects are inspected.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - First matching label, or nil if no matching flag effect exists.
- `int...` - Additional matching labels; a matching effect with no label contributes 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4857`
