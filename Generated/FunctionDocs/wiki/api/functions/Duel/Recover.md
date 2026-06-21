# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

以reason原因使玩家player回复value的LP，返回实际的回复值
如果受到回复变成伤害等效果的影响时，返回值为0.
is_step为true则是伤害/恢复LP过程的分解，需要调用Duel.RDComplete()触发时点

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4902`
