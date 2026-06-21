# Duel.RegisterFlagEffect

## Signature

```lua
Duel.RegisterFlagEffect(int player, int code, int reset_flag, int property, int reset_count, [int label]) -> Effect
```

## Description

为玩家player注册全局环境下的标识效果，并返回这个效果
此效果总是影响玩家的(EFFECT_FLAG_PLAYER_TARGET)并且不会被无效化
其余部分与Card.RegisterFlagEffect相同

## Parameters

- `player` `int`
- `code` `int`
- `reset_flag` `int`
- `property` `int`
- `reset_count` `int` - default: 1
- `label` `int` optional

## Returns

- `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4853`
