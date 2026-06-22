# Duel.GetFlagEffectLabel

## Signature

```lua
Duel.GetFlagEffectLabel(int player, int code) -> int|nil,int...
```

## Description

Returns the label values stored on player flag effects with code.
If no matching flag effect exists, the core returns nil; if multiple matching flag effects exist, it returns one label value for each.

## Parameters

- `player` `int`
- `code` `int`

## Returns

- `int|nil` - First matching label, or nil if no matching flag effect exists.
- `int...` - Additional matching labels.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4857`
