# Card.IsCanBeXyzMaterial

## Signature

```lua
Card.IsCanBeXyzMaterial(Card c, [Card|nil sc]) -> bool
```

## Description

Checks whether c can be used as Xyz Material, optionally for sc.
The core rejects Tokens, cards whose Xyz-material type is not a monster, cards with STATUS_FORBIDDEN, and applicable EFFECT_CANNOT_BE_XYZ_MATERIAL effects.

## Parameters

- `c` `Card`
- `sc` `Card|nil` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3645`
