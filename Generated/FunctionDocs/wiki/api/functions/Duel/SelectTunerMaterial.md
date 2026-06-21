# Duel.SelectTunerMaterial

## Signature

```lua
Duel.SelectTunerMaterial(int player, Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> Group
```

## Description

Let the player \[from the mg\] select a set of clips of the min-max cards that are tuned to be used for co-ordination of the required conditions for c.
F1 is to adjust the filter conditions to be met, f2 is outside the adjustment to meet the needs of the filter conditions

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
