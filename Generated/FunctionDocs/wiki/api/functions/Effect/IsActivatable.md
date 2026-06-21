# Effect.IsActivatable

## Signature

```lua
Effect.IsActivatable(Effect e, int player, [bool neglect_loc], [bool neglect_target]) -> bool
```

## Description

检查效果e能否由player发动
neglect_loc=true 为不检测发动位置(手卡)， neglect_target=true 为不检测对象要求

## Parameters

- `e` `Effect`
- `player` `int`
- `neglect_loc` `bool` optional - default: false
- `neglect_target` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:654`
