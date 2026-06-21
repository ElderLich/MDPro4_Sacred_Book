# Duel.SSet

## Signature

```lua
Duel.SSet(int player, Card|Group targets, [int target_player], [bool confirm]) -> int
```

## Description

Makes player Set targets to target_player's Spell & Trap Zone. If targets is a Group, returns the number of cards successfully Set.

## Parameters

- `player` `int`
- `targets` `Card|Group`
- `target_player` `int` optional - default: player
- `confirm` `bool` optional - default: true

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4871`
