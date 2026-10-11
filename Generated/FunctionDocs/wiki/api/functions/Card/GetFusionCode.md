# Card.GetFusionCode

## Signature

```lua
Card.GetFusionCode(Card c) -> int,...?
```

## Description

Returns c's Fusion Material codes: current code, second code when present, then EFFECT_ADD_FUSION_CODE values.
When the core is checking with not_material set, only the current and second codes are returned.

## Parameters

- `c` `Card`

## Returns

- `int` - Current code.
- `...?` - Additional Fusion Material code values, if any.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3439`
