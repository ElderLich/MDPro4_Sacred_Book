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
