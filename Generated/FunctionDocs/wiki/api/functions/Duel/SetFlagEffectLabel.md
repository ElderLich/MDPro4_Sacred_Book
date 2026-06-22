# Duel.SetFlagEffectLabel

## Signature

```lua
Duel.SetFlagEffectLabel(int player, int code, int label) -> bool|nil
```

## Description

Sets the first matching player flag effect's label to label and returns whether one was found.

## Parameters

- `player` `int` - Player whose matching flag effect is updated.
- `code` `int` - Flag-effect code to find.
- `label` `int` - New integer label stored on the first matching player flag effect.

## Returns

- `bool|nil` - True if a matching flag effect was updated; false if none exists; nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4856`
