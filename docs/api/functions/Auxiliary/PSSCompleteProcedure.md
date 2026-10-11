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

## Guided Examples

Learn how to use this function in context:

- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
