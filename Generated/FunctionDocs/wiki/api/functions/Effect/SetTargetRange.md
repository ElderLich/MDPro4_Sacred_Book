# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

为效果e设置Target Range属性
s_range指影响的我方区域
o_range值影响的对方区域
如果property属性中指定了EFFECT_FLAG_ABSOLUTE_RANGE标志，
那么s_range指玩家1受到影响的区域，o_range指玩家2受到影响的区域
如果这是一个召唤(覆盖)/限制召唤(覆盖)/特殊召唤手续
(EFFECT_SUMMON_PROC/EFFECT_LIMIT_SUMMON_PROC/EFFECT_SPSUMMON_PROC等)的效果，
并且property指定了EFFECT_FLAG_SPSUM_PARAM标志，
那么s_range表示特殊召唤到的哪个玩家的场地，
o_range表示可选择的表示形式

## Parameters

- `e` `Effect`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:615`
