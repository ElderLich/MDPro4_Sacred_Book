# Card.GetTunerLimit

## Signature

```lua
Card.GetTunerLimit(Card c) -> Effect,function|nil,int|nil,int,int
```

## Description

Returns the tuner-material-limit effect affecting c, that effect's target function or nil, its value or nil, and the allowed minimum and maximum counts; if no such effect applies, no values are returned.

## Parameters

- `c` `Card`

## Returns

- `Effect` - The tuner-material-limit effect.
- `function|nil` - The effect target function, if any.
- `int|nil` - The effect value, if any.
- `int` - Minimum allowed material count.
- `int` - Maximum allowed material count.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3601`
