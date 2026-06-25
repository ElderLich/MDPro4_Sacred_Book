# Duel.RDComplete

## Signature

```lua
Duel.RDComplete() -> void
```

## Description

Completes reserved step damage/recover processing after Duel.Damage or Duel.Recover is called with is_step=true.
Call this once after all stepped LP changes in the batch have been queued.

## How To Use It

Use this after one or more stepped `Duel.Damage` or `Duel.Recover` calls.

```lua
Duel.Damage(tp,500,REASON_EFFECT,true)
Duel.Damage(1-tp,500,REASON_EFFECT,true)
Duel.RDComplete()
```

Without this call, the reserved damage/recovery batch is not completed. Use ordinary sequential calls, often separated by `Duel.BreakEffect()`, when the card text wants one action and then another.

## Related Functions

- [Duel.Damage](/api/functions/Duel/Damage)
- [Duel.Recover](/api/functions/Duel/Recover)

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4903`
