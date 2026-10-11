# Card.IsFusionCode

## Signature

```lua
Card.IsFusionCode(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c can be treated as any supplied code while used as Fusion Material.
The core includes c's current code, second code, and EFFECT_ADD_FUSION_CODE values. If no Fusion-only code additions apply, or material-code checks are disabled, it falls back to Card.IsCode.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3441`
