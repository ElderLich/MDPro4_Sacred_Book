# Duel.XyzSummon

## Signature

```lua
Duel.XyzSummon(int player, Card c, [Group|nil mg], [int min], [int max]) -> void
```

## Description

Let the player player [from the mg] [choose min-max a material] on the c to call the excess procedure
Mg is not empty and min is 0 mg directly to all the excess material

## Parameters

- `player` `int`
- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4868`
