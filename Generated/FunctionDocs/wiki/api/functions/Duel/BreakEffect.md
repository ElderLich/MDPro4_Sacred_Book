# Duel.BreakEffect

## Signature

```lua
Duel.BreakEffect() -> void
```

## Description

Separates the current resolving effect into a later timing window, then raises EVENT_BREAK_EFFECT.
Use this when card text says to do one action, then do another action afterward, so later triggers do not see both actions as simultaneous.
Do not use this for simultaneous damage/recovery batches; those use stepped Duel.Damage or Duel.Recover calls followed by Duel.RDComplete.

## How To Use It

Use this between sequential parts of one resolving effect when later timing should see the first part before the next part happens.

```lua
if Duel.Destroy(tc,REASON_EFFECT)>0 then
    Duel.BreakEffect()
    Duel.Damage(1-tp,500,REASON_EFFECT)
end
```

Do not use it for simultaneous damage/recovery. Simultaneous LP batches use stepped `Duel.Damage` or `Duel.Recover` plus `Duel.RDComplete()`.

## Related Functions

- [Duel.Damage](/api/functions/Duel/Damage)
- [Duel.Recover](/api/functions/Duel/Recover)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4927`
