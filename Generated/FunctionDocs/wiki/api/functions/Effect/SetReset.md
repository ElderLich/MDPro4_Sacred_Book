# Effect.SetReset

## Signature

```lua
Effect.SetReset(Effect e, int reset_flag, [int reset_count]) -> void
```

## Description

Sets when e resets and how many reset checks it can survive.
If reset_count is 0 or omitted, the core stores 1. When a phase reset is used without an explicit turn side, the core applies both RESET_SELF_TURN and RESET_OPPO_TURN.

## How To Use It

`SetReset` controls when a temporary effect disappears.

Card-bound effects usually reset when the card leaves normal field relation:

```lua
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
```

Phase resets take an optional count:

```lua
e1:SetReset(RESET_PHASE+PHASE_END,2)
```

If the count is omitted or 0, MDPro3 stores 1. If a phase reset does not specify `RESET_SELF_TURN` or `RESET_OPPO_TURN`, the core adds both turn flags.

## Related Functions

- [Card.RegisterEffect](/api/functions/Card/RegisterEffect)
- [Effect.Reset](/api/functions/Effect/Reset)

## Parameters

- `e` `Effect`
- `reset_flag` `int`
- `reset_count` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:618`
