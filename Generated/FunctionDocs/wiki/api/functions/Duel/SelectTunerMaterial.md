# Duel.SelectTunerMaterial

## Signature

```lua
Duel.SelectTunerMaterial(int player, Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> Group
```

## Description

Lets player select Synchro Materials for scard using the fixed tuner, optional filters, count limits, and optional material group.

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4995`
