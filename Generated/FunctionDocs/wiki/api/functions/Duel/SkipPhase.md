# Duel.SkipPhase

## Signature

```lua
Duel.SkipPhase(int player, int phase, int reset_flag, int reset_count, [int value]) -> void
```

## Description

跳过玩家player的phase阶段，并在特定的阶段后reset，reset参数和效果相同
#value只对phase=PHASE_BATTLE才有用，value=1跳过战斗阶段的结束步骤，用于“变成回合结束阶段”等（招财猫王，闪光弹）

## Parameters

- `player` `int`
- `phase` `int`
- `reset_flag` `int`
- `reset_count` `int`
- `value` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4955`
