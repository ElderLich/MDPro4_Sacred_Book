# Auxiliary.PSSCompleteProcedure

## Signature

```lua
Auxiliary.PSSCompleteProcedure(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> void
```

## Description

Completes the procedure for monsters configured by Auxiliary.EnableReviveLimitPendulumSummonable after they are successfully Pendulum Summoned.
The operation checks Card.IsSummonType(SUMMON_TYPE_PENDULUM) before calling Card.CompleteProcedure.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Source

- `Utilities/procedure.lua:2114`
