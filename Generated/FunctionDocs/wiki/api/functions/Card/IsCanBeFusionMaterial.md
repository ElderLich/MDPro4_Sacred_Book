# Card.IsCanBeFusionMaterial

## Signature

```lua
Card.IsCanBeFusionMaterial(Card c, [Card|nil fc], [int summon_type]) -> bool
```

## Description

Checks whether c can be used as Fusion Material for fc and summon_type.
fc is optional and summon_type defaults to SUMMON_TYPE_FUSION. The binding has no ignore_mon argument; it delegates to the core Fusion Material legality checks.

## Parameters

- `c` `Card`
- `fc` `Card|nil` optional
- `summon_type` `int` optional - default: SUMMON_TYPE_FUSION

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3639`
