# Card.RegisterFlagEffect

## Signature

```lua
Card.RegisterFlagEffect(Card c, int code, int reset_flag, int property, int reset_count, [int label], [int desc]) -> Effect
```

## Description

为c注册一个标识用效果
注：注册给卡的标识用效果不会用于系统，
即使code与内置效果code重合也不会影响，
并且类型总是EFFECT_TYPE_SINGLE，reset方法，property和一般的效果相同，
并且不会无效化，不受卡的免疫效果影响

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `property` `int`
- `reset_count` `int`
- `label` `int` optional
- `desc` `int` optional

## Returns

- `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3552`
