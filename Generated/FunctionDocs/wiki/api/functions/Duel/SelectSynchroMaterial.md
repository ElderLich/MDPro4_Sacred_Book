# Duel.SelectSynchroMaterial

## Signature

```lua
Duel.SelectSynchroMaterial(int player, Card c, [function|nil f1], [function|nil f2], int min, int max, [Card|nil smat], [Group|nil mg]) -> Group
```

## Description

Let the player player [from mg] select a set of clips that are required for the cohomology c [must contain smat (if there is mg ~ = nil this parameter is ignored)] The number of min-max clips that satisfy the condition
F1 is to adjust the filter conditions to be met, f2 is outside the adjustment to meet the needs of the filter conditions

## Parameters

- `player` `int`
- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `min` `int`
- `max` `int`
- `smat` `Card|nil` optional
- `mg` `Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4993`
