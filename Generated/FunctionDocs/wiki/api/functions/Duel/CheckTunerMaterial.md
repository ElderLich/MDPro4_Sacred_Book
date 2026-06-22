# Duel.CheckTunerMaterial

## Signature

```lua
Duel.CheckTunerMaterial(Card c, Card tuner, [function|nil f1], [function|nil f2], int min, int max, [Group|nil mg]) -> bool
```

## Description

Checks whether tuner can be used with scard under the supplied tuner/non-tuner filters, count limits, and optional material group.

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
