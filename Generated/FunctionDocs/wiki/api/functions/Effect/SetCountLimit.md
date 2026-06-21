# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

设置一回合可以发动的次数count（仅触发型效果有效），相同的code(不等于0或1时)共用1个次数
code包含以下数值具有特殊的性质
EFFECT_COUNT_CODE_OATH          誓约使用次数
EFFECT_COUNT_CODE_DUEL          决斗中使用次数
EFFECT_COUNT_CODE_SINGLE        同一张卡多个效果公共使用次数（不限制同名卡）

## Parameters

- `e` `Effect`
- `count` `int` - default: 1
- `code` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`
