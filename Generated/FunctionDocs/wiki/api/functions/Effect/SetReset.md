# Effect.SetReset

## Signature

```lua
Effect.SetReset(Effect e, int reset_flag, [int reset_count]) -> void
```

## Description

Sets when e resets and how many reset checks it can survive.
When a phase reset is used without an explicit turn side, the core applies both RESET_SELF_TURN and RESET_OPPO_TURN.

## Parameters

- `e` `Effect`
- `reset_flag` `int`
- `reset_count` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:618`
