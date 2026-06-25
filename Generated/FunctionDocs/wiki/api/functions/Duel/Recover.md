# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Gives player LP for reason and returns the amount processed.
Effects can reverse recovery into damage; when recovery is reversed, this function returns 0 for recovery. Negative input amounts are clamped to 0 by the local binding.
With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## How To Use It

Use this during resolution when a player gains LP.

```lua
local gained=Duel.Recover(tp,1000,REASON_EFFECT)
if gained>0 then
    -- follow-up that requires actual recovery
end
```

The return value is the actual recovery applied. If recovery is reversed into damage, the recovery return value is 0. For simultaneous damage/recovery batches, use `is_step=true` and finish with `Duel.RDComplete()`.

## Related Functions

- [Duel.Damage](/api/functions/Duel/Damage)
- [Duel.RDComplete](/api/functions/Duel/RDComplete)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4902`
