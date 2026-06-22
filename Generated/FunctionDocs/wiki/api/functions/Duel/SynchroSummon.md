# Duel.SynchroSummon

## Signature

```lua
Duel.SynchroSummon(int player, Card c, [Card|nil tuner], [Group|nil mg], [int minc], [int maxc]) -> void
```

## Description

Performs a Synchro Summon of c for player, optionally requiring tuner and selecting materials from mg.
minc and maxc can restrict the number of non-Tuner materials used by the procedure.

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group|nil` optional
- `minc` `int` optional - default: 0
- `maxc` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4867`
