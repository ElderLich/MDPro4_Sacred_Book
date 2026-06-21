# Card.GetTunerLimit

## Signature

```lua
Card.GetTunerLimit(Card c) -> nil|Effect,function|nil,int|nil,int|nil,int|nil
```

## Description

如果卡片 c 受到同调素材限制效果 EFFECT_TUNER_MATERIAL_LIMIT 影响，则返回 Effect e,function target,int value,int min,int max ;否则返回nil

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
