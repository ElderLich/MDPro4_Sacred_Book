# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

手动减少玩家 p 对效果 e 的 count 个可用次数[ oath_only 为 该效果是否是 EFFECT_FLAG_OATH]

## Parameters

- `e` `Effect`
- `p` `int`
- `count` `int` optional - default: 1
- `oath_only` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`
