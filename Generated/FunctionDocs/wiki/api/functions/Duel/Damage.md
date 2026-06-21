# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

以reason原因给与玩家player造成value的伤害，返回实际收到的伤害值
如果受到伤害变成回复等效果的影响时，返回值为0.
is_step为true则是伤害/恢复LP过程的分解，需要调用Duel.RDComplete()触发时点

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`
