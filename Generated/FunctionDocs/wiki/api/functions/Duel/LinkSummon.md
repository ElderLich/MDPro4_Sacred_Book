# Duel.LinkSummon

## Signature

```lua
Duel.LinkSummon(int player, Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> void
```

## Description

Starts a rule Link Summon of c for player.
materials, lcard, minc, and maxc become temporary Link Summon limits; the binding yields to the core and returns no Lua value.

## Parameters

- `player` `int`
- `c` `Card`
- `materials` `Group|nil`
- `lcard` `Card|nil` optional
- `minc` `int` optional - default: 0
- `maxc` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4869`
