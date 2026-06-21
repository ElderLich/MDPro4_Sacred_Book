# Duel.SendtoExtraP

## Signature

```lua
Duel.SendtoExtraP(Card|Group targets, [int|nil player], int reason) -> int
```

## Description

The reason for the reason the spirit of the swing card targets sent to the player player extra card group, the return value is the actual number of operations
If player is nil, it returns the extra card group for the card holder

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4863`
