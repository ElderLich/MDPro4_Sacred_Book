# Card.GetTunerLimit

## Signature

```lua
Card.GetTunerLimit(Card c) -> nil|Effect,function|nil,int|nil,int|nil,int|nil
```

## Description

If card c is affected by the Tuner Material restriction effect EFFECT_TUNER_MATERIAL_LIMIT, return Effect e, function target, int value, int min, int max; otherwise return nil

## Parameters

- `c` `Card`

## Returns

- `nil|Effect`
- `function|nil`
- `int|nil`
- `int|nil`
- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3546`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
