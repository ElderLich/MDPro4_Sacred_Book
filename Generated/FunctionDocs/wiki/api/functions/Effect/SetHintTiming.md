# Effect.SetHintTiming

## Signature

```lua
Effect.SetHintTiming(Effect e, int s_time, [int o_time]) -> void
```

## Description

Sets when the client should offer or highlight e for the handler's controller and, optionally, the opponent.
If o_time is omitted, the local core copies s_time to the opponent-side mask; masks are interpreted relative to the handler's controller when prompts are checked.
This controls prompting and display timing only; it does not replace activation legality checks in the effect's condition, cost, or target callbacks.

## Parameters

- `e` `Effect`
- `s_time` `int` - Hint timing mask for the handler's controller.
- `o_time` `int` optional - Hint timing mask for the opponent. Defaults to s_time.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:624`
