# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Deals value effect damage to player for reason and returns the damage actually applied.
If damage is changed into LP recovery or prevented, the return value reflects the final applied damage. Negative input amounts are clamped to 0 by the local binding.
With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## How To Use It

Use this during resolution when a player takes effect damage or another scripted damage action.

```lua
local dealt=Duel.Damage(1-tp,800,REASON_EFFECT)
if dealt>0 then
    -- follow-up that requires actual damage
end
```

The return value is the actual damage applied. If damage is reversed, prevented, or the input amount is below 0, the returned damage can be 0. For simultaneous LP changes, pass `is_step=true` for each call and finish with `Duel.RDComplete()`.

## Related Functions

- [Duel.Recover](/api/functions/Duel/Recover)
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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`
