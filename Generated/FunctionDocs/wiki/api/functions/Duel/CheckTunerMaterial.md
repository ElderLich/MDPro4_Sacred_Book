# Duel.CheckTunerMaterial

## Signature

```lua
Duel.CheckTunerMaterial(Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> bool
```

## Description

Check to tuner as an adjustment [in the mg] whether there is a set of min-max card to meet the conditions as cohort call c material
F1 is to adjust the filter conditions to be met, f2 is outside the adjustment to meet the needs of the filter conditions

## Parameters

- `c` `Card`
- `tuner` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4996`
