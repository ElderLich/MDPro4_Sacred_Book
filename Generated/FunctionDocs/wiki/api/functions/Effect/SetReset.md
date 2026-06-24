# Effect.SetReset

## Signature

```lua
Effect.SetReset(Effect e, int reset_flag, [int reset_count]) -> void
```

## Description

Sets when e resets and how many reset checks it can survive.
If reset_count is 0 or omitted, the core stores 1. When a phase reset is used without an explicit turn side, the core applies both RESET_SELF_TURN and RESET_OPPO_TURN.
For card-bound temporary effects, combine the card-identity reset, such as RESET_EVENT+RESETS_STANDARD, with the phase or lifetime reset from the card text. See the Reset Flags And Effect Duration learning guide for full patterns.

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

- `e` `Effect` - Effect whose reset mask is replaced.
- `reset_flag` `int` - RESET_* mask describing the events or phases that can reset e.
- `reset_count` `int` optional - Number of matching reset checks before e resets; omitted or 0 is treated as 1.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:618`
