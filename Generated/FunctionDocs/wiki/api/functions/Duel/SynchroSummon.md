# Duel.SynchroSummon

## Signature

```lua
Duel.SynchroSummon(int player, Card c, [Card|nil tuner], [Group|nil mg], [int minc], [int maxc]) -> void
```

## Description

Performs a Synchro Summon of c for player, optionally requiring tuner and selecting materials from mg.
Use this in an effect operation after checking Card.IsSynchroSummonable; the chosen Synchro Monster's registered procedure still controls material legality.
minc and maxc can restrict the number of non-Tuner materials used by the procedure.

## Parameters

- `player` `int` - Player performing the Synchro Summon.
- `c` `Card` - Synchro Monster to Summon.
- `tuner` `Card|nil` optional - Optional required Tuner material.
- `mg` `Group|nil` optional - Optional material pool to select from.
- `minc` `int` optional - Optional minimum non-Tuner material count override; default: 0.
- `maxc` `int` optional - Optional maximum non-Tuner material count override; default: 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4867`
