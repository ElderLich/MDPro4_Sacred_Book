# Duel.SSet

## Signature

```lua
Duel.SSet(int player, Card|Group targets, [int target_player], [bool confirm]) -> int
```

## Description

Let the player player place the targets into the target trap's magic trap
If targets is Group, the number of successful operations is returned

## Parameters

- `player` `int`
- `targets` `Card|Group`
- `target_player` `int` optional - default: player
- `confirm` `bool` optional - default: true

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4871`
