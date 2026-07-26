# Card.IsCanBeRitualMaterial

## Signature

```lua
Card.IsCanBeRitualMaterial(Card c, [Card|nil sc]) -> bool
```

## Description

Checks whether c can be used as Ritual Material for sc.
Ritual scripts usually call this after choosing the Ritual Monster, filtering Duel.GetRitualMaterial's result with Card.IsCanBeRitualMaterial so monster-specific material restrictions are respected.
Pass nil for sc only when checking the generic material pool before a specific Ritual Monster is known.

## Parameters

- `c` `Card`
- `sc` `Card|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3644`
